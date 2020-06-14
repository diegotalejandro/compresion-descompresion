import os

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


def convert_bytes_number(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return num
        num /= 1024.0

def file_size_number(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes_number(file_info.st_size)

#----------------------------------------------------------------
total_texts = 0
total_rle = 0
for i in range(1,31):
    file_name_texts = "texts/" + str(i) + ".txt"
    file_name_rle = "rle/" + str(i) + ".txt"
    print("Nombre del archivo: " + str(i) + ".txt" + " - Tamaño del archivo original: " +
          file_size(file_name_texts) + " - Tamaño del archivo comprimido: " + file_size(file_name_rle))
    total_texts = total_texts + int(file_size_number(file_name_texts))
    total_rle = total_rle + int(file_size_number(file_name_rle))
    porcentaje = total_rle/total_texts
print("Porcentaje promedio de compresión de rle: " + str(porcentaje*100) + "%")
