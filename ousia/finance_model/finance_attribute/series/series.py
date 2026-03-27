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
# Series Class
#############################################################
class Series(FinanceAttribute, ABC):

    """
    Base class for all series attributes in the Ousia finance model framework.
    
    This class serves as the foundation for all series attribute types in the framework.
    It provides common functionality and enforces a consistent interface for finance
    series attribute validation, serialization, and deserialization.
    """
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: pd.Series, name: str = "Series"):
        """
        Constructor for the Series class.
        
        Args:
            name (str): The name of the attribute.
            value (pd.Series): The series value.
        Returns:
            Series: The created series object.
        """
        super().__init__(value=value, name=name)

    #############################################################
    # Getter & Setter Methods
    #############################################################
    def get_series(self) -> pd.Series:
        """
        Get the series.
        
        Returns:
            pd.Series: The series.
        """
        return self.value

    def set_series(self, series: pd.Series):
        """
        Set the series.
        
        Args:
            series (pd.Series): The series.
        """
        self.value = series

    def get_value(self, index: Any) -> Any:
        """
        Get the value at the specified index.
        
        Args:
            index (Any): The index of the value to get.
        Returns:
            Any: The value at the specified index.
        """
        return self.value.loc[index]

    def set_value(self, index: Any, value: Any):
        """
        Set the value at the specified index.
        
        Args:
            index (Any): The index of the value to set.
            value (Any): The value to set.
        """
        self.value.loc[index] = value
