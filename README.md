# Docker-RestfulWebService
RESTful Web Service - Docker
Python

    Download and install Python

    Move to Scripts folder in Python27

    Install Flash using the following commands

     pip install flask
     pip install flask -RESTful

Docker

    Download and install Docker Toolbox.

    Download the files in this repository to your local machine.

    Open the Docker Terminal.

    Navigate to the downloaded folder.

    Build the Docker Image using the following command.

    docker build -t flask-image:latest .

    Run the docker image in the container using the following command

    docker run -t -p 5000:5000 --name flask-container flask-image

To view the website, go to http://192.168.99.100:5000/movies in your web browser.
