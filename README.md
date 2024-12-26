### Сервис на основе FastAPI, который получает информацию о сети Tron.

##### 1. Установка необходимых пакетов

Сначала установим необходимые библиотеки:
```
pip install -r requirements.txt
```

##### 2. Импорт переменных окружения

Произвести импорт переменных окружения из файла [.env.dev](.env.dev) 
предварительно подставив корректные значения для подключения к базе данных
Postgres

##### 3. Реализация основного приложения

В приложении реализованы 3 метода:
/setup_database/ - для очистки и создания таблиц с БД
/address_info/ - для получения информации о кошельке и записи ее в БД
/requests/ - для получения информации о кошельках хранящихся в БД

Методы 2 и 3 покрыты тестами. 

##### 4. Запуск приложения

Чтобы запустить приложение, выполните команду:
```
uvicorn app.main:app --reload
```

Это запустит сервер на локальном хосте по умолчанию на порту 8000. Вы сможете отправлять запросы к сервису по следующим URL-адресам:
```
http://127.0.0.1:8000/docs для просмотра документации Swagger UI.
http://127.0.0.1:8000/openapi.json для доступа к спецификации OpenAPI.
```

##### 5. Запуск тестов

Для запуска тестов выполните команду:

```
pytest
```

Тесты проверят функциональность эндпоинтов и взаимодействие с базой данных.
