import cv2
import time
import numpy as np
from keras.models import load_model
from twilio.rest import Client

import pygame, sys
from pygame import mixer
pygame.init()
pygame.mixer.init()
sound = mixer.Sound('alarm.wav')

model = load_model('100-0.3327.model')
face_clsfr=cv2.CascadeClassifier('../data/haarcascade_frontalface_default.xml')

#source=cv2.VideoCapture(0)
source=cv2.VideoCapture('test_mask_raw.mp4')

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 20, (320,240))

labels_dict={1:'with_mask', 0:'without_mask'}
color_dict={1:(0,255,0), 0:(0,0,255)}

account_sid = "ACxxxxxxxxxXxxxx"
auth_token  = "93xxxxxxxxxxx"

myTwilioNumber = "+1xxxxxxxx"
destCellPhone  = "+82010xxxxxxxx"

while(True):

    ret,img=source.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_clsfr.detectMultiScale(gray,1.3, 5)  

    for x,y,w,h in faces:
    
        face_img=gray[y:y+w,x:x+w]
        resized=cv2.resize(face_img,(100,100))
        normalized=resized/255.0
        reshaped=np.reshape(normalized,(1,100,100,1))
        result=model.predict(reshaped)

        label=np.argmax(result,axis=1)[0]
      
        cv2.rectangle(img,(x,y),(x+w,y+h),color_dict[label],2)
        cv2.rectangle(img,(x,y-30),(x+w,y),color_dict[label],-1)
        
        if(labels_dict[label] == 'with_mask'):
            print("No Beep")
        else:
            sound.play()
            print("Beep")

            client = Client(account_sid, auth_token)
            client.messages.create(body = 'Test MSG: No Mask', 
                                   from_ = myTwilioNumber, 
                                   to = destCellPhone)
            time.sleep(2)
           
        cv2.putText(
          img, "{}: {:.2f}%".format(labels_dict[label], np.max(result) * 100),
          (x, y-10),
          cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
        
        
    cv2.imshow('Mask Detector LIVE',img)
    out.write(img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

source.release()
out.release()
cv2.destroyAllWindows()

writeVideo()