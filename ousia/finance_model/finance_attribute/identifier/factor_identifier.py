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
# Factor Identifier Classes
#############################################################
class FactorIdentifier(FinanceIdentifier):

    """
    Factor identifier class, base class for various factor identifier classes.
    """

    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["Factor Identifier"]
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "FactorIdentifier"):
        super().__init__(value=value, name=name)


class FactorName(FactorIdentifier):
    """
    FactorName identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["factor_name", "fname", "Factor Name"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "FactorName"):
        super().__init__(value=value, name=name)


class FactorFullName(FactorIdentifier):
    """
    FactorFullName identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["factor_full_name", "Factor Full Name"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "FactorFullName"):
        super().__init__(value=value, name=name)


class FactorTag(FactorIdentifier):
    """
    FactorTag identifier class.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _registry_aliases = ["factor_tag", "ftag", "Factor Tag"]

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "FactorTag"):
        super().__init__(value=value, name=name)
