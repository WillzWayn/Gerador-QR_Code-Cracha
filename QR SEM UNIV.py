# -*- coding: cp1252 -*-
# Roda apenas em Python 2.7
import pyqrcode
import tkinter
import png
import shutil
from pyqrcode import QRCode
from PIL import Image, ImageTk, ImageFont, ImageDraw

j = 3.7795275591 # 1 j = 1 mm

# TAMANHO EM MM
tamanhoQR = (int(35*j)+1,int(35*j)+1)
xDoPapel = int(148*j)+1
yDoPapel = int(45*j)+1

## LOOP, Abre um arquivo LISTA e pega os nomes separados pela tecla enter e armazena em jv
with open("LISTA.txt") as f:
    for line in f:
        print line
        jv=line.replace('\n','')
        
        url = pyqrcode.QRCode(jv,error = 'H')
        url.png('imgs/'+jv+'.png',scale=10)

        im = Image.open('imgs/'+jv+'.png')
        im = im.convert("RGBA")

        
        logo = Image.open('logo.png')
        #Box => a imagem ficará em um (x,y) inicial até (x2,y2) final.
        box = (135,135,235,235) #imagem terá 100 x 100 px
        
        im.crop(box)
        
        region = logo
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        
        im.paste(region,box)
       # font = ImageFont.truetype("Verdana.ttf", 25)
        font = ImageFont.truetype("Bodega Script\TTF\Bodega Script.ttf", 25)
# draw.text((x, y),"Sample Text",(r,g,b))
        #im.resize(600, 600)
        im.save('imgs/'+jv+'.png')
        im = im.resize(tamanhoQR, Image.ANTIALIAS)
###################
 
        img = Image.new('RGB', (xDoPapel,yDoPapel), "white")

        draw = ImageDraw.Draw(img) ####
        draw.text((tamanhoQR[0]+30, yDoPapel/2 - 10), jv ,(0,0,0), font=font)

        
        img.paste(im,(20,20))
        img.save('imgs/'+jv+'.png')
        
       

