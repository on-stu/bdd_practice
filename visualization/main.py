from PIL import Image
import numpy as np

def blackToTransparent(img):
    img = img.convert('RGBA')
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    return img

def whiteToRed(img):
    img = img.convert('RGBA')
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 0, 0, 100))
        else:
            newData.append(item)
    img.putdata(newData)
    return img

def whiteToBlue(img):
    img = img.convert('RGBA')
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((0, 0, 255, 100))
        else:
            newData.append(item)
    img.putdata(newData)
    return img

IMG_PATH = "visualization/imgs/"

input_image = Image.open(IMG_PATH + "input_0000"+ ".png")
mask_image = Image.open(IMG_PATH + "mask_0000"+ ".png")
output_image = Image.open(IMG_PATH + "output_0000"+ ".png")

# overlap input, mask and output images

# input image
input_image = input_image.resize((256, 256))
input_image = input_image.convert("RGBA")

# mask image
mask_image = mask_image.resize((256, 256))
mask_image = mask_image.convert("RGBA")
mask_image = whiteToRed(mask_image)
mask_image = blackToTransparent(mask_image)

# output image

output_image = output_image.resize((256, 256))
output_image = output_image.convert("RGBA")
output_image = whiteToBlue(output_image)
output_image = blackToTransparent(output_image)

# overlap input, mask and output images
new_img = input_image.copy()
new_img.paste(mask_image, (0, 0), mask_image)
new_img.paste(output_image, (0, 0), output_image)

new_img.save(IMG_PATH + "overlap_0000"+ ".png")



