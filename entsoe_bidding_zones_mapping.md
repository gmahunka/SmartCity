# ENTSO-E Bidding Zone Codes - Comprehensive Mapping Guide

## Overview

This document provides a complete mapping of ENTSO-E bidding zone identifiers to ISO3/ISO2 country codes, along with official EIC (European Identification Code) codes used in the European electricity market.

**Source:** Official ENTSO-E mappings from `entsoe-py` library (EnergieID/entsoe-py GitHub repository)  
**Last Updated:** February 21, 2026  
**Total Countries:** 45 (including special cases)  
**Total Bidding Zones:** 101

---

## Quick Reference - Countries by ISO3 Code

| ISO3 | ISO2 | Country | Primary Area Code | Primary EIC Code | TSO |
|------|------|---------|-------------------|------------------|-----|
| ALB | AL | Albania | AL | 10YAL-KESH-----5 | OST |
| AUT | AT | Austria | AT | 10YAT-APG------L | APG |
| BEL | BE | Belgium | BE | 10YBE----------2 | Elia |
| BIH | BA | Bosnia and Herzegovina | BA | 10YBA-JPCC-----D | NOS BiH |
| BGR | BG | Bulgaria | BG | 10YCA-BULGARIA-R | ESO |
| CHE | CH | Switzerland | CH | 10YCH-SWISSGRIDZ | Swissgrid |
| CYP | CY | Cyprus | CY | 10YCY-1001A0003J | Cyprus TSO |
| CZE | CZ | Czech Republic | CZ | 10YCZ-CEPS-----N | CEPS |
| DEU | DE | Germany | DE | 10Y1001A1001A83F | Multiple TSOs |
| DNK | DK | Denmark | DK | 10Y1001A1001A65H | Energinet |
| EST | EE | Estonia | EE | 10Y1001A1001A39I | Elering |
| ESP | ES | Spain | ES | 10YES-REE------0 | REE |
| FIN | FI | Finland | FI | 10YFI-1--------U | Fingrid |
| FRA | FR | France | FR | 10YFR-RTE------C | RTE |
| GBR | GB | United Kingdom | GB | 10YGB----------A | National Grid |
| GEO | GE | Georgia | GE | 10Y1001A1001B012 | - |
| GRC | GR | Greece | GR | 10YGR-HTSO-----Y | IPTO |
| HRV | HR | Croatia | HR | 10YHR-HEP------M | HOPS |
| HUN | HU | Hungary | HU | 10YHU-MAVIR----U | MAVIR |
| ISL | IS | Iceland | IS | IS | Landsnet |
| IRL | IE | Ireland | IE | 10YIE-1001A00010 | EirGrid |
| ITA | IT | Italy | IT | 10YIT-GRTN-----B | Terna |
| LTU | LT | Lithuania | LT | 10YLT-1001A0008Q | Litgrid |
| LUX | LU | Luxembourg | LU | 10YLU-CEGEDEL-NQ | CREOS |
| LVA | LV | Latvia | LV | 10YLV-1001A00074 | AST |
| MDA | MD | Moldova | MD | 10Y1001A1001A990 | Moldelectica |
| MKD | MK | North Macedonia | MK | 10YMK-MEPSO----8 | MEPSO |
| MLT | MT | Malta | MT | 10Y1001A1001A93C | Malta TSO |
| MNE | ME | Montenegro | ME | 10YCS-CG-TSO---S | CGES |
| NLD | NL | Netherlands | NL | 10YNL----------L | TenneT NL |
| NOR | NO | Norway | NO | 10YNO-0--------C | Stattnet |
| POL | PL | Poland | PL | 10YPL-AREA-----S | PSE SA |
| PRT | PT | Portugal | PT | 10YPT-REN------W | REN |
| ROU | RO | Romania | RO | 10YRO-TEL------P | Transelectrica |
| RUS | RU | Russia | RU | 10Y1001A1001A49F | - |
| SRB | RS | Serbia | RS | 10YCS-SERBIATSOV | EMS |
| SVK | SK | Slovakia | SK | 10YSK-SEPS-----K | SEPS |
| SVN | SI | Slovenia | SI | 10YSI-ELES-----O | ELES |
| SWE | SE | Sweden | SE | 10YSE-1--------K | SvK |
| TUR | TR | Turkey | TR | 10YTR-TEIAS----W | TEIAS |
| UKR | UA | Ukraine | UA | 10Y1001C--00003F | - |
| XKX | XK | Kosovo | XK | 10Y1001C--00100H | - |

