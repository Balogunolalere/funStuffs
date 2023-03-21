import requests
import json


def get_recommendations(prompt: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.watchthis.dev/?ref=futuretools.io',
        'content-type': 'application/json',
        'Origin': 'https://www.watchthis.dev',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    json_data = {
        'searched': prompt,
    }

    response = requests.post('https://www.watchthis.dev/api/getRecommendation', headers=headers, json=json_data)

    # Convert the plain text response to a JSON object
    response_text = response.text.strip().split("\n\n")
    response_json = [
        {"title": entry.split(": ")[0], "description": entry.split(": ")[1]}
        for entry in response_text
        if ": " in entry
    ]

    return json.dumps(response_json, indent=4)


response = get_recommendations('tv series and the characters should be vampires, it should be after 2018, it should have more than one season')

# Pretty print the JSON response
print(response)
