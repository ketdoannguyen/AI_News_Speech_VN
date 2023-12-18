import time

import pandas as pd
import requests
import tqdm

number = 1

def get_api(text, person):
    global number
    if number == 1:
        api_key = 'pfZsKNQYvj1CZwnRyOdASha4Pl1qJNTl'  # 1
    elif number == 2:
        api_key = 'c3r38KxajnMjtZ4V95ggxa3WVcyQTsBb'  # 2
    elif number == 3:
        api_key = 'eMQy9VMPNDMa4LnM828W5ctvjOuTKRek'  # 3
    elif number == 4:
        api_key = 'gm936wFJcmGN8WGPShF6G1S67HFV9iXh'  # 4
    elif number == 5:
        api_key = '0WQWEsA7rGhih6preBAqft56Hy66Hsxb'  # 5
    elif number == 6:
        api_key = 'CR6X2VLjiP0PUEGeN0Hwqyo6Lvjn3Fty'  # 6
    elif number == 7:
        api_key = 'xR0kWklCVUdWCiUPHjCWSuakJpHAhX1v'  # 7
    elif number == 8:
        api_key = 'eJPoGo4SbItvitkAxJYmxjivwgmrXto3'  # 8
    elif number == 9:
        api_key = 'ZfmREGOOvxJd5HyL0FPuHbFhYPPyeTbn'  # 9
    elif number == 10:
        api_key = 'JBE715oQE3Varh0hmNRtWrY4LZbzUOnM'  # 10
    elif number == 11:
        api_key = 'gWxgcKjlDQENcseGO8K4wQmpT2PZ219E'  # 11
    elif number == 12:
        api_key = 'r1RisDUsxbecTubSfOteZ5WCqgji9Twp'  # 12

    headers = {
        'api-key': api_key,
        'speed': '-0.5',
        'voice': person
    }
    response = requests.request('POST', url_api, data=text.encode('utf-8'), headers=headers)
    return response.text.split("\"")[3]

df = pd.read_csv("./dataset/news_dataset.csv")
list_topic = df["topic"]
list_content = df["content"]
list_title = df["title"]
list_source = df["source"]


url_api = 'https://api.fpt.ai/hmi/tts/v5'

list_person = {"banmai": "Ban Mai: Nữ miền Bắc",
               "linhsan": "Linh San: Nữ miền Nam",
               "minhquang": "Minh Quang: Nam miền Nam"}

dict_url = {}
for i, person in tqdm.tqdm(enumerate(list_person.keys())):
    list_url_each_person = []
    for topic, title, content in zip(list_topic, list_title, list_content):
        text = title + ". " + content
        text = " ".join(text.split())
        while True:
            url_audio = get_api(text, person)
            time.sleep(1)
            if url_audio != "API rate limit exceeded":
                list_url_each_person.append(url_audio)
                break
            else:
                print("Time deadline")
                time.sleep(5)

    dict_url[person] = list_url_each_person


df = pd.DataFrame(dict_url)

df.to_csv('./dataset/URL_audio_from_api.csv', index=False)
