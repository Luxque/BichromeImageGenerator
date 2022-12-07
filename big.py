from PIL import Image as im
import random


print("\nBichrome Image Generator\n")
fileName = input("Open File: ")
imageIn = im.open(fileName)
print("Opening the image file was successful.\n")

r1 = round(float(input("R Value of Color 1: ")))
g1 = round(float(input("G Value of Color 1: ")))
b1 = round(float(input("B Value of Color 1: ")))
print()

r2 = round(float(input("R Value of Color 2: ")))
g2 = round(float(input("G Value of Color 2: ")))
b2 = round(float(input("B Value of Color 2: ")))
print()

print("Option A: Checkboard")
print("Option B: Horizontal")
print("Option C: Vertical")
print("Option D: Random")
option = input("\nRendering Option: ").upper()
print()


pixelsIn = imageIn.load()
imageOut = im.new('RGBA', (tuple(imageIn.size)), (0, 0, 0, 0))
pixelsOut = imageOut.load()

for i in range(imageIn.size[0]):
    for j in range(imageIn.size[1]):
        alpha = pixelsIn[i][j][3]

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