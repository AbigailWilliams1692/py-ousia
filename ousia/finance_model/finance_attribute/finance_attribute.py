# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from abc import ABC
from typing import Any

# Local Packages
from ousia.base_model.attribute.attribute import Attribute


#############################################################
# FinanceAttribute Class
#############################################################
class FinanceAttribute(Attribute, ABC):
    
    """
    Base class for all finance attributes in the Ousia framework.
    
    This class serves as the foundation for all finance attribute types in the framework.
    It provides common functionality and enforces a consistent interface for
    finance attribute validation, serialization, and deserialization.
    """
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, name: str, data_type: type, value: Any = None):
        """
        Constructor for the FinanceAttribute class.
        
        Args:
            name (str): The name of the attribute.
            data_type (type): The data type of the attribute.
            value (Any, optional): The value of the attribute. Defaults to None.
        Returns:
            FinanceAttribute: The created finance attribute object.
        """
        super().__init__(name=name, data_type=data_type, value=value)
