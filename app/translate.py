import json
import requests
from flask_babel import _
from flask import current_app
import hashlib
import urllib.parse
import random


def translate(text, source_language, dest_language):
    if 'YOUDAO_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['YOUDAO_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    salt = random.randint(1, 65536)
    sign = current_app.config['YOUDAO_APP_KEY']+text + \
        str(salt)+current_app.config['YOUDAO_TRANSLATOR_KEY']
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()

    myurl = 'http://openapi.youdao.com/api' + '?appKey='+current_app.config['YOUDAO_APP_KEY']+'&q=' + \
        urllib.parse.quote(text)+'&from='+source_language+'&to='+dest_language + \
        '&salt='+str(salt)+'&sign='+sign

    r = requests.get(myurl)
    if r.status_code != 200:
        return _('Error: the translation service failed.')

    return json.loads(r.content.decode('utf-8')).get('translation')
