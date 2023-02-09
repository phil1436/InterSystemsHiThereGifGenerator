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
max_height = 270
font = 'font/DINAlternate-Bold.ttf'
run_custom_mode = False

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
    if (sys.argv[i] == "-c" or sys.argv[i] == "-custom"):
        run_custom_mode = True
        print("***Custom Mode***")


# generate gif
generator = HTGIFGenerator(path_to_background_image=template_file,
                           start_gif=start_gif,
                           end_gif=end_gif)
generator.set_duration(duration)
generator.set_hold(hold)
generator.set_max_width(max_width)
generator.set_max_height(max_height)
generator.set_default_font(font)

if not run_custom_mode:
    # get name from user
    name = input("Enter your name: ")

    # check if name is beween 2 and 10 characters
    while (len(name) < 2 or len(name) > 15):
        print("Please enter a name between 2 and 15 characters")
        name = input("Enter your name: ")
    # filepaths
    fp_out = file_output_path+"/HiThereIm"+name+".gif"

    generator.set_file_output(fp_out)

    generator.add_default_part("Hi", "There!")
    generator.add_default_part("I'm", name)
else:
    counter = 1
    fp_out = file_output_path+"/"
    while (True):
        print("Part " + str(counter))
        first = input("Enter first text (empty to stop): ")
        if first == "":
            break
        second = input("Enter second text (can be empty): ")

        if counter == 1:
            fp_out = fp_out + first + second + ".gif"
            generator.set_file_output(fp_out)

        if second == "":
            second = None
        generator.add_default_part(first, second)
        counter += 1

generator.generate()

print("GIF Generated!")
print("You can find it here: " + fp_out)
print("")
print("by phil1436")
