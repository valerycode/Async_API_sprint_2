# Microservices for online cinema(educational project):
- admin_service(admin panel for adding and editing information about films)
- auth_service(API for user authentication and registration with social accounts)
- fastapi_solution(API for getting films' information)

## Technologies:
Python 3, Django, FastAPI, Docker, Docker-Compose, NGINX, PostgreSQL, Redis, ElasticSearch, Flask, Swagger, SQLAlchemy

## How to launch the project:
Create an `env` file in the same directory where its example file is described.

Launch the project using the following docker-compose command:
```
docker-compose up -d
```
Create migrations and collect static files using the following command:
```
make setup
```
Load initial data from SQLite to PostgreSQL using the following command. After this, the ETL service will run.
(The data must be loaded within 10 minutes, otherwise the ETL service will die due to critical errors.)
Load data into ElasticSearch:
```
make load_data
```
Create a Django superuser:
```
make admin
```
Command to connect to the Redis server:
```
make redis
```
Command to apply migrations in the auth service:
```
make setup_auth
```

## Running in the browser
- Open the administrative site - http://127.0.0.1:80/admin/
- API - http://127.0.0.1:80/api/v1/
- Documentation page - http://127.0.0.1:80/api/openapi
- Authentication service path - http://127.0.0.1:80/auth

## Running tests
Go to the `fastapi_solution/tests/functional` directory and execute the command docker-compose up -d


### Project contributors:

https://github.com/Vatson76 - Team Lead
https://github.com/valerycode
https://github.com/KaterinaSolovyeva
