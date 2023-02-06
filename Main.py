import contextlib
import glob
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import sys

VERSION = "0.0.1"

print("""
      *******************************************
      **** InterSystems-HiThere-GIFGenerator ****
      *******************************************
      """)

for arg in sys.argv:
    if (arg == "-v" or arg == "-version"):
        print("Version: " + VERSION)
        quit()


name = "Philipp"
name = input("Enter your name: ")

# check if name is beween 2 and 10 characters
while (len(name) < 2 or len(name) > 10):
    print("Please enter a name between 2 and 10 characters")
    name = input("Enter your name: ")


# Open an Image
myFont = ImageFont.truetype('font/DINAlternate-Bold.ttf', 200)

filenames = []
frames = []
# iterate through each character in name
name_part = ""
im_part = ""
counter = 1

move_per_frame = 40

# ad "I'm"
for char in ["I", "'", "m"]:
    img = Image.open('imgs/test.png')
    im_part += char
    I1 = ImageDraw.Draw(img)

    # get the center of the image
    width, height = img.size

    y = height / 2 - 100
    x = width/2 - (counter * move_per_frame)

    # add name
    I1.text((x, y), im_part,
            fill=(0, 181, 175), font=myFont)

    filename = "out/"+str(counter)+".png"
    filenames.append(filename)
    # Save the edited image
    img.save(filename)
    frames.append(Image.open(filename))
    counter += 1

# add name
for char in name:
    img = Image.open('imgs/test.png')
    name_part += char
    I1 = ImageDraw.Draw(img)

    # get the center of the image
    width, height = img.size

    y = height / 2 - 100
    x = width/2 - (counter * move_per_frame)

    # add "I'm"
    #I1.text((x - 270, y), "I`m", fill=(0, 181, 175), font=myFont)

    # add name
    I1.text((x, y), name_part,
            fill=(51, 54, 149), font=myFont)

    filename = "out/"+str(counter)+".png"
    filenames.append(filename)
    # Save the edited image
    img.save(filename)
    frames.append(Image.open(filename))
    counter += 1


frames_inverted = frames[::-1]

for i in range(0, 10):
    frames.append(frames[-1])

for frame in frames_inverted:
    frames.append(frame)

# filepaths
fp_in = "out"
fp_out = "out/image.gif"

# frames = [Image.open(image) for image in glob.glob(f"{fp_in}/*.png")]
frame_one = frames[0]
gif = frame_one.save(fp_out, format="GIF", append_images=frames,
                     save_all=True, duration=200, loop=0, transparency=80)


frames = None
frames_inverted = None

""" for filename in filenames:
    os.remove(filename) """

quit()

# use exit stack to automatically close opened images
with contextlib.ExitStack() as stack:

    # lazily load images
    imgs = (stack.enter_context(Image.open(f))
            for f in sorted(glob.glob(fp_in)))

    # extract  first image from iterator
    img = next(imgs)

    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=0)


quit()

mg = Image.open('imgs/test.png')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

myFont = ImageFont.truetype('font/DINAlternate-Bold.ttf', 200)

# get the center of the image
width, height = img.size


y = height / 2 - 100

# add "I'm"
I1.text((width/2 - 470, y),
        "I`m", fill=(0, 181, 175), font=myFont)

# add name
I1.text((width/2 - 120, y), name,
        fill=(51, 54, 149), font=myFont)

# Display edited image
img.show()

# Save the edited image
img.save("out/test2.png")
