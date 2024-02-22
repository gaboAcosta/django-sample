variable "project" {}

variable "container_image" {}

variable "sql_instance" {}
variable "secret_django_secret" {}
variable "secret_database_name" {}
variable "secret_database_password" {}
variable "secret_database_host" {}

variable "secret_firebase_project_id" {}
variable "secret_firebase_private_key_id" {}
variable "secret_firebase_private_key" {}
variable "secret_firebase_client_email" {}
variable "secret_firebase_client_id" {}
variable "secret_firebase_cert_url" {}


variable "region" {
  default = "us-central1"
}

variable "zone" {
  default = "us-central1-c"
}
