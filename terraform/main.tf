# the providers is docker as we are building a container
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/dockerDesktopLinuxEngine"
}

# will now build a docker image called flask_app, 
resource "docker_image" "flask_app" {
  name = "flask-app:v1"
  build {
    context = "../app" # using the dockerfile found in /app. 
    tag     = ["flask-app:v1"] #version control, e.g. v2/v3
  }
}

# now build the actual container
resource "docker_container" "flask_container" {
  name  = "${var.app_name}-container"
  image = docker_image.flask_app.name

  ports {
    internal = var.container_port
    external = var.container_port
  }
}

#navigate to terraform folder, then run the 3 commands: init, plan, apply
#creates a tfstate file - make sure the container is the same, and has the same configs