# How to add users to Wordpress via Python


```bash
env | grep WP
WP_API_PASS="<application-passwords>"
WP_API_USER="<username>"
WP_BASE_URL="<https://example.com>"

```

Clone code

```bash
git clone ...

# Add user details directly to add_user.py file for now

    users = [
        {"email": "xyz@gmail.com","first_name": "Johny", "last_name": "Smith"},
        {"email": "liu.xyz@gmail.com","first_name": "Joe", "last_name": "Doe"},
    ]


cd 
chmod u+x add_user.py
./add_user.py
```
