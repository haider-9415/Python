import pikepdf

my_pdf = pikepdf.Pdf.open(f"{input('Enter PDF path:')}.pdf")

# to separtate on the basis of no. of pages

for n, page in enumerate(my_pdf.pages):
# 'n' will contain no. of page and 'page' will contains content of the page
    new_pdf = pikepdf.Pdf.new()
    new_pdf.pages.append(page)
    name = 'pdf-'+str(n)+'.pdf'
    new_pdf.save(name)

print('\nPDFs have been created :)\n')

