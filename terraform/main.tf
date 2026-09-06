terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" { region = var.aws_region }

module "network" {
  source = "./modules/network"
  name   = "gitops-${var.environment}"
  cidr   = var.vpc_cidr
  tags   = var.tags
}

module "platform" {
  source     = "./modules/platform"
  name       = "gitops-${var.environment}"
  subnet_ids = module.network.private_subnet_ids
  tags       = var.tags
}
