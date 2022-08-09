import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageEnhance, ImageTk
import matplotlib.pyplot as plt 
import random  
from PIL import ImageFont
from PIL import ImageDraw
import os.path


def color8(image): 
    pixels = image.load()
    w=image.width 
    h=image.height 
    brightnessAll = 0
    countAll = 0
    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            brightnessAll += sum([R,G,B])/(3)
            countAll +=1

    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB   
            if ((R > brightnessAll/ countAll) & (G > brightnessAll/ countAll) & (B > brightnessAll/ countAll)):
                R = 256; G = 256; B = 256   
            elif ((R > brightnessAll/ countAll) & (G > brightnessAll/ countAll)):
                R = 256; G = 256; B = 0  
            elif ((R > brightnessAll/ countAll) & (B > brightnessAll/ countAll)):
                R = 256; G = 0; B = 256    
            elif ((B > brightnessAll/ countAll) & (G > brightnessAll/ countAll)):
                R = 0; G = 256; B = 256   
            elif (R > brightnessAll/ countAll):
                R = 256; G = 0; B = 0
            elif (G > brightnessAll/ countAll):
                G = 256; R = 0; B = 0
            elif (B > brightnessAll/ countAll):
                B = 256; R = 0; G = 0
            else: B = 0; R = 0; G = 0
            pixels[i,j] = R,G,B
 
def bayer2x2(image):
    w=image.width 
    h=image.height  
    pixels = image.load() 
    bayer2 = [2,3,4,1]

    for i in range (len(bayer2)):
        bayer2[i] = bayer2[i] * 64 - 1
  
    k = []
    k = bayer2.copy() 
    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            R = R
            G = G
            B = B
             
            dif = k[(j%2*2+i%2)]
            if ((R > dif) & (G >  dif) & (B > dif)):
                R = 256; G = 256; B = 256   
            elif ((R > dif) & (G >dif)):
                R = 256; G = 256; B = 0  
            elif ((R > dif) & (B > dif)):
                R = 256; G = 0; B = 256    
            elif ((B > dif) & (G >dif)):
                R = 0; G = 256; B = 256   
            elif (R > dif):
                R = 256; G = 0; B = 0
            elif (G > dif):
                G = 256; R = 0; B = 0
            elif (B > dif):
                B = 256; R = 0; G = 0
            else: B = 0; R = 0; G = 0
            pixels[i,j] = R,G,B

def bayer8x8(image):
    w=image.width 
    h=image.height  
    pixels = image.load()

    d = [1, 33,  9, 41, 3,  35, 11, 43, 49, 17, 57, 25, 51, 19, 59, 27, 13, 45, 5, 
        37, 15, 47, 7, 39, 61, 29, 53, 21, 63, 31, 55, 23, 4, 36, 12, 44, 2, 34, 10, 42, 52,
        20, 60, 28, 50, 18, 58, 26, 16, 48, 8, 40, 14, 46, 6, 38, 64, 32, 56, 24, 62, 30,
        54, 22]

    for i in range (len(d)):
        d[i] = (d[i] * 4 - 1) / 256 
  
    brightnessAll = 0
    countAll = 0
    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            brightnessAll += sum([R,G,B])/(3)
            countAll +=1
  
    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            R = R/256
            G = G/256
            B = B/256     
    
            dif = d[(j%8*8+i%8)]
            if ((R > dif) & (G >  dif) & (B > dif)):
                R = 256; G = 256; B = 256   
            elif ((R > dif) & (G > dif)):
                R = 256; G = 256; B = 0  
            elif ((R > dif) & (B > dif)):
                R = 256; G = 0; B = 256    
            elif ((B > dif) & (G > dif)):
                R = 0; G = 256; B = 256   
            elif (R > dif):
                R = 256; G = 0; B = 0
            elif (G > dif):
                G = 256; R = 0; B = 0
            elif (B > dif):
                B = 256; R = 0; G = 0
            else: B = 0; R = 0; G = 0
            pixels[i,j] = R,G,B

def imageNoise(image):
     
    w=image.width 
    h=image.height     
    pixels = image.load()

    brightnessAll = 0
    countAll = 0
    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            brightnessAll += sum([R,G,B])/(256 * 3)
            countAll +=1

    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            brightness = sum([R,G,B])/(256 * 3)
             
            if (brightness + (random.uniform(-0.5, 0.5) - 0.5)> brightnessAll/countAll):
                pixels[i,j] = 250,250,250 
            else:
                pixels[i,j] = 0,0,0
                
