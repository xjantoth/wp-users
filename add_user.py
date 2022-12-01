#!/usr/bin/env python3

import base64
import random
import requests
import string
import sys
import os

def create_user(url, data, headers):
    try:
        response = requests.post(
            url=url,
            data=data,
            headers=headers,
            verify=False
        )
        json_res = response.json()
        return {"message": f"user id: {json_res['id']} email: {json_res['email']} username: {json_res['name']}"}

    except Exception as e:
        print(f"Could not create user with payload: {data}, error: {e}")
        sys.exit(1)

# send link to reset
def send_email(url, email):
    try:
        res = requests.post(
            url=url,
            data={
                "user_login": email
            },
            verify=False,
            allow_redirects=False
        )
        return res
    except Exception as e:
        print(f"Could not send email: {email} error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    users = [
        {"email": "xyz@gmail.com","first_name": "Johny", "last_name": "Smith"},
        {"email": "liu.xyz@gmail.com","first_name": "Joe", "last_name": "Doe"},
    ]

    base_url = os.environ.get('WP_BASE_URL', "")
    password = os.environ.get('WP_API_PASS', "")
    user = os.environ.get('WP_API_USER', "")

    if password == "" or user == "" or base_url == "":
        print(f"Please export WP_API_PASS, WP_API_USER, WP_BASE_URL env variables!")
        sys.exit(1)

    url_create_user = f"{base_url}/wp-json/wp/v2/users"
    url_reset_pass =f"{base_url}/wp-login.php?action=lostpassword"
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

    for i in users:
        user_data = {
            "username": i["email"],
            "email": i["email"],
            "first_name": i["first_name"],
            "last_name": i["last_name"],
            "roles": ["customer"],
            "password": ''.join(random.choice(string.ascii_lowercase) for i in range(25))
        }


        msg = f'********** Processing {i["email"]} **********'
        print(msg)
        print(create_user(url_create_user, user_data, headers))
        send_email(url_reset_pass, i["email"])
        print('*' * len(msg))
        print('\n\n')

# curl 'https://zdravievpraci.sk/wp-login.php?action=lostpassword' --form user_login=toth.janci@gmail.com

