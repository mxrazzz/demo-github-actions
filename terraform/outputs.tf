# after apply, see the info in terminal 
output "container_name" {
  description = "Name of the running container"
  value       = docker_container.flask_container.name
}

output "app_url" {
  description = "URL to access the application"
  value       = "http://localhost:${var.container_port}"
}