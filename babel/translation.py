import requests


def from_google(text, source, target):
    qs = {
        'key': '',
        'source': source,
        'target': target,
        'format': 'text',
        'q': text,
    }
    api_url = 'https://translation.googleapis.com/language/translate/v2'

    response = requests.post(api_url, params=qs)

    data = response.json()
    if response.ok:
        return data['data']['translations'][0]['translatedText']
    else:
        print("Error")
        print(data)
