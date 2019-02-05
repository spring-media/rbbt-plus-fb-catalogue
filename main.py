#!/usr/bin/env python

import re
import json
import coloredlogs, logging
import requests
from datetime import datetime
from ext.catalogue import CatalogueExtension
from ext.catalogue_entry import CatalogueEntryExtension
from feedgen.feed import FeedGenerator

from s3 import *


LOG = logging.getLogger(__name__)
coloredlogs.install(isatty=True, logger=LOG, level='DEBUG')

WELT_URL = 'https://welt.de'


def retrieve_premium_article_today(page):
    doug_ecs_url = 'https://doug-ecs-production.up.welt.de'

    response = requests.get(
        '%s%s%s' % (doug_ecs_url, '/_search?flag=premium&pageSize=100&page=', page),
        auth=('biggus', 'dickus')
    )

    response.raise_for_status()

    return json.loads(response.text)


def generate_feed(feed_generator, image_width, pages_count, page=1):

    articles_today = retrieve_premium_article_today(page)
    LOG.info('Loading articles from page %d of %d.' % (articles_today['response']['page'], pages_count))

    for result in articles_today['response']['results']:
        if bool(re.search('video\d+|testgpr', result['webUrl'])):
            continue

        if all(field in result for field in ('id', 'fields', 'sections')):
            feed_item = feed_generator.add_entry(order='append')
            feed_item.id(result['id'])
            feed_item.link(href='%s%s' % (WELT_URL, result['webUrl']) if 'webUrl' in result else '')
            feed_item.title(result['fields']['seoTitle'] if 'seoTitle' in result['fields'] else '')
            feed_item.description(result['fields']['intro'] if 'intro' in result['fields'] else '')
            feed_item.catalogue.id(result['id'])
            feed_item.catalogue.price('0.00')
            feed_item.catalogue.brand('WELTplus')
            feed_item.catalogue.condition('new')
            feed_item.catalogue.availability('in stock')
            feed_item.catalogue.image_link(retrieve_image_url(result, image_width))
            feed_item.catalogue.google_product_category('Media > Magazines & Newspapers')
            feed_item.catalogue.product_type(
                result['sections']['home'][1:-1].replace('/', ' > ') if 'home' in result['sections'] else None)
            feed_item.catalogue.custom_label_0(
                result['fields']['readingTimeMinutes'] if 'readingTimeMinutes' in result['fields'] else None)
            feed_item.catalogue.custom_label_1(
                retrieve_days_passed_since_today(result['fields']['publicationDate']) if 'publicationDate' in
                                                                                         result['fields'] else None)
        else:
            continue

    if articles_today['response']['page'] < pages_count:
        generate_feed(feed_generator, image_width, pages_count, page=articles_today['response']['page'] + 1)



def create_feed_generator():
    feed_generator = FeedGenerator()
    feed_generator.register_extension('catalogue', extension_class_feed=CatalogueExtension,
                                      extension_class_entry=CatalogueEntryExtension)

    feed_generator.title('WELT Product Feed Premium Items')
    feed_generator.description('WELT premium articles from today.')
    feed_generator.link(href=WELT_URL)

    return feed_generator


def retrieve_image_url(result, image_width):
    default_fallback_image = 'https://www.welt.de/img/masters/mobile160492822/7651629427-ci16x19-wWIDTH/welt-fallback-jpg.jpg'

    for element in result['elements']:
        image_urls = [asset['fields']['source'] for asset in element['assets']
                      if asset['type'] == 'image' and asset['fields']['width'] == image_width]

        if len(image_urls) != 0:
            if image_width == '320':
                return image_urls[0].replace('WIDTH', '1200-fnov-fpotr-fpi157750653')
            else:
                return image_urls[0].replace('WIDTH', '-fnov-fpotr-fpi157750653')

    return default_fallback_image.replace('WIDTH', '-fnov-fpotr-fpi157750653')


def generate(output, image_width):
    page_size = 500
    max_items = 5000

    feed_generator = create_feed_generator()
    generate_feed(feed_generator, image_width, max_items / page_size)

    LOG.info('Finished loading of all the premium articles. Writing result to %s.', output)

    feed_generator.rss_file(output, pretty=True)


def retrieve_days_passed_since_today(date):
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    time_passed = date.today() - date

    return str(time_passed.days)


if __name__ == '__main__':
    image_widths = [{'width': '320', 'name': '16_9'}, {'width': '1500', 'name': '1_1'}]

    for image_width in image_widths:
        file_name = 'premium_%s.rss' % (image_width['name'])

        try:
            generate(file_name, image_width)
            upload_data_to_s3_static(file_name)
        except IOError as err:
            print(err)

