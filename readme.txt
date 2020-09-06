Run in dev

>docker-compose up --build


For Prod
>docker build -t bookmyticket -f ./Dockerfile.prod .
>docker run -p 8000:8000 -i -t bookmyticket

eval $(minikube docker-env)


for local testing
kubectl port-forward service/bookmyticket 8000:8000

python manage.py collectstatic