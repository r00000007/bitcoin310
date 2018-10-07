from PIL import Image
import re

image = Image.open("aa.bmp")
rgb_im = image.convert('RGB')

sstr=""
for i in range(0,2799):
    r, g, b = rgb_im.getpixel((i, 310))
    if(r==255):
        sstr = sstr+"1"
    elif(r==0):
        sstr = sstr+"0"
print(sstr)
i =0
j =8
l = []
dlen = len(sstr)
for i in range(0,dlen,8):
     l.append(sstr[i:j])
     j=j+8
a = re.findall(r'[10]{8}',''.join(l))
print("\n")
print(a)
flag = []
for i in a:
     flag.append(chr(int(i,2)))
print(''.join(flag))

f = open('base64.txt','w')
f.write(''.join(flag))
f.close()