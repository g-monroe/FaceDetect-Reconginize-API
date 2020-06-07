from PIL import Image, ImageDraw, ImageFont
import face_recognition
import re
import glob
import os
from datetime import datetime
import json
from pprint import pprint
import urllib.request


print(str(datetime.now()))

with open('/macgyver/temp/data.json') as f:
    data = json.load(f)


known_image = data["known_image"][0]
test_image = data["test_image"][0]

urllib.request.urlretrieve(test_image, "/python/temp/test.jpg")
urllib.request.urlretrieve(known_image, "/python/temp/known.jpg")

known_image = "/python/temp/known.jpg"
test_image = "/python/temp/test.jpg"


image = face_recognition.load_image_file(test_image)
locations = face_recognition.face_locations(image)

if locations:
   print("Faces Found")
   known_image = face_recognition.load_image_file("/python/obama.jpg")
   unknown_image = face_recognition.load_image_file("/python/obama_letterman.jpg")

   biden_encoding = face_recognition.face_encodings(known_image)[0]
   unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

   results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

   if(results[0] == True):
      print("Match Found")
