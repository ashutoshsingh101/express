from google.cloud import vision

cv2.imwrite('temp.png',crop)
image_file= io.open('temp.png','rb')
content = image_file.read()
image = vision_client.image(content=content)
s = time.time()
want = image.detect_full_text()
