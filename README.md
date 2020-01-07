## Инструкция по установке

В системе должен быть установлен `python3` и для работы с докер пакет `docker` так же должен быть установлен.

В `python` скрипте используются пакеты `beautifulsoup4`, `requests`.

Домены указываются в файле `domain.csv`, коннекты к бд настраиваются `config.ini`.

#### Установка с использованием Virtual env

Введите в терминале:

```bash
python3 -m venv venv
source ./venv/bin/active
pip install beautifulsoup4
pip install requests
python main.py
```

#### Установка пакетов в систему

Введите в терминале: 

```bash
pip3 install beautifulsoup4
pip3 install requests
python3 main.py
```

#### Запуск через Docker

Введите в терминале:

```bash
docker build -t script .
docker run -it --rm -v $(pwd):/usr/src/app script
```