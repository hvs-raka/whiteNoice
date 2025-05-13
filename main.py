import os
import cv2
import numpy as np
import subprocess
from PIL import Image # light weight image processing tool




def printHeader():
    print("This is WhiteNoice (Data to video encoding)")
    print("Developed my me^ ^")



# function for encoding data
def encodingData(filePath,height,width,output_folder,video_name):
    data = read_The_File_BROOO(filePath)
    CreatingFrames(data,width,height,output_folder)
    make_video_from_frame(output_folder,video_name)

def read_The_File_BROOO(filePath):
    # opens file in 'rb' mode means reading file in raw binary
    with open(filePath, 'rb') as f:
        return f.read() # after reading byte-by-byte returning all bytes
    

# encrypting file bytes


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

def make_video_from_frame(output_frame, video_name,framerate=30):
    # using FFmpeg 
    command = [
        "ffmpeg",
        "-framerate", str(framerate),
        "-i", f"{output_frame}/frame%04d.png",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        video_name
    ]
    result = subprocess.run(command)


# decoding video back to original data 

def frameExtraction(video_file, output_folder):
    subprocess.run([
        "ffmpeg",
        "-i", video_file,
        f"{output_folder}/frame%04d.png"
    ])

def ReadingBits(frame_folder,width,height):
    bits = []

    for i in sorted(os.listdir(frame_folder)):
        if i.endswith('.png'):
            path = os.path.join(frame_folder,i)
            img = Image.open(path).convert('1') # convert to B&W

            for y in range(height):
                for x in range(width):
                    pixel = img.getpixel((x,y))
                    bits.append('0' if pixel == 0 else '1')
    
    return bits

def bits_to_file(bits, output_file):
    # remove extra bits if not multiple of 8
    extra_bits = len(bits) % 8
    if extra_bits:
        bits = bits[:-extra_bits]
    byte_data = bytearray()
    for i in range(0, len(bits),8):
        byte = bits[i:i+8]
        byte_str = ''.join(byte)
        byte_data.append(int(byte_str,2))
    
    with open(output_file,'wb') as f:
        f.write(byte_data)



# main function 

def main():
    printHeader()

    firstInput = int(input("Press 1 to start Encoding, 2 for Decoding: "))

    if firstInput==1:
        filePath = input("Enter the file path: ")
        width = input("Enter the width (default = 1920)") or 1920
        height = input("Enter the height (default = 1080)") or 1080
        output_folder = input("Enter the path of output folder: ")
        video_name = input("Enter the name of video(with format ex - .mp4): ")

        
        # checks if the file exists or nawt
        if(os.path.exists(filePath)):
            print(f"Path -> {filePath}")
            print(f"Height = {height}, Width = {width}")
            print(f"Output folder is {output_folder}")
            print(f"Video name = {video_name}")

            encodingData(filePath,height,width,output_folder,video_name)

        else:
            print("Enter correct path (try adding file with extension)")

    elif firstInput == 2:
        print("decoding..")
        video_file = input("Enter the path of video: ")
        frame_folder = input("Choose frame Output folder: ")
        output_file = input("Enter output file name (with extension): ")
        frame_width = input("Enter the frame width (default - 128)") or 128
        frame_height = input("Enter the frame height (default - 128)") or 128

        frameExtraction(video_file,frame_folder)
        bits = ReadingBits(frame_folder, frame_width, frame_height)
        bits_to_file(bits,output_file)

        print("Decoding Done.")


    else:
        print("Wrong input exiting.")

if __name__ == "__main__":
    main()