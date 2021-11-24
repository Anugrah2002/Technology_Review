# from django.http import HttpResponse, JsonResponse
import requests
import cloudinary
import cloudinary.uploader


cloudinary.config(
  cloud_name = 'detxlswii',
  api_key = '474368939111198',
  api_secret = 'gAmfegRLeJKZC66RWtNlW0Pp6tM'
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
