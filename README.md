# fastapi-sqlalchemy-postgres-example


sorta following example from [here](https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396)

use docker container for postgres, and run backend locally via unvicorn (`main.py`)


# How to run this

1. Run `docker-compose up` to start db container (postgres) and pgadmin for managing db (not required)
1. Run `alembic upgrade head` to apply alembic revisions to postgres db
1. Run `uvicorn main:app --reload` to run backend app locally
1. browse to swagger docs at http://localhost:8000/docs.
1. run the add/get foods queries.


# stuff I did

1. set up alembic stuff (`.env` and `env.py`)
1. Make initial migration (with db container up):  ` alembic revision --autogenerate -m "Add drink table"`
1. Apply first upgrade: `alembic upgrade head`.
1. Make second migration (drink table)
