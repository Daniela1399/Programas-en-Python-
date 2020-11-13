# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 00:04:46 2020

@author: Daniela G. Osuna
"""

import cv2
import numpy as np

captura = cv2.VideoCapture(0)

while(1):
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    
    rojo_bajos = np.array([0,100,20], dtype=np.uint8)
    rojo_altos = np.array([10,255,255], dtype=np.uint8)
    
    rojo_bajos1 = np.array([175,100,20], dtype=np.uint8)
    rojo_altos1 = np.array([179,255,255], dtype=np.uint8)
    
    amarillo_bajos = np.array([0,100,70], dtype=np.uint8)
    amarillo_altos = np.array([40,255,255], dtype=np.uint8)
    
    azul_bajos = np.array([100,100,20], dtype=np.uint8)
    azul_altos = np.array([122,255,255], dtype=np.uint8)
    
    mask_rojo = cv2.inRange(hsv, rojo_bajos, rojo_altos)
    mask_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
    mask_amarillo = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
    mask_azul = cv2.inRange(hsv, azul_bajos, azul_altos)
    
    mask = cv2.bitwise_or(mask_rojo, mask_rojo1)
    mask1 = cv2.bitwise_or(mask, mask_amarillo)
    mask2 = cv2.bitwise_or(mask1, mask_azul)
    
    
    moments = cv2.moments(mask2)
    area = moments['m00']
    
    if(area > 2000000):
        
        x=int(moments['m10']/moments['m00'])
        y=int(moments['m01']/moments['m00'])
        
        print("x = ", x)
        print("y = ", y)
        
        cv2.rectangle(imagen, (x, y), (x+2, y+2), (0,0,255), 2)
        
    cv2.imshow('mask', mask2)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
    
cv2.destroyAllWindows()