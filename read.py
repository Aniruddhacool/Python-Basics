#Python program to read text from the file
def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('text.txt')
