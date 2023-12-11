import pikepdf

path = input('Enter PDF path:')
file_name = input('Enter name to save:')
password = input('Enter password:')
own = input('Enter owner name:')

my_pdf = pikepdf.Pdf.open(f'{path}.pdf')

no_extr = pikepdf.Permissions(extract=False)

# to save and encrypt
my_pdf.save(f'{file_name}.pdf',encryption=pikepdf.Encryption(user=password,
                                                             owner=own,
                                                             allow=no_extr))


print('\nPDF has been protected\n')

