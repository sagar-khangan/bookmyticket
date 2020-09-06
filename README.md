# bookmyticket
Backend APIs for Ticket Booking application

###This repository contains djagno rest backed for Movie Booking app 

To run locally 

> $ pip install -r requirements.txt \
> $ python mange.py runserver

>To run sample tests 
> $ pytest

To run using docker locally for development

> $ docker-compose up --build

To use docker for deployment

> $ docker build -t bookmyticket -f ./Dockerfile.prod . \
> $ docker run -p 8000:8000 -i -t bookmyticket

This reporsitory also contains sample kubernetes configuration, to run on minikube 
> Build docker image using above command
> $ cd dedployment
> $ kubectl apply -f .
> $ minikube ip
> You can use minikube ip to run 

NOTE: You can configure these files to run on a production env as well.

To run kubernets service locally 
> $ kubectl port-forward service/bookmyticket 8000:8000
 
This repository also contains CI/CD - 
 CI file = .github/workflow/ci.yaml
 for CD deployment can be configured in Heroku which usees Procfile


