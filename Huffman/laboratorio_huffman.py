import sys
import os
import argparse
from HuffmanCoding import HuffmanCoding
import base64
from time import process_time
string_entrada = [
    zkncdmqafvewfqqwvftr,
    bydimeiddjncrvwahrxk,
    ejunnkwykphqeftguetc,
    wgnedmhdqcnthmxmaeih,
    ncucwiffwtzpzxnjryif,
    qyfrhgzdcirigmjviygq,
    jnmmqinxfvpkhnaacbfj,
    frnbmhxmjurqahxnuvqd,
    xjjcqbiqcwvrdqimrntt,
    dzvceqehcnkwpikmjizr,
    pazfvdujarttiqhteqeu,
    ptiuacatembkikmnjcpg,
    ubquwvrgfpmybdgyqxjt,
    crmbmpcxgunzdhgappxf,
    cadvcnpurjegkhbanhqe,
    xmjphxjgtkbqcpztyzex,
    cafddrnmbrkfefwfnbij,
    bbcdgpewhbxczptxxung,
    cczzetgbkkxukbgbaxum,
    iinqgcwfjuqpgiizrepn,
    mrububyyfnyumxmiquxg,
    qfbqvfzbmakwadcpjawe,
    ihuuzahpymjwuwecgvub,
    ekccrwnpqmmtuxeqmdty,
    xigjjpjivjtetepexdiy,
    akkgzttvqqmkzfxvzxhr,
    upwgqukarcvmyiyjnthg,
    zrqhnhdxkwxagpdirnhw,
    dzkxapxjabtmirggugav,
    ktueybhjxcgpymazdqkb]
def file_to_string(path):
    string = ""
    with open(path, 'rb') as file:
        content_file = file.read()        
        #base64_content_file = base64.b64encode(content_file)
        #string_img = string_img + base64_content_file.decode("utf-8")
    return content_file

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


def compress_string(file_name):
    h = HuffmanCoding(file_name)
    h.compress()
    #output_path = h.compress()
    #h.decompress(output_path)

time_start = process_time()
#--------------------------------------------------------
file_name = sys.argv[1]
if os.path.exists(file_name):    
    compress_string(file_name)
#--------------------------------------------------------
time_stop = process_time()
print("Tiempo de duración del programa: ", time_stop-time_start, " segundos.")
