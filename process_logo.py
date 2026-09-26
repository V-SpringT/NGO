from PIL import Image

def remove_white_bg(input_path, output_path, threshold=220):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Change all white (also shades of white)
        # to transparent
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    
    # Crop to bounding box of non-transparent pixels to make it as large as possible
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(output_path, "PNG")
    print(f"Processed {input_path} -> {output_path}")

remove_white_bg(r"d:\Ke hoạch bạc tỷ\NGO\assets\images\logo.png", r"d:\Ke hoạch bạc tỷ\NGO\assets\images\logo.png")
