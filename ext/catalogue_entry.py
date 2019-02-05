from lxml import etree
from feedgen.ext.base import BaseEntryExtension


class CatalogueEntryExtension(BaseEntryExtension):

    def __init__(self):
        self.__id = None
        self.__price = None
        self.__brand = None
        self.__condition = None
        self.__availability = None
        self.__custom_label_0 = None
        self.__custom_label_1 = None
        self.__google_product_category = None
        self.__image_link = None
        self.__product_type = None

    def extend_rss(self, feed):
        GOOGLE_NS = 'http://base.google.com/ns/1.0'

        if self.__id:
            price = etree.SubElement(feed, '{%s}id' % GOOGLE_NS)
            price.text = self.__id

        if self.__price:
            price = etree.SubElement(feed, '{%s}price' % GOOGLE_NS)
            price.text = self.__price

        if self.__brand:
            brand = etree.SubElement(feed, '{%s}brand' % GOOGLE_NS)
            brand.text = self.__brand

        if self.__condition:
            condition = etree.SubElement(feed, '{%s}condition' % GOOGLE_NS)
            condition.text = self.__condition

        if self.__availability:
            availability = etree.SubElement(feed, '{%s}availability' % GOOGLE_NS)
            availability.text = self.__availability

        if self.__custom_label_0:
            custom_label_0 = etree.SubElement(feed, '{%s}custom_label_0' % GOOGLE_NS)
            custom_label_0.text = self.__custom_label_0

        if self.__custom_label_1:
            custom_label_1 = etree.SubElement(feed, '{%s}custom_label_1' % GOOGLE_NS)
            custom_label_1.text = self.__custom_label_1

        if self.__image_link:
            image_link = etree.SubElement(feed, '{%s}image_link' % GOOGLE_NS)
            image_link.text = self.__image_link

        if self.__google_product_category:
            __google_product_category = etree.SubElement(feed, '{%s}google_product_category' % GOOGLE_NS)
            __google_product_category.text = self.__google_product_category

        if self.__product_type:
            __product_type = etree.SubElement(feed, '{%s}product_type' % GOOGLE_NS)
            __product_type.text = self.__product_type

        return feed

    def price(self, price=None):
        if price is not None:
            self.__price = price

        return self.__price

    def brand(self, brand=None):
        if brand is not None:
            self.__brand = brand

        return self.__brand

    def condition(self, condition=None):

        if condition is not None:
            self.__condition = condition

        return self.__condition

    def availability(self, availability=None):

        if availability is not None:
            self.__availability = availability

        return self.__availability


    def custom_label_0(self, custom_label_0=None):
        if custom_label_0 is not None:
            self.__custom_label_0 = custom_label_0

        return self.__custom_label_0

    def custom_label_1(self, custom_label_1=None):
        if custom_label_1 is not None:
            self.__custom_label_1 = custom_label_1

        return self.__custom_label_1

    def image_link(self, image_link=None):
        if image_link is not None:
            self.__image_link = image_link

        return self.__image_link

    def google_product_category(self, google_product_category=None):
        if google_product_category is not None:
            self.__google_product_category = google_product_category

        return self.__google_product_category

    def product_type(self, product_type=None):
        if product_type is not None:
            self.__product_type = product_type

        return self.__product_type

    def id(self, id=None):
        if id is not None:
            self.__id = id

        return self.__id

