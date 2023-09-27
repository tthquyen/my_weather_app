# TODO Mentors: Explain HTTP codes & statuses

"""
Reads:
    What are the HTTP codes? https://http.dev/status
"""

import requests

url = f'http://www.google.com'

response = requests.get(url)

# TODO TechWomen Exercise 1: Get a HTTP response of 200 code from the request and print the output
print(response)

# TODO TechWomen Exercise 2: Get a HTTP response of 404 code from the request and print the output

url = f'http://www.google.com/mycoolwebsite'

response = requests.get(url)
print(response)

# TODO TechWomen Exercise 3: Add a condition that checks whether the HTTP status code is 200 and print the output

url = f'http://www.google.com'

response = requests.get(url)

if response.status_code == 200:
    print("All good in the hood!")