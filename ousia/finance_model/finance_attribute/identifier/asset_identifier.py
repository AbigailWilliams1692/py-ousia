# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from abc import ABC

# Local Packages
from ousia.finance_model.finance_attribute.finance_identifier.finance_identifier import FinanceIdentifier


#############################################################
# Asset Identifier Classes
#############################################################
class AssetIdentifier(FinanceIdentifier):

    """
    Asset identifier class, base class for various asset identifier classes.
    """

    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["Asset Identifier"]
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "AssetIdentifier"):
        super().__init__(value=value, name=name)


class CUSIP(AssetIdentifier):
    """
    CUSIP identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["cusip"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "CUSIP"):
        super().__init__(value=value, name=name)


class SEDOL(AssetIdentifier):
    """
    SEDOL identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["sedol"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "SEDOL"):
        super().__init__(value=value, name=name)


class ISIN(AssetIdentifier):
    """
    ISIN identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["isin"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "ISIN"):
        super().__init__(value=value, name=name)


class BloombergTicker(AssetIdentifier):
    """
    Bloomberg Ticker identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["bloomberg_ticker", "bbg_ticker", "Bloomberg Ticker"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "BloombergTicker"):
        super().__init__(value=value, name=name)


class Ticker(AssetIdentifier):
    """
    Ticker identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["ticker", "TICKER"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "Ticker"):
        super().__init__(value=value, name=name)


class Issuer(AssetIdentifier):
    """
    Issuer identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["issuer", "ISSUER"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "Issuer"):
        super().__init__(value=value, name=name)


class EstId(AssetIdentifier):
    """
    EstId identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["est_id", "estid", "EST_ID", "ESTID"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "EstId"):
        super().__init__(value=value, name=name)
