terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.0"  
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
