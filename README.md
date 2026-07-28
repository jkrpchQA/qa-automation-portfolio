# QA Automation Portfolio

![tests](https://github.com/jkrpchQA/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)
![python](https://img.shields.io/badge/python-3.12-blue)
![playwright](https://img.shields.io/badge/Playwright-1.x-45ba4b)
![pytest](https://img.shields.io/badge/pytest-8.x-0a9edc)

Автотесты UI и API на **Python + pytest + Playwright + requests**. Проект демонстрирует навыки автоматизации на публичных стендах: UI — на [SauceDemo](https://www.saucedemo.com), API — на [JSONPlaceholder](https://jsonplaceholder.typicode.com).

## Что показано

- **Page Object Model** — UI-логика отделена от тестов, локаторы вынесены в классы страниц.
- **Стабильные локаторы** через `data-test` — не завязаны на вёрстку и динамические id.
- **API-клиент** — обёртка над `requests.Session`: та же идея инкапсуляции, что и POM.
- **Фикстуры** — переиспользуемая подготовка данных и клиента (`conftest.py`).
- **Параметризация** — один тест проверяет много входных данных (`@pytest.mark.parametrize`).
- **Маркеры** — `smoke`, `regression`, `ui`, `api`, `negative` для выборочного прогона.
- **Устойчивость к флаки** — автоповтор упавших тестов (`pytest-rerunfailures`) и увеличенный таймаут навигации.
- **Позитивные и негативные сценарии** — коды ответа, валидация, фильтрация, 404.
- **CI/CD** — GitHub Actions прогоняет тесты на каждый push и публикует HTML-отчёт.

> Работу с **токен-авторизацией** (auth-токен, защищённые эндпоинты) выполнял на текущем
> проекте через Postman с manager-токеном. Здесь для стабильности CI взят публичный
> стенд без авторизации, а акцент сделан на CRUD, валидации и структуре фреймворка.

## Структура

```
qa-automation-portfolio/
├── ui/                     # UI-автотесты (Playwright + POM)
│   ├── pages/              # Page Object классы
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── conftest.py         # фикстуры UI (login_page, logged_in_page, таймауты)
│   └── tests/
│       ├── test_login.py
│       ├── test_inventory.py
│       └── test_checkout.py   # полный E2E-сценарий покупки
├── api/                    # API-автотесты (requests)
│   ├── client.py           # PlaceholderClient
│   ├── conftest.py         # фикстуры API (client, post_payload)
│   └── tests/
│       ├── test_posts_read.py
│       ├── test_posts_crud.py
│       └── test_posts_negative.py
├── .github/workflows/tests.yml
├── pytest.ini
└── requirements.txt
```

## Запуск (macOS)

```bash
git clone https://github.com/jkrpchQA/qa-automation-portfolio.git
cd qa-automation-portfolio

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium

pytest
```

## Полезные команды

```bash
pytest -m smoke          # только smoke-тесты
pytest -m ui             # только UI
pytest -m api            # только API
pytest -m "ui and smoke" # UI smoke
pytest ui/tests/test_login.py         # конкретный файл
pytest --headed          # UI-тесты в видимом браузере
pytest --html=report.html --self-contained-html   # с HTML-отчётом
```

## Стек

| Слой         | Инструмент 
--------------------------
| Язык         | Python 3.12 
| Раннер       | pytest 
| UI           | Playwright 
| API          | requests 
| Устойчивость | pytest-rerunfailures 
| Отчёты       | pytest-html 
| CI           | GitHub Actions 
