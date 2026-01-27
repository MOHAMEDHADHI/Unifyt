"""Wire gauge conversion utilities for Unifyt.

This module provides conversions between wire gauge standards (AWG, SWG, BWG)
and metric/imperial diameter measurements. Wire gauges are non-linear lookup
tables rather than mathematical conversions.

Standards supported:
- AWG (American Wire Gauge) - Used in North America
- SWG (Standard Wire Gauge) - Used in UK
- BWG (Birmingham Wire Gauge) - Used for steel wire and tubing
"""

from typing import Dict, Optional, Union
from unifyt.quantity import Quantity


# American Wire Gauge (AWG) to diameter in millimeters
AWG_TO_MM: Dict[Union[int, str], float] = {
    '0000': 11.684, '000': 10.405, '00': 9.266, '0': 8.251,
    0: 8.251, 1: 7.348, 2: 6.544, 3: 5.827, 4: 5.189,
    5: 4.621, 6: 4.115, 7: 3.665, 8: 3.264, 9: 2.906,
    10: 2.588, 11: 2.305, 12: 2.053, 13: 1.828, 14: 1.628,
    15: 1.450, 16: 1.291, 17: 1.150, 18: 1.024, 19: 0.912,
    20: 0.812, 21: 0.723, 22: 0.644, 23: 0.573, 24: 0.511,
    25: 0.455, 26: 0.405, 27: 0.361, 28: 0.321, 29: 0.286,
    30: 0.255, 31: 0.227, 32: 0.202, 33: 0.180, 34: 0.160,
    35: 0.143, 36: 0.127, 37: 0.113, 38: 0.101, 39: 0.090,
    40: 0.079, 41: 0.071, 42: 0.063, 43: 0.056, 44: 0.051,
}

# Standard Wire Gauge (SWG) to diameter in millimeters
SWG_TO_MM: Dict[int, float] = {
    0: 8.839, 1: 7.620, 2: 7.010, 3: 6.401, 4: 5.893,
    5: 5.385, 6: 4.877, 7: 4.470, 8: 4.064, 9: 3.658,
    10: 3.251, 11: 2.946, 12: 2.642, 13: 2.337, 14: 2.032,
    15: 1.829, 16: 1.626, 17: 1.422, 18: 1.219, 19: 1.016,
    20: 0.914, 21: 0.813, 22: 0.711, 23: 0.610, 24: 0.559,
    25: 0.508, 26: 0.457, 27: 0.417, 28: 0.376, 29: 0.345,
    30: 0.315, 31: 0.295, 32: 0.274, 33: 0.254, 34: 0.234,
    35: 0.213, 36: 0.193, 37: 0.173, 38: 0.152, 39: 0.132,
    40: 0.122, 41: 0.112, 42: 0.102, 43: 0.091, 44: 0.081,
    45: 0.071, 46: 0.061, 47: 0.051, 48: 0.041, 49: 0.031,
    50: 0.025,
}

# Birmingham Wire Gauge (BWG) to diameter in millimeters
BWG_TO_MM: Dict[int, float] = {
    0: 8.636, 1: 7.620, 2: 7.214, 3: 6.579, 4: 6.045,
    5: 5.588, 6: 5.156, 7: 4.572, 8: 4.191, 9: 3.759,
    10: 3.404, 11: 3.048, 12: 2.769, 13: 2.413, 14: 2.108,
    15: 1.829, 16: 1.651, 17: 1.473, 18: 1.245, 19: 1.067,
    20: 0.889, 21: 0.813, 22: 0.711, 23: 0.635, 24: 0.559,
    25: 0.508, 26: 0.457, 27: 0.417, 28: 0.356, 29: 0.330,
    30: 0.305, 31: 0.279, 32: 0.254, 33: 0.229, 34: 0.203,
    35: 0.178, 36: 0.152,
}


