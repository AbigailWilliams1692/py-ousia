# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from datetime import date, datetime
from typing import Dict, List, Optional, Set, Union, TYPE_CHECKING

# Third-Party Packages
import pandas as pd

# Local Packages
from ousia.finance_model.finance_attribute.series.timeseries import TimeSeries
from ousia.finance_model.finance_attribute.exposure.holding import Holding, HoldingUnit

if TYPE_CHECKING:
    from ousia.finance_model.finance_entity.asset import Asset


#############################################################
# HoldingTimeSeries Class
#############################################################
class HoldingTimeSeries(TimeSeries):

    """
    HoldingTimeSeries class for time-indexed holding series in the Ousia finance model framework.
    
    This class represents a time series where each value is a Holding object,
    allowing tracking of portfolio holdings over time.
    """

    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: pd.Series, name: str = "HoldingTimeSeries"):
        """
        Constructor for the HoldingTimeSeries class.
        
        Args:
            value (pd.Series): The time series of Holding objects. Index must be date, datetime, or pd.Timestamp.
            name (str): The name of the attribute.
        Returns:
            HoldingTimeSeries: The created holding time series object.
        Raises:
            TypeError: If the series index is not a valid datetime type or values are not Holding objects.
        """
        self._validate_holdings(value=value)
        super().__init__(value=value, name=name)

    #############################################################
    # Validation Methods
    #############################################################
    @staticmethod
    def _validate_holdings(value: pd.Series) -> None:
        """
        Validate that all values in the series are Holding objects.
        
        Args:
            value (pd.Series): The series to validate.
        Raises:
            TypeError: If any value is not a Holding object.
        """
        if len(value) == 0:
            return
        
        for idx, val in value.items():
            if not isinstance(val, Holding):
                raise TypeError(
                    f"HoldingTimeSeries values must be Holding objects. "
                    f"Got {type(val).__name__} at index: {idx}"
                )

    #############################################################
    # Getter & Setter Methods
    #############################################################
    def set_series(self, series: pd.Series) -> None:
        """
        Set the series with index and holding validation.
        
        Args:
            series (pd.Series): The series to set.
        Raises:
            TypeError: If the series index is not valid or values are not Holding objects.
        """
        self._validate_index(value=series)
        self._validate_holdings(value=series)
        self.value = series

    def get_holding_at_date(self, dt: Union[date, datetime, pd.Timestamp]) -> Holding:
        """
        Get the Holding object at the specified date.
        
        Args:
            dt (Union[date, datetime, pd.Timestamp]): The date to get the holding for.
        Returns:
            Holding: The Holding object at the specified date.
        """
        return self.value.loc[dt]

    def set_holding_at_date(self, dt: Union[date, datetime, pd.Timestamp], holding: Holding) -> None:
        """
        Set the Holding object at the specified date.
        
        Args:
            dt (Union[date, datetime, pd.Timestamp]): The date to set the holding for.
            holding (Holding): The Holding object to set.
        Raises:
            TypeError: If the value is not a Holding object.
        """
        if not isinstance(holding, Holding):
            raise TypeError(f"Value must be a Holding object. Got {type(holding).__name__}")
        self.value.loc[dt] = holding

    def get_holding_value_at_date(self, dt: Union[date, datetime, pd.Timestamp], asset: "Asset") -> Union[float, int]:
        """
        Get the holding value for a specific asset at a specific date.
        
        Args:
            dt (Union[date, datetime, pd.Timestamp]): The date to get the holding for.
            asset (Asset): The asset to get the holding value for.
        Returns:
            Union[float, int]: The holding value for the asset at the date.
        """
        holding = self.get_holding_at_date(dt=dt)
        return holding.get_holding_value(asset=asset)

    def get_asset_holdings_over_time(self, asset: "Asset") -> pd.Series:
        """
        Get the holding values for a specific asset across all dates.
        
        Args:
            asset (Asset): The asset to get the holding values for.
        Returns:
            pd.Series: A time series of holding values for the asset.
        """
        return pd.Series(
            {dt: holding.get_holding_value(asset=asset) for dt, holding in self.value.items()},
            name=f"{asset}_holdings"
        )

    def get_holding_unit_at_date(self, dt: Union[date, datetime, pd.Timestamp]) -> HoldingUnit:
        """
        Get the holding unit for a specific date.
        
        Args:
            dt (Union[date, datetime, pd.Timestamp]): The date to get the holding unit for.
        Returns:
            HoldingUnit: The holding unit for the date.
        """
        holding = self.get_holding_at_date(dt=dt)
        return holding.get_holding_unit()

    #############################################################
    # Asset Statistics Methods
    #############################################################
    def get_all_assets_over_time(self) -> List["Asset"]:
        """
        Get all unique assets across all holdings in the time series.
        
        Returns:
            List[Asset]: A list of all unique assets.
        """
        all_assets = set()
        for holding in self.value:
            all_assets.update(holding.get_all_assets())
        return list(all_assets)

    def get_all_assets_at_date(self, dt: Union[date, datetime, pd.Timestamp]) -> List["Asset"]:
        """
        Get all unique assets at a specific date.
        
        Args:
            dt (Union[date, datetime, pd.Timestamp]): The date to get the assets for.
        Returns:
            List[Asset]: A list of all unique assets at the specified date.
        """
        holding = self.get_holding_at_date(dt=dt)
        return holding.get_all_assets()

    #############################################################
    # Conversion Methods
    #############################################################
    def to_dataframes(self) -> Dict[Union[date, datetime, pd.Timestamp], pd.DataFrame]:
        """
        Convert each holding in the time series to a DataFrame.
        
        Returns:
            Dict[Union[date, datetime, pd.Timestamp], pd.DataFrame]: A dictionary with dates as keys and DataFrames as values.
        """
        return {dt: holding.to_dataframe() for dt, holding in self.value.items()}
