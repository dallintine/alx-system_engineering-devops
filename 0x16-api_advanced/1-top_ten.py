#!/usr/bin/python3
<<<<<<< HEAD
"""Function to print hot posts on a given Reddit subreddit."""
=======
""" queries the Reddit API and prints the titles of the first
 10 hot posts listed for a given subreddit."""

>>>>>>> f76b6430d14c5b3cfa515ade96aecd5011262cd8
import requests


def top_ten(subreddit):
<<<<<<< HEAD
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
=======
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "MyPythonScript"},
                            allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in response.json().get("data").get("children")]
>>>>>>> f76b6430d14c5b3cfa515ade96aecd5011262cd8
