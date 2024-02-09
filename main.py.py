import requests
import datetime as dt

user_endpoint = "https://pixe.la/v1/users"

USER_NAME = "abdelrahman-elsaudy"
TOKEN = "hfe3432jk"

user_params ={
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

user_post = requests.post(url=user_endpoint,json=user_params)

#-------------------------------------------------------------------------------

graph_endpoint = f"{user_endpoint}/{USER_NAME}/graphs"
GRAPH_ID = "codegraph"

graph_params = {
    "id": GRAPH_ID,
    "name": "coding_tracker",
    "unit": "hr",
    "type": "float",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": TOKEN
}

graph_post = requests.post(url=graph_endpoint, json=graph_params, headers=header)

#-------------------------------------------------------------------------------

posting_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = dt.datetime.today()
today_date = today.date()
formatted_date = today_date.strftime("%Y%m%d")

posting_params = {
    "date": formatted_date,
    "quantity": input("How many hours did you code today?")
}

posting_post = requests.post(url=posting_endpoint, json=posting_params, headers=header)

#-------------------------------------------------------------------------------
#
# editing_endpoint = f"{posting_endpoint}/{formatted_date}"
#
# editing_params = {
#     "quantity": "2"
# }
#
# editing_put = requests.put(url=editing_endpoint, json=editing_params, headers=header)
#
# #-------------------------------------------------------------------------------
#
# # deleting_endpoint = editing_endpoint if I wanted to delete the last one I edited
#
# deleting = requests.delete(url=editing_endpoint, headers=header)
#
