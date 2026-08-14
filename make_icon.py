from app import create_image

image = create_image()
image.save("icon.ico", format="ICO", sizes=[(16,16), (32,32), (64,64)])