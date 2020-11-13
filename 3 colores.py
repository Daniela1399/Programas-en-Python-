import cv2
import numpy as np

img = cv2.imread('bola de colores.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lila_bajos = np.array([130,100,20])
lila_altos = np.array([165,255,255])

verde_bajos = np.array([36,100,20])
verde_altos = np.array([70,255,255])

naranja_bajos = np.array([11,100,20])
naranja_altos = np.array([23,255,255])

mask_lila = cv2.inRange(hsv, lila_bajos, lila_altos)
mask_verde = cv2.inRange(hsv, verde_bajos, verde_altos)
mask_naranja = cv2.inRange(hsv, naranja_bajos, naranja_altos)

mask_union = cv2.bitwise_or(mask_lila, mask_verde)
mask_union = cv2.bitwise_or(mask_union, mask_naranja)


cv2.imshow('Original', img)
cv2.imshow('Verde+Lila+Naranja', mask_union)
print('Pulsa para cerrar')
cv2.waitKey(0)
cv2.destroyAllWindows()
