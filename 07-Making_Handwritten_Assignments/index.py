# install 'pywhatkit' using pip
import pywhatkit as pwk

txt = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[34] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.
Python consistently ranks as one of the most popular programming languages.
"""

# there is a function the converts into handwritten and it accepts three parameters
# 1st is the given text, 2nd is the file where you have to save it & 3rd is the font color

pwk.text_to_handwriting(txt, "demo1.png", [155,0,0])

print('\nConverted :)\n')

