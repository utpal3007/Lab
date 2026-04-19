resource "azurerm_resource_group" "rg" {
  name     = "ai-agent-test-rg"
  location = "westeurope"

  tags = {
    environment = "test"
  }
}
