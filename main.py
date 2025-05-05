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
    num_frames = (len(bits) + bitsPerFrame -1) // bitsPerFrame

    os.makedirs(output_frames, exist_ok= True) # dir to store all PNGs ('exit_ok' so that it don't crash with existing folder)
    bit_index = 0
    # creating a blank grey scale image
    for frame_num in range(num_frames):
        frame = np.zeros((height,width), dtype=np.uint8) # here all pixels are set to 0 initially

        # here storing all bits into black or white
        for y in range(height):
            for x in range(width):
                if bit_index >= len(bits):  # checks if already encoded bits or not
                    break
                # if bit = 1 then 255 (white), else 0 
                frame[y,x] = 255 if bits[bit_index] else 0
                bit_index += 1
        # saving all those frames into 'output_frames' folder
        filename = os.path.join(output_frames,f"frame{frame_num:04d}.png")
        cv2.imwrite(filename,frame)

def make_video_from_frame(output_frame, video_name,framerate=1):
    # using FFmpeg 
    os.system(
        # calling ffmpeg via os.systems
        f"ffmpeg -framerate {framerate} -i {output_frame}/frame%04d.png"
        # libx264 use H.264 codec for video compression, pix_fmt is formatting pixels
        f"-c:v libx264 -pix_fmt yuv420p {video_name}"
    )


def main():
    filePath = input("Enter the file path: ")
    width = input("Enter the width (default = 1920)") or 1920
    height = input("Enter the height (default = 1080)") or 1080
    output_folder = input("Enter the path of output folder: ")
    video_name = input("Enter the name of video: ")
    # checks if the file exists or nawt
    if(os.path.exists(filePath)):
        print(f"Path -> {filePath}")
        print(f"Height = {height}, Width = {width}")
        print(f"Output folder is {output_folder}")
        print(f"Video name = {video_name}")

        data = read_The_File_BROOO(filePath)
        CreatingFrames(data,width,height,output_folder)
        make_video_from_frame(output_folder,video_name)
    else:
        print("Enter correct path (try adding file with extension)")

if __name__ == "__main__":
    main()