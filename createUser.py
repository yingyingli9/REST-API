# reference: https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/post_users

# importing the requests library
import requests
import os

# api-endpoint for List of Incidents
URL = "https://api.pagerduty.com/users"
api_key = os.environ['api_key']

headers = {
  "Content-Type": "application/json",
  "Accept": "application/vnd.pagerduty+json;version=2",
  "From": "yingyingli919@gmail.com",
  "Authorization": "Token token={}".format(api_key)
}


payload = {
  "user": {
    "type": "user",
    "name": "Andy",
    "email": "andy_example@gmail.com",
    "time_zone": "America/Lima",
    "color": "green",
    "role": "admin",
    "job_title": "CTO",
    "description": "example"
  }
}


# post request
r = requests.post(url=URL, headers=headers, json=payload)

print(r.json())
