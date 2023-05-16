#!/usr/bin/python3
<<<<<<< HEAD
"""
Contains the number_of_subscribers function
"""

=======
<<<<<<< HEAD
"""Function to query subscribers on a given Reddit subreddit."""
>>>>>>> 21c35ece6033d103b3c189a01f16aaaae15e1f54
import requests


def number_of_subscribers(subreddit):
<<<<<<< HEAD
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:\
v1.0.0 (by /u/aaorrico23)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
=======
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
=======
""" queries the Reddit API and returns the number of subscribers
 (not active users, total subscribers) for a given subreddit."""

import requests

def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "MyPythonScript"})
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
>>>>>>> f76b6430d14c5b3cfa515ade96aecd5011262cd8
>>>>>>> 21c35ece6033d103b3c189a01f16aaaae15e1f54
