import rle


def compress(path, compressed_file_name):
    with open(path, 'rb') as file:
        content_file = str(file.read(), 'utf-8')
    values, counts = rle.encode(content_file)    
    print(content_file)
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

    string_compress = values_string + ", " + counts_string

    f = open(compressed_file_name, 'w')
    f.write(string_compress)
    f.close()
    return values, counts


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
    original_file_name = "example.txt"
    compressed_file_name = "example_compress.txt"
    decompressed_file_name = "example_decompress.txt"
    values, counts = compress(original_file_name, compressed_file_name)
    print(values, counts)
    string_decompress = decompress(values, counts, decompressed_file_name)
    print(string_decompress)
    
main()


