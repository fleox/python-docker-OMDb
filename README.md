# Django Rest api demo OMDb
Dockerizing Django with Postgres, Gunicorn, and Nginx

## external libraries :
gspread [https://docs.gspread.org/en/v5.10.0/](https://docs.gspread.org/en/v5.10.0/)
djangorestframework [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

## How to use this project?

### Development

Uses the default Django development server.

1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Run command to import movies informations from OMDb
    ```sh
    $ docker-compose exec web python manage.py createsuperuser
    $ docker-compose exec web python manage.py populate_movies
    ```

    Test it out at [http://localhost:8000/apis/v1/](http://localhost:8000/apis/v1/)

    To see movies Fast & Furious : [http://localhost:8000/apis/v1/films/](http://localhost:8000/apis/v1/films/)

    To see movies Pirates des caraibes : [http://localhost:8000/apis/v1/films/pirates_caraibes/](http://localhost:8000/apis/v1/films/pirates_caraibes/)

    To upload spreadsheet with "Pirates des caraïbes" movies list : [http://localhost:8000/spreadsheet/](http://localhost:8000/spreadsheet/)

### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
