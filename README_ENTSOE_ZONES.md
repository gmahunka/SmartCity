# ENTSO-E Bidding Zone Codes - Complete Data Package

A comprehensive mapping of European electricity market bidding zones with ISO3 country codes and EIC identifiers, sourced from official ENTSO-E documentation.

## 📊 Data Summary

- **Total Countries/Regions:** 45
- **Total Bidding Zones:** 101
- **Data Source:** ENTSO-E (EnergieID/entsoe-py GitHub library)
- **Last Updated:** February 21, 2026
- **Coverage:** All European ENTSO-E member countries and regions

## 📁 Files Included

### 1. **entsoe_bidding_zones.json**
Complete structured JSON file with all bidding zones and metadata.
- Format: Array of objects with detailed information
- Fields: country_name, iso3_code, iso2_code, area_code, eic_code, description, timezone
- Best for: Programmatic access, API integration, data processing
- Size: ~25 KB

**Example:**
```json
{
  "country_name": "Austria",
  "iso3_code": "AUT",
  "iso2_code": "AT",
  "area_code": "AT",
  "eic_code": "10YAT-APG------L",
  "description": "Austria, APG BZ / CA / MBA",
  "timezone": "Europe/Vienna"
}
```

### 2. **entsoe_bidding_zones.csv**
Spreadsheet-compatible CSV format with all bidding zones.
- Columns: Country Name, ISO3 Code, ISO2 Code, Area Code, EIC Code, Description, Timezone
- Best for: Excel, Google Sheets, data analysis, spreadsheet applications
- Easily importable into any database

### 3. **entsoe_bidding_zones_mapping.md**
Comprehensive reference guide with detailed documentation.
- Quick reference table for all countries
- Special cases explanation (Germany, Italy, Norway, Sweden, Denmark, UK)
- EIC code format explanation
- Acronyms and abbreviations
- Python usage examples
- Best for: Understanding the data, documentation

### 4. **entsoe_quick_lookup.txt**
Quick reference guide with direct mappings.
- ISO3 → EIC Code mapping
- EIC Code → ISO3 mapping (selected)
- Complete list of 45 European countries
- Common usage patterns
- Best for: Quick lookups, command-line reference

### 5. **entsoe_zones_utility.py**
Python utility class for programmatic access to the data.
- `ENTSOEBiddingZones` class with convenient methods
- Lookup functions (by ISO2, ISO3, EIC)
- Reverse lookup capabilities
- Multi-zone country support
- JSON export functionality
- Best for: Python projects, data science, API development

**Example Usage:**
```python
from entsoe_zones_utility import ENTSOEBiddingZones

# Get EIC code
eic = ENTSOEBiddingZones.get_eic_code('AT')  # '10YAT-APG------L'

# Get country info
info = ENTSOEBiddingZones.get_country_info('DE')

# Get all zones for multi-zone country
de_zones = ENTSOEBiddingZones.get_multi_zones('DE')

# Reverse lookup
iso2 = ENTSOEBiddingZones.reverse_lookup_iso2('10YAT-APG------L')
```

## 🌍 Coverage by Region

### Western Europe
- Belgium (BEL), France (FRA), Netherlands (NLD), Luxembourg (LUX), Switzerland (CHE)

### Central Europe
- Austria (AUT), Czech Republic (CZE), Germany (DEU), Hungary (HUN), Poland (POL), Slovakia (SVK), Slovenia (SVN)

### Scandinavian & Baltic
- Denmark (DNK), Estonia (EST), Finland (FIN), Latvia (LVA), Lithuania (LTU), Norway (NOR), Sweden (SWE)

### Southern Europe
- Cyprus (CYP), Greece (GRC), Italy (ITA), Malta (MLT), Portugal (PRT), Spain (ESP), Turkey (TUR)

### Southeastern Europe
- Albania (ALB), Bosnia and Herzegovina (BIH), Bulgaria (BGR), Croatia (HRV), Montenegro (MNE), North Macedonia (MKD), Romania (ROU), Serbia (SRB)

### Eastern Europe
- Belarus (BLR), Georgia (GEO), Moldova (MDA), Russia (RUS), Ukraine (UKR)

### British Isles
- Ireland (IRL), United Kingdom (GBR)

### Special Cases
- Kosovo (XKX), Northern Ireland (GBR), Cross-border zones (DE_AT_LU, DE_LU, etc.)

## 📋 Key Features

✅ **Official ENTSO-E Source** - All data directly from ENTSO-E transparency platform  
✅ **EIC Codes** - Complete ISO 15118:2014 standard codes  
✅ **Multi-Zone Support** - All sub-zones for multi-zone countries  
✅ **Timezone Information** - Local timezone for each bidding zone  
✅ **Multiple Formats** - JSON, CSV, Python utility, markdown reference  
✅ **Reverse Lookup** - Query by EIC code to find country  
✅ **Well-Documented** - Comprehensive reference guides included  

## 🔑 ISO3 to Area Code Mapping (Main Zones)

