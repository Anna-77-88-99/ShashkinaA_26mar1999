# ShashkinaA_26mar1999

# Финальная аттестация 

# Вариант 2 - “Грибы”

## Шаг 1 Base (ветка - task1)

### Содержание документа
- Чек - лист
- Тестирование (Кроссбраузерное, совместимости, UX/UI)

## Шаг 2 API (ветка - task2)

### Содержание
- Инструкция к коллекции Postman "Дикий сбор"
- ДИКИЙСБОР.postman_collection.json

## Шаг 3 SQL (ветка - task3)

### Запросы в файле sql_query.sql + РЕЗУЛЬТАТЫ_ЗАПРОСОВ.docx 
- Выберите уникальные регионы сбора грибов.
- Выведите название, сезон сбора и съедобность грибов, которые относятся к категории «Трубчатые».
- Посчитайте количество грибов для каждой категории. Выведите название категории и количество в порядке убывания.
- Выведите название и описание съедобных грибов, которые лучше всего собирать в пяти самых больших по размеру (size) регионах.
- Выведите названия всех грибов, которые растут весной, относятся к категории «Пластинчатые» и которые лучше всего собирать в местах размером до 6000 условных единиц (size).

## Шаг 4 Auto (ветка - task4)

### Стек:
- pytest
- webdriver-manager
- selenium
- requests
- allure
- configparser
- json

### Шаги:
1. Скопировать проект из ветки task 4 `https://github.com/Anna-77-88-99/ShashkinaA_26mar1999/tree/task4`
2. Установить все зависимости `pip install -r requirements.txt`
3. Запустить тесты `python -m pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Структура:
- ./test - тесты
- ./pages - описание API + UI
- ./configuration - провайдер настроек
    - test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
    - test_data.json

### Библиотеки:
pip install pytest
pip install webdriver-manager
pip install selenium
pip install requests
pip install allure

### Полезные ссылки:
- [Подсказка по markdown] (https://www.markdownguide.org/cheat-sheet/)
- [Генератор .gitignore] (https://www.toptal.com/developers/gitignore)
- [Подсказка по pytest] (https://docs.pytest.org/en/stable/)
- [Подсказка по webdriver-manager] (https://pypi.org/project/webdriver-manager/)
- [Подсказка по Selenium] (https://www.selenium.dev/documentation/)
- [Подсказка по Requests] (https://requests.readthedocs.io/en/latest/index.html)
- [Подсказка по Allure Report] (https://allurereport.org/docs/) 

## Шаг 5 Soft (ветка - task5)

### Видео отчёт в формате .mp4
