import json
import pandas as pd

list_type = ["thời sự", "giải trí", "xã hội", "giáo dục", "đời sống"]

with open("./dataset/news_dataset.json", "r", encoding="utf8") as f:
    data = json.load(f)

list_content = []
list_source = []
list_title = []
list_topic = []

# #Check type of news
# dict_news_type = {}
# for news in tqdm.tqdm(data):
#     type_news = news["topic"].lower()
#     if type_news in list_type:
#         if type_news not in dict_news_type.keys():
#             dict_news_type[type_news] = 0
#         else:
#             dict_news_type[type_news] += 1
#
# dict_news_type = dict(sorted(dict_news_type.items(), key=lambda item: item[1]))
# print(dict_news_type)

total_character = 0

dict_count_topic = {}
for news in data:
    content = news["content"]
    topic = news["topic"].title()
    source = news["source"]
    title = news["title"]

    if topic.lower() in list_type:
        if 250 < len(content) < 400 and "http" not in content and sum(map(str.isalpha, content)) > len(content)*0.72 and title:
            if topic not in dict_count_topic.keys():
                dict_count_topic[topic] = 1
            else:
                dict_count_topic[topic] += 1

            if dict_count_topic[topic] <= 25:
                list_content.append(content)
                list_source.append(source)
                list_title.append(title)
                list_topic.append(topic)

                text = title + ". " + content
                text = " ".join(text.split())
                total_character += len(text)

# Save
df = pd.DataFrame(
    {'topic': list_topic,
     'title': list_title,
     'content': list_content,
     'source': list_source,
    })

df.to_csv('./dataset/news_dataset.csv', index=False)

print(len(list_content))
print(dict_count_topic)
print(total_character)