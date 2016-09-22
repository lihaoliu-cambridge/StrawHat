# !/usr/bin/env python
# coding = utf-8

import redis
print redis.__file__

r = redis.Redis(host='XXX.XXX.XXX.XXX', port=6339, db=0)

r.set('xxx', 'yyy')
print r.get('xxx')
