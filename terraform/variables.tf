# reference by using var.{name}
variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "flask-app"
}

variable "container_port" {
  description = "Port the container exposes"
  type        = number
  default     = 5000
}