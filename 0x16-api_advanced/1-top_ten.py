#!/usr/bin/python3
"""Module to consume Reddit API and
get the number of suscribers to given subreddit
"""

import requests


def top_ten(subreddit):
    """Takes a subreddir and makes a GET requests
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) \
                              AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
                              85.0.4183.102 Safari/537.36'}

    limit = 10
    query = {'limit': limit}
    response = requests.get(url,
                            headers=headers,
                            allow_redirects=False,
                            params=query)

    if response.status_code < 201:
        json_response = response.json()
        count = 0
        while count < limit:
            print(json_response.get('data')
                  .get('children')[count].get('data').get('title'))
            count += 1
    else:
        print(None)
