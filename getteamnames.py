import requests, json
url = requests.get("http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1")
text = url.text
i = 0
print(type(text))
data = json.loads(text)['dates'][0]['games']
teamName = json.loads(text)['dates'][0]['games'][5]['teams']['home']['team']['name']
##score = json.loads(text)['dates'][0]['games'][5]['teams']['home']['score']
x = range(len(data))
print(x)
print(teamName)
for v in x:
    i += 1
    teamName = json.loads(text)['dates'][0]['games'][v]['teams']['home']['team']['name']
    print(teamName)
