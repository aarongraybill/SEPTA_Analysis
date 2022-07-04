import json, urllib.request



url = urllib.request.urlopen("http://www3.septa.org/hackathon/Arrivals/90005")
text = json.loads(url.read())


with urllib.request.urlopen("http://www3.septa.org/hackathon/Arrivals/90005") as url:
    data = json.loads(url.read().decode())
    print(data)

for key in data.keys():
    pandas.Series(data[key][1]['Southbound'][3],index=data[key][1]['Southbound'][3].keys())

