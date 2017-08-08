import PythonMagick as pm 
import os

input_pdf_name = raw_input("enter file name: ")
os.system("pdftk "+input_pdf_name+" Burst output pages/pdf_name%02d.pdf")


img = pm.Image()
img.density("500")
page_list
for page in os.listdir("pages"):
    img.read(page)
    img.write("image/"+str(page.split('.')[0])+".jpg")
	
      
