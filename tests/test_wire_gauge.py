"""Tests for wire gauge conversion module."""

import pytest
from unifyt import Quantity, wire_gauge
from unifyt.wire_gauge import WireGaugeConverter


class TestAWGConversion:
    """Test American Wire Gauge conversions."""
    
    def test_awg_to_diameter_basic(self):
        """Test basic AWG to diameter conversion."""
        diameter = wire_gauge.awg_to_diameter(14)
        assert diameter.unit._name == 'millimeter'
        assert abs(diameter.magnitude - 1.628) < 0.001
    
    def test_awg_to_diameter_in_inches(self):
        """Test AWG to diameter in inches."""
        diameter = wire_gauge.awg_to_diameter(14, 'inch')
        assert diameter.unit._name == 'inch'
        assert abs(diameter.magnitude - 0.0641) < 0.001
    
    def test_awg_special_gauges(self):
        """Test special AWG gauges like 0000."""
        diameter = wire_gauge.awg_to_diameter('0000')
        assert abs(diameter.magnitude - 11.684) < 0.001
        
        diameter = wire_gauge.awg_to_diameter('00')
        assert abs(diameter.magnitude - 9.266) < 0.001
    
    def test_awg_invalid_gauge(self):
        """Test invalid AWG gauge raises error."""
        with pytest.raises(ValueError):
            wire_gauge.awg_to_diameter(999)
    
    def test_diameter_to_awg(self):
        """Test finding AWG from diameter."""
        diameter = Quantity(1.628, 'millimeter')
        gauge = wire_gauge.diameter_to_awg(diameter)
        assert gauge == 14
        
        # Test with slightly different diameter
        diameter = Quantity(1.6, 'millimeter')
        gauge = wire_gauge.diameter_to_awg(diameter)
        assert gauge == 14  # Should round to closest


class TestSWGConversion:
    """Test Standard Wire Gauge conversions."""
    
    def test_swg_to_diameter_basic(self):
        """Test basic SWG to diameter conversion."""
        diameter = wire_gauge.swg_to_diameter(14)
        assert diameter.unit._name == 'millimeter'
        assert abs(diameter.magnitude - 2.032) < 0.001
    
    def test_swg_to_diameter_in_inches(self):
        """Test SWG to diameter in inches."""
        diameter = wire_gauge.swg_to_diameter(14, 'inch')
        assert diameter.unit._name == 'inch'
        assert abs(diameter.magnitude - 0.080) < 0.001
    
    def test_swg_invalid_gauge(self):
        """Test invalid SWG gauge raises error."""
        with pytest.raises(ValueError):
            wire_gauge.swg_to_diameter(999)
    
    def test_diameter_to_swg(self):
        """Test finding SWG from diameter."""
        diameter = Quantity(2.032, 'millimeter')
        gauge = wire_gauge.diameter_to_swg(diameter)
        assert gauge == 14


class TestBWGConversion:
    """Test Birmingham Wire Gauge conversions."""
    
    def test_bwg_to_diameter_basic(self):
        """Test basic BWG to diameter conversion."""
        diameter = wire_gauge.bwg_to_diameter(14)
        assert diameter.unit._name == 'millimeter'
        assert abs(diameter.magnitude - 2.108) < 0.001
    
    def test_bwg_to_diameter_in_inches(self):
        """Test BWG to diameter in inches."""
        diameter = wire_gauge.bwg_to_diameter(14, 'inch')
        assert diameter.unit._name == 'inch'
        assert abs(diameter.magnitude - 0.083) < 0.001
    
    def test_bwg_invalid_gauge(self):
        """Test invalid BWG gauge raises error."""
        with pytest.raises(ValueError):
            wire_gauge.bwg_to_diameter(999)
    
    def test_diameter_to_bwg(self):
        """Test finding BWG from diameter."""
        diameter = Quantity(2.108, 'millimeter')
        gauge = wire_gauge.diameter_to_bwg(diameter)
        assert gauge == 14


