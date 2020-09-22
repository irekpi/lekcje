from twitter import Twitter
import pytest
from unittest.mock import patch, Mock, MagicMock
import requests


class ResponseGetMock:
    def json(self):
        return {'avatar_url': 'test'}


@pytest.fixture(params=[None, 'python'])
def username(request):
    return request.param


@pytest.fixture(params=['list', 'backend'], name='twitter')
def fixture_twitter(backend, username, request, monkeypatch):
    if request.param == 'list':
        twitter = Twitter(username=username)
    elif request.param == 'backend':
        twitter = Twitter(username=username, backend=backend)

    return twitter


def test_twitter_initialization(twitter):
    assert twitter


@patch.object(requests, 'get',
              return_value=ResponseGetMock())  # noqa ---> przekazanie tego obiektu do testu nizej jako pierwszy argument
def test_tweet_single_msg(avatar_mock, twitter):
    twitter.tweet('MSG')
    assert twitter.tweet_messages == ['MSG']


def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet('test' * 41)
    assert twitter.tweet_messages == []


def test_init_two_twitter_classes(backend):
    twitter_1 = Twitter(backend=backend)
    twitter_2 = Twitter(backend=backend)

    twitter_1.tweet('Test 1')
    twitter_2.tweet('test 2')

    assert twitter_2.tweet_messages == ['Test 1', 'test 2']


@pytest.mark.parametrize('message, expected', (
        ('Test #Tweet msg', ['tweet']),
        ('#Tweet in msg', ['tweet']),
        ('Test #TWEET msg', ['tweet']),
        ('Test #TWEET msg #SECONDTWEET ', ['tweet', 'secondtweet']),
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_username(avatar_mock, twitter):
    if not twitter.username:
        pytest.skip()
    twitter.tweet('Test message')
    assert twitter.tweets == [{
        'message': 'Test message',
        'avatar': 'test',
        'hashtags': [],
    }]
    avatar_mock.assert_called()


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_hashtags(avatar_mock, twitter):
    twitter.find_hashtags = Mock()
    twitter.find_hashtags.return_value = ['first']
    twitter.tweet('Test #second')
    assert twitter.tweets[0]['hashtags'] == ['first']
    twitter.find_hashtags.assert_called_with('Test #second')


def test_twitter_version(twitter):
    twitter.version = MagicMock()
    twitter.version.__eq__.return_value = '2.0'
    assert twitter.version == '2.0'
