"""
    big data sets are normally stored and extracted aas JSON

    it has a format of an onject

"""

import pandas as pd

fl1 = pd.read_json('data.json')
print('fl1.to_string():\n',fl1.to_string())
print('\n..........................................................................\n')



""" if json code is in a python file then we use DataFrame()
"""

python_data = {
    "Duration":{"0":60,"1":60,"2":60,"3":45,"4":45,"5":60,"6":60,"7":45,"8":30,"9":60,"10":60,
    },
    "Pulse":{"0":110,"1":117,"2":103,"3":109,"4":117,"5":102,"6":110,"7":104,"8":109,"9":98,"10":103,
    },
    "Maxpulse":{"0":130,"1":145,"2":135,"3":175,"4":148,"5":127,"6":136,"7":134,"8":133,"9":124,"10":147,
    },
    "Calories":{"0":409.1,"1":479.0,"2":340.0,"3":282.4,"4":406.0,"5":300.5,"6":374.0,"7":253.3,"8":195.1,"9":269.0,"10":329.3,
    },
}

data1 = pd.DataFrame(python_data)
print('data1:\n',data1)
print('\n..........................................................................\n')
