from io import StringIO
from PIL import Image
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO


im = BytesIO.generate_image("original_img.jpg")
out = BytesIO()
im.save(out, format=format, quality=100)
out.seek(0)




# img_name = "original_img.jpg"
# quality = 100
# original_img = Image.open(img_name)
# buffer = StringIO.StringIO()
# original_img.save(buffer, "JPEG", quality=quality)
# with open("./compressed_img_" + quality +".jpg", "w") as handle:
#     handle.write(buffer.contents())
