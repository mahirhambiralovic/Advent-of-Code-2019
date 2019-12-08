def set_pixels(image, complete, layer_i, pixel_i):
    # If transparent, set pixel to True and try next layer
    if image[layer_i][pixel_i] == (2,False):
        image[layer_i][pixel_i] == (2,True)
        set_pixels(image,complete,layer_i+1,pixel_i)

    # If unused color-pixel, add it to complete image
    elif image[layer_i][pixel_i][1] == False:
        complete.append(image[layer_i][pixel_i][0])
        # Then set it and pixel_i in all following layers to True
        image[layer_i][pixel_i] = (image[layer_i][pixel_i][0], True)
        if pixel_i != 150:
            for layer_j in range(layer_i+1, len(image)):
                image[layer_j][pixel_i] = (image[layer_j][pixel_i][0], True)


f = open("input.txt","r").read().strip("\n")
f = list(map(int, f))
layer = []
image = []
for i in range(len(f)):
    if (i % (25*6)) == 0 and i != 0:
        image.append(layer)
        layer = []
    layer.append((f[i],False))
image.append(layer)

complete = []
for layer_i in range(len(image)):
    for pixel_i in range(len(image[layer_i])):
        set_pixels(image,complete,layer_i,pixel_i)
row = 0
column = 0
for i in range(len(complete)):
    if column == 25:
        print()
        column = 0
    column +=1
    print(complete[i], end=" ")
print()
