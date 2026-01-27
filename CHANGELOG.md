# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added - New Units and Features 🚀

#### Wire Gauge Support
- **AWG (American Wire Gauge)**: Complete conversion table for gauges 0000, 000, 00, 0-44
- **SWG (Standard Wire Gauge)**: Complete conversion table for gauges 0-50
- **BWG (Birmingham Wire Gauge)**: Complete conversion table for gauges 0-36
- New `wire_gauge` module with bidirectional conversions (gauge ↔ diameter)
- Support for diameter in any length unit (mm, inch, etc.)

#### Torque Units
- `newton_meter`, `Nm`, `N_m` - SI torque unit
- `kilonewton_meter`, `kNm` - Large torque applications
- `foot_pound`, `ft_lb`, `foot_lb`, `pound_foot`, `lb_ft` - Imperial torque
- `inch_pound`, `in_lb`, `inch_lb` - Small fastener torque

#### Industrial Flow Units
- **Mass Flow**: `kilogram_per_second`, `kilogram_per_minute`, `kilogram_per_hour`, `ton_per_hour` (tph)
- **Volumetric Flow**: `cubic_meter_per_minute`, `cubic_meter_per_hour`, `cubic_foot_per_minute` (cfm), `cubic_foot_per_second` (cfs)
- Imperial mass flow: `pound_per_second`, `pound_per_minute`, `pound_per_hour`

#### Angular Velocity Units
- `radian_per_second`, `rad_s` - SI angular velocity
- `degree_per_second`, `deg_s` - Degrees per second
- `revolution_per_minute`, `rev_min` - Alternative to rpm
- `revolution_per_second`, `rev_s` - Revolutions per second

#### Paper/Fabric Weight
- `gsm`, `grams_per_square_meter` - Standard paper weight unit

#### Additional Specialized Units
- **Specific Energy**: `joule_per_kilogram`, `kilojoule_per_kilogram`, `megajoule_per_kilogram`, `calorie_per_gram`
- **Specific Volume**: `cubic_meter_per_kilogram`, `liter_per_kilogram`
- **Thermal Properties**: `calorie_per_gram_celsius`, `btu_per_pound_fahrenheit`
- **Surface Tension**: `newton_per_meter`, `dyne_per_centimeter`
- **Moment of Inertia**: `kilogram_meter_squared`, `gram_centimeter_squared`

### Changed
- Updated `_BASE_UNITS` dictionary to include new derived unit dimensions
- Enhanced unit mapping system to support new unit categories
- Improved documentation with wire gauge examples

### Documentation
- Added `wire_gauge.py` module with comprehensive docstrings
- Created `examples/new_units_demo.py` showcasing all new units
- Added `tests/test_wire_gauge.py` with full test coverage
- Updated README.md with wire gauge and new unit examples
- Enhanced unit catalog documentation

## [0.2.0] - 2024-12-24

### Added - Major Feature Release 🚀

#### Units (200+ new units added - now 300+ total!)

**Astronomical Units**:
- kiloparsec, megaparsec
- nautical_mile, fathom, chain, furlong, league
- picometer, femtometer, fermi

**Atomic & Nuclear**:
- atomic_mass_unit, dalton
- electron_mass, proton_mass, neutron_mass
- solar_mass, earth_mass
- carat, grain, stone, slug

**Advanced Time**:
- picosecond, femtosecond, attosecond
- shake, fortnight, month, decade, century, millennium

**Advanced Energy**:
- megajoule, gigajoule, erg
- british_thermal_unit, therm, quad
- ton_tnt, kiloton_tnt, megaton_tnt
- rydberg, hartree

**Advanced Power**:
- gigawatt, terawatt
- milliwatt, microwatt, nanowatt
- metric_horsepower, boiler_horsepower

**Advanced Pressure**:
- gigapascal, millibar, microbar, barye
- technical_atmosphere
- inch_mercury, millimeter_mercury

**Advanced Force**:
- meganewton, dyne
- kilogram_force, gram_force, ton_force
- poundal, kip

**Advanced Frequency**:
- terahertz, millihertz
- rpm (revolutions per minute)
- rps (revolutions per second)

**Advanced Voltage**:
- megavolt, microvolt, nanovolt
- statvolt

**Advanced Current**:
- microampere, nanoampere, picoampere
- kiloampere, statampere

**Capacitance**:
- farad, millifarad, microfarad, nanofarad, picofarad

**Inductance**:
- henry, millihenry, microhenry, nanohenry

**Magnetic Field**:
- tesla, millitesla, microtesla, nanotesla
- gauss, milligauss

**Magnetic Flux**:
- weber, milliweber, maxwell

**Illuminance**:
- lux, foot_candle, phot

**Luminous Flux**:
- lumen

**Radioactivity**:
- becquerel, kilobecquerel, megabecquerel, gigabecquerel
- curie, millicurie, microcurie
- rutherford

**Absorbed Dose**:
- gray, milligray, rad

**Equivalent Dose**:
- sievert, millisievert, microsievert
- rem, millirem

**Catalytic Activity**:
- katal, unit (enzyme unit)

**Data/Information**:
- bit, byte
- kilobyte, megabyte, gigabyte, terabyte, petabyte
- kibibyte, mebibyte, gibibyte, tebibyte

**Velocity**:
- knot, mach

**Acceleration**:
- gal (galileo), standard_gravity

