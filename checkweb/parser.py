from lxml import html
import requests

def parsing(domain):
    try:
        page = requests.get(domain)
        content = html.fromstring(page.content)
        error = False
    except Exception:
        error = True

    if not error:
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

        if 'favicon' in value and value['favicon'][0] == '/' and value['favicon'][:2] != '//':
            value['favicon'] = '//'+domain.split("/")[2]+value['favicon']
        return value

    return False
