from lxml import html
from django.conf import settings
import requests

def reCaptcha(request):
    response = request.POST['g-recaptcha-response']
    data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': response
    }
    verify = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = verify.json()
    return result['success']

def parsing(domain):
    try:
        page = requests.get(domain)
        content = html.fromstring(page.content.decode('utf-8'))
    except Exception:
        return False

    value = dict()
    elm = {
        'title': '//title/text()',
        'description': '//meta[@name="description"]/@content',
        'favicon': '//link[contains(@rel, "icon")]/@href',
        'robots': '//meta[@name="robots"]/@content',
    }

    for k,v in elm.items():
        try:
            value[k] = content.xpath(v)[0]
        except Exception:
            print(k, 'not found!')

    if 'favicon' in value and (value['favicon'][0] == '/' or value['favicon'][0] != 'h') and value['favicon'][:2] != '//':
        value['favicon'] = '//'+domain.split("/")[2]+"/"+value['favicon']
    return value
