import os 
from processArticle import *
from makeVideos import *
from wsgiref.util import FileWrapper
from uploadToYT import *
import os
import shutil
from gtts import gTTS
import random
import settings
# from ytuploader import *
import requests, json, datetime 
from uploadfiletoytserver import *



def checktime():
    fetchdata=requests.get('http://ytserver.eu-gb.cf.appdomain.cloud/techno/nextrandom/')
    data=fetchdata.json()
    nextran= datetime.datetime.strptime(data['nextrandom'],"%Y-%m-%dT%H:%M:%SZ")
    print(nextran)
    datime=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    print(datime)
    dateee=datetime.datetime.strptime(datime,"%Y-%m-%d %H:%M:%S")

    if nextran < dateee:
       print("We will post video")
       requestVideo()
    else:
        print("We will wait for minutes since it is time error")




def requestVideo():
    try:       
        r=requests.get('http://ytserver.eu-gb.cf.appdomain.cloud/techno/gettitle/')
        print(r)

        title=(r.json()['title'])
        YTtitle=(r.json()['Ytitle'])
        content=(r.json()['content'])
        summary=(r.json()['summary'])
        if title == 0 or title is None or content is None or content == '':
            print("Content or title is either blank or incorrect")
            exit()
        

        newYTtitle = YTtitle
        p = makeVideo(newYTtitle+' hd',content)

        if p =='GTTS ERR':
            shutil.rmtree(os.path.join(settings.BASE_DIR, r"dataset"))
            return HttpResponse('GTTS ERR')

        os.chdir(os.path.join(settings.BASE_DIR,''))

        credit = '''\nWe take DMCA very seriously. All the images are from Bing Images.Since all the contents are not moderated so If anyway we hurt anyone sentiment, send us a request with valid proof.
        '''
        keywords = ','.join(str(YTtitle).split())

        print(YTtitle)

        #command = 'python ./bott/uploadToYT.py --file="'+str(p)+'" --title="'+YTtitle+'" --description="'+(summary+'\n'+credit)+'" --keywords="'+keywords+',hour news,news" --category="24" --privacyStatus="public" --noauth_local_webserver ' 
        uploadvideotoytserver(p,YTtitle)
        
        #Youtube Uploading Via Selenium
        
        # video_path = p
        
        # uploader = YouTubeUploader(video_path)#, metadata_path, thumbnail_path)
        # was_video_uploaded, video_id = uploader.upload()
        # print(was_video_uploaded)
        # print(video_id)
        #End of Youtube Uploading
        
        #os.system(command) #comment this to stop uploading to youtube
        # shutil.rmtree(os.path.join(settings.BASE_DIR, r"dataset")) # comment this to stop removing the file from system
        print('Success')


    except Exception as e:
        print('views function')
        print(e)

    

checktime()
