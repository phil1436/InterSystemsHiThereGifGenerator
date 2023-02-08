from PIL import Image, ImageSequence
from PIL import ImageDraw
from PIL import ImageFont


class HTGIFPart:
    def __init__(self, path_to_font_ttf: str, first: str, second: str = None):
        self.first = first
        self.second = second
        self.first_color = (0, 181, 175)
        self.second_color = (51, 54, 149)
        self.font = path_to_font_ttf

    # change the color of the first part
    def set_first_color(self, color):
        self.first_color = color

    # change the color of the second part
    def set_second_color(self, color):
        self.second_color = color

    # toString
    def to_string(self):
        if (self.second == None):
            return self.first
        return self.first + " " + self.second


class HTGIFGenerator:
    def __init__(self, path_to_background_image: str, file_output: str = None, start_gif: str = None, end_gif: str = None):
        self.duration = 80
        self.hold = 15
        self.background = path_to_background_image
        width, height = Image.open(path_to_background_image).size
        self.max_width = width
        self.start_gif = start_gif
        self.end_gif = end_gif
        if (file_output == None):
            self.file_output = "HiThere.gif"
        else:
            self.file_output = file_output
        self.parts = []

    # change the duration of the gif
    def set_duration(self, duration: int):
        self.duration = duration

    # change the hold time
    def set_hold(self, hold: int):
        self.hold = hold

    # change the output file
    def set_file_output(self, file_output_path: str):
        self.file_output = file_output_path

    # change the start gif
    def set_start_gif(self, start_gif_path: str):
        self.start_gif = start_gif_path

    # change the end gif
    def set_end_gif(self, end_gif_path: str):
        self.end_gif = end_gif_path

    # change the max width of the text
    def set_max_width(self, max_width: int):
        self.max_width = max_width

    # add a part to the gif
    def add_part(self, part: HTGIFPart):
        self.parts.append(part)

    # reset the parts
    def reset(self):
        self.parts = []

    # generate the gif
    def generate(self):
        if (self.parts == []):
            raise ValueError("There should be at least one part!")

        frames = []

        # add start gif
        if (self.start_gif != None):
            for frame in ImageSequence.Iterator(Image.open(self.start_gif)):
                frame = frame.copy()
                frames.append(frame)

        # add the parts
        for parts in self.parts:
            part_imgs = self.generate_images(parts)

            # add start part
            for img in part_imgs:
                frames.append(img)
            # add hold
            for i in range(self.hold):
                frames.append(part_imgs[-1])
            # add end part
            for img in part_imgs[::-1]:
                frames.append(img)

        # add start gif
        if (self.end_gif != None):
            for frame in ImageSequence.Iterator(Image.open(self.end_gif)):
                frame = frame.copy()
                frames.append(frame)

        frame_one = frames[0]
        frame_one.save(self.file_output, format="GIF", append_images=frames[1:],
                       save_all=True, duration=self.duration, loop=0, disposal=2)

    # generate the images for a part
    def generate_images(self, part: HTGIFPart):

        img = Image.open(self.background)
        I1 = ImageDraw.Draw(img)

        # adjust font size
        myFont = ImageFont.truetype(part.font, 1)
        width, height = img.size
        size_width = I1.textlength(part.to_string(), myFont)
        pt = 1
        # get the maximal font size
        while (size_width < self.max_width - 30):
            pt += 1
            myFont = ImageFont.truetype(part.font, pt)
            size_width = I1.textlength(part.to_string(), myFont)

        images = []

        y = height / 2 - \
            (I1.textbbox((0, 0), part.to_string(), font=myFont)[3] / 2)

        first = ""
        for char in part.first:
            img = Image.open(self.background)
            first += char
            I1 = ImageDraw.Draw(img)

            letters_width = I1.textlength(first, myFont)

            x = width/2 - (letters_width / 2)

            I1.text((x, y), first,
                    fill=part.first_color, font=myFont)

            images.append(img)

        first_width = I1.textlength(first + " ", myFont)

        if (part.second == None):
            return images

        second = ""
        for char in part.second:
            img = Image.open(self.background)
            second += char
            I1 = ImageDraw.Draw(img)

            # get the center of the image
            width, height = img.size

            letters_width = I1.textlength(first + " " + second, myFont)
            x = width/2 - (letters_width / 2)

            I1.text((x, y), first,
                    fill=part.first_color, font=myFont)

            I1.text((x + first_width, y), second,
                    fill=part.second_color, font=myFont)
            images.append(img)
        return images
