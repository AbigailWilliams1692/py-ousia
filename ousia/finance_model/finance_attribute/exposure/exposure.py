# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from abc import ABC
from typing import Any, Dict, Optional

# Local Packages
from ousia.base_model.entity.entity import Entity
from ousia.finance_model.finance_attribute.finance_attribute import FinanceAttribute


#############################################################
# Exposure Class
#############################################################
class Exposure(FinanceAttribute, ABC):

    """
    Base class for all exposure attributes in the Ousia framework.
    
    This class serves as the foundation for all exposure attribute types in the framework.
    It provides common functionality and enforces a consistent interface for
    exposure attribute validation, serialization, and deserialization.
    """
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, value: Dict[Entity, Any], name: str = "Exposure"):
        """
        Constructor for the Exposure class.
        
        Args:
            name (str): The name of the attribute.
            data_type (type): The data type of the attribute.
            value (Any, optional): The value of the attribute. Defaults to None.
        Returns:
            Exposure: The created exposure object.
        """
        super().__init__(name=name, data_type=Dict, value=value)
    
    #############################################################
    # Getter & Setter Methods
    #############################################################
    def get_exposure(self, entity: Entity, default_exposure_value: Optional[Any] = None) -> Any:
        """
        Get the exposure value for a specific entity.
        
        Args:
            entity (Entity): The entity to get the exposure value for.
            default_exposure_value (Any, optional): The default exposure value to return if the entity is not found. Defaults to None.
        Returns:
            Any: The exposure value for the specified entity.
        """
        return self.value.get(entity, default_exposure_value)

    def set_exposure(self, entity: Entity, exposure_value: Any) -> None:
        """
        Set the exposure value for a specific entity.
        
        Args:
            entity (Entity): The entity to set the exposure value for.
            exposure_value (Any): The exposure value to set.
        """
        self.value[entity] = exposure_value

    def remove_exposure(self, entity: Entity) -> None:
        """
        Remove the exposure value for a specific entity.
        
        Args:
            entity (Entity): The entity to remove the exposure value for.
        """
        self.value.pop(entity, None)

    def get_exposures(self) -> Dict[Entity, Any]:
        """
        Get all exposure values.
        
        Returns:
            Dict[Entity, Any]: A dictionary containing all exposure values.
        """
        return self.value

    def set_exposures(self, exposures: Dict[Entity, Any]) -> None:
        """
        Set the exposure values for multiple entities.
        
        Args:
            exposures (Dict[Entity, Any]): A dictionary containing exposure values for multiple entities.
        """
        self.value = exposures

    def clear_exposures(self) -> None:
        """
        Clear all exposure values.
        """
        self.value.clear()
    