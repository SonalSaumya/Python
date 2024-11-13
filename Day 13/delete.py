import requests

url = "https://reqres.in/api/userid"
def delete_user(url,user_id):
    full_url = f"{url}/{user_id}"
    print(full_url)

    response = requests.delete(full_url)

    try:
        if response.status_code == 204:
            print(response)
            print("Deleted")
        # else:
        #     print("Failed to delete ", response.status_code)
    except Exception as e:
        print(e)

delete_user(url,2)


