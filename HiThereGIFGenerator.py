from PIL import Image, ImageSequence
from PIL import ImageDraw
from PIL import ImageFont


class GIFPart:
    def __init__(self, first: str, second: str):
        if (len(first) + len(second) > 20):
            raise ValueError(
                "The length of the first part and the second part must be less than 20 characters combined!")
        self.first = first
        self.second = second
        self.first_color = (0, 181, 175)
        self.second_color = (51, 54, 149)


class GIFGenerator:
    def __init__(self):
        self.duration = 80
        self.hold = 15
        self.max_width = 900
        self.template_file = "imgs/template.png"
        self.start_gif = "imgs/start.gif"
        self.end_gif = "imgs/end.gif"
        self.file_output = "out/test.gif"
        self.parts = []
        self.font = 'font/DINAlternate-Bold.ttf'

    def set_duration(self, duration):
        self.duration = duration

    def set_hold(self, hold):
        self.hold = hold

    def set_file_output_path(self, file_output_path):
        self.file_output_path = file_output_path

    def add_part(self, part):
        self.parts.append(part)

    def reset(self):
        self.parts = []

    def generate(self):
        if (self.parts == []):
            raise ValueError("There should be at least one part!")

        frames = []

        # add start gif
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
        for frame in ImageSequence.Iterator(Image.open(self.end_gif)):
            frame = frame.copy()
            frames.append(frame)

        frame_one = frames[0]
        frame_one.save(self.file_output, format="GIF", append_images=frames[1:],
                       save_all=True, duration=self.duration, loop=0, disposal=2)

    def generate_images(self, part: GIFPart):

        img = Image.open(self.template_file)
        I1 = ImageDraw.Draw(img)

        # adjust font size
        myFont = ImageFont.truetype(self.font, 1)
        width, height = img.size
        size_width = I1.textlength(part.first + " " + part.second, myFont)
        pt = 1
        # get the maximal font size
        while (size_width < self.max_width - 30):
            pt += 1
            myFont = ImageFont.truetype(self.font, pt)
            size_width = I1.textlength(part.first + " " + part.second, myFont)

        images = []

        y = height / 2 - \
            (I1.textbbox((0, 0), part.first + " " +
             part.second, font=myFont)[3] / 2)

        first = ""
        for char in part.first:
            img = Image.open(self.template_file)
            first += char
            I1 = ImageDraw.Draw(img)

            letters_width = I1.textlength(first, myFont)

            x = width/2 - (letters_width / 2)

            # add name
            I1.text((x, y), first,
                    fill=part.first_color, font=myFont)

            images.append(img)

        first_width = I1.textlength(first + " ", myFont)

        second = ""
        for char in part.second:
            img = Image.open(self.template_file)
            second += char
            I1 = ImageDraw.Draw(img)

            # get the center of the image
            width, height = img.size

            letters_width = I1.textlength(first + " " + second, myFont)
            x = width/2 - (letters_width / 2)

            I1.text((x, y), first,
                    fill=part.first_color, font=myFont)

            # add name
            I1.text((x + first_width, y), second,
                    fill=part.second_color, font=myFont)
            images.append(img)
        return images
