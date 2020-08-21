class Twitter:
    version = '1.0'

    def __init__(self):
        self.tweets = []

    def tweet(self, message):
        if len(message) > 140:
            raise Exception('Message to long')
        self.tweets.append(message)
