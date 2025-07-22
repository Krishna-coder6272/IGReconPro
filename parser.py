# parser.py

import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code
import pycountry

def format_phone(raw_phone):
    try:
        # Parse phone number
        phone_obj = phonenumbers.parse(raw_phone)
        country_code = region_code_for_country_code(phone_obj.country_code)
        country = pycountry.countries.get(alpha_2=country_code)
        country_name = country.name if country else "Unknown"

        return f"{raw_phone} ({country_name})"
    except Exception:
        return raw_phone + " (Unknown)"
