# Маскировка данных карты

Это проект на Python для маскировки счета и номера карты пользователя

## Проверить версию Python:

Убедитесь, что у вас установлен Python (версия 3.x). Вы можете проверить установленную версию Python, выполнив команду:
```
python --version
```

## Установка Poerty:
Если у вас еще не установлен Poetry, вы можете установить его, выполнив следующую команду
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Проверить Poetry добавлен в ваш PATH.
```bash
poetry --version
```

## Установка:
1. Клонируйте репозиторий:
```bash
git clone git@github.com:Alexander-kat2025/bank_card2.git
```
2. Перейдите в директорию проекта:
```
cd ваш-репозиторий
```
3. Установите необходимые зависимости:
```bash
poetry add --group lint flake8 black isort mypy