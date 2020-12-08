from django.views.generic import View
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class GetSerialList(View):
    def get(self, request):

        json_data = {'seialNum': '11111111'}
        cursor = connection.cursor()
        cursor.execute("select * from index_video as video where video.city = '郑州市' and (video.done is null or video.done = 0)")
        rows = cursor.fetchall()
        alldata = []
        for item in rows:
            print(item)
            alldata.append({'serialNum': item[4], 'name': item[5], 'phone': item[6], 'entityid': item[1]})
        print('rows', len(rows))
        return JsonResponse({'total': len(rows), 'allData': alldata})

class GetVideoList(View):
    def get(self, request):
        entity = request.GET.get('entity')
        print('========>entity:', entity)
        cursor = connection.cursor()
        sql = 'select * from entities as en where en.id = %s%s%s ' % ('"', entity, '"')
        print('======>sql:', sql)
        cursor.execute(sql)
        rows = cursor.fetchall()
        alldata = []
        for item in rows:

            strbody = item[2].decode('utf-8')
            dictBody = json.loads(strbody)
            videoList = dictBody['qfs_videos']
            print(len(videoList))
            for oneVideo in videoList:
                print(oneVideo['data'][1])
                alldata.append(oneVideo['data'][1])
        print('rows', len(rows))
        return JsonResponse({'total': len(alldata), 'videoList': alldata})

    @csrf_exempt
    def post(self, request):
        serialNum = request.POST.get('serialNum')
        print('========>serialNum:', serialNum)
        return JsonResponse({'total': '22223'})