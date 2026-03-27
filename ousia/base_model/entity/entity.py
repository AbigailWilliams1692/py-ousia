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
from ousia.base_model.attribute import Attribute


#############################################################
# Entity Class
#############################################################
class Entity(ABC):

    """
    Base class for all entities in the Ousia framework.
    
    This class serves as the foundation for all entity types in the framework.
    It provides common functionality and enforces a consistent interface for
    entity validation, serialization, and deserialization.
    """
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, *attributes: tuple[Attribute, ...]):
        """
        Constructor for the Entity class.
        
        Args:
            *attributes (tuple[Attribute, ...]): The attributes of the entity.
            **kwargs: Additional keyword arguments.
        """
        # Register the attributes with the Entity object
        for attribute in attributes:
            setattr(self, attribute.name, attribute.value)
    
    def __str__(self) -> str:
        """
        String representation of the Entity object.
        
        Returns:
            str: String representation of the Entity object.
        """
        return f"{self.__class__.__name__}[{id(self)}][{', '.join([f'{attribute.name}={attribute.value}' for attribute in self._attributes])}]"

    def __repr__(self) -> str:
        """
        Representation of the Entity object.
        
        Returns:
            str: Representation of the Entity object.
        """
        return f"{self.__class__.__name__}[{id(self)}]"

    def __hash__(self) -> int:
        """
        Hash of the Entity object.
        
        Returns:
            int: Hash of the Entity object.
        """
        return hash(self.__repr__())

    def __eq__(self, other: object) -> bool:
        """
        Equality check for the Entity object.
        
        Args:
            other (object): The object to compare with.
            
        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        return self.__hash__() == other.__hash__()

    #############################################################
    # Getter & Setter
    #############################################################
    def get_attribute(self, name: str) -> Attribute:
        """
        Get an attribute by name.
        
        Args:
            name (str): The name of the attribute.
            
        Returns:
            Attribute: The attribute with the given name.
        """
        return getattr(self, name)
    
    def set_attribute(self, attribute: Attribute) -> None:
        """
        Set an attribute.
        
        Args:
            attribute (Attribute): The attribute to set.
        """
        setattr(self, attribute.name, attribute.value)
    
    def get_attributes(self) -> Dict[str, Attribute]:
        """
        Get all attributes of the entity.
        
        Returns:
            Dict[str, Attribute]: a dictionary of all attributes
        """
        return {attr: getattr(self, attr) for attr in dir(self) if isinstance(getattr(self, attr), Attribute)}

    def get_attribute_value(self, name: str) -> Any:
        """
        Get an attribute value by name.
        
        Args:
            name (str): The name of the attribute.
            
        Returns:
            Any: The value of the attribute with the given name.
        """
        return getattr(self, name).value

    def set_attribute_value(self, name: str, value: Any) -> None:
        """
        Set an attribute value by name.
        
        Args:
            name (str): The name of the attribute.
            value (Any): The value to set.
        """
        getattr(self, name).value = value
    
    def remove_attribute(self, name: str) -> None:
        """
        Remove an attribute by name.
        
        Args:
            name (str): The name of the attribute to remove.
        """
        delattr(self, name)

    #############################################################
    # Serialization & Deserialization
    #############################################################
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the entity to a dictionary of attributes' name and value pairs.
        
        Returns:
            Dict[str, Any]: A dictionary representation of the entity.
        """
        return {attr: getattr(self, attr).value for attr in dir(self) if isinstance(getattr(self, attr), Attribute)}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], attribute_mapping: Dict[str, Type[Attribute]]) -> "Entity":
        """
        Create an entity from a dictionary of representation.
        
        Args:
            data (Dict[str, Any]): A dictionary representation of the entity's attributes.
            attribute_mapping (Dict[str, Type[Attribute]]): A mapping of attribute names to their types.
        Returns:
            Entity: The created entity.
        Raises:

        """
        attributes = []
        for key, value in data.items():
            if key in attribute_mapping:
                attributes.append(attribute_mapping[key](name=name, value=value))
            else:
                raise ValueError(f"Attribute {key} not found in attribute mapping")
        return cls(*attributes)

    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert the entity to a pandas DataFrame.
        
        Returns:
            pd.DataFrame: A DataFrame representation of the entity.
        """
        return pd.DataFrame({attr: getattr(self, attr).value for attr in dir(self) if isinstance(getattr(self, attr), Attribute)}, index=[0])

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame, attribute_mapping: Dict[str, Type[Attribute]]) -> "Entity":
        """
        Create an entity from a pandas DataFrame.
        
        Args:
            df (pd.DataFrame): A DataFrame representation of the entity (Assume there is only one row).
            attribute_mapping (Dict[str, Type[Attribute]]): A mapping of attribute names to their types.
        Returns:
            Entity: The created entity.
        """
        return cls.from_dict(data=df.iloc[0].to_dict(), attribute_mapping=attribute_mapping)
