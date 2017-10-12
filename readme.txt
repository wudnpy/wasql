Терминальные команды:
  Работа с Django.
    django-admins startproject project_name # создает папку проекта, с модулями поумолчанию.

    django-admins -h # возвращает список команд.
      [django]
      check
      compilemessages
      createcachetable
      dbshell
      diffsettings
      dumpdata
      flush
      inspectdb
      loaddata
      makemessages
      makemigrations
      migrate
      runserver
      sendtestemail
      shell
      showmigrations
      sqlflush
      sqlmigrate
      sqlsequencereset
      squashmigrations
      startapp
      startproject
      test
      testserver

    py manage.py startapp app_name # создает приложение.

    py manage.py createsuperuser # запускает процесс создания профиля администратора Django.

    py manage.py runserver # запускает сервер.


  Управление БД SQL Lite.
    # миграция - набор команд для бд.
    py manage.py makemigrates # создает миграцию.
    py manage.py migrate # применяет миграцию.

  Работа с шаблонами.

    {{}} # в эти скобки заключаются переменные, обрабатываемые шаблонизатором. Переменные передаются через 3 параметр функции render.
    {%%} # в эти скобки заключаются тэги (тэги делятся на две группы: управляющие конструкции и тэги шаблона).
    <переменная шаблона>|<фильтр 1:[значение фильтра 1]>|<фильтр 2: значение фильтра 2]> # шаблон фильтров. Фильтры служат для преобразования значения переменной.
