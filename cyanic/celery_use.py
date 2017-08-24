from celery_demo import add
import time


res = add.delay(4, 4)
print(res.ready())

time.sleep(5)

print(res.ready())