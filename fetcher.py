# fetcher.py

import requests
from json import decoder
from urllib.parse import quote_plus

def get_user_id(username, session_id):
    headers = {
        "User-Agent": "iPhone UA",
        "x-ig-app-id": "936619743392459"
    }

    api = requests.get(
        f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}',
        headers=headers,
        cookies={'sessionid': session_id}
    )

    try:
        if api.status_code == 404:
            return {"id": None, "error": "User not found"}

        user_id = api.json()["data"]["user"]["id"]
        return {"id": user_id, "error": None}

    except decoder.JSONDecodeError:
        return {"id": None, "error": "Rate limit"}

def get_user_info(search, session_id, search_type="username"):
    if search_type == "username":
        data = get_user_id(search, session_id)
        if data["error"]:
            return data
        user_id = data["id"]
    else:
        try:
            user_id = str(int(search))
        except ValueError:
            return {"user": None, "error": "Invalid ID"}

    try:
        response = requests.get(
            f'https://i.instagram.com/api/v1/users/{user_id}/info/',
            headers={'User-Agent': 'Instagram 64.0.0.14.96'},
            cookies={'sessionid': session_id}
        )
        if response.status_code == 429:
            return {"user": None, "error": "Rate limit"}

        response.raise_for_status()

        info_user = response.json().get("user")
        if not info_user:
            return {"user": None, "error": "Not found"}

        info_user["userID"] = user_id
        return {"user": info_user, "error": None}

    except requests.exceptions.RequestException:
        return {"user": None, "error": "Not found"}

def advanced_lookup(username):
    payload = "signed_body=SIGNATURE." + quote_plus(
        '{"q":"%s","skip_recovery":"1"}' % username
    )

    headers = {
        "Accept-Language": "en-US",
        "User-Agent": "Instagram 101.0.0.15.120",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-IG-App-ID": "124024574287414",
        "Accept-Encoding": "gzip, deflate",
        "Host": "i.instagram.com",
        "Connection": "keep-alive",
        "Content-Length": str(len(payload))
    }

    try:
        api = requests.post(
            'https://i.instagram.com/api/v1/users/lookup/',
            headers=headers,
            data=payload
        )
        return {"user": api.json(), "error": None}
    except decoder.JSONDecodeError:
        return {"user": None, "error": "rate limit"}
