# -*- coding: utf-8 -*-
__author__ = 'Shinobu Jamella Hoshino, knochenflamme@gmail.com'

import user_agents
import random
from StringIO import StringIO
import urllib2
import httplib
import gzip
import zlib
import chardet
import google

UA = random.choice(user_agents.user_agents)

def pagesource(URL):
    request = urllib2.Request(URL, headers = {'User-Agent': UA, 'Referer': URL, 'Accept-Encoding': 'gzip, deflate'})
    try:
        response = urllib2.urlopen(request, timeout=90)
#        response = requests.get(URL, headers = {'User-Agent': UA, 'Referer': URL}).content
        ContentEncoding = response.info().get('Content-Encoding')
        if ContentEncoding == 'gzip':
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            return f.read()
        elif ContentEncoding == 'deflate':
            return zlib.decompress(response.read(), 16+zlib.MAX_WBITS)
        else:
            return response.read()

    except urllib2.HTTPError, e:
        return r'ERROR! QwQ<br/>' + str(e.code) + ' ' + str(e.reason)
    except httplib.HTTPException, e:
        return r'ERROR! QwQ<br/>HTTPException'
    except google.appengine.runtime.DeadlineExceededError:
        return r'ERROR! QwQ<br/>DeadlineExceededError'
    except google.appengine.runtime.apiproxy_errors.DeadlineExceededError:
        return r'ERROR! QwQ<br/>apiproxy_errors.DeadlineExceededError'
    except google.appengine.api.urlfetch_errors.DeadlineExceededError:
        return r'ERROR! QwQ<br/>urlfetch_errors.DeadlineExceededError'