#!/usr/bin/python3

"""
This script fetches the status from https://alx-intranet.hbtn.io/status using the requests package.
It then displays the body of the response in a specific format.
"""

import requests

def fetch_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status.
    """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    status_body = fetch_status()

    # Displaying the body of the response
    print("- Body response:")
    print("\t- type:", type(status_body))
    print("\t- content:", status_body)
