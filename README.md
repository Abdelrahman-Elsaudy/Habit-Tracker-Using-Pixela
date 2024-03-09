# Habit Tracker Using Pixela

---

- This tool allows you to log your daily practice of a certain habit to be able to track it, visualize it and improve it.
- It's an application of API `post`, `put` and `delete` requests in addition to `datetime` module and `strftime()` method.


---
## How it works:

---

You can visit [Pixela](https://pixe.la/) and scroll down to _How Do I User Pixela?_ for a step-by-step guide on how to create a graph that tracks a habit 
you are interested in.

---

**1. Signing Up**

- This one requires only an endpoint and parameters, and we are given their criteria [here](https://docs.pixe.la/entry/post-user).

```
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
```

- This is a `post` request:
```
user_post = requests.post(url=user_endpoint, json=user_params)
```
---

**2. Creating The Graph**

- Also a `post` request its criteria [here](https://docs.pixe.la/entry/post-graph).
- The extra prerequisite here is an authentication header.
```
header = {
    "X-USER-TOKEN": TOKEN
}
```

```
graph_post = requests.post(url=graph_endpoint, json=graph_params, headers=header)
```
---

**3. Posting a Pixel**

- This is also a `post ` request to post a pixel on the graph, its criteria is [here](https://docs.pixe.la/entry/post-pixel).
- Here we use the `datetime` module and `strftime` method to get today as yyyMMdd as required, we can do this with [datetime](https://www.w3schools.com/python/python_datetime.asp) documentation.
```
today = dt.datetime.today()
today_date = today.date()
formatted_date = today_date.strftime("%Y%m%d")
```

```
posting_pixel = requests.post(url=posting_endpoint, json=posting_params, headers=header)
```
---

**4. Viewing The Graph**

- To be able to view the graph, we visit a web page that is written like this:
> https://pixe.la/v1/users/{user_name}/graphs/{graph_name}.html


---

**5. Editing a Pixel**

- To be able to edit a log, this is a `put` request, its criteria is [here](https://docs.pixe.la/entry/put-graph).
```
editing_put = requests.put(url=editing_endpoint, json=editing_params, headers=header)
```

---

**6. Deleting a Pixel**

- To be able to delete a log, this is a `delete` request, its criteria is [here](https://docs.pixe.la/entry/delete-graph).
```
deleting = requests.delete(url=editing_endpoint, headers=header)
```

---
_Credits to: 100-Days of Code Course on Udemy._