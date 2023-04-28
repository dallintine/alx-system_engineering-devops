#!/usr/bin/python3
<<<<<<< HEAD
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
=======
""" This modules defines a function recurse that
queries the Reddit API and returns a list containing the titles of all hot
 articles for a given subreddit. """

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """queries the Reddit API and returns a list containing the titles of all
 hot articles for a given subreddit."""

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={"User-Agent": "MyPythonScript"},
                            params={"count": count, "after": after},
                            allow_redirects=False)
    if response.status_code >= 400:
        return None

    full_hotlst = hot_list + [child.get("data").get("title")
                              for child in response.json()
                              .get("data")
                              .get("children")]
    page_info = response.json()
    if not page_info.get("data").get("after"):
        return full_hotlst

    return recurse(subreddit, full_hotlst, page_info.get("data").get("count"),
                   page_info.get("data").get("after"))
>>>>>>> f76b6430d14c5b3cfa515ade96aecd5011262cd8
