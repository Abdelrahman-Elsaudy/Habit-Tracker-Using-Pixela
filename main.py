import requests
import datetime as dt


# ----------------------------------- SIGNING UP ----------------------------------- #


user_endpoint = "https://pixe.la/v1/users"

USER_NAME = "abdelrahman-elsaudy"
with open("api.txt") as file:
    TOKEN = file.read()


user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

user_post = requests.post(url=user_endpoint, json=user_params)


# ----------------------------------- CREATING GRAPH ----------------------------------- #


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


# ----------------------------------- POSTING AN INPUT ----------------------------------- #


posting_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = dt.datetime.today()
today_date = today.date()
formatted_date = today_date.strftime("%Y%m%d")

posting_params = {
    "date": "20240305",
    "quantity": input("How many hours did you code today?")
}

posting_pixel = requests.post(url=posting_endpoint, json=posting_params, headers=header)


# ----------------------------------- EDITING AN INPUT ----------------------------------- #


editing_endpoint = f"{posting_endpoint}/20240129"

editing_params = {
    "quantity": "2"
}

editing_put = requests.put(url=editing_endpoint, json=editing_params, headers=header)


# ----------------------------------- DELETING AN INPUT ----------------------------------- #


# deleting_endpoint = editing_endpoint if I wanted to delete the last one I edited.

deleting = requests.delete(url=editing_endpoint, headers=header)
