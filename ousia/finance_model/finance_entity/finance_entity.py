# !usr/bin/env python3
# -*- coding: utf-8 -*-
 
#############################################################
# Import Libraries
#############################################################
# Standard Packages
from abc import ABC
from typing import Any, Dict, Optional, Type, Union
 
# Third-Party Packages
import pandas as pd
 
# Local Packages
from ousia.base_model.entity.entity import Entity
from ousia.finance_model.finance_attribute.finance_attribute import FinanceAttribute
from ousia.finance_model.finance_attribute.identifier.finance_identifier import FinanceIdentifier
 
 
#############################################################
# FinanceEntity Class
#############################################################
class FinanceEntity(Entity, ABC):
 
    """
    Base class for all finance entities in the Ousia framework.
 
    This class serves as the foundation for all finance entity types in the framework.
    It provides common functionality and enforces a consistent interface for
    finance entity validation, serialization, and deserialization.
    """
 
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, *attributes: tuple[FinanceAttribute, ...]):
        """
        Constructor for the FinanceEntity class.
 
        Args:
            *attributes (tuple[FinanceAttribute, ...]): The finance attributes of the entity.
        """
        super().__init__(*attributes)

    #############################################################
    # Finance Identifier Methods
    #############################################################
    def _get_identifier_type(self) -> Type[FinanceIdentifier]:
        """
        Get the identifier type for this finance entity.
        
        Returns:
            Type[AssetIdentifier]: The identifier type for this finance entity.
        """
        return FinanceIdentifier

    def _check_identifier(self) -> bool:
        """
        Check if this finance entity has an identifier.
        
        Returns:
            bool: True if this finance entity has an identifier, False otherwise.
        """
        id_type = self._get_identifier_type()
        has_id = any(isinstance(attribute, id_type) for attribute in self.get_attributes().values())
        if not has_id:
            raise ValueError(f"{self.__class__.__name__} must have at leat one identifier!")

    def get_all_identifiers(self) -> List[FinanceIdentifier]:
        """
        Get all identifiers of this finance entity.
        
        Returns:
            list[AssetIdentifier]: A list of all identifiers of this finance entity.
        """
        id_type = self._get_identifier_type()
        return [attribute for attribute in self.get_attributes().values() if isinstance(attribute, id_type)]

    def get_all_identifiers_df(self) -> pd.DataFrame:
        """
        Get all identifiers of this finance entity as a DataFrame.
        
        Returns:
            pd.DataFrame: A DataFrame containing all identifiers of this finance entity.
        """
        # Generate a dataframe with each identifier as a column
        return pd.DataFrame([{identifier.name: identifier.value} for identifier in self.get_all_identifiers()], index=[0])
