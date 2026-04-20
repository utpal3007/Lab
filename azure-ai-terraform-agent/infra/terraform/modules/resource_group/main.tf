resource "azurerm_resource_group" "this" {
  name     = var.name
  location = var.location

  tags = merge(
    {
      environment = var.environment
      managed_by  = "terraform"
    },
    var.extra_tags
  )
}
