variable "name" {
  description = "Storage account name (3-24 lowercase alphanumeric)"
  type        = string

  validation {
    condition     = can(regex("^[a-z0-9]{3,24}$", var.name))
    error_message = "Storage account name must be 3-24 lowercase alphanumeric characters."
  }
}

variable "resource_group_name" {
  description = "Resource group that owns this storage account"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "westeurope"
}

variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "account_tier" {
  description = "Performance tier: Standard or Premium"
  type        = string
  default     = "Standard"

  validation {
    condition     = contains(["Standard", "Premium"], var.account_tier)
    error_message = "account_tier must be Standard or Premium."
  }
}

variable "replication_type" {
  description = "Replication strategy: LRS, GRS, ZRS, GZRS, RAGRS, RAGZRS"
  type        = string
  default     = "LRS"
}

variable "blob_soft_delete_days" {
  description = "Days to retain deleted blobs (0 = disabled)"
  type        = number
  default     = 7
}

variable "extra_tags" {
  description = "Additional tags to apply"
  type        = map(string)
  default     = {}
}
