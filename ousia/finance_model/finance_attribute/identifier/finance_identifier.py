# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from abc import ABC

# Local Packages
from ousia.finance_model.finance_attribute.finance_attribute import FinanceAttribute


#############################################################
# FinanceIdentifier Class
#############################################################
class FinanceIdentifier(FinanceAttribute, ABC):

    """
    Base class for all identifier attributes in the Ousia finance model framework.
    
    This class serves as the foundation for all identifier attribute types in the framework.
    It provides common functionality and enforces a consistent interface for finance
    identifier attribute validation, serialization, and deserialization.
    """
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: str, name: str = "FinanceIdentifier"):
        """
        Constructor for the FinanceIdentifier class.
        
        Args:
            name (str): The name of the attribute.
            data_type (type): The data type of the attribute.
            value (Any, optional): The value of the attribute. Defaults to None.
        Returns:
            FinanceIdentifier: The created finance identifier object.
        """
        super().__init__(name=name, data_type=str, value=value)
