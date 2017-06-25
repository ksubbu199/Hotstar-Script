import os
import json
import requests

hotStarUrl = raw_input('Video url:')
tempList = hotStarUrl.split('/')
videoId = tempList[len(tempList)-1]
if videoId == "watch":
    videoId = tempList[len(tempList)-2]
print videoId
getSrc = "http://getcdn.hotstar.com/AVS/besc?action=GetCDN&asJson=Y&channel=TABLET&id="+videoId+"&type=VOD"
resp = requests.get(getSrc)
jsonData = json.loads(resp.text)
videoUrl = jsonData['resultObj']['src']
print "Paste URL and click play"
print videoUrl
os.system('firefox https://www.hlsplayer.net/')
