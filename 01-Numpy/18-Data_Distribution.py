"""
    in this, we will see the visualization of data using seaborn

    seaborn is a library that uses matplotlib to plot graph 

    to install matplotlib --> pip install matplotlib

    to install seaborn --> pip install seaborn


"""
import matplotlib.pyplot as plt
import seaborn as sns

""" we use distplot that plot histogram by default 
    and it takes some values by default
"""
arr1 = [0,1,2,3,4,5,6]

sns.distplot(arr1)
plt.show()


# to remove histogram
arr2 = [0,1,2,3,4,5,6]

sns.distplot(arr2, hist=False)
plt.show()
