import json
import re
from urllib.parse import urljoin
import requests

USER_API = 'https://api.github.com/users'


class Twitter:
    version = '1.0'

    def __init__(self, backend=None, username=None):
        self.backend = backend
        self._tweets = []
        self.username = username

    def find_hashtags(self, message):
        return [msg.lower() for msg in re.findall(r"#(\w+)", message)]

    def tweet(self, message):
        if len(message) > 140:
            raise Exception('Message to long')
        self.tweets.append({
            'message': message,
            'avatar': self.get_user_avatar(),
            'hashtags': self.find_hashtags(message),
        })
        if self.backend:
            with open(self.backend, 'w') as twitter_file:
                self.backend.write(json.dumps(self._tweets))

    def get_user_avatar(self):
        if not self.username:
            return None
        url = urljoin(USER_API, self.username)
        resp = requests.get(url)
        return resp.json()['avatar_url']

    @property
    def tweets(self):
        if self.backend and not self._tweets:
            backend_text = self.backend.read()
            if backend_text:
                self._tweets = json.loads(backend_text)
        return self._tweets

    @property
    def tweet_messages(self):
        return [tweet['message'] for tweet in self._tweets]
