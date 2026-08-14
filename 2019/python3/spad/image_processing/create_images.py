#!/usr/bin/python3
import sys
print("Python executable being used:", sys.executable)

import os
import json
from PIL import Image

# 1. Create the directory layout
os.makedirs("IMAGES/Large", exist_ok=True)
os.makedirs("IMAGES/Small", exist_ok=True)
os.makedirs("TRANSFORM", exist_ok=True)

# 2. Generate sample Large/Small images (800x600 pixels, solid blue)
color_list = ['blue', 'red', 'green', 'white', 'black',
              'cyan', 'yellow', 'orange', 'pink', 'brown']
for i in range(10):
    img_large = Image.new('RGB', (800, 600), color=color_list[i])
    img_large.save(f"IMAGES/Large/sample_large_{i}.jpg")

    # 3. Generate a sample Small image (200x200 pixels, solid green)
    img_small = Image.new('RGB', (200, 200), color=color_list[i])
    img_small.save(f"IMAGES/Small/sample_small_{i}.jpg")

# 4. Create Sample JSON Transform File 1: Grayscale and Resize
transforms_1 = [
    {"transform": "grayscale", "arg": []},
    {"transform": "resize", "arg": [100, 100]}
]
with open("TRANSFORM/config_grayscale_resize.json", "w") as f:
    json.dump(transforms_1, f, indent=4)

# 5. Create Sample JSON Transform File 2: Rotate and Mirror
transforms_2 = [
    {"transform": "rotate", "arg": [90]},
    {"transform": "mirror", "arg": []}
]
with open("TRANSFORM/config_rotate_mirror.json", "w") as f:
    json.dump(transforms_2, f, indent=4)

print("Sample folders, images, and JSON transform files created successfully!")