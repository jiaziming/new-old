#!/usr/bin/python
# -*-coding:utf-8-*-

# -*- coding: utf-8 -*-
import oss2,os

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('<yourAccessKeyId>', '<yourAccessKeySecret>')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', '<yourBucketName>')
# 必须以二进制的方式打开文件，因为需要知道文件包含的字节数。
with open('<yourLocalFile>', 'rb') as fileobj:
    # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
    fileobj.seek(1000, os.SEEK_SET)
    # Tell方法用于返回当前位置。
    current = fileobj.tell()
    bucket.put_object('<yourObjectName>', fileobj)