#-*- coding: utf-8 -*-

def strip(strtemp):
    return strtemp.strip()

while True:
    judge = raw_input('After file processing,you want to create a new file (Y), or overwrite it (N) :(Y/N)')
    if judge.lower() == 'y':
        with open('/tmp/file_11_new','w') as newfile:
            with open('/tmp/file_11') as oldfile:
                lines = oldfile.readlines()
                for line in map(strip,lines):
                    newfile.write(repr(line))
                    newfile.write('\n')
    else:
        with open('/tmp/file_11') as oldfile:
            lines = oldfile.readlines()
        with open('/tmp/file_11','w') as oldfile:
            for line in map(strip,lines):
                oldfile.write(repr(line))
                oldfile.write('\n')