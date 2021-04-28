# Django + DRF

this project is implemented on Django and Django REST framework

## Installation

1 Clone this project

```bash
git clone "https://github.com/KorenivskyOlexandr/test_API_task.git"
```

2 You should create virtualenv in project folder and activate one

```bash
cd test_API_task
python3 -m venv venv
source venv/bin/activate
(venv) $
```

Further we work only with venv

3 Installation python packages

```bash
pip install -r requirements.txt
```

4 Create database, migrations and superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Usage

Server start

```bash
python manage.py runserver
```

### Run tests

You may run tests

```bash
python manage.py test
```

You may stop your server use CTRL + C

Exit from venv

```bash
(venv) $ deactive
$
```
