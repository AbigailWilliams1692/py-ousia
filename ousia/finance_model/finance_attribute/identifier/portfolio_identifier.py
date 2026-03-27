# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from abc import ABC

# Local Packages
from ousia.finance_model.finance_attribute.finance_identifier.asset_identifier import AssetIdentifier


#############################################################
# Portfolio Identifier Classes
#############################################################
class PortfolioIdentifier(AssetIdentifier):

    """
    Portfolio identifier class, base class for various portfolio identifier classes.
    """

    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["Portfolio Identifier"]
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "PortfolioIdentifier"):
        super().__init__(value=value, name=name)


class PortfolioName(PortfolioIdentifier):
    """
    PortfolioName identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["portfolio_name", "port_name", "Portfolio Name"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "PortfolioName"):
        super().__init__(value=value, name=name)


class PortfolioFullName(PortfolioIdentifier):
    """
    PortfolioFullName identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["portfolio_full_name", "port_full_name", "Portfolio Full Name"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "PortfolioFullName"):
        super().__init__(value=value, name=name)


class PortfolioCode(PortfolioIdentifier):
    """
    PortfolioCode identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["portfolio_code", "port_code", "Portfolio Code"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "PortfolioCode"):
        super().__init__(value=value, name=name)