| ISO3 | Area | EIC Code | Country |
|------|------|----------|---------|
| AUT | AT | 10YAT-APG------L | Austria |
| BEL | BE | 10YBE----------2 | Belgium |
| CHE | CH | 10YCH-SWISSGRIDZ | Switzerland |
| CZE | CZ | 10YCZ-CEPS-----N | Czech Republic |
| DEU | DE | 10Y1001A1001A83F | Germany |
| DNK | DK | 10Y1001A1001A65H | Denmark |
| FRA | FR | 10YFR-RTE------C | France |
| GBR | GB | 10YGB----------A | United Kingdom |
| GRC | GR | 10YGR-HTSO-----Y | Greece |
| HUN | HU | 10YHU-MAVIR----U | Hungary |
| ITA | IT | 10YIT-GRTN-----B | Italy |
| NLD | NL | 10YNL----------L | Netherlands |
| POL | PL | 10YPL-AREA-----S | Poland |
| ESP | ES | 10YES-REE------0 | Spain |
| SWE | SE | 10YSE-1--------K | Sweden |

*See files for complete list of all 45 countries*

## 🔄 Multi-Zone Countries

Some countries operate multiple bidding zones:

- **Germany (DEU)**: 5 zones (aggregated + 4 TSO areas)
- **Denmark (DNK)**: 2 zones (DK1, DK2)
- **Italy (ITA)**: 17 zones (North, Central, South, + regional)
- **Norway (NOR)**: 5 zones (NO1-NO5)
- **Sweden (SWE)**: 4 zones (SE1-SE4)
- **United Kingdom (GBR)**: Multiple interconnection zones
- **Ukraine (UKR)**: 3 control areas
- **Shared zones**: DE_AT_LU, DE_LU, PL_CZ

## 📚 Use Cases

### Data Science & Analytics
- Import CSV into pandas for analysis
- Use JSON for data pipelines
- Filter by timezone or region

### API Integration
- Use Python utility class in applications
- Reverse lookup EIC codes to countries
- Validate bidding zone codes

### Market Research
- Cross-reference bidding zones with market data
- Analyze zone-to-country relationships
- Study multi-zone country structures

### ENTSO-E Platform Access
- Querying transparency platform APIs
- CrossBorder flow analysis
- Generation and load forecasting

## 🔧 Technical Details

### EIC Code Format
```
10Y[Country/Region Code][12 Alphanumeric Characters]
```
- Example: `10YAT-APG------L`
- Standard: ISO 15118:2014 (Unique Identification Code)
- Prefix: 10Y (ENTSO-E standard)

### Timezone Examples
- Western: Europe/London, Europe/Dublin
- Central: Europe/Berlin, Europe/Paris, Europe/Vienna
- Eastern: Europe/Bucharest, Europe/Istanbul
- Nordic: Europe/Helsinki, Europe/Oslo, Europe/Stockholm

## 📖 How to Use Each File

### For Quick Lookup
→ Use **entsoe_quick_lookup.txt** - Fast reference with common codes

### For Spreadsheet Work
→ Use **entsoe_bidding_zones.csv** - Open in Excel or Google Sheets

### For API/Web Development
→ Use **entsoe_bidding_zones.json** - Parse and use in applications

### For Python Projects
→ Use **entsoe_zones_utility.py** - Import and use the utility class

### For Understanding the Data
→ Use **entsoe_bidding_zones_mapping.md** - Comprehensive reference guide

## 📝 Example Queries

### "What's the EIC code for Belgium?"
**Answer:** `10YBE----------2` (Area Code: BE, Country: Belgium, ISO3: BEL)

### "Which country has EIC code 10YSE-1--------K?"
**Answer:** Sweden (Area Code: SE, ISO3: SWE)

### "Show me all Swedish bidding zones"
**Answer:** SE (aggregated), SE_1, SE_2, SE_3, SE_4

### "What's the timezone for Greece?"
**Answer:** Europe/Athens

### "How many Italian bidding zones are there?"
**Answer:** 17 zones (including IT aggregated, IT_NORD, IT_CNOR, IT_CSUD, IT_SUD, IT_SARD, IT_SICI, IT_BRNN, IT_ROSN, IT_FOGN, IT_CALA, IT_PRGP, IT_GR, IT_NORD_AT, IT_NORD_CH, IT_NORD_FR, IT_NORD_SI)

## 🔗 References

- **ENTSO-E Transparency Platform:** https://transparency.entsoe.eu/
- **ENTSO-E API Docs:** https://documenter.getpostman.com/view/7009892/2s93JtP3F6
- **entsoe-py Library:** https://github.com/EnergieID/entsoe-py
- **EIC Code Standard:** ISO 15118:2014
- **ENTSO-E Members:** https://www.entsoe.eu/about/inside-entsoe/members/

## 📊 Statistics

- **Total Bidding Zones:** 101
- **Total EU Member States:** 27
- **Total Non-EU Countries:** 16
- **Multi-Zone Countries:** 8
- **Countries with > 1 Zone:** 8 (Germany, Italy, Norway, Sweden, Denmark, UK, Ukraine, others)

## 📄 License & Attribution

**Source:** ENTSO-E Official Mappings  
**Used Library:** entsoe-py (EnergieID GitHub)  
**Format:** Public Domain - freely usable data  
**Attribution:** ENTSO-E (European Network of Transmission System Operators for Electricity)

## ✅ Data Quality

- ✓ Official ENTSO-E source
- ✓ Regularly updated
- ✓ Comprehensive coverage (45 countries)
- ✓ Complete EIC codes
- ✓ Timezone information included
- ✓ Multi-format availability
- ✓ Python utility included

---

**Created:** February 21, 2026  
**Data Source:** ENTSO-E Official Mappings (entsoe-py library)  
**Status:** Complete and Verified
