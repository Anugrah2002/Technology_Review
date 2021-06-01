from  ytuploader import *

video_path = './song/qqq.mp3'
metadata_path = './metadata.json'
uploader = YouTubeUploader(video_path, metadata_path)
was_video_uploaded, video_id = uploader.upload()
assert was_video_uploaded