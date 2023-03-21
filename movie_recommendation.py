import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.watchthis.dev/?ref=futuretools.io',
    'content-type': 'application/json',
    'Origin': 'https://www.watchthis.dev',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

json_data = {
    'searched': "Give me a list of 10 tv show recommendations that fit all of the following categories: . Make sure it fits the following description as well: it should have more than one season, it should be after 2018, the characters should have powers or have superheros. If you do not have 5 recommendations that fit these criteria perfectly, do your best to suggest other tv show's that I might like. Please return this response as a numbered list with the tv show's title, followed by a colon, and then a brief description of the tv show. There should be a line of whitespace between each item in the list.",
}

response = requests.post('https://www.watchthis.dev/api/getRecommendation', headers=headers, json=json_data)

# Convert the plain text response to a JSON object
response_text = response.text.split("\n\n")
response_json = [{"title": entry.split(": ")[0], "description": entry.split(": ")[1]} for entry in response_text]

# Pretty print the JSON response
print(json.dumps(response_json, indent=4))