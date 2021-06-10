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
print (len(bol))
for i in bol:
    if "CELL" in i:
        if i not in liste:
            liste.append(i)
#print (len(liste))
for i in liste:
    
    yaz.write(str("BEGIN:VCARD\n")+i+str("\n"))
oku2=open("yeni.vcf","r").readlines()
yaz1=open("yeni1.vcf","a")
for i in oku2:
    if "\n"!=i:
       yaz1.write(i)
yaz.close()
yaz1.close()
os.system("ERASE yeni.vcf")
os.system("ren yeni1.vcf yeni.vcf")
