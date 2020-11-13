import cv2
import numpy as np

img = cv2.imread('bola de colores.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

rojo_bajos = np.array([0,100,20])
rojo_altos = np.array([10,255,255])
rojo_bajos1 = np.array([171,100,20])
rojo_altos1 = np.array([183,255,255])

lila_bajos = np.array([130,100,20])
lila_altos = np.array([165,255,255])

azul_bajos = np.array([100,100,20])
azul_altos = np.array([122,255,255])

verde_bajos = np.array([37,100,20])
verde_altos = np.array([70,255,255])

amarillo_bajos = np.array([24,98,20])
amarillo_altos = np.array([32,255,255])

mask_rojo = cv2.inRange(hsv, rojo_bajos, rojo_altos)
mask_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
mask_lila = cv2.inRange(hsv, lila_bajos, lila_altos)
mask_azul = cv2.inRange(hsv, azul_bajos, azul_altos)
mask_verde = cv2.inRange(hsv, verde_bajos, verde_altos)
mask_amarillo = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)

mask_union = cv2.bitwise_or(mask_rojo, mask_rojo1)
mask_union1 = cv2.bitwise_or(mask_union,mask_lila)
mask_union2 = cv2.bitwise_or(mask_union1, mask_azul)
mask_union3 = cv2.bitwise_or(mask_union2, mask_verde)
mask_union4 = cv2.bitwise_or(mask_union3, mask_amarillo)

cv2.imshow('Original', img)
cv2.imshow('Rojo+Lila+Azul+Verde+Amarillo', mask_union4)
print('Pulsa para cerrar')
cv2.waitKey(0)
cv2.destroyAllWindows()
