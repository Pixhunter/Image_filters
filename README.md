# Image_filters

This is the image filter app.<br/>
So you will have an image with those filters:<br/>
                 - original image<br/>
                 - bayer filter with 2x2 matrix <br/>
                 - bayer filter with 4x4 matrix<br/>
                 - bayer filter with 8x8 matrix<br/>
                 
Filters depends of image pixels britness:
                 - black and white colors only<br/>
                 - black and white colors with random noise<br/>
                 - 8 colors (black, white, red, green, blue, cyan, magenta, yellow)<br/>
                 - 8 colors with random noise<br/>
                
The Bayer filter is a matrix of different sizes that use each pixel and then compare matrix values and pixel color value (Red, Green, Blue).<br/>

                                       [ 0.1250 1.0000 0.1875 0.8125 ]             
    Bayer 2x2 = [ 4 1 ]    Bayer 4x4 = [ 0.6250 0.3750 0.6875 0.4375 ]     Bayer 8x8 (see in code)   
                [ 2 3 ]                [ 0.2500 0.8750 0.0625 0.9375 ]       
                                       [ 0.7500 0.5000 0.5625 0.3125 ] 
If matrix value bigger then pixel value - we use value 0 for pixel, else - 256 (when matrix less). We see the 8 ways to comparing. <br/>
We compare each color with matrix value, for example if Red, Green and Blue colors have bigger value then matrix value - it will be black color (R=256, G=256, B=256). Another example - if one or two colors have bigger value then matrix value - we also set to those color(s) max value 256 (so if less we set 0).<br/>
<br/>

For another filters we use the medium corntrast of the image. The first we do - we count every pixel medium value:<br/>
$$\left(\sum_{k=1}^n\left((R + G + B)\over 3\right) / n \right) = Value $$<br/>
Then we compare each pixel color value with this medium contrast value - if it is bigger then pixel value we set 0 and else we set 256 for each color like with the Bayer matrix.<br/>
With this method we use black and white pallete and 8 colors pallete.<br/>
<br/>
The next two methods usind two previous but with some noising with black and white colors and 8 colors pallete:
$$\left(R + (random.uniform(-0.5, 0.5) - 0.5\right) \geq Value $$<br/>
This noise makes picture not to be solid.<br/>

This is the example of program result:<br/>

 
![result(2)](https://user-images.githubusercontent.com/88940110/183755211-511237ca-f3b4-4fdf-bc59-a10ddf37ad93.jpg)
![result(6)](https://user-images.githubusercontent.com/88940110/183759812-3ec54063-4426-4c22-b5f0-f1aea1f5180a.jpg)
![result(11)](https://user-images.githubusercontent.com/88940110/183759882-6c4ee75f-f115-4423-b043-5b19e15c1a1e.jpg)
![result(15)](https://user-images.githubusercontent.com/88940110/183759894-c78b0222-5b7a-40e0-b296-a4cbae9c6097.jpg)
![result(12)](https://user-images.githubusercontent.com/88940110/183759898-21ee4734-3045-4093-8293-409d9e5116dc.jpg)
![result(22)](https://user-images.githubusercontent.com/88940110/183759904-769bd1b2-7eec-408a-a06c-10e1d30b1bc0.jpg)
![result(21)](https://user-images.githubusercontent.com/88940110/183759909-7bcbae8c-d0d6-45b2-b999-85195d513a29.jpg)
