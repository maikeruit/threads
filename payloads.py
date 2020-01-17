# -*- coding: utf-8 -*-

import re
import random
from urllib.parse import urlparse

script = '''
<script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-5346178e032a46d1"></script>
<script type="text/javascript">
addthis.layers({
    'theme' : 'transparent',
    'share' : {
        'position' : 'left',
        'numPreferredServices' : 5
    }, 
    'follow' : {
        'services' : []
    },  
    'whatsnext' : {},  
        'recommended' : {} 
    });
</script>
'''


def data(path):
    o = urlparse(path)
    domain = re.sub(r'(\.[a-z]+)*', '', o.hostname)
    template_list = ['02_Global_Meds', '06_Solaris_girl', '03_Sky_Pharmacy', '04_Three_Funny_Doctors']

    return [
        dict(
            payload={
                'users': '<h1>{}</h1>Big Sale | Save up to 15% | Big Packs | <b>{}</b> | Free Shipping'.format(
                    domain.title(), domain) + script,
                'USERS_CODE': 'save'
            },
            params={
                'controller': 'settings'
            }
        ),
        dict(
            payload={
                'main_name': '{} | Best | Sell | Worldwide delivery'.format(domain.title()),
                'NAME': ' save'
            },
            params={
                'controller': 'seo'
            }
        ),
        dict(
            payload={
                'main_name': '{} | Beste | Verkaufen | Weltweite Lieferung'.format(domain.title()),
                'NAME': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'de'
            }
        ),
        dict(
            payload={
                'main_name': '{} | Meilleur | Vendre | Livraison dans le monde'.format(domain.title()),
                'NAME': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'fr'
            }
        ),
        dict(
            payload={
                'main_name': '{} | El Mejor | Vender | Envíos a todo el mundo'.format(domain.title()),
                'NAME': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'es'
            }
        ),
        dict(
            payload={
                'main_name': '{} | Il migliore | Vendi | Consegna in tutto il mondo'.format(domain.title()),
                'NAME': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'it'
            }
        ),
        dict(
            payload={
                'second_path_prefix': '{}-'.format(domain.title()),
                'SECOND_PATH_EDIT': 'save'
            },
            params={
                'controller': 'seo'
            }
        ),
        dict(
            payload={
                'second_path_prefix': '{}-'.format(domain.title()),
                'SECOND_PATH_EDIT': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'de'
            }
        ),
        dict(
            payload={
                'second_path_prefix': '{}-'.format(domain.title()),
                'SECOND_PATH_EDIT': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'fr'
            }
        ),
        dict(
            payload={
                'second_path_prefix': '{}-'.format(domain.title()),
                'SECOND_PATH_EDIT': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'es'
            }
        ),
        dict(
            payload={
                'second_path_prefix': '{}-'.format(domain.title()),
                'SECOND_PATH_EDIT': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'it'
            }
        ),
        dict(
            payload={
                'image_prefix': '{}-'.format(domain.title()),
                'IMAGES_EDIT': 'save'
            },
            params={
                'controller': 'seo',
            }
        ),
        dict(
            payload={
                'image_prefix': '{}-'.format(domain.title()),
                'IMAGES_EDIT': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'de'
            }
        ),
        dict(
            payload={
                'image_prefix': '{}-'.format(domain.title()),
                'IMAGES_EDIT': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'fr'
            }
        ),
        dict(
            payload={
                'image_prefix': '{}-'.format(domain.title()),
                'IMAGES_EDIT': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'es'
            }
        ),
        dict(
            payload={
                'image_prefix': '{}-'.format(domain.title()),
                'IMAGES_EDIT': 'save'
            },
            params={
                'controller': 'seo',
                'lang': 'it'
            }
        ),
        dict(
            payload={
                'template': random.choice(template_list),
                'rnd[01_Blue_Doctor]': 16,
                'rnd[02_Global_Meds]': 7,
                'rnd[03_Sky_Pharmacy]': 7,
                'rnd[04_Three_Funny_Doctors]': 7,
                'rnd[05_Two_Sexy_Girls]': 7,
                'rnd[06_Solaris_girl]': 7,
                'rnd[07_Green_Cialis]': 7,
                'rnd[08_Red_ED]': 7,
                'rnd[09_Viagra_blue]': 7,
                'rnd[10_Aqua_blue]': 7,
                'rnd[11_Happy_parents]': 7,
                'rnd[12_Ideal_figure]': 7,
                'rnd[13_First_med]': 7,
                'template_bil': 'default',
                'TEMPLATE_SETTINGS': 'save'
            },
            params={
                'controller': 'settings'
            }
        )
    ]


def update(path):
    return [
        dict(
            url=path,
            params={
                'controller': 'update',
                'step': 1
            }
        ),
        dict(
            url=path,
            params={
                'controller': 'update',
                'step': 2
            }
        ),
        dict(
            url=path,
            params={
                'controller': 'update',
                'step': 2
            }
        )
    ]


def get_session(config):
    payload = {
        'login2': config.get('config', 'login'),
        'pass2': config.get('config', 'shop_pwd')
    }
    params = {
        'act': 'enter'
    }

    return payload, params
