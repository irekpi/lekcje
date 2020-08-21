from twitter import Twitter
import pytest


def test_twitter_initialization():
    twitter = Twitter()
    assert twitter


def test_tweet_single_msg():
    twitter = Twitter()
    twitter.tweet('MSG')
    assert twitter.tweets == ['MSG']


def test_tweet_long_message():
    twitter = Twitter()
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
    assert twitter.tweets == []
