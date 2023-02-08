import sys
from HiThereGIFGenerator import HTGIFGenerator, HTGIFPart

VERSION = "0.0.1"

template_file = "imgs/template.png"
start_gif = "imgs/start.gif"
end_gif = "imgs/end.gif"
file_output_path = "out"
duration = 80
hold = 15
max_width = 900
font = 'font/DINAlternate-Bold.ttf'

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
    if (sys.argv[i] == "-h" or sys.argv[i] == "-hold"):
        hold = int(sys.argv[i+1])
        print("Hold: " + str(hold) + " frames")
    if (sys.argv[i] == "-o" or sys.argv[i] == "-output"):
        file_output_path = sys.argv[i+1]
        print("Output: " + file_output_path)

# get name from user
name = input("Enter your name: ")

# check if name is beween 2 and 10 characters
while (len(name) < 2 or len(name) > 15):
    print("Please enter a name between 2 and 15 characters")
    name = input("Enter your name: ")

# filepaths
fp_out = file_output_path+"/HiThereIm"+name+".gif"

# generate gif
generator = HTGIFGenerator(template_file, fp_out, start_gif, end_gif)
generator.set_duration(duration)
print("Duration: " + str(duration))
generator.set_hold(hold)
generator.set_max_width(max_width)

hi_part = HTGIFPart(font, "Hi", "There!")
name_part = HTGIFPart(font, "I'm", name)

generator.add_part(hi_part)
generator.add_part(name_part)
generator.generate()

print("GIF Generated!")
print("You can find it here: " + fp_out)
print("")
print("by phil1436")