class WireGaugeConverter:
    """Converter for wire gauge standards to physical dimensions."""
    
    @staticmethod
    def awg_to_diameter(gauge: Union[int, str], unit: str = 'millimeter') -> Quantity:
        """
        Convert AWG (American Wire Gauge) to diameter.
        
        Args:
            gauge: AWG gauge number (e.g., 14, '00', '0000')
            unit: Target unit for diameter ('millimeter', 'inch', etc.)
            
        Returns:
            Quantity with wire diameter
            
        Raises:
            ValueError: If gauge number is not recognized
            
        Examples:
            >>> diameter = WireGaugeConverter.awg_to_diameter(14)
            >>> print(diameter)  # 1.628 millimeter
            
            >>> diameter_in = WireGaugeConverter.awg_to_diameter(14, 'inch')
            >>> print(diameter_in)  # 0.0641 inch
        """
        if gauge not in AWG_TO_MM:
            valid_gauges = sorted([g for g in AWG_TO_MM.keys() if isinstance(g, int)])
            raise ValueError(
                f"AWG gauge {gauge} not recognized. "
                f"Valid gauges: 0000, 000, 00, 0, {min(valid_gauges)}-{max(valid_gauges)}"
            )
        
        diameter_mm = AWG_TO_MM[gauge]
        diameter = Quantity(diameter_mm, 'millimeter')
        
        if unit != 'millimeter':
            diameter = diameter.to(unit)
        
        return diameter
    
    @staticmethod
    def swg_to_diameter(gauge: int, unit: str = 'millimeter') -> Quantity:
        """
        Convert SWG (Standard Wire Gauge) to diameter.
        
        Args:
            gauge: SWG gauge number (0-50)
            unit: Target unit for diameter
            
        Returns:
            Quantity with wire diameter
            
        Raises:
            ValueError: If gauge number is not recognized
            
        Examples:
            >>> diameter = WireGaugeConverter.swg_to_diameter(14)
            >>> print(diameter)  # 2.032 millimeter
        """
        if gauge not in SWG_TO_MM:
            valid_range = f"{min(SWG_TO_MM.keys())}-{max(SWG_TO_MM.keys())}"
            raise ValueError(
                f"SWG gauge {gauge} not recognized. "
                f"Valid gauges: {valid_range}"
            )
        
        diameter_mm = SWG_TO_MM[gauge]
        diameter = Quantity(diameter_mm, 'millimeter')
        
        if unit != 'millimeter':
            diameter = diameter.to(unit)
        
        return diameter
    
    @staticmethod
    def bwg_to_diameter(gauge: int, unit: str = 'millimeter') -> Quantity:
        """
        Convert BWG (Birmingham Wire Gauge) to diameter.
        
        Args:
            gauge: BWG gauge number (0-36)
            unit: Target unit for diameter
            
        Returns:
            Quantity with wire diameter
            
        Raises:
            ValueError: If gauge number is not recognized
            
        Examples:
            >>> diameter = WireGaugeConverter.bwg_to_diameter(14)
            >>> print(diameter)  # 2.108 millimeter
        """
        if gauge not in BWG_TO_MM:
            valid_range = f"{min(BWG_TO_MM.keys())}-{max(BWG_TO_MM.keys())}"
            raise ValueError(
                f"BWG gauge {gauge} not recognized. "
                f"Valid gauges: {valid_range}"
            )
        
        diameter_mm = BWG_TO_MM[gauge]
        diameter = Quantity(diameter_mm, 'millimeter')
        
        if unit != 'millimeter':
            diameter = diameter.to(unit)
        
        return diameter
    
    @staticmethod
    def diameter_to_awg(diameter: Quantity) -> Optional[int]:
        """
        Find closest AWG gauge for a given diameter.
        
        Args:
            diameter: Wire diameter as Quantity
            
        Returns:
            Closest AWG gauge number, or None if outside range
            
        Examples:
            >>> diameter = Quantity(1.6, 'millimeter')
            >>> gauge = WireGaugeConverter.diameter_to_awg(diameter)
            >>> print(gauge)  # 14
        """
        diameter_mm = diameter.to('millimeter').magnitude
        
        # Find closest gauge
        closest_gauge = None
        min_diff = float('inf')
        
        for gauge, dia in AWG_TO_MM.items():
            if isinstance(gauge, int):  # Skip string gauges like '0000'
                diff = abs(dia - diameter_mm)
                if diff < min_diff:
                    min_diff = diff
                    closest_gauge = gauge
        
        return closest_gauge
    
    @staticmethod
    def diameter_to_swg(diameter: Quantity) -> Optional[int]:
        """
        Find closest SWG gauge for a given diameter.
        
        Args:
            diameter: Wire diameter as Quantity
            
        Returns:
            Closest SWG gauge number, or None if outside range
        """
        diameter_mm = diameter.to('millimeter').magnitude
        
        closest_gauge = None
        min_diff = float('inf')
        
        for gauge, dia in SWG_TO_MM.items():
            diff = abs(dia - diameter_mm)
            if diff < min_diff:
                min_diff = diff
                closest_gauge = gauge
        
        return closest_gauge
    
    @staticmethod
    def diameter_to_bwg(diameter: Quantity) -> Optional[int]:
        """
        Find closest BWG gauge for a given diameter.
        
        Args:
            diameter: Wire diameter as Quantity
            
        Returns:
            Closest BWG gauge number, or None if outside range
        """
        diameter_mm = diameter.to('millimeter').magnitude
        
        closest_gauge = None
        min_diff = float('inf')
        
        for gauge, dia in BWG_TO_MM.items():
            diff = abs(dia - diameter_mm)
            if diff < min_diff:
                min_diff = diff
                closest_gauge = gauge
        
        return closest_gauge


# Convenience functions at module level
def awg_to_diameter(gauge: Union[int, str], unit: str = 'millimeter') -> Quantity:
    """Convert AWG gauge to diameter. See WireGaugeConverter.awg_to_diameter for details."""
    return WireGaugeConverter.awg_to_diameter(gauge, unit)


def swg_to_diameter(gauge: int, unit: str = 'millimeter') -> Quantity:
    """Convert SWG gauge to diameter. See WireGaugeConverter.swg_to_diameter for details."""
    return WireGaugeConverter.swg_to_diameter(gauge, unit)


def bwg_to_diameter(gauge: int, unit: str = 'millimeter') -> Quantity:
    """Convert BWG gauge to diameter. See WireGaugeConverter.bwg_to_diameter for details."""
    return WireGaugeConverter.bwg_to_diameter(gauge, unit)


def diameter_to_awg(diameter: Quantity) -> Optional[int]:
    """Find closest AWG gauge for diameter. See WireGaugeConverter.diameter_to_awg for details."""
    return WireGaugeConverter.diameter_to_awg(diameter)


def diameter_to_swg(diameter: Quantity) -> Optional[int]:
    """Find closest SWG gauge for diameter. See WireGaugeConverter.diameter_to_swg for details."""
    return WireGaugeConverter.diameter_to_swg(diameter)


def diameter_to_bwg(diameter: Quantity) -> Optional[int]:
    """Find closest BWG gauge for diameter. See WireGaugeConverter.diameter_to_bwg for details."""
    return WireGaugeConverter.diameter_to_bwg(diameter)


__all__ = [
    'WireGaugeConverter',
    'awg_to_diameter',
    'swg_to_diameter',
    'bwg_to_diameter',
    'diameter_to_awg',
    'diameter_to_swg',
    'diameter_to_bwg',
    'AWG_TO_MM',
    'SWG_TO_MM',
    'BWG_TO_MM',
]
