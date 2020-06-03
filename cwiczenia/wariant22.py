import urllib.request
import json
from pprint import pprint


# POST GETTER
url_post = "https://jsonplaceholder.typicode.com/posts"
json_post = urllib.request.urlopen(url_post)
post_data = json.loads(json_post.read())

# USER GETTER
url_user = "https://jsonplaceholder.typicode.com/users"
json_user = urllib.request.urlopen(url_user)
user_data = json.loads(json_user.read())


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


if __name__ == '__main__':
    script()