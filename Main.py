import sys
from HiThereGIFGenerator import HTGIFGenerator, HTGIFPart

VERSION = "0.0.2"

print("""
      *******************************************
      **** InterSystems-HiThere-GIFGenerator ****
      *******************************************
      """)

template_file = "imgs/template.png"
start_gif = "imgs/start.gif"
end_gif = "imgs/end.gif"
file_output_path = "out"
duration = 80
hold = 15
max_width = 900
max_height = 270
font = 'DINAlternate-Bold.ttf'
run_custom_mode = False
whitespace = " "
add_hashtag = False

# check for arguments
for i in range(len(sys.argv)):
    arg = sys.argv[i].lower()
    if (arg == "-v" or arg == "-version"):
        print("Version: " + VERSION)
        print("")
        print("by phil1436")
        quit()
    if (arg == "-help"):
        print("""
              
    Configurations:
    
    [-v|-version] - show version
    [-h|-hold] [int] - set the hold time
    [-d|-duration] [int] - set the duration time
    [-o|-output] [path] - set the output path
    [-f|-font] [path_to_ttf_file] - set the font, by referencing a ttf file
    [-c|-custom] - run in custom mode
    [-w|-whitespaces|-whitespace] [on|off] - set if whitespaces should be used
    [-hashtag|-itisnotjustajob] - adds the hashtag #ItIsNotJustAJob to the end of the gif
              """)
        print("")
        print("by phil1436")
        quit()
    if (arg == "-d" or arg == "-duration"):
        duration = int(sys.argv[i+1])
        print("Duration: " + str(duration))
    if (arg == "-h" or arg == "-hold"):
        hold = int(sys.argv[i+1])
        print("Hold: " + str(hold) + " frames")
    if (arg == "-o" or arg == "-output"):
        file_output_path = sys.argv[i+1]
        print("Output: " + file_output_path)
    if (arg == "-c" or arg == "-custom"):
        run_custom_mode = True
        print("***Custom Mode***")
    if (arg == "-w" or arg == "-whitespaces" or arg == "-whitespace"):
        if (sys.argv[i+1].lower() == "off"):
            whitespace = ""
            print("Whitespaces: off")
        else:
            print("Whitespaces: on")
    if (arg == "-hashtag" or arg == "-itisnotjustajob"):
        add_hashtag = True
    if (arg == "-f" or arg == "-font"):
        font = sys.argv[i+1]


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

    generator.add_default_part("Hi" + whitespace, "There!")
    generator.add_default_part("I'm" + whitespace,  name)
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
        generator.add_default_part(first + whitespace, second)
        counter += 1

if (add_hashtag):
    generator.add_default_part("#ItIsNot", "JustAJob")


generator.generate()

print("GIF Generated!")
print("You can find it here: " + fp_out)
print("")
print("by phil1436")
