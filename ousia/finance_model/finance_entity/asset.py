# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from typing import List, Type

# Third-Party Packages
import pandas as pd

# Local Packages
from ousia.finance_model.finance_entity.finance_entity import FinanceEntity
from ousia.finance_model.finance_attribute.finance_attribute import FinanceAttribute
from ousia.finance_model.finance_identifier.asset_identifier import AssetIdentifier


#############################################################
# Asset Class
#############################################################
class Asset(FinanceEntity):

    """
    Asset class. Represents a financial asset.
    
    This class serves as the foundation for all asset types in the framework.
    It provides common functionality and enforces a consistent interface for
    asset validation, serialization, and deserialization.
    """
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, *attributes: tuple[FinanceAttribute, ...]):
        """
        Constructor for the Asset class.
        
        Args:
            *attributes (tuple[FinanceAttribute, ...]): The finance attributes of the asset.
        """
        super().__init__(*attributes)

        # Check if this asset has at least one identifier
        self._check_identifier()

    #############################################################
    # Asset Identifier Methods
    #############################################################
    def _get_identifier_type(self) -> Type[AssetIdentifier]:
        """
        Get the type of identifier for this asset.
        
        Returns:
            Type[AssetIdentifier]: The type of identifier for this asset.
        """
        return AssetIdentifier
        