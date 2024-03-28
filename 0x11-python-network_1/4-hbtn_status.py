#!/usr/bin/python3

"""
Fetches the status from https://alx-intranet.hbtn.io/status using the requests package.
Then displays the body of the response in a specific format.
"""

import requests

def fetch_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status.
    """
    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    status_body = fetch_status()

    # Displaying the body of the response
    print("- Body response:")
    print("\t- type:", type(status_body))
    print("\t- content:", status_body)
