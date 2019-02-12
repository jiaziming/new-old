#!/usr/bin/python
# -*-coding:utf-8-*-

import redis

r = redis.Redis(host='127.0.0.1',port=6379)

r.set('name','chunyun',ex=2)


all_keys = r.keys()
print(all_keys)

print(r.get('alex'))
print(r.get('name'))