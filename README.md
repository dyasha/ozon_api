# Описание проекта

Этот проект представляет собой решение тестового задания на позицию стажера-разработчика. Он включает в себя создание эндпоинта и сервиса для получения данных авторизации в API Озона, а затем получения данных методом [PostingAPI_GetEtgb](https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetEtgb) за период today() - 4 и записи полученных данных в базу данных ClickHouse.


## Технологии
- Python
- FastAPI
- ClickHouse
- SQLAlchemy
- Requests
- uvicorn
- alembic

## Установка и запуск
1. Установите Poetry, если он еще не установлен:

   >https://python-poetry.org/docs/#installation

2. Склонируйте репозиторий и перейдите в его директорию:
   >git clone https://github.com/dyasha/ozon_api.git

   >cd ozon_api
3. Установите зависимости с помощью Poetry:

    >poetry shell

    >poetry install
4. Скачайте образ ClickHouse
   >docker pull clickhouse/clickhouse-server
5. Сделайте запуск контейнера
   >docker run -d --name some-clickhouse-server -p 8123:8123 -p 9000:9000 --ulimit nofile=262144:262144 yandex/clickhouse-server
6. Выполните миграцию Базы Данных
   >alembic upgrade head
7. Запустите приложение
   >uvicorn ozon_api.app:app --reload
## Установка и запуск с docker-compose
ps не доработано, внутри контейнера web нужно выполнить alembic upgrade head
1. Выполните команду
   >docker compose up

### Проект будет доступен по адресу http://127.0.0.1:8000/docs

#### __Будущие улучшения__
- [X] Создание асинхронной БД

## __Автор__
###  [Береснев Владислав](https://github.com/dyasha)
>А [здесь](https://gitlab.com/dyasha) расположен мой gitlab =)
