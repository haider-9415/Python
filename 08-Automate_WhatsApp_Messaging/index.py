import pywhatkit as pwk

number = input('Enter no. to send(with country code): ')
message = input('Enter message: ')
hour = int(input('Enter hour(A/T 24-hours): '))
minuite = int(input('Enter minuites: '))


pwk.sendwhatmsg(number, message, hour, minuite)

