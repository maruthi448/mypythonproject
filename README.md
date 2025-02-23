
git config --global user.email “mailid@.com"
git config --global user.name "username"

Git add .
Git status
Git commit -m “changes”
Git push origin

Git remote -v

Git remote add  origin git url

How to add system variables in Mac
~/.zshrc    or ~/.bashrc

export API_USERNAME="myusername"
export API_PASSWORD="mypassword"


source ~/.bashrc  
or 
source ~/.zshrc

——————————————————
Create a virtual python process

python3 -m venv myenv

source myenv/bin/activate

To deactivate:deactivate 

Install dependencies 
pip install pyyaml gitpython cryptography
pip install fastapi uvicorn gitpython pyyaml



To run the python project

uvicorn app:app --host 0.0.0.0 --port 8000 --reload

Python.py is the script and app = FastAPI()

uvicorn python:app -—host 0.0.0 -—port 8080 -—reload

http://localhost:8000/gitpushtotargeturl

http://localhost:8000/home

docker commands:
#check docker demon is running or not
ps aux | grep docker

#to get the info about docker
docker info
#build the docker image
docker build -t mypython-gitproject-to-push-target-repo .

#run the docker image
docker run -p 8000:8000 mypython-gitproject-to-push-target-repo
#or
docker run -p 8081:8081 -e GIT_USERNAME=$GIT_USERNAME -e GIT_TOKEN=$GIT_TOKEN my-fastapi-app
#or
docker run --env-file .env -p 8081:8081 my-fastapi-app


note:
uvicorn app:app --host 0.0.0.0 --port 8000
docker run -p 8081:8000 mypython-gitproject-to-push-target-repo

docker run -d --env-file .env -p 8081:8081 mypython-gitproject-to-push-target-repo
docker logs -f <container_id>  # Check logs interactively
docker exec -it <container_id> /bin/sh  # Enter the running container



uvicorn app:app --host 0.0.0.0 --port 8081
docker run -p 8081:8081 my-project

#docker commands
docker --version   # Check Docker version
docker info   # Get system-wide info about Docker

#Container Management
docker ps                      # List running containers
docker ps -a                   # List all containers (including stopped ones)
docker start <container_id>     # Start a stopped container
docker stop <container_id>      # Stop a running container
docker restart <container_id>   # Restart a container
docker rm <container_id>        # Remove a stopped container
docker logs <container_id>      # View logs of a container
docker exec -it <container_id> /bin/sh  # Access container shell (for Alpine-based containers)
docker exec -it <container_id> /bin/bash  # Access shell (for Ubuntu-based containers)

#Image Management
docker images                  # List all images
docker rmi <image_id>           # Remove an image
docker pull <image_name>        # Download an image from Docker Hub
docker build -t my-app .        # Build an image from Dockerfile (in current directory)

#Running Containers
docker run -d -p 8080:80 my-app   # Run a container in detached mode, mapping ports
docker run -it ubuntu /bin/bash   # Run an interactive Ubuntu container
docker run --name my-container -p 5000:5000 my-app  # Run container with a custom name

#Network & Volume Management
docker network ls                # List networks
docker volume ls                 # List volumes
docker network create my-network # Create a new network
docker volume create my-volume   # Create a new volume


#Docker Compose
docker-compose up                # Start services defined in `docker-compose.yml`
docker-compose up -d             # Start services in detached mode
docker-compose down              # Stop all services
docker-compose ps                # List services

#Clean Up Unused Resources
docker system prune              # Remove all stopped containers, unused networks, and dangling images
docker volume prune              # Remove unused volumes
docker image prune               # Remove unused images
docker container prune           # Remove stopped containers

#Debugging & Inspecting
docker inspect <container_id>     # Get details about a container
docker stats                      # Show live container stats (CPU, RAM, etc.)
docker top <container_id>          # Display running processes inside a container


--------------------------------------------------------------

Manually Running Containers
If you don't want docker-compose, you can manually start each container:

1️⃣ Run FastAPI Container

docker run -d --name mypython-app -p 8081:8081 \
  -e OPENOBSERVE_URL=http://localhost:5080 \
  -e OPENOBSERVE_USER=your-email@example.com \
  -e OPENOBSERVE_PASSWORD=your-password \
  mypython-app-image

2️⃣ Run Prometheus Container

docker run -d --name prometheus -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
3️⃣ Run OpenObserve Container
docker run -d --name openobserve -p 5080:5080 \
  -e ZO_ROOT_USER_EMAIL=your-email@example.com \
  -e ZO_ROOT_USER_PASSWORD=your-password \
  public.ecr.aws/zinclabs/openobserve:latest
4️⃣ Manually Connect Containers to the Same Network

docker network create monitoring
docker network connect monitoring mypython-app
docker network connect monitoring prometheus
docker network connect monitoring openobserve
🔹 Summary: Why Use docker-compose.yml?
✅ Easier management – Start all services with docker-compose up -d
✅ Automatic networking – No need to manually link containers
✅ Environment variables in one place – No long docker run commands
✅ Persistent storage support – Save Prometheus data easily
✅ Scalability – Easily add replicas of FastAPI app










