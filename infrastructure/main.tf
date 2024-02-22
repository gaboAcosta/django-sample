terraform {
  backend "gcs" {
    bucket = "gabo-acosta-terraform-bucket"
    prefix = "terraform/state"
  }
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
  zone    = var.zone
}

# [START cloudrun_service]
resource "google_cloud_run_v2_service" "default" {
  location = "us-central1"
  name     = "django-test-service"

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello"
    }
  }
}
# [END cloudrun_service_tasks_service]

# [START cloudrun_service_tasks_sa]
resource "google_service_account" "default" {
  account_id   = "cloud-run-task-invoker"
  display_name = "Cloud Run Task Invoker"
}
# [END cloudrun_service_tasks_sa]

# [START cloudrun_service_tasks_run_invoke_permissions]
resource "google_cloud_run_service_iam_binding" "default" {
  location = google_cloud_run_v2_service.default.location
  service  = google_cloud_run_v2_service.default.name
  role     = "roles/run.invoker"
  members  = ["allUsers"]
}
# [END cloudrun_service_tasks_run_invoke_permissions]

# [START cloudrun_service_tasks_token_permissions]
resource "google_project_iam_binding" "project_binding" {
  project = google_cloud_run_v2_service.default.project
  role    = "roles/iam.serviceAccountTokenCreator"
  members = ["serviceAccount:${google_service_account.default.email}"]
}
# [END cloudrun_service_tasks_token_permissions]

# [START artifact_registry_repository]
resource "google_artifact_registry_repository" "my-repo" {
  location      = "us-central1"
  repository_id = "django-test-service-repository"
  description   = "Django app images repository"
  format        = "DOCKER"
}
# [END artifact_registry_repository]