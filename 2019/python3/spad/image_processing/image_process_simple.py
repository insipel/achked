#!/usr/bin/python3

import os
import json
from PIL import Image, ImageOps

class ImageProcess:
    def __init__(self, image_path:str, json_path:str, output_path:str):
        self.image_path = image_path
        self.json_path = json_path
        self.output_path = output_path
        self.transformers = {
            "mirror": self.apply_mirror,
            "flip": self.apply_flip,
            "rotate": self.apply_rotate,
            "grayscale": self.apply_grayscale,
            "resize": self.apply_resize
        }

    def apply_mirror(self, img, transform, args):
        print(f"applying mirror")
        return ImageOps.mirror(img)

    def apply_flip(self, img, transform, args):
        print(f"applying flip")
        return ImageOps.flip(img)

    def apply_rotate(self, img, transform, args):
        print(f"applying rotate")
        angle = args[0] if args else 90
        return img.rotate(angle, expand=True)

    def apply_grayscale(self, img, transform, args):
        print(f"applying grayscale")
        return img.convert('L')

    def apply_resize(self, img, transform, args):
        print(f"applying resize")
        width, height = args[0], args[1]
        return img.resize((width, height))

    def apply_one_transform(self, img, transform, args):
        return(self.transformers[transform](img, transform, args))

    def transform_single_image(self, image_file, json_file):
        try:
            with Image.open(image_file) as img:
                with open(json_file, "r") as jf:
                    transforms = json.load(jf)
                
                transformed_img = img.copy()
                for transform in transforms:
                    t = transform.get('transform')
                    args = transform.get('arg', [])
                    transformed_img = self.apply_one_transform(transformed_img, t, args)
                
                os.makedirs(self.output_path, exist_ok=True)
                base_name = os.path.splitext(os.path.basename(image_file))[0]
                json_name = os.path.splitext(os.path.basename(json_file))[0]
                out_file = os.path.join(self.output_path, f"{base_name}_{json_name}_out.jpg")
                print(f"output file:{out_file}")
                transformed_img.save(out_file)
        except Exception as e:
            print(f"Error processing {image_file} with {json_file}, exception:{e}")

    def process_transformation(self, image_files, json_files):
        for image_file in image_files:
            for json_file in json_files:
                self.transform_single_image(image_file, json_file)

    def run(self):
        image_files = []
        json_files = []
        for subfolder in ["Large", "Small"]:
            image_path = os.path.join(self.image_path, subfolder)
            if not os.path.exists(image_path):
                continue
            for f in os.listdir(image_path):
                if f.lower().endswith((".jpg", ".png")):
                    image_files.append(os.path.join(image_path, f))
                    print(f"image filename:{image_files[-1]}")
        if not os.path.exists(self.json_path):
            return           
        for f in os.listdir(self.json_path):
            if f.lower().endswith((".json")):
                json_files.append(os.path.join(self.json_path, f))
                print(f"json filename:{json_files[-1]}")
        self.process_transformation(image_files, json_files)

if __name__ == "__main__":
    print(f"Starting main")
    image_processor = ImageProcess("./IMAGES", "./TRANSFORM", "./OUTPUT")
    image_processor.run()
