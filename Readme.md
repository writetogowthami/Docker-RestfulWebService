-Setup the project with the app.py and JSON file in a single folder.

-In the docker terminal, use command "touch Dockerfile" to create the Dockerfile and setup the DockerFile accordingly.

-Create Docker Image by running : "docker build -t flask-image:latest ."

-You can check the image created using "docker images"

-Run the app image inside a container using "docker run -d -p 5000:5000 --name flask-container flask-image" 

-Check running docker container by "docker ps"

-App will now be running at this address : http://0.0.0.0:5000