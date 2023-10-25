"""
    serialization --> it is the process of transforming data or an object in memory(RAM) to a sequence of bytes
                      called "byte stream"

                      these byte streams in binary file can be stored in a disk, database or sent through a network

                      it is also called "pickling"
"""

"""
    de-serialization --> it is the inverse of serialization process where a byte stream is converted back to python object
                        
                        it is also called "unpickling"
"""

"""
    pickle module --> it is used for implementing binary protocols for serialization and de-serialization a python object structure

                      it deals with binary files

                      here, data are not written but dumped and not read but loaded

                      it provides two methods 1)dump() 2)load()
                      1) dump() --> it is used for pickling
                      2) load() --> it is used for unpickling
"""