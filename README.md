# Twitoff


Setup from scratch:
```sh
cd /path/to/twitoff
pipenv install
pipenv install Flask Flask-SQLAlchemy Flask-Migrate
pipenv install python-dotenv requests basilica tweepy
```
Run for Windows:
```sh
set FLASK_APP=TWITOFF
flask run
```

Setup and migrate the database:

```sh
flask db init #> generates app/migrations dir
# run both when changing the schema:
flask db migrate #> creates the db (with "alembic_version" table)
flask db upgrade #> creates the tables
```