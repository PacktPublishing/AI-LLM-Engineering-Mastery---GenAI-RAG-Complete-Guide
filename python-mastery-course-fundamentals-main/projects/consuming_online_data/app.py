import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {"title": "Python and APIs", "body": "This is a test", "userid": 2}
response = requests.post(url, json=data)

print(response.json())

# res = requests.get(url)

# posts = res.json()

# for post in posts[:10]:
#     print(f"Post Title: {post['title']}")
