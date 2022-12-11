from PIL import Image as im


print("\nWhite Background Remover\n")
fileName = input("Open File: ")
imageIn = im.open(fileName)
print("Opening the image file was successful.\n")

pixelsIn = imageIn.load()
imageOut = im.new('RGBA', (tuple(imageIn.size)), (0, 0, 0, 0))
pixelsOut = imageOut.load()


for i in range(imageIn.size[0]):
    for j in range(imageIn.size[1]):
        detect = pixelsIn[i,j][0] > 200 and pixelsIn[i,j][1] > 200 and pixelsIn[i,j][2]

        if detect: 
            pixelsOut[i, j] = (0, 0, 0, 0)
        else: 
            pixelsOut[i, j] = (255, 255, 255, 255)
            print("✔️ At " + str((i, j)) + ": " + str(pixelsIn[i, j]) + " 👉 " + str(pixelsOut[i, j]))


print("\nImage generated.")
print("Image Size: " + str(imageOut.size[0]) + " × " + str(imageOut.size[1]))
imageOut.show()
imageOut.save(fileName.split(".")[0] + "_out.png")