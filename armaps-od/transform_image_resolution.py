from PIL import Image
import os
import argparse
def rescale_images(directory, size):
    for img in os.listdir(directory):
        im = Image.open(directory+img)
        im = im.rotate(-90, expand=True)
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(directory+img)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Image size')
    args = parser.parse_args()

    directories = [x[0] for x in os.walk(args.directory)] 

    for directory in directories[1:]:   
        rescale_images(directory+"/", args.size)