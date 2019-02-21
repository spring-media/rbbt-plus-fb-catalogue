#!/usr/bin/env python

from feed.feed import *
from aws.s3 import *
from ConfigParser import ConfigParser


def run():
    file_name = "premium.rss"

    config = ConfigParser()
    config.read('properties.ini')

    generate(file_name, config)
    upload_data_to_s3_static(file_name, extra_args={"ContentType": "application/rss+xml"})


if __name__ == '__main__':
    run()
