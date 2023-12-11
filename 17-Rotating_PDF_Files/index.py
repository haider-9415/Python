import pikepdf

pdf = input('Enter pdf path:')
file_name = input('Enter name to save rotated pdf:')
degree = int(input('Enter degree:'))

my_pdf = pikepdf.Pdf.open(f'{pdf}.pdf')

# to get pages in the pdf
pages = my_pdf.pages

for i in pages:
    # to rotate at 180 degree
    i.Rotate = degree
    my_pdf.save(f'{file_name}.pdf')
