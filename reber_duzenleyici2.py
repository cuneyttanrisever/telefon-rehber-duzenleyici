# -*- coding: utf-8 -*-
import os
import re
print("""
#############################
# Coded : Cüneyt TANRISEVER #
#############################
""")
yaz=open("yeni.vcf","w+")
oku=open("rehber.vcf","r").read()
bol=oku.split("BEGIN:VCARD")
liste=[]
for i in bol:
    if "CELL" in i:
        if i not in liste:
            liste.append(i)
rehberlist=[]
rehberlist1=[]
a1="BEGIN:VCARD\nVERSION:2.1\n"
a2="\nTEL;CELL:"
a3="\nEND:VCARD\n"
for i in liste:
    try:
        b=re.findall("FN:(.*?)\nTEL",i)
        b[0]
    except IndexError:
         b=re.findall("FN:(.*?)\n",i)
    a=re.findall("TEL;CELL:(.*?)\n",i)
    rehberlist.append(a[0].replace(" ",""))
    an=re.findall("FN:(.*?)\n",i)
    if []==an:
        an1=re.findall("FN;(.*?)\n",i)
        rehberlist1.append("FN;"+str(an1[0]))
    else:
        rehberlist1.append("FN:"+str(an[0]))
for i in range(len(rehberlist)):
    yazdir=a1+str(rehberlist1[i]+a2+str(rehberlist[i])+a3)
    yaz.write(yazdir)
yaz.close()
print("kişileriniz yeni.vcf dosyasına kayıt edildi.")

