import re
import os.path as path
from datetime import datetime
from urlparse import urljoin
from urlparse import urlparse as parse


def format_date_time_from_string(str):
    return datetime \
        .strptime(str, '%Y-%m-%dT%H:%M:%SZ') \
        .strftime('%d/%m/%Y')


def build_author_data_from_result(authors):
    authors = map(lambda author: author['name'] if author['name'] else '', authors)

    return {"email": ", ".join(list(authors))}


def retrieve_days_passed_since_today(date):
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    time_passed = date.today() - date

    return str(time_passed.days)


def strip_tags(text):
    tag_re = re.compile(r'<[^>]+>')

    return tag_re.sub('', text)


def retrieve_image_url(result, image_width):
    default_fallback_image = 'https://www.welt.de/img/masters/mobile160492822/7651629427-ci16x19-wWIDTH/welt-fallback-jpg.jpg'

    for element in result['elements']:
        image_urls = [asset['fields']['source'] for asset in element['assets']
                      if asset['type'] == 'image' and asset['fields']['width'] == image_width]

        if len(image_urls) != 0:
            if image_width == '320':
                return image_urls[0].replace('WIDTH', '1200-fnov-fpotl-fpi157750653')
            else:
                return image_urls[0].replace('WIDTH', '-fnov-fpotl-fpi157750653')

    return default_fallback_image.replace('WIDTH', '-fnov-fpotl-fpi157750653')


class FeedContentWrapper:

    def __init__(self, result):
        self.result = result
        self.id = result['id'] if 'id' in result else None
        self.author = build_author_data_from_result(result['authors'])
        self.seo_title = result['seoTitle']
        self.web_url = result['webUrl']
        self.intro = result['intro']
        self.topic = result['topic']
        self.reading_time = result['readingTimeMinutes']
        self.premium_paragraph = strip_tags(result['premiumParagraph'])
        self.image_url_1_1 = result['images'][0]['imageUrl_1x1'] if result[
            'images'] else "https://www.welt.de/img/masters/mobile160492822/7651629427-ci16x19-w1200/welt-fallback-jpg.jpg"
        self.image_url_16_9 = result['images'][0]['imageUrl_16x9'] if result[
            'images'] else "https://www.welt.de/img/masters/mobile160492822/7651629427-ci102l-w1200/welt-fallback-jpg.jpg"
        self.headline = result['headline']
        self.category = result['sectionData']['home']['URL'][1:-1].replace('/', ' > ')
        self.age = retrieve_days_passed_since_today(result['publicationDate'])
        self.publication_date = format_date_time_from_string(result['publicationDate'])

    def add_premium_logo_to_image_url(self, default_image=True):
        url = self.image_url_16_9 if default_image else self.image_url_1_1
        paths = path.split(parse(url).path)
        path_to_replace = "%s%s/%s" % (paths[0], "-fnov-fpotl-fpi157750653", paths[1])

        return urljoin(url, path_to_replace)
