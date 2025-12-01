import requests

pixela_endpoint = "https://pixe.la/v1/users"

# Find more info on https://docs.pixe.la/entry/post-user#Request-Body
user_params = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)

print(response.text)

# def main():
#     print('Hello Day 37')
#
# if __name__ == '__main__':
#     main()
