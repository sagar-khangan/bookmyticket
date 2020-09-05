Run in dev

>docker-compose up


For Prod
>docker build -t bookmyticket -f ./Dockerfile.prod .
>docker run -p 8000:8000 -i -t bookmyticket