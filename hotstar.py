import os
import json
import requests
import urllib

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

#videofile=urllib.urlretrieve(videoUrl)
videofile = urllib.URLopener()
videofile.retrieve(videoUrl,videoId+".m3u8")
os.system("ffplay -protocol_whitelist 'file,http,https,tcp,tls' -i "+videoId+".m3u8")
