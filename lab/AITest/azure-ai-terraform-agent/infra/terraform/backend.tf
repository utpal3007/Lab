terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstateai13"
    container_name       = "tfstate"
    key                  = "dev.tfstate"
  }
}