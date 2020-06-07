import face_recognition
import re
from datetime import datetime
import json
import urllib.request
import sys, getopt

def main(argv):
   image1 = ''
   image2 = ''
   try:
      opts, args = getopt.getopt(argv,"hi:c:",["ifile=", "cfile"])
   except getopt.GetoptError:
      print('detect.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('detect.py -i <image> -c <compareImage>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         image1 = arg
      elif opt in ("-c", "--cfile"):
         image2 = arg
   image = face_recognition.load_image_file(image1)
   locations = face_recognition.face_locations(image)

   if locations:
      known_imageRec = face_recognition.load_image_file(image2)
      test_imageRec = face_recognition.load_image_file(image1)

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

if __name__ == "__main__":
   main(sys.argv[1:])