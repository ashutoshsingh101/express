#client


from dcm import data_chunking_level_1
from interpreter import image_interpreter
from oir import optical_image_recognition
import time
import PythonMagick as pm 
import os
from mine import primary_search,secondary_search
height=1200
width=1000

skip_color_start=170
skip_color_end=225

blue=0
red=255
green =0

primary_row=[9,254,165]
secondary_col=[8,255,-1]
secondary_row=[8,255,165]


key_word_name = 'patient name'
key_word_test_start = 'test name'
key_word_test_end = 'please correlate'

index_of_name_chunk = 2
index_of_test_start_idetifier = 3
index_of_test_end_idetifier = index_of_test_start_idetifier+2

identifier_row_name = 3
identifier_column_name= 2


identifier_row_test = 2
identifier_column_test= 2


name_data = []
test_data = []

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
	os.remove("pages/"+page)


for item in os.listdir("image"):
    if item.endswith(".jpg") or item.endswith(".png"):
        image = "image/"+item
    

        #start_t = time.time()
        data_dict,gray,horizontal_chunk_index= chunking.draw_table_on_image_file(image,primary_row,secondary_col,secondary_row)
        # horizontal_chunk_index, gray = chunking.draw_row_chunks_on_image_file(image,primary_row)
        horizontal_chunks.append(horizontal_chunk_index)
        # interpret.draw_primary_row_chunks(image,height,width,horizontal_chunk_index)
        # interpret.draw_table(image,data_dict)
        out=oir.crop_image(gray,data_dict)
        out_final.append(out)
        # interpret.print_output_data(out)
        find_start = primary_search()
        data_list  = find_start.clean_data(out.tolist())
        name_start_index = find_start.data_division_start(data_list,key_word_name, index_of_name_chunk, identifier_row_name ,identifier_column_name)
        print('name:'+str(name_start_index))

        test_start_index = find_start.data_division_start(data_list,key_word_test_start, index_of_test_start_idetifier, identifier_row_test, identifier_column_test)
        print('test:'+str(test_start_index))

        secondary_divide = secondary_search()
        divided_data_name = secondary_divide.secondary_division(name_start_index,test_start_index,data_list)

        test_end_index = len(data_list)
        print('end:'+str( test_end_index))

        test_data.append(data_list[test_start_index:len(data_list)])
        os.remove("image/"+item)
# #        end_t = time.time()
# # print("total: "+str(end_t-start_t))
# # print(out_final)
# # print(horizontal_chunks)

print(name_data)
print(test_data)
