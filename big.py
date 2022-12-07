from PIL import Image as im
import random


print("\nBichrome Image Generator\n")
fileName = input("Open File: ")
imageIn = im.open(fileName)
print("Opening the image file was successful.\n")

hex1 = input("Hexadecimal value of color 1: ")
r1 = int(hex1[0] + hex1[1], 16)
g1 = int(hex1[2] + hex1[3], 16)
b1 = int(hex1[4] + hex1[5], 16)
print()

hex2 = input("Hexadecimal value of color 2: ")
r2 = int(hex2[0] + hex2[1], 16)
g2 = int(hex2[2] + hex2[3], 16)
b2 = int(hex2[4] + hex2[5], 16)
print()

print("Option A: Checkboard")
print("Option B: Vertical")
print("Option C: Horizontal")
print("Option D: Random")
option = input("\nRendering Option: ").upper()
print()


pixelsIn = imageIn.load()
imageOut = im.new('RGBA', (tuple(imageIn.size)), (0, 0, 0, 0))
pixelsOut = imageOut.load()

for i in range(imageIn.size[0]):
    for j in range(imageIn.size[1]):
        alpha = pixelsIn[i, j][3]

        if alpha != 0:
            if option == 'A':
                mode = (i+j) % 2 != 0
            elif option == 'B':
                mode = i % 2 != 0
            elif option == 'C':
                mode = j % 2 != 0
            elif option == 'D':
                mode = random.choice([True, False])
            else:
                exit()

            if mode: 
                pixelsOut[i, j] = (r1, g1, b1, alpha)
            else:
                pixelsOut[i, j] = (r2, g2, b2, alpha)
            
            print("✔️ At " + str((i, j)) + ": " + str(pixelsIn[i, j]) + " 👉 " + str(pixelsOut[i, j]))


print("\nImage generated.")
print("Image Size: " + str(imageOut.size[0]) + " × " + str(imageOut.size[1]))
imageOut.show()
imageOut.save(fileName.split('.')[0] + "_out.png")