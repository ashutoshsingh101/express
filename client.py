#client


from dcm import data_chunking_level_1
from interpreter import image_interpreter
from oir import optical_image_recognition
import time
import PythonMagick as pm 
import os

height=1200
width=1000

skip_color_start=170
skip_color_end=225

blue=0
red=0
green =0

primary_row=[9,254,165]
secondary_col=[8,255,-1]
secondary_row=[5,254,165]

chunking = data_chunking_level_1(height,width,skip_color_start,skip_color_end)
interpret = image_interpreter(red,green,blue)
oir=optical_image_recognition()
out_final=[]
horizontal_chunks = []

input_pdf_name = raw_input("enter file name: ")
os.system("pdftk "+input_pdf_name+" Burst output pages/pdf_name%02d.pdf")


img = pm.Image()
img.density("500")

for page in os.listdir("pages"):
    if page.endswith(".pdf"):
        img.read("pages/"+page)
        img.write("image/"+str(page.split('.')[0])+".jpg")


for item in os.listdir("image"):
    if item.endswith(".jpg") or item.endswith(".png"):
        image = "image/"+item
    

        start_t = time.time()
        data_dict,gray,horizontal_chunk_index= chunking.draw_table_on_image_file(image,primary_row,secondary_col,secondary_row)
        # horizontal_chunk_index, gray = chunking.draw_row_chunks_on_image_file(image,primary_row)
        horizontal_chunks.append(horizontal_chunk_index)
        # interpret.draw_primary_row_chunks(image,height,width,horizontal_chunk_index)
        # interpret.draw_table(image,data_dict)
        out=oir.crop_image(gray,data_dict)
        out_final.append(out)
        interpret.print_output_data(out)
    end_t = time.time()
print("total: "+str(end_t-start_t))
# print(out_final)
# print(horizontal_chunks)



