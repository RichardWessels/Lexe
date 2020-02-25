import requests

def extra_word_data(word, API_KEY):
    response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={API_KEY}")
    response = response.json()

    syllables = response[0]["hwi"]["hw"]
    part_of_speech = response[0]["fl"]

    return syllables, part_of_speech