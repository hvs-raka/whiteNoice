import os
import cv2
import numpy as np


def read_The_File_BROOO(filePath):
    # opens file in 'rb' mode means reading file in raw binary
    with open(filePath, 'rb') as f:
        return f.read() # after reading byte-by-byte returning all bytes

def bytesToBits(byte):
    return[(byte >> i) & 1 for i in reversed(range(8))] # converting bytes to bits

# Encryption function will be added here

def CreatingFrames(data,width,height,output_frames):
    bits = [] # list of bits
    for byte in data:
        bits.extend(bytesToBits(byte)) # for every byte converted append bits into bits list
    bitsPerFrame = height * width
    numOfFrames = (len(bits) + bitsPerFrame -1) // bitsPerFrame

    os.makedirs(output_frames, exist_ok= True) # dir to store all PNGs ('exit_ok' so that it don't crash with existing folder)
    bit_index = 0


    # exhausted sleeping ...ZZZZZZ..ZZZZ



def main():
    filePath = input("Enter the file path: ")
    width = input("Enter the width ()")
    # checks if the file exists or nawt
    if(os.path.exists(filePath)):
        print("Path -> " + filePath)
    else:
        print("Enter correct path (try adding file with extension)")

if __name__ == "__main__":
    main()