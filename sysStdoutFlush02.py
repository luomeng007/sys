# -*- coding: utf-8 -*-

import time
import sys

for i in range(5):
    # print(i, end=' ')
    sys.stdout.write("%d" % i),
    sys.stdout.flush()
    time.sleep(1)