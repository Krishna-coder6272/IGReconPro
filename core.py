# core.py

import argparse
from fetcher import get_user_info, advanced_lookup
from parser import format_phone
from export import export_to_json
from utils import color, log

def main():
    parser = argparse.ArgumentParser(description="IGReconPro - Instagram OSINT Tool")
    parser.add_argument('-s', '--sessionid', required=True, help="Instagram session ID")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--username', help="Instagram username")
    group.add_argument('-i', '--id', help="Instagram user ID")

    args = parser.parse_args()
    session_id = args.sessionid
    search = args.username if args.username else args.id
    search_type = "username" if args.username else "id"

    log(f"🔍 Searching for: {search}", "cyan")
    info_data = get_user_info(search, session_id, search_type)

    if info_data["error"]:
        log(f"❌ Error: {info_data['error']}", "red")
        return

    user = info_data["user"]
    log(f"✅ Found: @{user['username']}", "green")
    print("-" * 50)

    print(f"{color('Username', 'yellow')}: {user['username']}")
    print(f"{color('User ID', 'yellow')}: {user['userID']}")
    print(f"{color('Full Name', 'yellow')}: {user['full_name']}")
    print(f"{color('Verified', 'yellow')}: {user['is_verified']}")
    print(f"{color('Business Account', 'yellow')}: {user['is_business']}")
    print(f"{color('Private Account', 'yellow')}: {user['is_private']}")
    print(f"{color('Followers', 'yellow')}: {user['follower_count']} | Following: {user['following_count']}")
    print(f"{color('Posts', 'yellow')}: {user['media_count']}")
    print(f"{color('IGTV', 'yellow')}: {user['total_igtv_videos']}")
    if user.get("external_url"):
        print(f"{color('External URL', 'yellow')}: {user['external_url']}")
    print(f"{color('Biography', 'yellow')}:\n  {user['biography']}")
    print(f"{color('WhatsApp Linked', 'yellow')}: {user.get('is_whatsapp_linked')}")
    print(f"{color('Memorial Account', 'yellow')}: {user.get('is_memorialized')}")
    print(f"{color('New User', 'yellow')}: {user.get('is_new_to_instagram')}")

    # Optional public email
    if user.get("public_email"):
        print(f"{color('Public Email', 'yellow')}: {user['public_email']}")

    # Optional public phone
    if user.get("public_phone_number"):
        phone = f"+{user['public_phone_country_code']} {user['public_phone_number']}"
        formatted = format_phone(phone)
        print(f"{color('Public Phone', 'yellow')}: {formatted}")

    print("-" * 50)

    # Advanced Lookup
    lookup = advanced_lookup(user['username'])

    if lookup['error'] == "rate limit":
        log("⚠️ Rate limit hit. Try after some time.", "red")
    elif lookup["user"].get("message") == "No users found":
        log("❌ Lookup failed: No users found", "red")
    else:
        obfuscated_email = lookup["user"].get("obfuscated_email")
        obfuscated_phone = lookup["user"].get("obfuscated_phone")
        if obfuscated_email:
            print(f"{color('Obfuscated Email', 'magenta')}: {obfuscated_email}")
        if obfuscated_phone:
            print(f"{color('Obfuscated Phone', 'magenta')}: {obfuscated_phone}")

    export_to_json(user, user['username'])
    log("✅ All data fetched & saved successfully!", "green")

if __name__ == "__main__":
    main()
