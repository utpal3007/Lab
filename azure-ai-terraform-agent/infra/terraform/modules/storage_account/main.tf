resource "azurerm_storage_account" "this" {
  name                     = var.name
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = var.account_tier
  account_replication_type = var.replication_type

  # Secure defaults
  min_tls_version                 = "TLS1_2"
  https_traffic_only_enabled      = true
  allow_nested_items_to_be_public = false

  blob_properties {
    delete_retention_policy {
      days = var.blob_soft_delete_days
    }
  }

  tags = merge(
    {
      environment = var.environment
      managed_by  = "terraform"
    },
    var.extra_tags
  )
}
