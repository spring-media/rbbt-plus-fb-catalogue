import coloredlogs, logging
import json
import time
from feedgen.feed import FeedGenerator
from ext.catalogue import CatalogueExtension
from ext.catalogue_entry import CatalogueEntryExtension

from data.query import *

from data.data import FeedContentWrapper

WELT_URL = 'https://welt.de'

LOG = logging.getLogger(__name__)
coloredlogs.install(isatty=True, logger=LOG, level='DEBUG')


def generate_feed(results, generator):
    """
    Generates a feed based on the 'Google Merchant Center' specification
    (https://support.google.com/merchants/answer/160589?hl=en).
    :param results: Result contents returned from the GraphQL query result.
    :param generator: Feed generator object
    """

    for result in results:
        content = FeedContentWrapper(result)

        content.add_premium_logo_to_image_url()
        feed_item = generator.add_entry(order='append')
        feed_item.id(content.id)
        feed_item.author(author=content.author)
        feed_item.link(href='%s%s' % (WELT_URL, content.web_url))
        feed_item.catalogue.availability_date(content.publication_date)
        feed_item.title(content.seo_title)
        feed_item.description(content.intro)
        feed_item.content(content.premium_paragraph)
        feed_item.catalogue.id(content.id)
        feed_item.catalogue.brand('WELT Plus')
        feed_item.catalogue.condition('new')
        feed_item.catalogue.google_product_category('Media > Magazines & Newspapers')
        feed_item.catalogue.product_type(content.category)
        feed_item.catalogue.image_link(content.add_premium_logo_to_image_url())
        feed_item.catalogue.additional_image_link(content.add_premium_logo_to_image_url(default_image=False))
        feed_item.catalogue.custom_label_0(content.topic)
        feed_item.catalogue.custom_label_1(content.headline)
        feed_item.catalogue.custom_label_2(str(content.reading_time))
        feed_item.catalogue.custom_label_3(content.age)
        feed_item.catalogue.custom_label_4(content.tags)


def build_feed_generator():
    feed_generator = FeedGenerator()
    feed_generator.register_extension('catalogue', extension_class_feed=CatalogueExtension,
                                      extension_class_entry=CatalogueEntryExtension)

    feed_generator.title('WELT Product Feed Premium Items')
    feed_generator.description('WELT premium articles from today.')
    feed_generator.link(href=WELT_URL)

    return feed_generator


def generate(output, config):
    page_size = 100
    article_limit = 5000
    generator = build_feed_generator()

    client = WeltGraphQLClient(config.get('GraphQl', 'endpoint'), config.get('GraphQl', 'api_key'))

    for page in range(1, article_limit // page_size):
        result_data = json.loads(client.retrieve_premium_content(page, page_size))
        results = result_data['data']['paginated_search']['results']

        LOG.info("Downloading page %d of %d." % (page, (article_limit // page_size)))

        generate_feed(results, generator)

        time.sleep(2)

    generator.rss_file(output, pretty=True)

    LOG.info('Finished loading of all the premium articles. Writing result to %s.', output)
