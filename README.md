# Демо проект автоматизации тестирования сайта [Уфанет.ру](https://ufanet.ru/)
___
## Проект представляет собой набор UI-тестов покрывающих следующий функционал:
1. Авторизация
2. Переключение контента на странице
3. Проверка корректного перехода между страницами
___
## Используемый стек:
<p align="left">
<img src="media/python-original-wordmark.svg" width="50" height="50"/>
<img src="media/pytest-original-wordmark.svg" width="50" height="50"/>
<img src="media/selenium-original-icon.png" width="50" height="50"/>
<img src="media/jenkins-original.svg" width="50" height="50"/>
<img src="media/allurereport-original-icon.png" width="50" height="50"/>
<img src="media/selenoid-original-icon.png" width="50" height="50"/>
</p>

Проект написан на языке программирования Python, с использованием фреймворков Pytest, Selene. 

Реализована удаленная сборка тестов в Jenkins.

Запуск тестов в Selenoid.

После прохождения тестов система отправляет краткий отчет в *Telegram*.

Так же в Jenkins будет доступен подробный отчет Allure.

### Главная страница Allure-отчета

<p align="center">
<img src="media/allure-report-main-page.png"/>
</p>

### Детализация шагов

<p align="center">
<img src="media/allure-report-steps.png"/>
</p>


### Графики прохождения тестов

<p align="center">
<img src="media/allure-report-graphs.png"/>
</p>


## Уведомления в Telegram с использованием бота

> После завершения сборки специальный бот, созданный в <code>Telegram</code>, автоматически обрабатывает и отправляет сообщение с отчетом о прогоне.

<p align="center">
<img src="media/telegram-report.png"/>
</p>

## Пример запуска теста в Selenoid

> К каждому тесту в отчете прилагается видео. Одно из таких видео представлено ниже.
<p align="center">
  <img src="media/selenoid-video.gif"/>
</p>