# this is a comment, yo -> https://github.com/CullenMar/205proj1section2
from PIL import Image
def median( inputList ): #gets median value from an array
    a = 0
    while a < 8:
        if (inputList[a] > inputList[a + 1]):
            b = inputList[a]
            inputList[a] = inputList[a + 1]
            inputList[a + 1] = b
            if (a > 1):
                a -= 2
        a += 1
    return (inputList[4])
imageList = []
for z in range (1, 10):
    im1 = Image.open("Images/" + str(z) + ".png")
    imageList.append(im1)
width1, height1 = im1.size #gets width and height values
finalImage = Image.new("RGB", (width1, height1), "RED")
pixel = finalImage.load()
redList = []
greenList = []
blueList = []
for x in range (width1): #analyzes each pixel and paints median value to new image
    for y in range (height1):
        for myImage in imageList:
            red1, green1, blue1 = myImage.getpixel((x, y))
            redList.append(red1)
            greenList.append(green1)
            blueList.append(blue1)
        pixel[x, y] = (median(redList), median(greenList), median(blueList))
        del redList[:]
        del greenList[:]
        del blueList[:]
finalImage.save("Images/finalImage.png") #saves result to a png file