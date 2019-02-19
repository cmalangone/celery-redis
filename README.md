# celery-redis

### Celery Monitor

redis-cli monitor

### Celery example
celery -A tasks worker --loglevel=info

Example
(celery-redis) cinzia ~/gitRepositories/celery-redis (master) $ python
Python 2.7.15 |Anaconda, Inc.| (default, Dec 14 2018, 13:10:39)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from tasks import *
>>> reverse('Ciznia')
'ainziC'
>>> reverse.delay('Cinzia')
<AsyncResult: c58664c4-2eba-444d-be5c-151956246ae5>
>>>


### Celery client for Node.js
https://github.com/mher/node-celery