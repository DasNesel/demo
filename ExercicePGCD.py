# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:27:34 2017

@author: Matthieu
"""

def PGCD(a,b):
    while a%b!= 0:
        a,b=b,a%b
    return b