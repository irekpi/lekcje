import urllib.request
import json
# urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts") as post_url:
# json_post = urllib.urlopen(url_post)

# POST GETTER
url_post = "https://jsonplaceholder.typicode.com/posts"
json_post = urllib.request.urlopen(url_post)
post_data = json.loads(json_post.read())

# USER GETTER
url_user = "https://jsonplaceholder.typicode.com/users"
json_user = urllib.request.urlopen(url_user)
user_data = json.loads(json_user.read())

baza = {}

for i in user_data:
    user = i['id']
    #print(user)
    for j in post_data:
        post = j['userId']
        #print (post)
        if post == user:
            user_post = 'user_post'
            baza.setdefault(user_post, []).append([
                j['userId'],
                j['id'],
                j['title'],
                j['body']
            ])


print(type(user_data))
print(type(baza))


# posts = {
#     'apple': 2,
#     'banana': 'called',
# }
# if post_data['user_id'] == user_data['id']:
#     posts.append([{
#         post_data['id'],
#         post_data['title'],
#         post_data['body']}])
# print(post_data)
# print(user_data['name'])