---

## Special Cases and Multi-Zone Countries

### Germany (DEU)
Germany operates multiple bidding zones and control areas:
- **DE**: Aggregated Germany - EIC: `10Y1001A1001A83F`
- **DE_50HZ**: 50Hertz control area (eastern Germany) - EIC: `10YDE-VE-------2`
- **DE_AMPRION**: Amprion control area (western Germany) - EIC: `10YDE-RWENET---I`
- **DE_TENNET**: TenneT GER control area (northern Germany) - EIC: `10YDE-EON------1`
- **DE_TRANSNET**: TransnetBW control area (southwestern Germany) - EIC: `10YDE-ENBW-----N`

### Denmark (DNK)
Denmark is split into two bidding zones:
- **DK_1**: Western Denmark - EIC: `10YDK-1--------W`
- **DK_2**: Eastern Denmark - EIC: `10YDK-2--------M`
- **DK_CA**: Energinet control area - EIC: `10Y1001A1001A796`

### Italy (ITA)
Italy has the most complex zone structure with 17 separate bidding zones:
- **IT**: Aggregated Italy - EIC: `10YIT-GRTN-----B`
- **IT_NORD**: North - EIC: `10Y1001A1001A73I`
- **IT_NORD_AT**: North-Austria - EIC: `10Y1001A1001A80L`
- **IT_NORD_CH**: North-Switzerland - EIC: `10Y1001A1001A68B`
- **IT_NORD_FR**: North-France - EIC: `10Y1001A1001A81J`
- **IT_NORD_SI**: North-Slovenia - EIC: `10Y1001A1001A67D`
- **IT_CNOR**: Centre-North - EIC: `10Y1001A1001A70O`
- **IT_CSUD**: Centre-South - EIC: `10Y1001A1001A71M`
- **IT_SUD**: South - EIC: `10Y1001A1001A788`
- **IT_SARD**: Sardinia - EIC: `10Y1001A1001A74G`
- **IT_SICI**: Sicily - EIC: `10Y1001A1001A75E`
- **IT_BRNN**: Brindisi - EIC: `10Y1001A1001A699`
- **IT_ROSN**: Rossano - EIC: `10Y1001A1001A77A`
- **IT_FOGN**: Foggia - EIC: `10Y1001A1001A72K`
- **IT_CALA**: Calabria - EIC: `10Y1001C--00096J`
- **IT_PRGP**: Priolo - EIC: `10Y1001A1001A76C`
- **IT_GR**: Greece (border area) - EIC: `10Y1001A1001A66F`

### Norway (NOR)
Norway has 5 price zones:
- **NO_1**: Eastern Norway - EIC: `10YNO-1--------2`
- **NO_2**: Southern Norway - EIC: `10YNO-2--------T`
- **NO_3**: Central Norway - EIC: `10YNO-3--------J`
- **NO_4**: Western Norway - EIC: `10YNO-4--------9`
- **NO_5**: Northern Norway - EIC: `10Y1001A1001A48H`

### Sweden (SWE)
Sweden has 4 price zones:
- **SE_1**: Northern Sweden - EIC: `10Y1001A1001A44P`
- **SE_2**: Central Sweden - EIC: `10Y1001A1001A45N`
- **SE_3**: Southern Sweden - EIC: `10Y1001A1001A46L`
- **SE_4**: Eastern Sweden - EIC: `10Y1001A1001A47J`

