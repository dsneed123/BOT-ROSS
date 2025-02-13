import requests

def get_random_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    
    if response.status_code == 200:
        meme = response.json()
        return meme["url"]
    else:
        return "Failed to fetch meme."


