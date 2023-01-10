import cv2
import numpy as np
video = cv2.VideoCapture('video.mp4')
pacotes = 0
liberado = False
#sub = cv2.createBackgroundSubtractorMOG2()
inicio = (700,450)
final = (520,550)
while True:
    ret,img = video.read()
    img = cv2.resize(img,(1100,720),)
    imgcinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    #imgsub= sub.apply(imgcinza)
    x,y,w,h = 490, 400, 30, 150
    retval,imgth = cv2.threshold(imgcinza, 140, 255, cv2.THRESH_BINARY)
    recorte = imgth[y:y+h,x:x+w]
    brancos = cv2.countNonZero(recorte)
    cv2.rectangle(imgth, inicio, final, (0, 0, 255), 50)

    if brancos > 2000 and liberado == True:
        pacotes += 1

    if brancos < 2000:
        liberado = True
    else:
        liberado = False

    if liberado == False:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    else:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0, 255),4)

    cv2.rectangle(imgth, (x, y), (x + w, y + h), (255, 255, 255), 6)

    text = f'pacotes: {pacotes}'
    print(brancos)
    cv2.putText(img, text, (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.imshow("Video Original", img)
    cv2.imshow("Detectar", recorte)

    print(liberado)
    #cv2.imshow('video original',img)
    #cv2.imshow('video', cv2.resize(imgth,(600,500)))
    cv2.waitKey(20)