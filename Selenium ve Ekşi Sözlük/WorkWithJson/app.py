import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")


data = r.json()                    # json response is stored in 'data'


post_num = data['id']
user = data['userId']
title = data['title']
body = data['body']

print(f"Post number: {post_num}")
print(f"Written by user: {user}")
print("Title: " + title)
print()                             # just for space
print(body)


print(r.json())