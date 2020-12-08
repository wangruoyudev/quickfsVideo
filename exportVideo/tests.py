import requests
import json


#todo 获取省内全部视频核验的客户流水号等信息

def getSerialNumList():
     questUrl = 'https://sphy.quickfs.com.cn/api/video/getSerialList'
     res = requests.get(url=questUrl)
     print(res.text)


#todo 用entityid 字段代替流水号去请求对应的视频下载列表
def getVideoList():
     questUrl = 'https://sphy.quickfs.com.cn/api/video/GetVideoList'
     data = {
          'entity': '4b34e99002484bc1b6dcc8c0388c519b'
     }
     res = requests.post(url=questUrl, data=data)
     videoData = json.loads(res.text)
     print(videoData['total'])
     downloadOneVideoList(videoData['videoList'])

# todo 用流水号去请求对应的视频下载列表
def getVideoListBySerialNum():
     questUrl = 'https://sphy.quickfs.com.cn/api/video/getVideoListBySerial'
     data = {
          'serialNum': 'ME20180420X00000000000009519708'
     }
     res = requests.post(url=questUrl, data=data)
     print(res.status_code)
     print(res.text)



#todo 下载对应的一个客户全部视频片段
def downloadOneVideoList(videoList):
     for downloadUrl in videoList:
          f = requests.get(downloadUrl)
          with open("xxxxx.mp4", "wb") as code:
               code.write(f.content)

# getSerialNumList()
# getVideoList()
getVideoListBySerialNum()

