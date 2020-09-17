#!/usr/bin/python3
"""
Request the top ten hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Gets recursively the top hot posts in Reddit API
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    query = {'after': after, 'limit': 2}
    response = requests.get(url,
                            allow_redirects=False,
                            params=query,
                            headers={'User-Agent': 'MyMachintosh'})
    if response and response.status_code < 300:
        after = response.json().get('data').get('after')
        if (after is None or len(hot_list) == 10):
            return hot_list
        post_list = response.json().get('data').get('children')
        for children in post_list:
            hot_list.append(children.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    else:
        return None
