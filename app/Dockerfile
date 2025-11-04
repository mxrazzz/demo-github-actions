#instructions to create a docker image for our python app

# we get the python image as its a python app - for other languages we do diff containers
FROM python:3.11-slim

# Set  working directory inside the container
WORKDIR /app 

# place the requirements file inside /app (current wd)
COPY requirements.txt . 

#this installs dependencies now using RUN , no cache to save space
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the application code to the container
COPY app.py .

# doc that tells us it runs on port 5000
EXPOSE 5000 

# Command to run the application (runs directly as exec form)
CMD ["python", "app.py"]

# Build the Docker image with:
# docker build -t flask-app:v1 .

# Run the Docker container with: (docker desktop must be running)

# docker run -d -p 5000:5000 --name flask-container flask-app:v1
# -d means it runs detached so in background
# -p 5000:5000 maps port 5000 in my pc to port 5000 in the container -> like a tunnel
# --name gives the container a name flask-container
# flask-app:v1 is the image name we built above

# To stop and remove the container:
# docker stop flask-container
# docker rm flask-container