import json, re

with open('bhs_photos.json') as json_data:
    d = json.load(json_data)


for a_item in d:

    matches = re.findall('#[0-9]{1,}\s[A-z]{3,}\s[A-z]{3,}', a_item['title'])


    if len(matches) > 0:
        print(matches)
