from PIL import Image
import uuid
from os.path import abspath


def convert_mcd_skin_format(ImagePath, SkinFormat):
    img = Image.open(ImagePath)
    img = img.convert("RGBA")

    if img.width != 64:
        return False
    if img.height != 64:
        return False

    img2 = img.crop((16, 0, 24, 8))
    img2 = img2.rotate(180)
    img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(img2, (16, 0, 24, 8))

    img2 = img.crop((48, 0, 56, 8))
    img2 = img2.rotate(180)
    img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(img2, (48, 0, 56, 8))

    img2 = img.crop((24, 8, 32, 16))
    img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(img2, (24, 8, 32, 16))

    img2 = img.crop((56, 8, 64, 16))
    img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(img2, (56, 8, 64, 16))

    img3 = img.crop((8, 8, 16, 16))

    img4 = img.crop((40, 8, 48, 16))
    img3.alpha_composite(img4, (0, 0))
    img.alpha_composite(img3, (56, 20))

    if SkinFormat == 'Classic':
        # convert slim1
        img5 = img.crop((45, 20, 53, 32))
        img.paste(img5, (44, 20, 52, 32))

        img6 = img.crop((53, 21, 56, 32))
        img.paste(img6, (51, 21, 54, 32))

        img7 = Image.new("RGBA", (2, 12))
        img.paste(img7, (54, 20))

        img8 = img.crop((49, 17, 51, 20))
        img.paste(img8, (48, 17, 50, 20))

        img9 = Image.new("RGBA", (2, 4))
        img.paste(img9, (50, 16))
        # 2
        img5 = img.crop((45, 37, 53, 48))
        img.paste(img5, (44, 37, 52, 48))

        img6 = img.crop((53, 37, 56, 48))
        img.paste(img6, (51, 37, 54, 48))

        img7 = Image.new("RGBA", (2, 12))
        img.paste(img7, (54, 36))

        img8 = img.crop((49, 33, 51, 36))
        img.paste(img8, (48, 33, 50, 36))

        img9 = Image.new("RGBA", (2, 4))
        img.paste(img9, (50, 32))
        # 3
        img5 = img.crop((40, 53, 44, 64))
        img.paste(img5, (39, 53, 43, 64))

        img6 = img.crop((44, 53, 48, 64))
        img.paste(img6, (43, 53, 47, 64))

        img7 = Image.new("RGBA", (2, 12))
        img.paste(img7, (46, 52))

        img8 = img.crop((41, 49, 44, 52))
        img.paste(img8, (40, 49, 43, 52))

        img9 = Image.new("RGBA", (2, 4))
        img.paste(img9, (42, 48))
        # 4
        img5 = img.crop((53, 53, 60, 64))
        img.paste(img5, (52, 53, 59, 64))

        img6 = img.crop((61, 53, 64, 64))
        img.paste(img6, (59, 53, 62, 64))

        img7 = Image.new("RGBA", (2, 12))
        img.paste(img7, (62, 52))

        img8 = img.crop((57, 49, 60, 52))
        img.paste(img8, (56, 49, 59, 52))

        img9 = Image.new("RGBA", (2, 4))
        img.paste(img9, (58, 48))
        # end
    # flip
    img10 = img.crop((16, 52, 28, 64))
    img10 = img10.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(img10, (16, 52))

    img12 = img.crop((28, 53, 32, 64))
    img12 = img12.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(img12, (28, 53, 32, 64))
    #2
    img10 = img.crop((0, 20, 12, 32))
    img10 = img10.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(img10, (0, 20))

    img12 = img.crop((12, 20, 16, 32))
    img12 = img12.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(img12, (12, 20))
    #3
    img13 = img.crop((20, 48, 24, 52))

    img14 = img.crop((24, 48, 28, 52))

    img.paste(img13, (24, 48))
    img.paste(img14, (20, 48))
    # 4
    img15 = img.crop((4, 16, 8, 20))
    img16 = img.crop((8, 16, 12, 20))
    img15 = img15.rotate(180)
    img15 = img15.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(img15, (8, 16))
    img.paste(img16, (4, 16))

    # 5
    img17 = img.crop((4, 32, 8, 36))
    img17 = img17.rotate(180)
    img.paste(img17, (4, 32))

    # 6
    img18 = img.crop((0, 16, 16, 32))
    img19 = img.crop((16, 48, 32, 64))
    img.paste(img18, (16, 48))
    img.paste(img19, (0, 16))
    img_name = str(uuid.uuid4()) + '.png'
    img.save(img_name)
    return abspath(img_name)
