variable "resource_group_name" {
  description = "Name of the main resource group"
  type        = string
  default     = "ai-agent-test-rg"
}

variable "storage_account_name" {
  description = "Name of the storage account (3-24 lowercase alphanumeric)"
  type        = string
  default     = "tfstateai13"
}

variable "location" {
  description = "Azure region for all resources"
  type        = string
  default     = "westeurope"
}

variable "environment" {
  description = "Deployment environment: dev, staging, prod"
  type        = string
  default     = "dev"
}
