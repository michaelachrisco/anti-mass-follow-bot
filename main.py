import os
import requests
from typing import List

GITHUB_API_URL = "https://api.github.com"
USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GH_TOKEN")
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def get_followers(username: str) -> List[str]:
    followers = []
    page = 1
    while True:
        url = f"{GITHUB_API_URL}/users/{username}/followers?page={page}&per_page=100"
        res = requests.get(url, headers=HEADERS)
        if res.status_code != 200:
            print("Error fetching followers:", res.text)
            break
        data = res.json()
        if not data:
            break
        followers.extend([user['login'] for user in data])
        page += 1
    return followers


def is_mass_follower(username: str, threshold: int = 1000) -> bool:
    url = f"{GITHUB_API_URL}/users/{username}"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        print(f"Error checking user {username}:", res.text)
        return False
    user_data = res.json()
    return user_data.get("following", 0) >= threshold


def block_user(username: str):
    url = f"{GITHUB_API_URL}/user/blocks/{username}"
    res = requests.put(url, headers=HEADERS)
    if res.status_code == 204:
        print(f"Blocked {username}")
    else:
        print(f"Failed to block {username}:", res.text)


def main():
    if not USERNAME or not TOKEN:
        print("Missing GITHUB_USERNAME or GH_TOKEN environment variable.")
        return

    print(f"Scanning followers of @{USERNAME}...")
    followers = get_followers(USERNAME)
    print(f"Found {len(followers)} followers.")

    for follower in followers:
        if is_mass_follower(follower):
            print(f"{follower} is a suspected bot. Blocking...")
            block_user(follower)


if __name__ == "__main__":
    main()
