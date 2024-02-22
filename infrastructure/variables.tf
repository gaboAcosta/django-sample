variable "project" {}
variable "sql_instance" {}
variable "secret_django_secret" {}
variable "secret_database_name" {}
variable "secret_database_password" {}
variable "secret_database_host" {}

variable "region" {
  default = "us-central1"
}

variable "zone" {
  default = "us-central1-c"
}