class TestWireGaugeComparison:
    """Test comparison between different gauge standards."""
    
    def test_gauge_14_comparison(self):
        """Test that gauge 14 differs across standards."""
        awg_14 = wire_gauge.awg_to_diameter(14)
        swg_14 = wire_gauge.swg_to_diameter(14)
        bwg_14 = wire_gauge.bwg_to_diameter(14)
        
        # All should be different
        assert awg_14.magnitude != swg_14.magnitude
        assert awg_14.magnitude != bwg_14.magnitude
        assert swg_14.magnitude != bwg_14.magnitude
        
        # AWG 14 should be smallest
        assert awg_14.magnitude < swg_14.magnitude
        assert awg_14.magnitude < bwg_14.magnitude
    
    def test_converter_class_methods(self):
        """Test using WireGaugeConverter class directly."""
        diameter = WireGaugeConverter.awg_to_diameter(14)
        assert abs(diameter.magnitude - 1.628) < 0.001
        
        gauge = WireGaugeConverter.diameter_to_awg(diameter)
        assert gauge == 14


class TestNewUnits:
    """Test newly added units."""
    
    def test_torque_units(self):
        """Test torque unit conversions."""
        # Newton-meter
        torque_nm = Quantity(100, 'newton_meter')
        assert torque_nm.magnitude == 100
        
        # Shorthand
        torque_nm2 = Quantity(100, 'Nm')
        assert torque_nm2.magnitude == 100
        
        # Foot-pound
        torque_ftlb = Quantity(75, 'foot_pound')
        torque_nm_converted = torque_ftlb.to('newton_meter')
        assert abs(torque_nm_converted.magnitude - 101.69) < 0.1
        
        # Inch-pound
        torque_inlb = Quantity(120, 'inch_pound')
        torque_nm_converted = torque_inlb.to('newton_meter')
        assert abs(torque_nm_converted.magnitude - 13.56) < 0.1
    
    def test_gsm_unit(self):
        """Test GSM (grams per square meter) unit."""
        paper = Quantity(80, 'gsm')
        assert paper.magnitude == 80
        
        # Convert to kg/m²
        paper_kg = paper.to('kilogram/meter^2')
        assert abs(paper_kg.magnitude - 0.08) < 0.001
    
    def test_mass_flow_rate(self):
        """Test mass flow rate units."""
        flow_kg_hr = Quantity(1000, 'kilogram_per_hour')
        flow_kg_s = flow_kg_hr.to('kilogram_per_second')
        assert abs(flow_kg_s.magnitude - 0.2778) < 0.001
        
        # Ton per hour
        flow_tph = Quantity(5, 'ton_per_hour')
        flow_kg_s = flow_tph.to('kilogram_per_second')
        assert abs(flow_kg_s.magnitude - 1.389) < 0.01
    
    def test_volumetric_flow_rate(self):
        """Test volumetric flow rate units."""
        flow_cfm = Quantity(500, 'cubic_foot_per_minute')
        flow_m3_s = flow_cfm.to('cubic_meter_per_second')
        assert abs(flow_m3_s.magnitude - 0.236) < 0.01
        
        # Cubic meter per hour
        flow_m3_hr = Quantity(100, 'cubic_meter_per_hour')
        flow_m3_s = flow_m3_hr.to('cubic_meter_per_second')
        assert abs(flow_m3_s.magnitude - 0.0278) < 0.001
    
    def test_angular_velocity(self):
        """Test angular velocity units."""
        rpm = Quantity(1800, 'rpm')
        rad_s = rpm.to('radian_per_second')
        assert abs(rad_s.magnitude - 188.5) < 0.5
        
        # Revolution per second
        rev_s = Quantity(30, 'revolution_per_second')
        rad_s = rev_s.to('radian_per_second')
        assert abs(rad_s.magnitude - 188.5) < 0.5
        
        # Degree per second
        deg_s = Quantity(360, 'degree_per_second')
        rad_s = deg_s.to('radian_per_second')
        assert abs(rad_s.magnitude - 6.28) < 0.01


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
