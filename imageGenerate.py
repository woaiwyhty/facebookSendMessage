from PIL import Image
import random
from random import randint
import time
import os

class imageGenerate:
    __L = []
    def __init__(self, file_dir):
        self.__L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                self.__L.append(file)

    def removeFile(self, path):
        if os.path.exists(path):
            os.remove(path)

    def imageCorp(self, img):
        width = img.size[0]
        height = img.size[1]
        if width == height:
            return img
        if width > height:
            left = int((width - height) / 2)
            img = img.crop((left, 0, left + height, height))
        else:
            left = int((height - width) / 2)
            img = img.crop((0, left, width, left + width))
        return img

    def process_profile(self):
        # open a profile picture from path
        # todo: check invalidate path
        name = random.choices(self.__L, k=4)
        picture_path = []
        for i in name:
            picture_path.append('./profilephoto/' + i)
        height = 240
        img_a = Image.open(picture_path[0])
        img_b = Image.open(picture_path[1])
        img_c = Image.open(picture_path[2])
        img_d = Image.open(picture_path[3])
        img_a = self.imageCorp(img_a)
        img_b = self.imageCorp(img_b)
        img_c = self.imageCorp(img_c)
        img_d = self.imageCorp(img_d)
        destWidth = int(img_a.size[0] * height / img_a.size[1])
        img_a = img_a.resize((destWidth, height))

        destWidth1 = int(img_b.size[0] * height / img_b.size[1])
        img_b = img_b.resize((destWidth1, height))

        destWidth2 = int(img_c.size[0] * height / img_c.size[1])
        img_c = img_c.resize((destWidth2, height))

        destWidth3 = int(img_d.size[0] * height / img_d.size[1])
        img_d = img_d.resize((destWidth3, height))


        totalWidth = max(destWidth + destWidth1, destWidth2 + destWidth3) + 10
        random_color = (randint(0, 255), randint(0, 255), randint(0, 255), 1)
        # random_color = (255, 255, 255, 1)
        img_R = Image.new('RGB', (totalWidth, height * 2 + 10), random_color)
        img_R.paste(img_a, (5, 5,  destWidth + 5, height + 5))
        img_R.paste(img_b, (destWidth + 5, 5, destWidth + destWidth1 + 5, height + 5))
        img_R.paste(img_c, (5, height + 5,  destWidth2 + 5, height + height + 5))
        img_R.paste(img_d, (destWidth2 + 5, height + 5, destWidth2 + destWidth3 + 5, height + height + 5))
        # img_R = img_R.rotate(20)
        # img_R.show()
        new_path = 'generated_profile/' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + str(random.randint(1000, 10000)) + '.png'
        img_R.save(new_path, 'JPEG')

        return new_path
        # picture_path = './profilephoto/' + name
        #
        # img_a = Image.open('./profilephoto/' + name)
        # img_a = img_a.convert('RGBA')
        #
        # size = img_a.size
        # random_color = (randint(0, 255), randint(0, 255), randint(0, 255), 1)
        # img_b = Image.new('RGBA', size, random_color)
        #
        # img = Image.blend(img_a, img_b, 0.2)
        # # img.show()
        #

        # return new_path

# print(max(10, 15))
# m_gen = imageGenerate('profilephoto')
#
# print(os.path.abspath(m_gen.process_profile()))