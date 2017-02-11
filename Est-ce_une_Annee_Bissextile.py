#!/usr/bin/python
# -*- coding: utf-8 -*-

##Programme : Est-ce une année bissextile ?

#Import
import sys

#Year = input("Tappez une année : ")
Year = int(sys.argv[1])

if Year % 400 == 0  :
    print Year, "est une annee bissextile !"
elif Year % 4 == 0 and Year % 100 != 0 :
    print Year, "est une annee bissextile !"
else :
    print Year, "n'est pas une annee bissextile."

#Liste d'années bissextiles :
''' 
1600
1956
2000
2016
2400
'''
