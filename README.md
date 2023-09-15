# Django Rest api demo OMDb
Dockerizing Django with Postgres, Gunicorn, and Nginx

## external libraries :
This project use Django, djangorestframework for Rest api and gspread for update Google sheet.

It run on Docker container with Postgress.

Usually I use [https://doc.traefik.io/traefik/](Traefick) as a proxy for all my apps but I preferred to keep it simple here

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
    $ docker compose exec web python manage.py migrate
    $ docker-compose exec web python manage.py createsuperuser
    $ docker-compose exec web python manage.py populate_movies
    ```

    Test it out at [http://localhost:8000/apis/v1/](http://localhost:8000/apis/v1/)

    To see movies Fast & Furious : [http://localhost:8000/apis/v1/films/](http://localhost:8000/apis/v1/films/)

    To see movies Pirates des caraibes : [http://localhost:8000/apis/v1/films/pirates_caraibes/](http://localhost:8000/apis/v1/films/pirates_caraibes/)

    To upload spreadsheet with "Pirates des caraïbes" movies list : [http://localhost:8000/spreadsheet/](http://localhost:8000/spreadsheet/)


### what remains to be done

1. Add fixtures.
1. add tests and CI/CD
1. add a back cache (Redis) to improve the loading of web servers
1. put session in Redis to improve the loading of web servers
1. add a front cache (Varnish) to improve the loading of web servers
1. Add CDN type Cloudflare to improve the loading of web servers

### website hosting

Deployment options vary, we can use solutions like Docker, Heroku, AWS, or a traditional web server.

currently I use dedicated OVH servers and I use DeployHq to deploy apps. It's all about saving money.

### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
