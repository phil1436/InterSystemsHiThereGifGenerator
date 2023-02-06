from PIL import Image, ImageSequence
from PIL import ImageDraw
from PIL import ImageFont
import os
import sys

VERSION = "0.0.1"

template_file = "imgs/template.png"
start_gif = "imgs/start.gif"
end_gif = "imgs/end.gif"
duration = 70
file_output_path = "out"

print("""
      *******************************************
      **** InterSystems-HiThere-GIFGenerator ****
      *******************************************
      """)

# check for arguments
for i in range(len(sys.argv)):
    if (sys.argv[i] == "-v" or sys.argv[i] == "-version"):
        print("Version: " + VERSION)
        quit()
    if (sys.argv[i] == "-d" or sys.argv[i] == "-duration"):
        duration = int(sys.argv[i+1])
        print("Duration: " + str(duration))

# get name from user
name = input("Enter your name: ")

# check if name is beween 2 and 10 characters
while (len(name) < 2 or len(name) > 10):
    print("Please enter a name between 2 and 10 characters")
    name = input("Enter your name: ")

print("Generating GIF", end="")


name_width = len(name) * 150
im_width = 150
total_width = name_width + im_width
max_width = 900

# 1px = 3/4pt

letters = 3  # "I'm"
for char in name:
    if char.isupper():
        letters += 1
    elif char in ["I", "i", "l", "!", "t", "r", "j"]:
        letters += 0.5
    else:
        letters += 1
pt = 20
# set font
myFont = ImageFont.truetype('font/DINAlternate-Bold.ttf', pt)

img = Image.open(template_file)

I1 = ImageDraw.Draw(img)

size_width = I1.textlength("I'm " + name, myFont)
while (size_width < max_width - 30):
    pt += 1
    myFont = ImageFont.truetype('font/DINAlternate-Bold.ttf', pt)
    size_width = I1.textlength("I'm " + name, myFont)

px_per_letter = int(size_width / letters)

print("size_width: " + str(size_width))
# test image

img = Image.open(template_file)
I1 = ImageDraw.Draw(img)


# get the center of the image
width, height = img.size

y = height / 2 - 100

# add name
I1.text((200, y), "I'm",
        fill=(0, 181, 175), font=myFont)

I1.text((200 + (3 * px_per_letter), y), name,
        fill=(51, 54, 149), font=myFont)

filename = "out/test.png"
img.save(filename)

# end test
filenames = []
name_frames = []


# iterate through each character in name
name_part = ""
im_part = ""
counter = 1

# ad "I'm"
for char in ["I", "'", "m"]:
    img = Image.open(template_file)
    im_part += char
    I1 = ImageDraw.Draw(img)

    # get the center of the image
    width, height = img.size

    letters_width = I1.textlength(im_part, myFont)

    y = height / 2 - 100
    x = width/2 - (letters_width / 2)

    # add name
    I1.text((x, y), im_part,
            fill=(0, 181, 175), font=myFont)

    filename = "out/Im"+str(counter)+".png"
    filenames.append(filename)
    # Save the edited image
    img.save(filename)
    name_frames.append(Image.open(filename))
    counter += 1

print(".", end="")

counter = 1

im_width = I1.textlength("I'm ", myFont)

# add name
for char in name:
    img = Image.open(template_file)
    name_part += char
    I1 = ImageDraw.Draw(img)

    # get the center of the image
    width, height = img.size

    letters_width = I1.textlength("I'm " + name_part, myFont)
    y = height / 2 - 100
    x = width/2 - (letters_width / 2)

    # add "I'm"
    I1.text((x, y), "I`m",
            fill=(0, 181, 175), font=myFont)

    # add name
    I1.text((x + im_width, y), name_part,
            fill=(51, 54, 149), font=myFont)

    filename = "out/name"+str(counter)+".png"
    filenames.append(filename)
    # Save the edited image
    img.save(filename)
    name_frames.append(Image.open(filename))
    counter += 1

print(".", end="")

name_frames_inverted = name_frames[::-1]
frames = []

# add start gif
for frame in ImageSequence.Iterator(Image.open(start_gif)):
    frame = frame.copy()
    frames.append(frame)

print(".", end="")

# add name frames
for frame in name_frames:
    frames.append(frame)

# hold name for 10 frames
for i in range(0, 10):
    frames.append(frames[-1])

# add inverted name frames
for frame in name_frames_inverted:
    frames.append(frame)

# add end gif
for frame in ImageSequence.Iterator(Image.open(end_gif)):
    frame = frame.copy()
    frames.append(frame)

print(".", end="")

# filepaths
fp_out = file_output_path+"/HiThereIm"+name+".gif"

# generate gif
frame_one = frames[0]
gif = frame_one.save(fp_out, format="GIF", append_images=frames[1:],
                     save_all=True, duration=duration, loop=0, disposal=2)

print(".")


frames = None
frames_inverted = None

# delete generated images
for filename in filenames:
    os.remove(filename)

print("GIF Generated!")
print("You can find it here: " + fp_out)
print("")
print("by phil1436")
