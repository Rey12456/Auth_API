terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.0"  
    }
    google = {
      source  = "hashicorp/google"
      version = ">= 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example_rg" {
  name     = "example-resource-group"
  location = "southcentralus"
  
  tags = {
    environment = "dev"
    source      = "terraform"
  }
}

output "resource_group_id" {
  description = "ID of the created resource group"
  value       = azurerm_resource_group.example_rg.id
}

output "resource_group_location" {
  description = "Location of the created resource group"
  value       = azurerm_resource_group.example_rg.location
}

output "resource_group_tags" {
  description = "Tags of the created resource group"
  value       = azurerm_resource_group.example_rg.tags
}
