import sys
from PIL import Image
import time
import random
from tqdm import tqdm



class Exception(Exception):
	pass


n = 2*4

original = Image.open("garden.jpg")
original.load()

style = Image.open("gogh.jpeg")
style.load()

width, height = original.size

new_im = Image.new('RGB', (width, height))
new_im.load()

allPos = []

for y in tqdm(range(int(height/n))):
    for x in range(int(width/n)):
        fullString = ""
        for i in range(n):
            for j in range(n):
              r, g, b = style.getpixel((x*n+j, y*n+i))
              fullString+=format(r, '02x')+format(g, '02x')+format(b, '02x')
        
        if(fullString not in allPos):
            allPos.append(fullString)



table = {}
visited = []

que = [] 





for index in tqdm(range(int((height/n)**2))):
    error = 99999999999999999999999999999999999999999999999999999999999999999999
    bestString = ""
    for string in allPos:
        #print(string)
        tempError = 0
        #print(len(string))
        for i in range(n**2):
            allVal  = string[i*6:(i+1)*6]
            #print(i)
            r = int(allVal[0:2],16)
            g = int(allVal[2:4],16)
            b = int(allVal[4:6],16)

            y = int(index/(height/n))
            x = int(index%(height/n))
            k = int(i/n)
            z = i%n

            rg, gg, bg = original.getpixel((x*n+z, y*n+k))
            tempError += (r-rg)**2+(b-bg)**2+(g-gg)**2
        if(tempError<error):
            error = tempError
            bestString = string
    
    for i in range(n**2):
            allVal  = bestString[i*6:(i+1)*6]
            r = int(allVal[0:2],16)
            g = int(allVal[2:4],16)

            b = int(allVal[4:6],16)


            y = int(index/(height/n))
            x = int(index%(height/n))
            k = int(i/n)
            z = i%n

            
            new_im.putpixel((x*n+z, y*n+k), (r, g, b))


new_im.save('pic.jpg')