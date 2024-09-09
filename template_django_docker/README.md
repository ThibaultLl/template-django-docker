# Dockerised app with Django💚, Postgres🔍️, Gunicorn✨, and Nginx🌐

### ⚡️|Development

Uses the default Django development server.

1. CP and rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```
	

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

1. Init app (inside app container):
    ```sh
    $ python manage.py createsuperuser
    ```

1. Init data from backup.sql (inside db container):
    ```sh
    $ docker cp backup.sql <container_id_or_name>:backup.sql
    ```
    ```sh
    $ docker exec -it <container_id_or_name> /bin/bash
    ```
    ```sh
    $ psql -U <username> -d <database_name> -f backup.sql
    ```

### 🚀|Production

Uses gunicorn + nginx.

1. CP and Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

1. Init app (inside app container):
    ```sh
    $ python manage.py migrate
    ```
    ```sh
    $ python manage.py collectstatic
    ```
    ```sh
    $ python manage.py createsuperuser
    ```

1. Init data from backup.sql (inside db container):
    ```sh
    $ docker cp backup.sql <container_id_or_name>:backup.sql
    ```
    ```sh
    $ docker exec -it <container_id_or_name> /bin/bash
    ```
    ```sh
    $ psql -U <username> -d <database_name> -f backup.sql
    ```

### ♻️|Backup and restore data from database
1. File for Ubuntu VM backup.sh (dev):
    Save in the NAS :
    ```sh
    #!/bin/bash
    
    docker exec -it intranet-docker-db-1 pg_dump -U hello_django -d hello_django_dev --data-only > Z:/1-" "Dossiers/PROJET" "INTRANET/4" "-" "SAUVEGARDES" "BDD/backup_$(date +\%Y-\%m-\%d-\%H:\%M).sql
    ```
1. File for Ubuntu VM backup_prod.sh (prod):
    ```sh
    #!/bin/bash
    
    docker exec -it intranet-docker_db_1 pg_dump -U hello_django -d hello_django_prod --data-only > /mnt/sauvegardes_bdd/backup_$(date +\%d-\%m-\%Y-\%H:\%M).sql
    ```
    
1. Restore database
   
   :rotating_light: **Beware to rebuild containers/images/volumes before to execute this command** :rotating_light:
   ```sh
   cat backup.sql | docker exec -i intranet-docker-db-1 psql -U hello_django -d hello_django_dev
   ```

1. Automate backup :

   Open Cron tasks :
   ```sh
   crontab -e
   ```
   Execute the script every friday at 18:00 :
   ```sh
   0 18 * * 5 /backup-directory/backup.sh
   ```