def imageBandW(image):
     
    w=image.width 
    h=image.height     
    pixels = image.load()

    brightnessAll = 0
    countAll = 0
    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            brightnessAll += sum([R,G,B])/(256 * 3)
            countAll +=1

    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            brightness = sum([R,G,B])/(256 * 3) 
            if (brightness > brightnessAll/countAll):
                pixels[i,j] = 250,250,250 
            else:
                pixels[i,j] = 0,0,0
                
def imageNoiseColor(image):
    w=image.width 
    h=image.height     
    pixels = image.load()
  
    enhancerBrightness = ImageEnhance.Brightness(image)  
    factorB = 1.5 
    image = enhancerBrightness.enhance(factorB) 

    brightnessAll = 0
    countAll = 0
    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            brightnessAll += sum([R,G,B])/(256 * 3)
            countAll +=1

    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            R = R/256
            B = B/256
            G = G/256 
             
            if ((R + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll) & (G + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll) & (B + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll)):
                pixels[i,j] = 250,250,250 
            elif ((R + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll) & (G + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll)):
                pixels[i,j] = 250,250,0 
            elif ((B + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll) & (G + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll)):
                pixels[i,j] = 0,250,250 
            elif ((R + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll) & (B + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll)):
                pixels[i,j] = 250,0,250 
            elif (R + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll):
                pixels[i,j] = 250,0,0 
            elif (G + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll):
                pixels[i,j] = 0,250,0 
            elif (B + (random.uniform(-0.5, 0.5) - 0.5) > brightnessAll/countAll):
                pixels[i,j] = 0,0,250 
            else:
                pixels[i,j] = 0,0,0
                
def bayer4x4(image):
    w=image.width 
    h=image.height 
    
    pixels = image.load()

    d = [0.1250, 1.0000, 0.1875, 0.8125, 0.6250, 0.3750, 0.6875,
     0.4375,0.2500, 0.8750, 0.0625, 0.9375, 0.7500, 0.5000, 0.5625, 0.3125]

    for i in range (len(d)):
        d[i] = (d[i] * 255)

    dDark = [0.1250, 1.0000, 0.1875, 0.8125, 0.6250, 0.3750, 0.6875,
     0.4375,0.2500, 0.8750, 0.0625, 0.9375, 0.7500, 0.5000, 0.5625, 0.3125]

    for i in range (len(dDark)):
        dDark[i] = (dDark[i] * 255) 
    
    brightnessAll = 0
    countAll = 0
    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            brightnessAll += sum([R,G,B])/(3)
            countAll +=1

    k = []
    if (brightnessAll/countAll > 128) :
        k = d.copy()
    else: k = dDark.copy()

    for i in range (w):
        for j in range (h):
            pixelRGB = image.getpixel((i,j))
            R,G,B = pixelRGB  
            R = R
            G = G
            B = B
             
            dif = k[(j%4*4+i%4)]
            if ((R > dif) & (G >  dif) & (B > dif)):
                R = 256; G = 256; B = 256   
            elif ((R > dif) & (G >dif)):
                R = 256; G = 256; B = 0  
            elif ((R > dif) & (B > dif)):
                R = 256; G = 0; B = 256    
            elif ((B > dif) & (G >dif)):
                R = 0; G = 256; B = 256   
            elif (R > dif):
                R = 256; G = 0; B = 0
            elif (G > dif):
                G = 256; R = 0; B = 0
            elif (B > dif):
                B = 256; R = 0; G = 0
            else: B = 0; R = 0; G = 0
            pixels[i,j] = R,G,B
            
