#!/usr/bin/env python

import os
from feed.feed import *
from aws.s3 import *
from ConfigParser import ConfigParser

if __name__ == '__main__':
    file_name = "premium.rss"

    config = ConfigParser()
    config.read(os.environ['CONFIG'])

    generate(file_name, config)
    upload_data_to_s3_static(file_name, extra_args={"ContentType": "application/rss+xml"})
