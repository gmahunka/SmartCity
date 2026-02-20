"""
ENTSO-E Bidding Zone Mapping Utility
Provides convenient access to ENTSO-E bidding zone codes and their ISO3 mappings
"""

import json
from typing import Dict, List, Optional, Tuple


class ENTSOEBiddingZones:
    """Utility class for ENTSO-E bidding zone lookups"""
    
    # Core mapping dictionary
    ZONES = {
        'AT': ('AUT', '10YAT-APG------L', 'Austria', 'Europe/Vienna'),
        'AL': ('ALB', '10YAL-KESH-----5', 'Albania', 'Europe/Tirane'),
        'BY': ('BLR', '10Y1001A1001A51S', 'Belarus', 'Europe/Minsk'),
        'BE': ('BEL', '10YBE----------2', 'Belgium', 'Europe/Brussels'),
        'BA': ('BIH', '10YBA-JPCC-----D', 'Bosnia and Herzegovina', 'Europe/Sarajevo'),
        'BG': ('BGR', '10YCA-BULGARIA-R', 'Bulgaria', 'Europe/Sofia'),
        'CH': ('CHE', '10YCH-SWISSGRIDZ', 'Switzerland', 'Europe/Zurich'),
        'CY': ('CYP', '10YCY-1001A0003J', 'Cyprus', 'Asia/Nicosia'),
        'CZ': ('CZE', '10YCZ-CEPS-----N', 'Czech Republic', 'Europe/Prague'),
        'DE': ('DEU', '10Y1001A1001A83F', 'Germany', 'Europe/Berlin'),
        'DK': ('DNK', '10Y1001A1001A65H', 'Denmark', 'Europe/Copenhagen'),
        'EE': ('EST', '10Y1001A1001A39I', 'Estonia', 'Europe/Tallinn'),
        'ES': ('ESP', '10YES-REE------0', 'Spain', 'Europe/Madrid'),
        'FI': ('FIN', '10YFI-1--------U', 'Finland', 'Europe/Helsinki'),
        'FR': ('FRA', '10YFR-RTE------C', 'France', 'Europe/Paris'),
        'GB': ('GBR', '10YGB----------A', 'United Kingdom', 'Europe/London'),
        'GE': ('GEO', '10Y1001A1001B012', 'Georgia', 'Asia/Tbilisi'),
        'GR': ('GRC', '10YGR-HTSO-----Y', 'Greece', 'Europe/Athens'),
        'HR': ('HRV', '10YHR-HEP------M', 'Croatia', 'Europe/Zagreb'),
        'HU': ('HUN', '10YHU-MAVIR----U', 'Hungary', 'Europe/Budapest'),
        'IS': ('ISL', 'IS', 'Iceland', 'Atlantic/Reykjavik'),
        'IE': ('IRL', '10YIE-1001A00010', 'Ireland', 'Europe/Dublin'),
        'IT': ('ITA', '10YIT-GRTN-----B', 'Italy', 'Europe/Rome'),
        'LT': ('LTU', '10YLT-1001A0008Q', 'Lithuania', 'Europe/Vilnius'),
        'LU': ('LUX', '10YLU-CEGEDEL-NQ', 'Luxembourg', 'Europe/Luxembourg'),
        'LV': ('LVA', '10YLV-1001A00074', 'Latvia', 'Europe/Riga'),
        'MD': ('MDA', '10Y1001A1001A990', 'Moldova', 'Europe/Chisinau'),
        'MK': ('MKD', '10YMK-MEPSO----8', 'North Macedonia', 'Europe/Skopje'),
        'MT': ('MLT', '10Y1001A1001A93C', 'Malta', 'Europe/Malta'),
        'ME': ('MNE', '10YCS-CG-TSO---S', 'Montenegro', 'Europe/Podgorica'),
        'NL': ('NLD', '10YNL----------L', 'Netherlands', 'Europe/Amsterdam'),
        'NO': ('NOR', '10YNO-0--------C', 'Norway', 'Europe/Oslo'),
        'PL': ('POL', '10YPL-AREA-----S', 'Poland', 'Europe/Warsaw'),
        'PT': ('PRT', '10YPT-REN------W', 'Portugal', 'Europe/Lisbon'),
        'RO': ('ROU', '10YRO-TEL------P', 'Romania', 'Europe/Bucharest'),
        'RU': ('RUS', '10Y1001A1001A49F', 'Russia', 'Europe/Moscow'),
        'RS': ('SRB', '10YCS-SERBIATSOV', 'Serbia', 'Europe/Belgrade'),
        'SK': ('SVK', '10YSK-SEPS-----K', 'Slovakia', 'Europe/Bratislava'),
        'SI': ('SVN', '10YSI-ELES-----O', 'Slovenia', 'Europe/Ljubljana'),
        'SE': ('SWE', '10YSE-1--------K', 'Sweden', 'Europe/Stockholm'),
        'TR': ('TUR', '10YTR-TEIAS----W', 'Turkey', 'Europe/Istanbul'),
        'UA': ('UKR', '10Y1001C--00003F', 'Ukraine', 'Europe/Kiev'),
        'XK': ('XKX', '10Y1001C--00100H', 'Kosovo', 'Europe/Rome'),
    }
    
    # Multi-zone countries
    MULTI_ZONE_MAPPING = {
        'DE': {
            'DE_50HZ': ('10YDE-VE-------2', '50Hertz', 'Europe/Berlin'),
            'DE_AMPRION': ('10YDE-RWENET---I', 'Amprion', 'Europe/Berlin'),
            'DE_TENNET': ('10YDE-EON------1', 'TenneT GER', 'Europe/Berlin'),
            'DE_TRANSNET': ('10YDE-ENBW-----N', 'TransnetBW', 'Europe/Berlin'),
        },
        'DK': {
            'DK_1': ('10YDK-1--------W', 'Western Denmark', 'Europe/Copenhagen'),
            'DK_2': ('10YDK-2--------M', 'Eastern Denmark', 'Europe/Copenhagen'),
        },
        'IT': {
            'IT_NORD': ('10Y1001A1001A73I', 'North', 'Europe/Rome'),
            'IT_CNOR': ('10Y1001A1001A70O', 'Centre-North', 'Europe/Rome'),
            'IT_CSUD': ('10Y1001A1001A71M', 'Centre-South', 'Europe/Rome'),
            'IT_SUD': ('10Y1001A1001A788', 'South', 'Europe/Rome'),
            'IT_SARD': ('10Y1001A1001A74G', 'Sardinia', 'Europe/Rome'),
            'IT_SICI': ('10Y1001A1001A75E', 'Sicily', 'Europe/Rome'),
            'IT_BRNN': ('10Y1001A1001A699', 'Brindisi', 'Europe/Rome'),
            'IT_ROSN': ('10Y1001A1001A77A', 'Rossano', 'Europe/Rome'),
            'IT_FOGN': ('10Y1001A1001A72K', 'Foggia', 'Europe/Rome'),
            'IT_CALA': ('10Y1001C--00096J', 'Calabria', 'Europe/Rome'),
            'IT_PRGP': ('10Y1001A1001A76C', 'Priolo', 'Europe/Rome'),
            'IT_GR': ('10Y1001A1001A66F', 'Greece border', 'Europe/Rome'),
        },
        'NO': {
            'NO_1': ('10YNO-1--------2', 'Eastern', 'Europe/Oslo'),
            'NO_2': ('10YNO-2--------T', 'Southern', 'Europe/Oslo'),
            'NO_3': ('10YNO-3--------J', 'Central', 'Europe/Oslo'),
            'NO_4': ('10YNO-4--------9', 'Western', 'Europe/Oslo'),
            'NO_5': ('10Y1001A1001A48H', 'Northern', 'Europe/Oslo'),
        },
        'SE': {
            'SE_1': ('10Y1001A1001A44P', 'Northern', 'Europe/Stockholm'),
            'SE_2': ('10Y1001A1001A45N', 'Central', 'Europe/Stockholm'),
            'SE_3': ('10Y1001A1001A46L', 'Southern', 'Europe/Stockholm'),
            'SE_4': ('10Y1001A1001A47J', 'Eastern', 'Europe/Stockholm'),
        },
        'UA': {
            'UA_DOBTPP': ('10Y1001A1001A869', 'DobTPP', 'Europe/Kiev'),
            'UA_BEI': ('10YUA-WEPS-----0', 'BEI', 'Europe/Kiev'),
            'UA_IPS': ('10Y1001C--000182', 'IPS', 'Europe/Kiev'),
        },
        'GB': {
            'GB_IFA': ('10Y1001C--00098F', 'IFA Interconnector', 'Europe/London'),
            'GB_IFA2': ('17Y0000009369493', 'IFA2 Interconnector', 'Europe/London'),
            'GB_ELECLINK': ('11Y0-0000-0265-K', 'ElecLink Interconnector', 'Europe/London'),
        },
    }
    
    @classmethod
    def get_eic_code(cls, iso2_or_area: str) -> Optional[str]:
        """
        Get EIC code from ISO2 code or area code
        
        Args:
            iso2_or_area: ISO2 code (e.g., 'AT') or area code (e.g., 'DE_50HZ')
        
        Returns:
            EIC code or None if not found
        """
        iso2_or_area = iso2_or_area.upper()
        
        # Try main zones first
        if iso2_or_area in cls.ZONES:
            return cls.ZONES[iso2_or_area][1]
        
        # Try multi-zone mapping
        for country, zones in cls.MULTI_ZONE_MAPPING.items():
            if iso2_or_area in zones:
                return zones[iso2_or_area][0]
        
        return None
    
    @classmethod
    def get_iso3_code(cls, iso2: str) -> Optional[str]:
        """Get ISO3 code from ISO2 code"""
        iso2 = iso2.upper()
        if iso2 in cls.ZONES:
            return cls.ZONES[iso2][0]
        return None
    
    @classmethod
    def get_country_info(cls, iso2: str) -> Optional[Dict]:
        """Get complete information for a country"""
        iso2 = iso2.upper()
        if iso2 not in cls.ZONES:
            return None
        
        iso3, eic, country, timezone = cls.ZONES[iso2]
        return {
            'iso2': iso2,
            'iso3': iso3,
            'country': country,
            'eic_code': eic,
            'timezone': timezone,
            'zones': cls.MULTI_ZONE_MAPPING.get(iso2, {})
        }
    
    @classmethod
    def get_all_zones(cls) -> Dict[str, Tuple[str, str, str, str]]:
        """Get all bidding zones"""
        return cls.ZONES.copy()
    
    @classmethod
    def get_multi_zones(cls, iso2: str) -> Optional[Dict]:
        """Get all sub-zones for a multi-zone country"""
        iso2 = iso2.upper()
        return cls.MULTI_ZONE_MAPPING.get(iso2, None)
    
    @classmethod
    def get_all_iso3_codes(cls) -> List[str]:
        """Get all ISO3 codes"""
        return sorted(set(zone[0] for zone in cls.ZONES.values()))
    
    @classmethod
    def get_all_eic_codes(cls) -> List[str]:
        """Get all EIC codes"""
        eic_codes = [zone[1] for zone in cls.ZONES.values()]
        for country_zones in cls.MULTI_ZONE_MAPPING.values():
            for zone_info in country_zones.values():
                eic_codes.append(zone_info[0])
        return sorted(eic_codes)
    
    @classmethod
    def reverse_lookup_iso2(cls, eic_code: str) -> Optional[str]:
        """Reverse lookup: get ISO2 code from EIC code"""
        eic_code = eic_code.upper()
        
        # Check main zones
        for iso2, (_, zone_eic, _, _) in cls.ZONES.items():
            if zone_eic.upper() == eic_code:
                return iso2
        
        # Check multi-zones
        for country, zones in cls.MULTI_ZONE_MAPPING.items():
            for area_code, (zone_eic, _, _) in zones.items():
                if zone_eic.upper() == eic_code:
                    return country
        
        return None
    
    @classmethod
    def to_json(cls) -> str:
        """Export all mappings to JSON"""
        data = {
            'main_zones': {k: {
                'iso3': v[0],
                'eic_code': v[1],
                'country': v[2],
                'timezone': v[3]
            } for k, v in cls.ZONES.items()},
            'multi_zones': {k: {area: {
                'eic_code': zone_info[0],
                'description': zone_info[1],
                'timezone': zone_info[2]
            } for area, zone_info in zones.items()}
            for k, zones in cls.MULTI_ZONE_MAPPING.items()}
        }
        return json.dumps(data, indent=2)


# Example usage
if __name__ == '__main__':
    # Get EIC code for Austria
    print("EIC for Austria:", ENTSOEBiddingZones.get_eic_code('AT'))
    
    # Get country info
    print("\nGermany Info:")
    info = ENTSOEBiddingZones.get_country_info('DE')
    print(json.dumps(info, indent=2))
    
    # Get all zones for Germany
    print("\nGerman Zones:")
    de_zones = ENTSOEBiddingZones.get_multi_zones('DE')
    print(json.dumps(de_zones, indent=2))
    
    # Reverse lookup
    print("\nReverse lookup EIC '10YAT-APG------L':")
    print(ENTSOEBiddingZones.reverse_lookup_iso2('10YAT-APG------L'))
    
    # Get all ISO3 codes
    print(f"\nTotal ISO3 codes: {len(ENTSOEBiddingZones.get_all_iso3_codes())}")
    print("Sample:", ENTSOEBiddingZones.get_all_iso3_codes()[:10])
