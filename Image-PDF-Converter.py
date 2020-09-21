from fpdf import FPDF
import glob
from pdf2image import convert_from_path



pages = convert_from_path('toconvert.pdf', 500)



pdf = FPDF()
imagelist = glob.glob('images/*.png')



pdf.add_page()
x=0
y=0
scale = 0.47
width, height = float(297*scale), float(210*scale)

for image in imagelist:
    if(y <= 280):
        pdf.image(image, x, y , width, height)

    else:
        pdf.add_page()
        y = 0
        pdf.image(image, x, y, width, height)

    y = y + float(210*scale)

pdf.output("yourfile.pdf", "F")
