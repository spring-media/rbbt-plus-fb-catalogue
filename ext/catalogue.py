from feedgen.ext.base import BaseExtension


class CatalogueExtension(BaseExtension):

    def extend_ns(self):
        return {'g': 'http://base.google.com/ns/1.0'}
