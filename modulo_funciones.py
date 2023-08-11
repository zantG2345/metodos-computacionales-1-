# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:13:34 2021

@author: santi
"""

def numero_par(numero:int)->bool:
    rta=numero%2==0 
    return rta


def es_divisible(numero1:int,numero2:int)->bool:
    divisibilidad=numero1%numero2==0
    return divisibilidad 
    
def edad_conducir(edad:int)->bool:
    return edad>16
     
def dinero_suficiente(dinero:int,cuenta:int,propina:bool)->bool:
    propina=cuenta*10/100
    ac=dinero-(cuenta+propina)
    sd=dinero-cuenta
    rta=ac>0
    return rta


respuesta= dinero_suficiente(500, 300,1)
print (respuesta)

