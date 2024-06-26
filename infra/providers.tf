terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.14.0"
    }
  }

  required_version = "~> 1.5.2"
}

provider "aws" {
  region = "us-west-1"
}
