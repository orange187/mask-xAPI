import requests


def create_topic(topicdata):

    url = 'http://3.84.114.207/'
    r = requests.post(url=url,json=topicdata)
    return r

def get_token():
    return