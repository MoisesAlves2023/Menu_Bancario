import cv2 as cv
from time import sleep

video = cv.VideoCapture("video.mp4")

contador = 0
detec = []
linhax = 700
#start_frame_number = 1

def pegar_centro(x,y,w,h):
    centrox = int((x+x+w)/2)
    centroy = int((y+y+h)/2)
    centroponto = (centrox, centroy)
    cv.circle(frame, centroponto, 1, (0, 0, 255), 5)
    return centrox

def pegar_centro1(x,y,w,h):
    centrox1 = int((x-l+x+w)/2)
    centroy1 = int((y+y+h)/2)
    centroponto1 = (centrox1, centroy1)
    cv.circle(frame, centroponto1, 1, (0,0,255), 5)
    return centrox1

def pegar_centro2(x,y,w,h):
    centrox2 = int((x+l+x+w) / 2)
    centroy2 = int((y+y+h) / 2)
    centroponto2 = (centrox2, centroy2)
    cv.circle(frame, centroponto2, 1, (0, 0, 255), 5)
    return centrox2

def info(detec):
    global contador
    for (centrox) in detec:
        if 709 > centrox > 696:
            contador += 1
            #video.set(cv.CAP_PROP_POS_FRAMES, start_frame_number)
            detec.clear()
            cv.line(frame, (700, 350), (700, 600), (255, 255, 255), 3)
            print("Pacotes detectados até o momento: " + str(contador))

while True:
    ret, frame = video.read()
    corte = frame[359:648, 587:1100]
    cinza = cv.cvtColor(corte, cv.COLOR_BGR2GRAY)
    retvalue,th = cv.threshold(cinza,140,255,cv.THRESH_BINARY)
    cv.line(frame, (700, 350), (700, 600), (0, 255, 0), 3)
    contorno,hierarchy = cv.findContours(th,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for cnt in contorno:
        area = cv.contourArea(cnt)
        if 10000 > area > 5000:
            (x, y, w, h) = cv.boundingRect(cnt)
            x = 587 + x
            y = 359 + y
            cv.rectangle(frame, (x, y),(x+w, y+h), (0, 0, 255), 3)
            centro = pegar_centro(x,y,w,h)
            cv.putText(frame, str(area), (x, y), 1, 1, (0, 255, 0))
            detec.append(centro)
            
            if(centro) not in detec:
                detec.append(centro)

            info(detec)
            
        if area > 10000:
            (x,y,w,h) = cv.boundingRect(cnt)
            l = int(w/2)
            x = 587 + x
            y = 359 + y
            ret1 = cv.rectangle(frame,(x, y), (x+l, y+l), (0, 0, 255), 3)
            centro1 = pegar_centro1(x,y,w,h)
            ret2 = cv.rectangle(frame, (x+l, y), (x+l+l, y+h), (255, 0, 0), 3)
            centro2 = pegar_centro2(x,y,w,h)

    cv.putText(frame, str(contador), (450, 70), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv.imshow("video", frame)
    cv.imshow("corte", corte)
    cv.imshow("th",th)

    cv.waitKey(20)
