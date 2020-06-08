from HuffmanCoding import HuffmanCoding
import base64
from time import process_time

def img_to_base64(path):
    string_img = ""
    with open(path, 'rb') as file_img:
        content_file = file_img.read()
        base64_content_file = base64.b64encode(content_file)
        string_img = string_img + base64_content_file.decode("utf-8")
    return string_img

def base64_to_img(path, img_name):
    with open(path, 'rb') as file_img:
        string_img = file_img.read()
    content_file = base64.b64decode(string_img)
    with open(img_name, 'wb') as f:
        f.write(content_file)

def write_string_in_a_file(string, file_name):
    f = open(file_name, 'w')
    f.write(string)
    f.close()


def compress_and_decompress_img(file_name):
    h = HuffmanCoding(file_name)
    output_path = h.compress()
    h.decompress(output_path)

time_start = process_time()
#--------------------------------------------------------
original_img_name = 'img_1_1.jpg'
file_name = 'temp_file.txt'
file_name_decompressed = "temp_file_decompressed.txt"
img_name_decompressed = "img_decompressed.png"

string_img = img_to_base64(original_img_name)
write_string_in_a_file(string_img, file_name)
compress_and_decompress_img(file_name)
base64_to_img(file_name_decompressed, img_name_decompressed)
#--------------------------------------------------------
time_stop = process_time()
print("Tiempo de duración del programa: ", time_stop-time_start, " segundos.")
