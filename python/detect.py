import face_recognition
import re
from datetime import datetime
import json
import urllib.request
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print('detect.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('detect.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         image = face_recognition.load_image_file(arg)
         locations = face_recognition.face_locations(image)
         if locations:
            print('{"faces": ' + str(len(locations)) + '}')
         else:
            print('{"faces": 0}')

if __name__ == "__main__":
   main(sys.argv[1:])
