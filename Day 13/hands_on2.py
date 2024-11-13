import requests
post_url = "https://jsonplaceholder.typicode.com/posts"

post_data = {
    "city": "New York",
    "temperature": 28,
    "hunidity": 60,
    "condition": "Sunny"
}


def info(url,jsonbody):
    response = requests.post(post_url, json=post_data)
    if response.status_code == 201:
        print("Response recieved")
    else:
        print("Failed to receive ", response.status_code)

    print(response.status_code)

info(post_url,post_data)


