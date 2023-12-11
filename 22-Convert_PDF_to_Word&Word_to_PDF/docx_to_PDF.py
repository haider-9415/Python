# run --> pip install docx2pdf


from docx2pdf import convert

docx_file = input('Enter docx file path:')
file_name = input('Enter name ot save file:')

convert(f'{docx_file}.docx', f'{file_name}.pdf')
