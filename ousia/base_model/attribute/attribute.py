# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from abc import ABC
from typing import Any

#############################################################
# Attribute Class
#############################################################
class Attribute(ABC):
    
    """
    Base class for all attributes in the Ousia framework.
    
    This class serves as the foundation for all attribute types in the framework.
    It provides common functionality and enforces a consistent interface for
    attribute validation, serialization, and deserialization.
    """

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, name: str, data_type: type, value: Any):
        """
        Constructor for the Attribute class.
        
        Args:
            name (str): The name of the attribute.
            data_type (type): The data type of the attribute.
            value (Any): The value of the attribute.
        Returns:
            Attribute: The created attribute object.
        """
        self._name = name
        self._data_type = data_type
        # Check value type before setting
        self.validate_value(value=value, data_type=data_type)
        self._value = value

    def __str__(self):
        """
        String representation of the attribute.
        
        Returns:
            str: The string representation of the attribute.
        """
        return f"{self.__class__.__name__}[{id(self)}][{self._name}: {self._value.__repr__()}]"

    def __repr__(self):
        """
        String representation of the attribute.
        
        Returns:
            str: The string representation of the attribute.
        """
        return f"{self.__class__.__name__}[{id(self)}]"

    #############################################################
    # Properties
    #############################################################
    @property
    def name(self) -> str:
        """
        Get the name of the attribute.
        
        Returns:
            str: The name of the attribute.
        """
        return self._name
    
    @name.setter
    def name(self, name: str):
        """
        Set the name of the attribute.
        
        Args:
            name (str): The name of the attribute.
        """
        self._name = name
    
    @property
    def data_type(self) -> type:
        """
        Get the data type of the attribute.
        
        Returns:
            type: The data type of the attribute.
        """
        return self._data_type
    
    @data_type.setter
    def data_type(self, data_type: type):
        """
        Set the data type of the attribute.
        
        Args:
            data_type (type): The data type of the attribute.
        """
        self._data_type = data_type
    
    @property
    def value(self) -> Any:
        """
        Get the value of the attribute.
        
        Returns:
            Any: The value of the attribute.
        """
        return self._value
    
    @value.setter
    def value(self, value: Any):
        """
        Set the value of the attribute.
        
        Args:
            value (Any): The value of the attribute.
        """
        # Check the data type of the value to set
        self.validate_value(value=value, data_type=self._data_type)
        self._value = value

    #############################################################
    # Util Methods
    #############################################################
    @staticmethod
    def validate_value(value: Any, data_type: type) -> None:
        if not self.validate_value(value, data_type):
            raise TypeError(f"Value must be of type {data_type}")
    