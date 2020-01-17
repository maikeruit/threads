# -*- coding: utf-8 -*-

import requests
import csv
import configparser
import payloads
import utils
import logger
import re
from bs4 import BeautifulSoup
from threading import Thread, Lock
from urllib.parse import urlparse, parse_qs
from requests.exceptions import ConnectionError


class MyThread(Thread):
    """
    Класс для создания потоков через класс
    """

    def __init__(self, row, config, logger, lock):
        Thread.__init__(self)
        self.row = row
        self.config = config
        self.logger = logger
        self.lock = lock

    def run(self):
        """
        Запуск основного скрипта

        :return: None
        """
        domain = row.get('domain')
        logger.info('Calling thread: {}'.format(domain))

        try:
            install(self.row, self.config, self.logger, self.lock)
        except ConnectionError as err:
            logger.error('Connection error: {0}'.format(err))
        except Exception as err:
            logger.error('Undefined error: {0}'.format(err))


def install(row, config, logger, lock):
    """
    Основной скрипт, выполняющий все необходимые настройки на сервере
    :param row:
    :param config:
    :param logger:
    :param lock:
    :return:
    """
    install_path = '{protocol}://{domain}'.format(
        protocol=config.get('config', 'protocol'),
        domain=row.get('domain')
    )

    url = utils.install(config, install_path)

    with requests.session() as s:
        s.get(url)

        payload, params = payloads.get_session(config)
        r = s.post(url, data=payload, params=params)

        with lock:
            logger.info('{status} - {url} - %s'.format(
                status=r.status_code,
                url=url
            ), params)

        data = payloads.data(url)

        for index, datum in enumerate(data):
            payload = datum.get('payload')
            params = datum.get('params')
            r = s.post(url, data=payload, params=params)

            with lock:
                logger.info('{status} - {url} - %s'.format(
                    status=r.status_code,
                    url=url
                ), params)

        """
        Шаги обновления бд, на всякий случай прохожу все 3,
        если в этом нет необходимости можно сократить сразу до 3 шага
        """
        for index in range(3):
            params = {
                'controller': 'update',
                'step': index + 1
            }

            r = s.get(url, params=params)

            with lock:
                logger.info('{status} - {url} - %s'.format(
                    status=r.status_code,
                    url=url
                ), params)

            if index + 1 == 3:
                soup = BeautifulSoup(r.content, 'html.parser')
                links = soup.find_all(href=True)
                link = next(link.get('href') for link in links if re.search(r'\.sql', link.get('href')))

                if link:
                    query = parse_qs(urlparse(link).query)

                    params.update({
                        'part': query.get('part').pop()
                    })

                    r = s.get(url, params=params)

                    with lock:
                        logger.info('{status} - {url} - %s'.format(
                            status=r.status_code,
                            url=url
                        ), params)
                else:
                    with lock:
                        logger.warning('No sql links - {url} - %s'.format(
                            url=url
                        ), params)


if __name__ == '__main__':
    """
    Построчное чтение csv файла и запуск для каждой строки отдельного потока
    """
    logger = logger.init_logger(__name__, testing_mode=False)
    lock = Lock()
    config = configparser.ConfigParser()
    config.read('config.ini')

    with open('domain.csv') as file:
        reader = csv.DictReader(file, delimiter=';')

        for i, row in enumerate(reader):
            thread = MyThread(row, config, logger, lock)
            thread.start()
