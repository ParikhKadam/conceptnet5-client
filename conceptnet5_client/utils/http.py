import sys
import urllib
import urllib.request

try: 
    import simplejson as json
except ImportError: 
    import json

from urllib.error import URLError
from urllib3.exceptions import HTTPError

from conceptnet5_client.utils.debug import print_debug
from conceptnet5_client.cache.file_cache import cache


@cache
def make_http_request(url, urlenc):
    '''
    Makes and http request to the 'url', if response to that
    'url' is not cached yet.

    Returns the response in json format.
    '''
    request = urllib.request.Request(url)
    try:
        data = urllib.request.urlopen(request)
        datastr = data.readall().decode('utf-8')
    except HTTPError as e:
        print_debug('Error code: %s' % e.code, 'HTTPError')
        sys.exit()
    except URLError as e:
        print_debug('Reason: %s' % e.reason, 'URLError')
        sys.exit()
    return json.loads(datastr)
