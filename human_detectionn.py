from itertools import count
from re import A
from turtle import pd
import cv2
from cv2 import rectangle
import numpy as np
from matplotlib import pyplot as plt
import time

import firebase_admin


cred_obj = firebase_admin.credentials.Certificate("countingpeople-f2000-firebase-adminsdk-qizfa-44872a8ce6.json")
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': "https://countingpeople-f2000-default-rtdb.europe-west1.firebasedatabase.app"
	})
from firebase_admin import db
ref=db.reference("/")

 
 

         


def motionDetection():
    
    cap = cv2.VideoCapture('https://manifest.googlevideo.com/api/manifest/hls_variant/expire/1652972169/ei/KAaGYqvdPIzW1wL_u5ngAQ/ip/88.242.129.161/id/AdUw5RdyZxI.2/source/yt_live_broadcast/requiressl/yes/tx/24197277/txs/24197275%2C24197276%2C24197277/hfr/1/playlist_duration/30/manifest_duration/30/maxh/2160/maudio/1/spc/4ocVC078gtTxZ7jmT4EMA5C8VKyS-yc62mKkSqnB-A/vprv/1/go/1/pacing/0/nvgoi/1/keepalive/yes/fexp/24001373%2C24007246/dover/11/itag/0/playlist_type/DVR/sparams/expire%2Cei%2Cip%2Cid%2Csource%2Crequiressl%2Ctx%2Ctxs%2Chfr%2Cplaylist_duration%2Cmanifest_duration%2Cmaxh%2Cmaudio%2Cspc%2Cvprv%2Cgo%2Citag%2Cplaylist_type/sig/AOq0QJ8wRAIgbrDHvzVpUbBO1BtzgQXjFEB2ILiC7KMOVfBmV1YxU6YCIAFWFuNMCHQXc1CmvdDiIBz1cNj18tsCi2Xjm-UVfIhD/file/ind')

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    
   


    while cap.isOpened():
     diff = cv2.absdiff(frame1, frame2)
     gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
     blur = cv2.GaussianBlur(gray, (5,5), 0)
     _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
     dilated = cv2.dilate(thresh, None, iterations=3)
     contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     
    
     myList=[]
     sayac=0

     for contour in contours:
         (x,y,w,h)=cv2.boundingRect(contour)
         if cv2.contourArea(contour) <0.001:
         
             continue
         
         cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),1)
         cv2.putText(frame1,'                         '.format('                    '),(10,50), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,1),1)
       
         #cv2.putText(frame1,"insan sayisi "+str(sayac), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)
         
 
         sayac+=1
         
     myList.append(sayac)
     ref.set({
 "Square":
 {
     "count people":myList}
})
 
         
       
     cv2.putText(frame1,"insan sayisi "+str(sayac), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)
     cv2.putText(frame1,'time square{}'.format(''),(10,20), cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,0,0),1)
     cv2.imshow('Times square garden stream',frame1)
     print(myList)
     frame1=frame2
     ret,frame2=cap.read()
     
     
     if cv2.waitKey(30) & 0xff == ord("q"):
    

      break
    

    
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    
    motionDetection()
   
    
    

