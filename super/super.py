# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:21:25 2017

@author: Leo

install opencv
https://programarfacil.com/blog/vision-artificial/instalar-opencv-python-anaconda/

"""

#import matplotlib.image as im
#import numpy as np
#import matplotlib.pylab as plt
import cv2 

def test_1():
    '''
    Prueba de la libreria opencv
    '''
    img = cv2.imread('im1.bmp')
    cv2.imshow('prueba',img)
    cv2.waitKey(0)
    pass

def test_2():
    '''
    Convertir imagen a escala de grises
    '''
    img = cv2.imread('im1.bmp')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print ("El valor del piexel (150,150) = ",gray[150][150])
    cv2.imshow('prueba gris',gray)
    cv2.waitKey(0)

def test_3():
    '''
    obtener centroide de una matriz 3x3
    '''
    l = [[0,1,0],[1,1,1],[0,1,0]]
    
    # obtener area, sumX y sumY
    area = 0
    sum_x = 0
    sum_y = 0
    for i,fila in enumerate(l):
        for j,pixel in enumerate(fila):
            if pixel >= 1:
                area +=1
                sum_x += j+1
                sum_y += i+1
    
    print ('sum_x:',sum_x,'\nsum_y:',sum_y)
    print ("El Centroide es Xg,Yg: (",sum_x/area,',',sum_y/area,')')
    pass


def test_4():
    '''
    Obtener el centroide de una imagen 
    '''
    nombre = 'hex.jpg'
    img = cv2.imread(nombre)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    area = 0
    sum_x = 0
    sum_y = 0
    for i,fila in enumerate(gray):
        for j,pixel in enumerate(fila):
            if pixel >= 1:
                area +=1
                sum_x += j+1
                sum_y += i+1
    
    print ('sum_x:',sum_x,'\nsum_y:',sum_y)
    print ("El Centroide es Xg,Yg: (",int(sum_x/area),',',int(sum_y/area),')')
    pass

def bordes():
    '''
    Obtener el borde de las figuras de una imagen y el numero de imagenes
    
    fuente: 
    https://programarfacil.com/blog/vision-artificial/detector-de-bordes-canny-opencv/
    
    '''
    nombre = 'hex.jpg'
#    original = cv2.imread("imagenes/monedas.jpg")
    original = cv2.imread(nombre)
    cv2.imshow("original", original)
     
    # Convertimos a escala de grises
    gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
     
    # Aplicar suavizado Gaussiano
    gauss = cv2.GaussianBlur(gris, (5,5), 0)
     
    cv2.imshow("suavizado", gauss)
     
    # Detectamos los bordes con Canny
    canny = cv2.Canny(gauss, 50, 150)
     
    cv2.imshow("canny", canny)
     
    # Buscamos los contornos
    (_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     
    # Mostramos el número de monedas por consola
    print("He encontrado {} objetos".format(len(contornos)))
     
    cv2.drawContours(original,contornos,-1,(0,0,255), 2)
    cv2.imshow("contornos", original)
     
    cv2.waitKey(0)
    pass

    
#test_1()
#test_2()
#test_3()
#test_4()
bordes()