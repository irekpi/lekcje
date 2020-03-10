import requests
from pprint import pprint
from math import dist


def _get(url):
    try:
        response = requests.get(url)
    except requests.RequestException:
        raise Exception('Cannot ')
    else:
        if response.status_code != 200:
            print('Cannot download data')
            return None
    return response


post_data = _get('https://jsonplaceholder.typicode.com/posts').json()
user_data = _get('https://jsonplaceholder.typicode.com/users').json()


def script():
    base = {}
    for user in user_data:
        user_id = user['id']
        for post in post_data:
            user_post = post['userId']
            if user_post == user_id:
                base.setdefault(user_id, {'user_name': user.get('name', 'No name')}).setdefault('posts', []).append({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body'],
                })

    pprint(base)


def counter():
    count = {}

    for item in post_data:
        if item['userId'] in count:
            count[item['userId']] += 1
        else:
            count[item['userId']] = 1

    for i in user_data:
        print('User {} posted: {} posts.'.format(i['username'], max(*count)))


def unique():
    unique_title = []

    for item in post_data:
        title = item['title']
        if title not in unique_title:
            unique_title.append(title)
    pprint(unique_title)


def get_user_data(user):
    try:
        geo = user['address']['geo']
        lat = float(geo['lat'])
        lng = float(geo['lng'])
        return lat, lng, user['name']
    except KeyError as error:
        print(error)
        raise


def distance():
    user_data = _get('https://jsonplaceholder.typicode.com/users').json()
    result = []

    for user1 in user_data:
        shortest_dist = None
        from_lat, from_lng, from_user = get_user_data(user1)
        user2_name = ''
        print('___')
        # del user_data[0]
        for user2 in user_data:
            to_lat, to_lng, to_user = get_user_data(user2)
            if from_user == to_user:
                continue
            way = dist([from_lat, from_lng], [to_lat, to_lng])
            if shortest_dist is None or way < shortest_dist:
                user2_name = to_user
                shortest_dist = way
            print(way, shortest_dist)
        result.append({
            'from_user': from_user,
            'to_user': user2_name,
            'shortest_dist': shortest_dist
        })
    return result


if __name__ == '__main__':
    # script()
    # counter()
    # unique()
    distance()

