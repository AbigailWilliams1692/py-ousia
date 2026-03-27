# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from datetime import date, datetime
from typing import Any, Union

# Third-Party Packages
import pandas as pd

# Local Packages
from ousia.finance_model.finance_attribute.series.series import Series


#############################################################
# TimeSeries Class
#############################################################
class TimeSeries(Series):

    """
    TimeSeries class for time-indexed series attributes in the Ousia finance model framework.
    
    This class represents a series with a datetime-based index (date, datetime, or Timestamp).
    It provides functionality for time series validation, serialization, and deserialization.
    """
    
    #############################################################
    # Class Attributes
    #############################################################
    _valid_index_types = (date, datetime, pd.Timestamp)

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: pd.Series, name: str = "TimeSeries"):
        """
        Constructor for the TimeSeries class.
        
        Args:
            value (pd.Series): The time series value. Index must be date, datetime, or pd.Timestamp.
            name (str): The name of the attribute.
        Returns:
            TimeSeries: The created time series object.
        Raises:
            TypeError: If the series index is not a valid datetime type.
        """
        self._validate_index(value=value)
        super().__init__(value=value, name=name)

    #############################################################
    # Validation Methods
    #############################################################
    def _validate_index(self, value: pd.Series) -> None:
        """
        Validate that the series index is a valid datetime type.
        
        Args:
            value (pd.Series): The series to validate.
        Raises:
            TypeError: If the series index is not a valid datetime type.
        """
        if len(value) == 0:
            return
        
        # Check if index is DatetimeIndex
        if isinstance(value.index, pd.DatetimeIndex):
            return
        
        # Check if all index values are valid datetime types
        for idx in value.index:
            if not isinstance(idx, self._valid_index_types):
                raise TypeError(
                    f"TimeSeries index must be of type date, datetime, or pd.Timestamp. "
                    f"Got {type(idx).__name__} for index value: {idx}"
                )

    #############################################################
    # Getter & Setter Methods
    #############################################################
    def set_series(self, series: pd.Series) -> None:
        """
        Set the series with index validation.
        
        Args:
            series (pd.Series): The series to set.
        Raises:
            TypeError: If the series index is not a valid datetime type.
        """
        self._validate_index(value=series)
        self.value = series

    def get_value_at_date(self, dt: Union[date, datetime, pd.Timestamp]) -> Any:
        """
        Get the value at the specified date/datetime.
        
        Args:
            dt (Union[date, datetime, pd.Timestamp]): The date/datetime to get the value for.
        Returns:
            Any: The value at the specified date/datetime.
        """
        return self.value.loc[dt]

    def set_value_at_date(self, dt: Union[date, datetime, pd.Timestamp], value: Any) -> None:
        """
        Set the value at the specified date/datetime.
        
        Args:
            dt (Union[date, datetime, pd.Timestamp]): The date/datetime to set the value for.
            value (Any): The value to set.
        """
        self.value.loc[dt] = value
    
    def get_values_by_date_range(self, start: Union[date, datetime, pd.Timestamp], end: Union[date, datetime, pd.Timestamp]) -> pd.Series:
        """
        Get a subset of the time series within the specified date range.
        
        Args:
            start (Union[date, datetime, pd.Timestamp]): The start date.
            end (Union[date, datetime, pd.Timestamp]): The end date.
        Returns:
            pd.Series: The subset of the time series within the date range.
        """
        return self.value.loc[start:end]

    def get_start_date(self) -> Union[date, datetime, pd.Timestamp]:
        """
        Get the start date of the time series.
        
        Returns:
            Union[date, datetime, pd.Timestamp]: The start date.
        """
        return self.value.index.min()

    def get_end_date(self) -> Union[date, datetime, pd.Timestamp]:
        """
        Get the end date of the time series.
        
        Returns:
            Union[date, datetime, pd.Timestamp]: The end date.
        """
        return self.value.index.max()
