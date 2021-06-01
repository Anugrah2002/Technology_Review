# from django.http import HttpResponse, JsonResponse
import requests
import cloudinary
import cloudinary.uploader


cloudinary.config(
  cloud_name = 'drpb4oxcc',
  api_key = '354327896332831',
  api_secret = 'CvetvSAc2xW33TRe_CaitVsi9S8'
)



def uploadvideotoytserver(filepath,YTtitle):
    try:
        print(filepath)
        filepath = str(filepath)
        # filepath = filepath.replace(' ','\ ')
        filepath="final.mp4"
        print(filepath)
        myurl = 'http://ytserver.eu-gb.cf.appdomain.cloud/techno/savevideo/'
        upload_data = cloudinary.uploader.upload_large(filepath)
        videoPublicId=str(upload_data['public_id'])
        videoUrl=str(upload_data['secure_url'])
        print(videoPublicId)
        print(videoUrl)
        title=YTtitle 
        getdata = requests.post(myurl,data={'title':title,'videoPublicId':videoPublicId,'videoUrl':videoUrl})
        print(getdata.text)  
    except Exception as e:
        print(e)