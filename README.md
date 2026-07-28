# QA Automation Portfolio

![tests](https://github.com/jkrpchQA//qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)
![python](https://img.shields.io/badge/python-3.12-blue)
![playwright](https://img.shields.io/badge/Playwright-1.x-45ba4b)
![pytest](https://img.shields.io/badge/pytest-8.x-0a9edc)

Автотесты UI и API на **Python + pytest + Playwright + requests**. Проект демонстрирует навыки автоматизации на публичных стендах: UI — на [SauceDemo](https://www.saucedemo.com), API — на [restful-booker](https://restful-booker.herokuapp.com).

## Что показано

- **Page Object Model** — UI-логика отделена от тестов, локаторы вынесены в классы страниц.
- **Стабильные локаторы** через `data-test` — не завязаны на вёрстку и динамические id.
- **API-клиент** — обёртка над `requests.Session` с авторизацией по токену (тот же принцип инкапсуляции, что POM).
- **Фикстуры и teardown** — подготовка данных и гарантированная очистка после тестов (`created_booking`).
- **Параметризация** — один тест проверяет много входных данных (`@pytest.mark.parametrize`).
- **Маркеры** — `smoke`, `regression`, `ui`, `api`, `negative` для выборочного прогона.
- **Позитивные и негативные сценарии** — включая проверку авторизации, валидации и кодов ответа.
- **CI/CD** — GitHub Actions прогоняет тесты на каждый push и публикует HTML-отчёт.

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
│   ├── conftest.py         # фикстуры UI (login_page, logged_in_page)
│   └── tests/
│       ├── test_login.py
│       ├── test_inventory.py
│       └── test_checkout.py   # полный E2E-сценарий покупки
├── api/                    # API-автотесты (requests)
│   ├── client.py           # BookerClient
│   ├── conftest.py         # фикстуры API (client, auth_client, created_booking)
│   └── tests/
│       ├── test_auth.py
│       ├── test_booking_crud.py
│       └── test_booking_negative.py
├── .github/workflows/tests.yml
├── pytest.ini
└── requirements.txt
```

## Запуск

```bash
# 1. Клонировать и перейти в проект
git clone https://github.com/jkrpchQA//qa-automation-portfolio.git
cd qa-automation-portfolio

# 2. Виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate

# 3. Зависимости
pip install -r requirements.txt

# 4. Браузер для Playwright
playwright install chromium

# 5. Прогнать все тесты
pytest
```

После прогона в корне появится `report.html` — открыть в браузере.

## Полезные команды

```bash
pytest -m smoke          # только smoke-тесты
pytest -m ui             # только UI
pytest -m api            # только API
pytest -m "ui and smoke" # UI smoke
pytest ui/tests/test_login.py         # конкретный файл
pytest --headed          # UI-тесты в видимом браузере (наблюдать прогон)
```

## Стек

| Слой   | Инструмент |
|--------|-----------|
| Язык   | Python 3.12 |
| Раннер | pytest |
| UI     | Playwright |
| API    | requests |
| Отчёты | pytest-html |
| CI     | GitHub Actions |