def imgGo(img_name): 
     
    image = Image.open(img_name)
    heigth_b = 200
    canvas = Image.new('RGB', ((image.width) * 4, (image.height) * 2  + heigth_b), 'black')
    myFont = ImageFont.truetype("arial.ttf", 65)

    image_copy = image.copy()
    img_width = 0
    img_heigth = 0
    position = (img_width, img_heigth)
    canvas.paste(image_copy, position) 
    image_editable = ImageDraw.Draw(canvas)
    image_editable.text((int(image.width/3), image.height - 5), "Original", font = myFont, fill = (237, 230, 211))

    image_copy = image.copy()
    color8(image_copy) 
    img_width = (image.width) * 2
    img_heigth = image.height * 1 + int(heigth_b/2)
    position = (img_width, img_heigth)
    canvas.paste(image_copy, position) 
    image_editable.text((int(img_width + image.width/3), img_heigth + image.height), "8 Colors", font = myFont, fill = (237, 230, 211))

    image_copy = image.copy()
    bayer8x8(image_copy)     
    img_width = (image.width) * 3
    img_heigth = image.height * 0
    position = (img_width, img_heigth)
    canvas.paste(image_copy, position)
    image_editable.text((int(img_width + image.width/3), img_heigth + image.height - 5), "Bayer 8x8", font = myFont, fill = (237, 230, 211))

    image_copy = image.copy()
    bayer4x4(image_copy)  
    img_width = (image.width) * 2
    img_heigth = image.height * 0
    position = (img_width, img_heigth)
    canvas.paste(image_copy, position)  
    image_editable.text((int(img_width + image.width/3), img_heigth + image.height - 5), "Bayer 4x4", font = myFont, fill = (237, 230, 211))

    image_copy = image.copy()
    bayer2x2(image_copy)   
    img_width = (image.width) * 1
    img_heigth = image.height * 0
    position = (img_width, img_heigth)
    canvas.paste(image_copy, position) 
    image_editable.text((int(img_width + image.width/3), img_heigth + image.height - 5), "Bayer 2x2", font = myFont, fill = (237, 230, 211))

    image_copy = image.copy()
    imageNoise(image_copy) 
    img_width = (image.width) * 1
    img_heigth = image.height * 1 + int(heigth_b/2)
    position = (img_width, img_heigth)
    canvas.paste(image_copy, position) 
    image_editable.text((int(img_width + image.width/7), img_heigth + image.height), "Black & White Noise", font = myFont, fill = (237, 230, 211))

    image_copy = image.copy()
    imageNoiseColor(image_copy) 
    img_width = (image.width) * 3
    img_heigth = image.height * 1 + int(heigth_b/2)
    position = (img_width, img_heigth)
    canvas.paste(image_copy, position) 
    image_editable.text((int(img_width + image.width/4), img_heigth + image.height), "8 Colors Noise", font = myFont, fill = (237, 230, 211)) 

    image_copy = image.copy()
    imageBandW(image_copy)
    img_width = (image.width) * 0
    img_heigth = image.height * 1 + int(heigth_b/2)
    position = (img_width, img_heigth)
    canvas.paste(image_copy, position)
    image_editable.text((int(img_width + image.width/4), img_heigth + image.height), "Black & White", font = myFont, fill = (237, 230, 211))
    
    imgplot = plt.imshow(canvas)
    img_name = "result"
    n = 1
    img_names = img_name
    while (1): 
        check_file = os.path.isfile(img_names + ".jpg")
        if (check_file):
            img_names = img_name + "(" + str(n) + ")"
            n += 1
            
        else: break

    canvas.save(img_names + ".jpg")
    
def open_image_file(): 
    filetypes = (
        ('JPG files', '*.jpg'),
        ('PNG files', '*.png'),
        ('All files', '*.*')
    ) 
    f = fd.askopenfilename(filetypes=filetypes)
    imgGo(f)
    
window = tk.Tk()
window.title('Image changing filters')
window.resizable(False, False)
window.geometry('500x310')
window.configure(background='black')  
 
open_button = ttk.Button(
    window,
    text='Open image',
    command=open_image_file
)
pole = ttk.Label(text="", foreground="white", background="black")
pole.grid(row=0, column=0, padx=20)
text = ttk.Label(text="\n\nThis is the image filter app.\
                 \n\nSo you will have an image with those filters:\n\
                 - original image\n\
                 - bayer filter with 2x2 matrix\n\
                 - bayer filter with 4x4 matrix\n\
                 - bayer filter with 8x8 matrix\n\n\
Filters depends of image pixels britness:\n\
                 - black and white colors only\n\
                 - black and white colors with random noise\n\
                 - 8 colors (black, white, red, green, blue, cyan, magenta, yellow)\n\
                 - 8 colors with random noise\n", foreground="white", background="black")
text.grid(row=0, column=1)
open_button.grid(column=1, row=1, padx=100, pady=5)
 
window.mainloop()
