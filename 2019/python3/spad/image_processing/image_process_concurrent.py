import os
import json
from concurrent.futures import ProcessPoolExecutor, as_completed
from PIL import Image, ImageOps

def apply_mirror(img, transform_name, args):
    return ImageOps.mirror(img)

def apply_flip(img, transform_name, args):
    return ImageOps.flip(img)

def apply_rotate(img, transform_name, args):
    angle = args[0] if args else 90
    return img.rotate(angle)

def apply_resize(img, transform_name, args):
    width, height = args[0], args[1]
    return img.resize((width, height))

def apply_grayscale(img, transform_name, args):
    return img.convert('L')

transform_functions = {
    "mirror": apply_mirror,
    "flip": apply_flip,
    "rotate": apply_rotate,
    "resize": apply_resize,
    "grayscale": apply_grayscale
}

def apply_transform(img, transform_name, args):
    return transform_functions[transform_name](img, transform_name, args)

def process_image_with_all_transforms(img_path, output_dir, subfolder_name):
    """Loads an image ONCE and applies all cached transforms to it."""
    try:
        with Image.open(img_path) as img:
            base_name = os.path.splitext(os.path.basename(img_path))[0]
            target_dir = os.path.join(output_dir, subfolder_name)
            os.makedirs(target_dir, exist_ok=True)
            
            # Keep image in memory, apply every JSON transform configuration
            for json_name, transforms in _worker_transforms_cache.items():
                transformed_img = img.copy()
                for t in transforms:
                    transformed_img = apply_transform(transformed_img, t.get('transform'), t.get('arg', []))
                
                out_path = os.path.join(target_dir, f"{base_name}_{json_name}.jpg")
                transformed_img.save(out_path, quality=95)
    except Exception as e:
        print(f"Error processing image {img_path}: {e}")

def _init_worker(transform_root):
    """Runs once, in each worker process, before it pulls any tasks."""
    global _worker_transforms_cache
    cache = {}
    for fname in os.listdir(transform_root):
        if fname.endswith('.json'):
            j_name = os.path.splitext(fname)[0]
            with open(os.path.join(transform_root, fname), 'r') as f:
                cache[j_name] = json.load(f)
    _worker_transforms_cache = cache
    print(f"[worker pid={os.getpid()}] loaded {len(cache)} transform configs")

def run_optimized_multiprocessing(images_root, transform_root, output_root, max_workers=None):
    # 1. Pre-load and cache all JSON transformations into memory
    # Get the cache from via the intializer which is once per worker and not
    # per task

    # 2. Gather image paths
    image_tasks = []
    for subfolder in ['Large', 'Small']:
        folder_path = os.path.join(images_root, subfolder)
        if os.path.exists(folder_path):
            for fname in os.listdir(folder_path):
                if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                    image_tasks.append((os.path.join(folder_path, fname), subfolder))
                    
    # 3. Distribute work across processes (1 task per image, handling all 200 transforms inside)
    print(f"Starting processing for {len(image_tasks)} images across available cores...")
    # with ProcessPoolExecutor(max_workers=max_workers) as executor:
    with ProcessPoolExecutor(
        max_workers=max_workers,
        initializer=_init_worker,
        initargs=(transform_root,)) as executor:
        futures = [
            executor.submit(process_image_with_all_transforms, img_path, output_root, subfolder)
            for img_path, subfolder in image_tasks
        ]
        for future in as_completed(futures):
            future.result() # Catch any raised exceptions
    print("Batch processing complete.")

if __name__ == "__main__":
    run_optimized_multiprocessing(
        images_root="./IMAGES",
        transform_root="./TRANSFORM",
        output_root="./OUTPUT",
        max_workers=3)
