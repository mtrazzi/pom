import os, sys
import configparser
from time import time
from json import loads
from urllib.parse import urlencode
from urllib.request import urlopen

config_path = os.path.join(os.path.expanduser('~'),'.config/beeminder/.pomrc')

def auth_token():
    dict1 = {}
    section = 'account'
    Config = configparser.ConfigParser()
    Config.read(config_path)
    options = Config.options(section)
    for option in options:
      dict1[option] = Config.get(section, option)
    return dict1['auth_token']
 
comment = sys.argv[3] if len(sys.argv) >= 3 else ''

post = {'auth_token': auth_token(), 'timestamp': round(time()), 'value': sys.argv[2], 'comment': comment}
params = urlencode(post)
params = params.encode('utf-8')

data = loads(urlopen('https://www.beeminder.com/api/v1/users/me/goals/%s/datapoints.json' % sys.argv[1], params).read().decode('utf-8'))
