# SCADA-SIM

Учебный проект: REST-сервис с имитацией "живых" данных промышленного оборудования.

## О проекте

Разработка, цель которой - создание прототипа SCADA-системы.
Проект имитирует работу промышленных датчиков и отображает их показания в реальном времени.

## Стек технологий
- **Бэкенд:** Python (Flask) + PostgreSQL (SQLAlchemy)
- **Фронтенд:** HTML/JS (Vanilla)
- **API:** REST API

## Инструкция по запуску

### 1. Подготовка окружения
Убедитесь, что у вас установлен Python и PostgreSQL.

1. Клонируйте проект и перейдите в папку `back/`:
   ```bash
   cd back
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate
   # Linux/macOS: source venv/bin/activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Подготовка базы данных
1. Запустите PostgreSQL.
2. Создайте пустую базу данных:
   ```bash
   # В консоли psql или через терминал:
   createdb -U postgres -h localhost scada_db
   ```
3. (Опционально) Наполните базу тестовыми данными:
   ```sql
   INSERT INTO sensors (name, kks, min_val, max_val, current_val, unit, type) 
   VALUES 
   ('Температура котла', 'K-101', 20.0, 150.0, 50.0, '°C', 'AI'),
   ('Давление пара', 'P-101', 0.5, 5.0, 2.0, 'бар', 'AI');
   ```

### 3. Запуск
1. Отредактируйте настройки подключения в начале файла `back/app.py` (поля `DB_USER`, `DB_PASSWORD` и т.д.).
2. Запустите бэкенд:
   ```bash
   python back/app.py
   ```
3. Откройте `back/index.html` в браузере.
