# !usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################
# Import Libraries
#############################################################
# Standard Packages
from typing import List, Optional, Type, Union

# Third-Party Packages
import pandas as pd

# Local Packages
from ousia.finance_model.finance_entity.finance_entity import FinanceEntity
from ousia.finance_model.finance_attribute.finance_attribute import FinanceAttribute
from ousia.finance_model.finance_attribute.identifier.portfolio_identifier import PortfolioIdentifier
from ousia.finance_model.finance_attribute.exposure.holding import Holding
from ousia.finance_model.finance_attribute.series.holding_timeseries import HoldingTimeSeries


#############################################################
# Portfolio Class
#############################################################
class Portfolio(FinanceEntity):

    """
    Portfolio class. Represents a financial portfolio.
    
    This class serves as the foundation for all portfolio types in the framework.
    A portfolio contains either a single Holding object or a HoldingTimeSeries object,
    but not both. It may also have a benchmark portfolio for comparison.
    """
    
    #############################################################
    # Default Methods
    #############################################################
    def __init__(
        self, 
        holding: Optional[Holding] = None,
        holding_timeseries: Optional[HoldingTimeSeries] = None,
        benchmark: Optional["Portfolio"] = None,
        *attributes: tuple[FinanceAttribute, ...],
    ):
        """
        Constructor for the Portfolio class.
        
        Args:
            *attributes (tuple[FinanceAttribute, ...]): The finance attributes of the portfolio.
            holding (Optional[Holding]): A single Holding object. Mutually exclusive with holding_timeseries.
            holding_timeseries (Optional[HoldingTimeSeries]): A HoldingTimeSeries object. Mutually exclusive with holding.
            benchmark (Optional[Portfolio]): A benchmark portfolio for comparison.
        Raises:
            ValueError: If both holding and holding_timeseries are provided.
        """
        # Initialize the parent FinanceEntity with the provided attributes
        super().__init__(*attributes)

        # Check if this portfolio has at least one identifier
        self._check_identifier()

        # Validate that only one of holding or holding_timeseries is provided
        if holding is not None and holding_timeseries is not None:
            raise ValueError("Portfolio cannot have both a Holding and a HoldingTimeSeries. Provide only one.")
        
        # Set the fields of the portfolio
        self._holding = holding
        self._holding_timeseries = holding_timeseries
        self._benchmark = benchmark

    #############################################################
    # Portfolio Identifier Methods
    #############################################################
    def _get_identifier_type(self) -> Type[PortfolioIdentifier]:
        """
        Get the type of identifier for this portfolio.
        
        Returns:
            Type[PortfolioIdentifier]: The type of identifier for this portfolio.
        """
        return PortfolioIdentifier

    #############################################################
    # Holding Methods
    #############################################################
    def get_holding(self) -> Optional[Holding]:
        """
        Get the Holding object.
        
        Returns:
            Optional[Holding]: The Holding object, or None if not set.
        """
        return self._holding

    def set_holding(self, holding: Holding) -> None:
        """
        Set the Holding object. Clears any existing HoldingTimeSeries.
        
        Args:
            holding (Holding): The Holding object to set.
        """
        if not isinstance(holding, Holding):
            raise TypeError(f"Expected Holding object, got {type(holding).__name__}")
        self._holding = holding
        self._holding_timeseries = None
    
    def set_holding_value(self, asset: "Asset", value: float) -> None:
        """
        Set the holding value for a specific asset.
        
        Args:
            asset (Asset): The asset to set the value for.
            value (float): The value to set.
        """
        if self._holding is None:
            raise ValueError("Holding not set")
        else:
            self._holding.set_holding_value(asset=asset, value=value)

    def has_holding(self) -> bool:
        """
        Check if the portfolio has a single Holding object.
        
        Returns:
            bool: True if the portfolio has a Holding object.
        """
        return self._holding is not None

    def get_holding_unit(self) -> Optional[HoldingUnit]:
        """
        Get the HoldingUnit.
        
        Returns:
            Optional[HoldingUnit]: The HoldingUnit, or None if not set.
        """
        if self._holding is None:
            return None
        return self._holding.get_holding_unit()

    def get_holding_timeseries(self) -> Optional[HoldingTimeSeries]:
        """
        Get the HoldingTimeSeries object.
        
        Returns:
            Optional[HoldingTimeSeries]: The HoldingTimeSeries object, or None if not set.
        """
        return self._holding_timeseries

    def set_holding_timeseries(self, holding_timeseries: HoldingTimeSeries) -> None:
        """
        Set the HoldingTimeSeries object. Clears any existing Holding.
        
        Args:
            holding_timeseries (HoldingTimeSeries): The HoldingTimeSeries object to set.
        """
        if not isinstance(holding_timeseries, HoldingTimeSeries):
            raise TypeError(f"Expected HoldingTimeSeries object, got {type(holding_timeseries).__name__}")
        self._holding_timeseries = holding_timeseries
        self._holding = None

    def get_holding_at_date(self, date: datetime) -> Optional[Holding]:
        """
        Get the Holding object at a specific date.
        
        Args:
            date (datetime): The date to get the Holding object for.
        
        Returns:
            Optional[Holding]: The Holding object at the specified date, or None if not found.
        """
        if self._holding_timeseries is None:
            return None
        return self._holding_timeseries.get_holding_at_date(date)

    def set_holding_at_date(self, date: datetime, holding: Holding) -> None:
        """
        Set the Holding object at a specific date.
        
        Args:
            date (datetime): The date to set the Holding object for.
            holding (Holding): The Holding object to set.
        """
        if self._holding_timeseries is None:
            raise ValueError("HoldingTimeSeries not set")
        self._holding_timeseries.set_holding_at_date(date, holding)

    def get_holding_unit_at_date(self, date: datetime) -> Optional[HoldingUnit]:
        """
        Get the HoldingUnit at a specific date.
        
        Args:
            date (datetime): The date to get the HoldingUnit for.
        
        Returns:
            Optional[HoldingUnit]: The HoldingUnit at the specified date, or None if not found.
        """
        if self._holding_timeseries is None:
            return None
        return self._holding_timeseries.get_holding_unit_at_date(date)
    
    def get_holding_units_at_date(self, date: datetime) -> Optional[List[HoldingUnit]]:
        """
        Get the HoldingUnits at a specific date.
        
        Args:
            date (datetime): The date to get the HoldingUnits for.
        
        Returns:
            Optional[List[HoldingUnit]]: The HoldingUnits at the specified date, or None if not found.
        """
        if self._holding_timeseries is None:
            return None
        return self._holding_timeseries.get_holding_units_at_date(date)

    def has_holding_timeseries(self) -> bool:
        """
        Check if the portfolio has a HoldingTimeSeries object.
        
        Returns:
            bool: True if the portfolio has a HoldingTimeSeries object.
        """
        return self._holding_timeseries is not None

    #############################################################
    # Benchmark Methods
    #############################################################
    def get_benchmark(self) -> Optional["Portfolio"]:
        """
        Get the benchmark portfolio.
        
        Returns:
            Optional[Portfolio]: The benchmark portfolio, or None if not set.
        """
        return self._benchmark

    def set_benchmark(self, benchmark: "Portfolio") -> None:
        """
        Set the benchmark portfolio.
        
        Args:
            benchmark (Portfolio): The benchmark portfolio to set.
        """
        if not isinstance(benchmark, Portfolio):
            raise TypeError(f"Expected Portfolio object, got {type(benchmark).__name__}")
        self._benchmark = benchmark

    def has_benchmark(self) -> bool:
        """
        Check if the portfolio has a benchmark.
        
        Returns:
            bool: True if the portfolio has a benchmark.
        """
        return self._benchmark is not None
