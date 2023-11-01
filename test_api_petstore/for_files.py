def open_file(file):
    fp = open(file, 'rb')
    files = {'file' : fp}
    return files

def close_file(file):
    file['file'].close