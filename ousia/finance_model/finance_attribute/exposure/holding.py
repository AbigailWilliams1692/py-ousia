# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from enum import Enum
from typing import Dict, List, TYPE_CHECKING, Union

# Third Party Packages
import pandas as pd

# Local Packages
if TYPE_CHECKING:
    from ousia.finance_model.finance_attribute.asset.asset import Asset
from ousia.finance_model.finance_attribute.exposure.exposure import Exposure


#############################################################
# HoldingUnit Class
#############################################################
class HoldingUnit(Enum):
    """
    Holding unit enum. Represents the unit of a holding.
    """
    WEIGHT = "WEIGHT"
    SHARE = "SHARE"
    VALUE = "VALUE"


#############################################################
# Holding Class
#############################################################
class Holding(Exposure):
    
    """
    Holding class. Represents the holding of a portfolio.
    """
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: Dict["Asset", Union[float, int]], name: str = "Holding", holding_unit: HoldingUnit = HoldingUnit.WEIGHT):
        """
        Constructor for the Holding class.
        
        Args:
            value (Dict[Entity, Any]): The value of the holding.
            name (str): The name of the holding.
            holding_unit (HoldingUnit): The unit of the holding.
        Returns:
            Holding: The created holding object.
        """
        super().__init__(value=value, name=name)
        self.holding_unit = holding_unit

    #############################################################
    # Getter & Setter Methods
    #############################################################
    def get_holding_unit(self) -> HoldingUnit:
        """
        Get the holding unit.
        
        Returns:
            HoldingUnit: The holding unit.
        """
        return self.holding_unit
    
    def set_holding_unit(self, holding_unit: HoldingUnit) -> None:
        """
        Set the holding unit.
        
        Args:
            holding_unit (HoldingUnit): The holding unit.
        """
        self.holding_unit = holding_unit

    def get_holding_value(self, asset: "Asset") -> Union[float, int]:
        """
        Get the holding value for a specific asset.
        
        Args:
            asset (Asset): The asset to get the holding value for.
        
        Returns:
            Union[float, int]: The holding value.
        """
        return self.value.get(asset, 0.0)

    def set_holding_value(self, asset: "Asset", value: Union[float, int]) -> None:
        """
        Set the holding value for a specific asset.
        
        Args:
            asset (Asset): The asset to set the holding value for.
            value (Union[float, int]): The holding value.
        """
        self.value[asset] = value

    def get_all_holdings(self) -> Dict["Asset", Union[float, int]]:
        """
        Get the holding contents.
        
        Returns:
            Dict[Entity, Any]: The holdings.
        """
        return self.value
    
    def set_all_holdings(self, holdings: Dict["Asset", Union[float, int]]) -> None:
        """
        Set the holdings.
        
        Args:
            holdings (Dict[Entity, Union[float, int]]): The holdings.
        """
        self.value = holdings

    def get_total_holding_units(self) -> Union[float, int]:
        """
        Get the total holding units.
        
        Returns:
            float: The total holding units.
        """
        total = sum(self.value.values())
        if self.get_holding_unit() == HoldingUnit.SHARE:
            total = int(total)
        return total

    def get_all_assets(self) -> List["Asset"]:
        """
        Get all assets in the holding.
        
        Returns:
            List[Asset]: The list of assets.
        """
        return list(self.value.keys())

    #############################################################
    # Conversion Methods
    #############################################################
    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert the holding to a DataFrame that contains the dataframe form of each asset and its holding value
        in one row.
        
        Returns:
            pd.DataFrame: The holding as a DataFrame.
        """
        # Initialize a list container
        rows = []

        # Iterate through each asset and its holding value
        for asset, holding_value in self.value.items():
            asset_df = asset.to_dataframe()
            asset_df[self.name] = holding_value
            asset_df["HoldingUnit"] = self.holding_unit.value
            rows.append(asset_df)
        
        if not rows:
            return pd.DataFrame()
        
        return pd.concat(objs=rows, axis=0, ignore_index=True)
