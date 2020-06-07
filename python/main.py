import face_recognition
import re
from datetime import datetime
import json
import urllib.request


image = face_recognition.load_image_file("python/temp/test.jpg")
locations = face_recognition.face_locations(image)

if locations:
   known_imageRec = face_recognition.load_image_file("python/temp/known.jpg")
   test_imageRec = face_recognition.load_image_file("python/temp/test.jpg")

   known_encoding = face_recognition.face_encodings(known_imageRec)[0]
   test_encoding = face_recognition.face_encodings(test_imageRec)[0]

   results = face_recognition.compare_faces([known_encoding], test_encoding)

   if(results[0] == True):

      # Find all facial features in all the faces in the image
      m = re.findall(r"\d+", str(locations[0]))

      for face_landmarks in locations:
         x0 = int(m[1])
         y0 = int(m[0])
         x1 = int(m[3])
         y1 = int(m[2])
         arrList = [x0, y0, x1, y1]
         arrList = str(arrList)
      if( len(locations) == 1 ):
         print('{"faces": ' + str(len(locations)) + ', "match": true, "coordinates": ' + arrList + '}')
      else:
         print('{"faces": ' + str(len(locations)) + ', "match": true, "info": "Multiple faces found in test image."}')

   else:
      print('{"faces": ' + str(len(locations)) + ', "match": false }')
else:
   print('{"faces": 0, "matches": 0}')
exit
