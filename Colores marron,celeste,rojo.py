import cv2
import numpy as np

img = cv2.imread("pelota.jpg")
img2 = cv2.imread("peluche.jpg")
img3 = cv2.imread("plato.jpg")

hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv2=cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
hsv3=cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

rojo_bajo = np.array([0,100,20])
rojo_alto = np.array([179,255,255])

marron_bajo = np.array([0,20,5])
marron_alto = np.array([71,209,127])

celeste_bajo = np.array([46,14,41])
celeste_alto = np.array([241,209,237])
  
mask = cv2.inRange(hsv,rojo_bajo,rojo_alto)
mask2 = cv2.inRange(hsv2,marron_bajo,marron_alto)
mask3 = cv2.inRange(hsv3,celeste_bajo,celeste_alto)

cv2.imshow('Foto/Original/1',img)
cv2.imshow('Rojo extraido.',mask)

cv2.imshow('Foto/Original/2',img2)
cv2.imshow('Marron extraido.',mask2)

cv2.imshow('Foto/Original/3',img3)
cv2.imshow('Celeste extraido.',mask3)

print("oprime cualquier tecla para cerrar las ventanas")
cv2.waitKey(0)
cv2.destroyAllWindows()

