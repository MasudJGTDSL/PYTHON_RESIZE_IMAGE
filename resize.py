from PIL import Image, ImageFile
import os, sys
ImageFile.LOAD_TRUNCATED_IMAGES = True

#! To Run: python resize.py 
#* TODO: in resize function image_width must be provide as requirement! 

class ResizeImage():

    def __init__(self, image_width, path, result_path):
        self.image_width = image_width
        self.path = path
        self.result_path = result_path
        self.total_image = 0
        self.resize()
    
    def resize(self):
        for imageName in os.listdir(self.path):
            self.total_image += 1
            image = Image.open(self.path+imageName)
            new_image_height = int(self.image_width*(image.size[1]/image.size[0]))
            image = image.convert('RGB')
            imageResize = image.resize((self.image_width,new_image_height), Image.LANCZOS)
            imageResize.save(self.result_path + imageName, 'JPEG', quality=90)

        print(f"Total number of image processed: {self.total_image} Nos.")


path = r"./images/"
result_path = r"./resized_images/"

if __name__ == '__main__': 
    img = ResizeImage(200, path, result_path) 