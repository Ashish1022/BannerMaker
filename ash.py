from PIL import Image

img1 = Image.open(r"imgs/mainCard3.png") 
  
img2 = Image.open(r"photos/home2.jpg") 
    
# img1.paste(img2, (0,0), mask=img2) 
Image.Image.paste(img1, img2, (146, 165))
# img1.save('imgs/mainCard3.png')
img1.show()


