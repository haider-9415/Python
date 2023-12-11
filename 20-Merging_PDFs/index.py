from glob import glob
from pikepdf import Pdf

n = int(input('Enter no. of PDFs: '))
list_pdf = []

for i in range(n):
    pdf_path = input('Enter path of the pdf:')
    list_pdf.append(f'{pdf_path}.pdf')

print(list_pdf)

new_pdf = Pdf.new()

for pdf in list_pdf:
    old_pdf = Pdf.open(pdf)
    new_pdf.pages.extend(old_pdf.pages)

new_pdf.save('test.pdf')

