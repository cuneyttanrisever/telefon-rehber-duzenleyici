# -*- coding: utf-8 -*-
import os
print("""
#############################
# Coded : Cüneyt TANRISEVER #
#############################
""")
oku=open("rehber.vcf","r").read()
bol=oku.split("BEGIN:VCARD")
#print (bol[2])
liste=[]
yaz=open("yeni.vcf","a")
yaz1=open("yeni1.vcf","w")
yaz1.close()
print (len(bol))
for i in bol:
    if "CELL" in i:
        if i not in liste:
            liste.append(i)
#print (len(liste))
for i in liste:
    yaz.write(str("BEGIN:VCARD\n")+i+str("\n"))
yaz2=open("yeni.vcf","r").readlines()
yaz1=open("yeni1.vcf","a")
for i in yaz2:
    if "\n"!=i:
       yaz1.write(i)
yaz.close()
yaz1.close()
yaz2=[]
os.system("ERASE yeni.vcf")
os.system("ren yeni1.vcf yeni.vcf")
