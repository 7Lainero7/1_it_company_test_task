# Django CashFlow App

Управление финансовыми записями: типы транзакций, категории, подкатегории, статус и комментарии — всё через удобную админку.

---

## Быстрый старт

### 1. Клонируй репозиторий и установи зависимости

```bash
git clone https://github.com/7Lainero7/1_it_company_test_task.git
cd 1_it_company_test_task
python -m venv .venv
.venv/Scripts/Activate.ps1  # или source .venv\bin\activate в linux
pip install -r requirements.txt
```

---

### 2. Создай базу данных и применяй миграции

```bash
python manage.py migrate
```

---

### 3. Загрузка начальных данных

```bash
python manage.py loaddata apps/dds/fixtures/initial_data.json
```

### 4. Создай суперюзера

```bash
python manage.py createsuperuser
```

---

### 5. (Опционально) Сгенерируй случайные транзакции

```bash
python manage.py seed_dds_data --count 50
```
### 6. Запусти сервер

```bash
python manage.py runserver
```

---

## Фронт JS фильтрация в админке

- Категории автоматически фильтруются по типу
- Подкатегории — по выбранной категории
- Проверки и валидация — через JS и сервер

---

## Логин в админку

Открой браузер: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  
Введи данные суперюзера, и начинай работу.

---

## Тесты

*В разработке…*

---

## Зависимости

- Django 5.2+
- Faker (для генерации записей)
