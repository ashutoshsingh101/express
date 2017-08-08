from dynamic_graph.sot.dynamics.dynamic import Dynamic
from wand.image import Image
from PIL import Image as Img

with Image(filename="pages/101.pdf") as img:
	img.save("pages/1.jpg")
