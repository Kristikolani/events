Installation Instructions
=========================

Clone the repo

```
git clone https://github.com/Kristikolani/events.git
```

Enter repo and create virtual environment

```
cd events
python -m venv --prompt=events venv
. venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run migrations

```
python manage.py migrate 
```

Run local development server

```
python manage.py runserver
```

Visit the following url on your browser: http://localhost:8000/

Deploy
======
