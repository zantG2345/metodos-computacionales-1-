# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 09:20:53 2021

@author: santi
"""

def calcular_multiplicacion_en_columna(matriz: list)->int:
        """ Multiplicación en la columna
        Parámetros:
          matriz (list): Una matriz de enteros, sobre la cual hay que calcular la suma de la columna dada por
                         parámetro.
          columna (int): Entero que indica sobre cual de las columnas hay que hacer las multiplicaciones. Es un
                         valor entre 0 y M-1, donde M es la cantidad de columnas de la matriz.
        Retorno:
          int: El valor de la multiplicación de todos los elementos que se encuentran en una columna particular de
               la matríz.
        """
        
        rta=0
        for i in range(0,len(matriz)):
            for j in range(0,len(matriz)):
                rta+=matriz[i][j]
        return rta


print (calcular_multiplicacion_en_columna([[0,1,3],[32,23],[2,3,4]]))
         