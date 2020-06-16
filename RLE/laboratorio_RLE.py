import rle
from time import process_time

def compress(path, file_number):
    with open(path, 'rb') as file:
        content_file = str(file.read(), 'utf-8')
    values, counts = rle.encode(content_file)    
    values_string = "["
    for value in values[:-1]:
        values_string = values_string + "\'" + value + "\'" + ","
    else:
         values_string = values_string + "\'" + value + "\'"
    values_string = values_string + "]"

    counts_string = "["
    for count in counts[:-1]:
        counts_string = counts_string + "\'" + str(count) + "\'" + ","
    else:
        counts_string = counts_string + "\'" + str(count) + "\'"
    counts_string = counts_string + "]"

    string_compress = values_string + "," + counts_string

    f = open("rle/" + file_number + ".txt", 'w')
    f.write(string_compress)
    f.close()


def decompress(values, counts, decompressed_file_name):
    array_decompress = rle.decode(values, counts)
    string_decompress = ""
    for word in array_decompress:
        string_decompress = string_decompress + str(word)
    f = open(decompressed_file_name, 'w')
    f.write(string_decompress)
    f.close()
    return string_decompress

def main():
    time_start = process_time()
    # --------------------------------------------------------
    for i in range(1, 31):
        compress("texts/" + str(i) + ".txt", str(i))
    # --------------------------------------------------------
    time_stop = process_time()
    print("Tiempo de duración de la compresión: ",
      (time_stop-time_start)/30, " segundos.")

main()


