#!/usr/bin/env python

import redis
from time import sleep

r = redis.Redis()

c = 0
while True:
    r.rpush('zonk1024', c, c**2)
    print 'Pushed: {} {}'.format(c, c**2)
    c += 1
    sleep(1)
