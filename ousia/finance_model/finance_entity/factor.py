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
from ousia.finance_model.finance_identifier.factor_identifier import FactorIdentifier


#############################################################
# Factor Class
#############################################################
class Factor(FinanceEntity):

    """
    Factor class. Represents a financial factor.
    
    This class serves as the foundation for all factor types in the framework.
    It provides common functionality and enforces a consistent interface for
    factor validation, serialization, and deserialization.
    """
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(self, *attributes: tuple[FinanceAttribute, ...]):
        """
        Constructor for the Factor class.
        
        Args:
            *attributes (tuple[FinanceAttribute, ...]): The finance attributes of the factor.
        """
        super().__init__(*attributes)

        # Check if this factor has at least one identifier
        self._check_identifier()

    #############################################################
    # Factor Identifier Methods
    #############################################################
    def _get_identifier_type(self) -> Type[FactorIdentifier]:
        """
        Get the type of identifier for this factor.
        
        Returns:
            Type[FactorIdentifier]: The type of identifier for this factor.
        """
        return FactorIdentifier