# reference: https://v2.developer.pagerduty.com/v2/page/api-reference#!/Incidents/get_incidents

# importing the requests library
import requests
import os

# api-endpoint for List of Incidents
URL = "https://api.pagerduty.com/incidents"
api_key = os.environ['api_key']

# set up header
headers = {
  "Accept": "application/vnd.pagerduty+json;version=2",
  "Authorization": "Token token={}".format(api_key)
}
 
# defining a params dict for the parameters to be sent to the API
# statuses, incident_key, service_ids, team_ids, user_ids
PARAMS = {}
 
# sending get request and saving the response as response object
# get request
r = requests.get(url = URL, headers = headers, params = PARAMS)
 
# extracting data in json format
data = r.json()

print data