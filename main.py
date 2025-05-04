import os
import cv2
import numpy as np


def read_The_File_BROOO(filePath):
    with open(filePath, 'rb') as f:
        return f.read()


def main():
    filePath = input("Enter the file path: ")
    # checks if the file exists or nawt
    if(os.path.exists(filePath)):
        print("Path -> " + filePath)
    else:
        print("Enter correct path (try adding file with extension)")

if __name__ == "__main__":
    main()