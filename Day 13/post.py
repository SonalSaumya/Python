import requests
post_url = "https://reqres.in/api/users"
post_data = {
    "name": "John Doe",
    "job": "Software Developer"

}

response = requests.post(post_url, json=post_data)