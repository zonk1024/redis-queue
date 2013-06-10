#!/usr/bin/env python

import redis
from time import sleep
r = redis.Redis()

while True:
    v = r.lpop('zonk1024')
    if v:
        print v
        sleep(.5)
    else:
        break