**Viscosity**:
- pascal_second, poise, centipoise (dynamic)
- stokes, centistokes (kinematic)

**Thermal Properties**:
- watt_per_meter_kelvin (thermal conductivity)
- joule_per_kelvin (heat capacity)
- joule_per_kilogram_kelvin (specific heat)

**Molar Mass**:
- gram_per_mole, kilogram_per_mole

**Concentration**:
- molar, millimolar, micromolar, nanomolar

**Density**:
- kilogram_per_cubic_meter
- gram_per_cubic_centimeter
- gram_per_liter

**Flow Rate**:
- cubic_meter_per_second
- liter_per_second, liter_per_minute
- gallon_per_minute

**Fuel Efficiency**:
- mile_per_gallon, kilometer_per_liter
- liter_per_100km

**Angle**:
- arcminute, arcsecond, gradian

**Dimensionless**:
- ppt (parts per trillion)

#### Constants (50+ new constants added - now 80+ total!)

**Electromagnetic**:
- Faraday constant (F)
- Vacuum impedance (Z_0)
- Conductance quantum (G_0)
- Josephson constant (K_J)
- Von Klitzing constant (R_K)
- Magnetic flux quantum (Phi_0)
- Bohr magneton (mu_B)
- Nuclear magneton (mu_N)
- Proton/electron/neutron magnetic moments
- Proton gyromagnetic ratio

**Radiation**:
- Wien displacement constant
- First radiation constant
- Second radiation constant

**Atomic & Particle**:
- Compton wavelength
- Classical electron radius
- Thomson cross section
- Electron g-factor
- Muon mass
- Tau mass

**Planck Units**:
- Planck length (l_P)
- Planck mass (m_P)
- Planck time (t_P)
- Planck temperature (T_P)
- Planck energy (E_P)

**Cosmological**:
- Hubble constant (H_0)
- CMB temperature (T_CMB)
- Age of universe
- Critical density (rho_c)

**Solar System**:
- Solar luminosity (L_sun)
- Solar radius (R_sun)
- Jupiter mass (M_jupiter)
- Moon mass (M_moon)
- Schwarzschild radii (Earth, Sun)

### Changed
- Version bumped to 0.2.0
- Documentation updated across all files
- Examples updated with new units
- API reference expanded

### Performance
- No performance degradation
- Unit caching maintained
- Memory efficient despite 3x more units

## [0.1.0] - 2024-12-24

### Added
- Initial release of Unifyt
- Core `Quantity` class for representing values with units
- `Unit` class for unit management and conversions
- `Dimension` class for tracking physical dimensions
- `UnitRegistry` for custom unit definitions
- `UnitContext` for unit system management
- Support for 100+ units including:
  - Basic SI units (length, mass, time, etc.)
  - Imperial units
  - Energy units (joule, calorie, kWh, eV)
  - Power units (watt, horsepower)
  - Pressure units (pascal, bar, atm, psi)
  - Force units (newton, pound_force)
  - Frequency units (hertz, MHz, GHz)
  - Voltage and electrical units
  - Volume units (liter, gallon)
  - Angle units (radian, degree)
- Physical constants module with 30+ constants:
  - Fundamental constants (c, h, G, k_B, etc.)
  - Astronomical constants (AU, ly, M_sun, etc.)
  - Atomic constants (a_0, m_e, m_p, etc.)
- Utility functions module:
  - Array creation (linspace, arange, zeros, ones, full)
  - Array operations (concatenate, stack)
  - Statistical functions (sum, mean, std, min, max)
  - Mathematical functions (sqrt, clip, isclose)
- Serialization support:
  - JSON serialization/deserialization
  - Pickle support
  - File save/load functions
  - Custom JSON encoder/decoder
- Performance optimizations:
  - Unit caching for faster parsing
  - Efficient dimension checking
  - NumPy vectorization
- Comprehensive test suite with 50+ tests
- Full documentation:
  - User guide with examples
  - Complete API reference
  - Performance guide
  - Migration guide from Pint/Unyt
  - Feature documentation
- Example scripts:
  - Basic usage examples
  - Scientific calculations
  - Custom unit definitions
  - Array operations
  - Advanced features (constants, utils, serialization)
- Development tools:
  - Setup script
  - Test runner
  - Code formatter
  - Code quality checker
- Type hints for better IDE support
- Full PEP 561 compliance

### Features
- Intuitive API for creating and manipulating quantities
- Automatic unit conversion in arithmetic operations
- Support for compound units (e.g., meter/second)
- Array operations with NumPy integration
- Custom unit definitions
- Unit system contexts
- Comparison operations
- Power operations
- Dimensionality checking
- Physical constants with proper units
- Utility functions for common operations
- Serialization to JSON and pickle

### Documentation
- User guide with comprehensive examples
- Complete API reference
- Quick start guide
- Performance optimization guide
- Migration guide from other libraries
- Contributing guidelines
- README with feature overview
- Inline documentation with docstrings

### Performance
- Unit caching reduces parsing overhead
- NumPy integration for vectorized operations
- Efficient dimension tracking
- Optimized conversion calculations
- 2-5x faster than Pint for array operations

[Unreleased]: https://github.com/MEERAN2314/unifyt/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/MEERAN2314/unifyt/releases/tag/v0.2.0
[0.1.0]: https://github.com/MEERAN2314/unifyt/releases/tag/v0.1.0