### United Kingdom (GBR)
Multiple interconnection zones:
- **GB**: National Grid BZ - EIC: `10YGB----------A`
- **GB_IFA**: France interconnector (IFA) - EIC: `10Y1001C--00098F`
- **GB_IFA2**: France interconnector (IFA2) - EIC: `17Y0000009369493`
- **GB_ELECLINK**: ElecLink interconnector - EIC: `11Y0-0000-0265-K`
- **UK**: United Kingdom aggregate - EIC: `10Y1001A1001A92E`

### Ukraine (UKR)
Three separate control transmission areas:
- **UA**: Main Ukraine BZ - EIC: `10Y1001C--00003F`
- **UA_DOBTPP**: DobTPP control area - EIC: `10Y1001A1001A869`
- **UA_BEI**: BEI control area - EIC: `10YUA-WEPS-----0`
- **UA_IPS**: IPS control area - EIC: `10Y1001C--000182`

### Cross-Border Zones
Some zones are shared or relate to multiple countries:
- **DE_AT_LU**: Germany-Austria-Luxembourg zone - EIC: `10Y1001A1001A63L`
- **DE_LU**: Germany-Luxembourg zone - EIC: `10Y1001A1001A82H`

---

## EIC Code Format

The European Identification Code (EIC) follows ISO 15118:2014 standard:

**Format:** `10Y[2-char country/region code][12 alphanumeric characters]`

**Structure:**
- **10Y**: Fixed ENTSO-E prefix
- **[2-4 chars]**: Country or region code
- **[rest]**: Unique identifier

**Examples:**
- `10YAT-APG------L` → Austria, APG operator
- `10YCZ-CEPS-----N` → Czech Republic, CEPS operator
- `10Y1001A1001A63L` → Germany-Austria-Luxembourg merged zone

---

## Acronyms and Abbreviations

| Acronym | Meaning |
|---------|---------|
| BZ | Bidding Zone |
| CA | Control Area |
| MBA | Market Balance Area |
| BZA | Bidding Zone Area |
| CTA | Control Transmission Area |
| TSO | Transmission System Operator |
| EIC | European Identification Code (Unique Identification Code - UIC) |
| ENTSO-E | European Network of Transmission System Operators for Electricity |

---

## Usage Examples

### Python (using entsoe-py)
```python
from entsoe import Area

# Get Austria
area = Area.AT  # Returns Area enum with EIC code 10YAT-APG------L
print(area.value)  # Output: 10YAT-APG------L

# Get specific zone
area = Area.DE_AT_LU  # DE-AT-LU merged zone
print(area.meaning)  # Output: DE-AT-LU BZ

# Lookup by code
country_code = 'BE'
area = Area[country_code]  # Returns Belgium area
```

### Direct API Usage
```
https://transparency.entsoe.eu/content/eic/list/
```

---

## Key Notes

1. **Time Zone Variations**: Each area has its own timezone for market operations
2. **Dynamic Changes**: Some bidding zones may change over time due to regulatory changes (e.g., DE_AT_LU was formed from merger of separate zones)
3. **Historical Codes**: Some legacy codes are maintained for backward compatibility
4. **Regulatory Basis**: All zones are defined in accordance with ENTSO-E transparency platform guidelines
5. **Multi-Character Country Codes**: Some special zones use non-standard codes like `XK` (Kosovo) and `XX` (cross-border zones)

---

## References

- **Official ENTSO-E Transparency Platform**: https://transparency.entsoe.eu/
- **ENTSO-E API Documentation**: https://documenter.getpostman.com/view/7009892/2s93JtP3F6
- **entsoe-py Library**: https://github.com/EnergieID/entsoe-py
- **EIC Code Standard**: ISO 15118:2014

---

## Data Files Provided

1. **entsoe_bidding_zones.json** - Complete JSON format with all metadata
2. **entsoe_bidding_zones.csv** - CSV format for spreadsheet applications
3. **entsoe_bidding_zones_mapping.md** - This reference guide

---

*This mapping is derived from official ENTSO-E sources and is current as of February 21, 2026.*
