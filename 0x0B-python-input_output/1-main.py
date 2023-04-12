#!/usr/bin/python3

writeFile = __import__('1-write_file').write_file

nb_characters_written = writeFile("test.txt", "Holberton School is so cool!\n")
print(nb_characters_written)