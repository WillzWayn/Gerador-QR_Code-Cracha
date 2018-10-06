# -*- coding: cp1252 -*-
# Roda apenas em Python 2.7
import pyqrcode
import tkinter
import png
import shutil
from pyqrcode import QRCode
from PIL import Image, ImageTk, ImageFont, ImageDraw


##https://conectabell.com/python-pillow-creando-imagenes-con-pil/

# TAMANHO EM MM
j = 3.7795275591 # 1 j = 1 mm
tamanhoQR = (int(35*j)+1,int(35*j)+1)
xDoPapel = int(140*j)+1
yDoPapel = int(45*j)+1



## LOOP, Abre um arquivo LISTA e pega os nomes separados pela tecla enter e armazena em jv
with open("LISTA.txt") as f:
    for line in f:
        print line.replace('\n','').split('42')      
        
        jv=line.replace('\n','') # Separa as linhas do texto
        jv = jv.split('42') #NO arquivo lista.txt deixei NOME42UNIV, usando esse comando, ele cria um vetor com NOME, UNIV
        #onde jv[0] vai ser o nome da pessoa, e jv[1] a universidade
        univ = jv[1] # cria uma variavel chamada univ
        jv = jv[0]  #como ja tinha feito o codigo todo e adicionei a universidade depois, mudei o nome da variavel jv[0] p jv. ai nao preciso mexer no codigo
        #tamanho do nome para shiftar na etiqueta
        tamNome = len(jv)*4+10
        tamUniv = len(univ)*4
        
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
        font = ImageFont.truetype("arial.ttf", 20)
# draw.text((x, y),"Sample Text",(r,g,b))
        #im.resize(600, 600)
        im.save('imgs/'+jv+'.png')
        im = im.resize(tamanhoQR, Image.ANTIALIAS)
###################
 
        img = Image.new('RGB', (xDoPapel,yDoPapel), "white")

        draw = ImageDraw.Draw(img) ####
        draw.text(((xDoPapel-tamanhoQR[0])/2 + tamanhoQR[0] - tamNome, yDoPapel/2 - 30), jv ,(0,0,0), font=font) ## NOME
        font = ImageFont.truetype("arial.ttf", 15)
        draw.text(((xDoPapel-tamanhoQR[0])/2+tamanhoQR[0] - tamUniv, yDoPapel/2), univ,(0,0,0), font=font)

        
        img.paste(im,(20,20))
        img.save('imgs/'+jv+'.png')
        
       

