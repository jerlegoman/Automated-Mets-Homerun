import requests, json
import time
url = requests.get("http://mars.cs.qc.cuny.edu/~haje4621/json/games.json")
text = url.text
score = 0
newScore = 0
i = 0
print(type(text))
data = json.loads(text)['dates'][0]['games']
##teamName = json.loads(text)['dates'][0]['games'][5]['teams']['home']['team']['name']
##score = json.loads(text)['dates'][0]['games'][5]['teams']['home']['score']
x = range(len(data))
print(x)
##print(teamName)
for v in x:
    i += 1
    teamNameH = json.loads(text)['dates'][0]['games'][v]['teams']['home']['team']['name']
    teamNameA = json.loads(text)['dates'][0]['games'][v]['teams']['away']['team']['name']
    print(teamNameH)
    print(teamNameA)
    while json.loads(text)['dates'][0]['games'][v]['status']['statusCode'] == 'L':
        if teamNameH == "Houston Astros" and json.loads(text)['dates'][0]['games'][v]['status']['statusCode'] == 'L':
            newScore = json.loads(text)['dates'][0]['games'][v]['teams']['home']['score']
        if teamNameA == "Houston Astros" and json.loads(text)['dates'][0]['games'][v]['status']['statusCode'] == 'L':
            newScore = json.loads(text)['dates'][0]['games'][v]['teams']['away']['score']
            print("found")
            print(newScore)
        if score < newScore:
            score = newScore
            print("Homerun!")
        print(newScore)
        time.sleep(4)
        url = requests.get("http://mars.cs.qc.cuny.edu/~haje4621/json/games.json")
        text = url.text




