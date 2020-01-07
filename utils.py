import requests
import logging
from bs4 import BeautifulSoup


def install(config, install_path):
    """
    Начальная конфигурация, для настройки соединения с базой данных и установкой пароля для админа
    :param config:
    :param install_path:
    :return:
    """
    url = '{url}/cms/{path}/install.php'.format(
        url=install_path,
        path=config.get('config', 'path')
    )
    payload = {
        'dbhost': config.get('config', 'dbhost'),
        'dbbase': config.get('config', 'dbbase'),
        'dbuser': config.get('config', 'dbuser'),
        'dbuserpassword': config.get('config', 'dbuserpassword'),
        'useModRewrite': config.get('config', 'useModRewrite'),
        'useSSLSupport': config.get('config', 'useSSLSupport'),
        'shop_pwd': config.get('config', 'shop_pwd')
    }

    r = requests.post(url, data=payload)

    soup = BeautifulSoup(r.content, 'html.parser')

    return '{protocol}://{secret}'.format(
        protocol=config.get('config', 'protocol'),
        secret=soup.a.text
    )


def logger():
    """
    Настройка логгирования

    :return: Logger
    """
    logger = logging.getLogger('threads')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('threads.log')
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
