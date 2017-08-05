#client
from dcm import data_chunking_level_1
from interpreter import image_interpreter
import time


height=1200
width=1000

skip_color_start=170
skip_color_end=225

blue=0
red=0
green =0

primary_row=[12,254,165]
secondary_col=[7,255,-1]
secondary_row=[5,254,165]

image='images/test1-'

start_t = time.time()
for i in range(1,15):
        if i < 10:
                image=image+"0"+str(i)+'.png'
        else:
                image=image+str(i)+'.png'
        print(image)
        chunking = data_chunking_level_1(height,width,skip_color_start,skip_color_end)
        data_dict,gray = chunking.draw_table_on_image_file(image,primary_row,secondary_col,secondary_row)
#        interpret = image_interpreter(red,green,blue)
#        interpret.draw_table(image,data_dict)
#        print(data_dict)
        image='images/test1-'
end_t = time.time()
print("total: "+str(end_t-start_t))
# oir=optical_image_recognition()
# out=oir.crop_image(gray,data_dict)
# interpret.print_output_data(out)
