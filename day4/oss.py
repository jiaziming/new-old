#!/usr/bin/python
# -*- coding: utf-8 -*-

import oss2

auth = oss2.Auth('<LTAIsyMo3MQBIkJ9>','<Dbge0vDAYtJE1Ke1l4m15xDGbUP4Gx>')

bucket = oss2.Bucket(auth,'<oss-cn-beijing.aliyuncs.com>','<ws-nginxstorage>')

bucket.put_object_from_file('<1123>','</Users/jia/new-python/day12/pyton-3/jiaziming.txt>')