from lxml import etree
from feedgen.ext.base import BaseEntryExtension


class CatalogueEntryExtension(BaseEntryExtension):

    def __init__(self):
        self.__id = None
        self.__brand = None
        self.__condition = None
        self.__custom_label_0 = None
        self.__custom_label_1 = None
        self.__custom_label_2 = None
        self.__custom_label_3 = None
        self.__custom_label_4 = None
        self.__google_product_category = None
        self.__premium_paragraph = None
        self.__availability_date = None
        self.__image_link = None
        self.__additional_image_link = None
        self.__product_type = None

    def extend_rss(self, feed):
        google_ns = 'http://base.google.com/ns/1.0'

        if self.__id:
            id = etree.SubElement(feed, '{%s}id' % google_ns)
            id.text = self.__id

        if self.__brand:
            brand = etree.SubElement(feed, '{%s}brand' % google_ns)
            brand.text = self.__brand

        if self.__availability_date:
            availability_date = etree.SubElement(feed, '{%s}availability_date' % google_ns)
            availability_date.text = self.__availability_date

        if self.__condition:
            condition = etree.SubElement(feed, '{%s}condition' % google_ns)
            condition.text = self.__condition

        if self.__custom_label_0:
            custom_label_0 = etree.SubElement(feed, '{%s}custom_label_0' % google_ns)
            custom_label_0.text = self.__custom_label_0

        if self.__custom_label_1:
            custom_label_1 = etree.SubElement(feed, '{%s}custom_label_1' % google_ns)
            custom_label_1.text = self.__custom_label_1

        if self.__custom_label_2:
            custom_label_2 = etree.SubElement(feed, '{%s}custom_label_2' % google_ns)
            custom_label_2.text = self.__custom_label_2

        if self.__custom_label_3:
            custom_label_3 = etree.SubElement(feed, '{%s}custom_label_3' % google_ns)
            custom_label_3.text = self.__custom_label_3

        if self.__custom_label_4:
            custom_label_4 = etree.SubElement(feed, '{%s}custom_label_4' % google_ns)
            custom_label_4.text = self.__custom_label_4

        if self.__image_link:
            image_link = etree.SubElement(feed, '{%s}image_link' % google_ns)
            image_link.text = self.__image_link

        if self.__additional_image_link:
            additional_image_link = etree.SubElement(feed, '{%s}additional_image_link' % google_ns)
            additional_image_link.text = self.__additional_image_link

        if self.__google_product_category:
            __google_product_category = etree.SubElement(feed, '{%s}google_product_category' % google_ns)
            __google_product_category.text = self.__google_product_category

        if self.__product_type:
            __product_type = etree.SubElement(feed, '{%s}product_type' % google_ns)
            __product_type.text = self.__product_type

        return feed

    def brand(self, brand=None):
        if brand is not None:
            self.__brand = brand

        return self.__brand

    def availability_date(self, availability_date=None):
        if availability_date is not None:
            self.__availability_date = availability_date

            return self.__availability_date

    def condition(self, condition=None):
        if condition is not None:
            self.__condition = condition

        return self.__condition

    def custom_label_0(self, custom_label_0=None):
        if custom_label_0 is not None:
            self.__custom_label_0 = custom_label_0

        return self.__custom_label_0

    def custom_label_1(self, custom_label_1=None):
        if custom_label_1 is not None:
            self.__custom_label_1 = custom_label_1

        return self.__custom_label_1

    def custom_label_2(self, custom_label_2=None):
        if custom_label_2 is not None:
            self.__custom_label_2 = custom_label_2

        return self.__custom_label_2

    def custom_label_3(self, custom_label_3=None):
        if custom_label_3 is not None:
            self.__custom_label_3 = custom_label_3

        return self.__custom_label_3

    def custom_label_4(self, custom_label_4=None):
        if custom_label_4 is not None:
            self.__custom_label_4 = custom_label_4

        return self.__custom_label_3

    def image_link(self, image_link=None):
        if image_link is not None:
            self.__image_link = image_link

        return self.__image_link

    def additional_image_link(self, additional_image_link=None):
        if additional_image_link is not None:
            self.__additional_image_link = additional_image_link

        return self.__additional_image_link

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
