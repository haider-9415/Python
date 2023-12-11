# run --> pip install pdf2docx

from pdf2docx import Converter

pdf = input('Enter PDF path:')
file_name = input('Enter name ot save file:')

obj = Converter(f'{pdf}.pdf')
obj.convert(f'{file_name}.docx')
obj.close()