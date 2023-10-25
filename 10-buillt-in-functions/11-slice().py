# slice(start,stop,step) --> it returns a slice object
# remember, start and step attributes are optional, their default values are None

""" if we don't assign then all slice objects that are not assigned have same memory address """
print("slice(10) --> ",slice(10))
print("type(slice(10)) --> ",type(slice(10)))
print("id(slice(10)) --> ",id(slice(10)),'\n')
print("slice(10,34) --> ",slice(10,34))
print("type(slice(10,34)) --> ",type(slice(10,34)))
print("id(slice(10,34)) --> ",id(slice(10,34)),'\n')
print("slice(10,34,2) --> ",slice(10,34,2))
print("type(slice(10,34,2)) --> ",type(slice(10,34,2)))
print("id(slice(10,34,2)) --> ",id(slice(10,34,2)),'\n')

""" if we assign then all slice objects that are assigned have different memory addresses """
v1 = slice(10); v2 = slice(10,34); v3 = slice(10,34,2)
print("v1 --> ",v1)
print("type(v1) --> ",type(v1))
print("id(v1) --> ",id(v1),'\n')
print("v2 --> ",v2)
print("type(v2) --> ",type(v2))
print("id(v2) --> ",id(v2),'\n')
print("v3 --> ",v3)
print("type(v3) --> ",type(v3))
print("id(v3) --> ",id(v3),'\n')




# for string
str1 = 'haider'
str2 = 'this is the lecture to know the in-built functions of string '
str3 = 'HANZALA'
str4 = 'Naeem'

""" the slice() works as well as we do slicing in string """
v4=slice(5); v5=slice(2,7); v6=slice(-8,-4); v7=slice(2,8,2); v8=slice(5,30,3)
print("str3[v4] --> ",str3[v4]); print("str3[:5:] --> ",str3[:5:],'\n')
print("str1[v5] --> ",str1[v5]); print("str1[2:7] --> ",str1[2:7],'\n')
print("str2[v6] --> ",str2[v6]); print("str2[-8:-4] --> ",str2[-8:-4],'\n')
print("str1[v7] --> ",str1[v7]); print("str1[2:8:2] --> ",str1[2:8:2],'\n')
print("str2[v8] --> ",str2[v8]); print("str2[5:30:3] --> ",str2[5:30:3],'\n')
v9=slice(-2); v10=slice(-7,-2,2); v11=slice(-30,None,3); v12=slice(None,None,-1);v13=slice(None,0,-1)
print("str4[v9] --> ",str4[v9]); print("str4[-2] --> ",str4[:-2:],'\n')
print("str3[v10] --> ",str3[v10]); print("str3[-7:-2:-2] --> ",str3[-7:-2:2],'\n')
print("str2[v11] --> ",str2[v11]); print("str2[-30::3] --> ",str2[-30::3],'\n')
print("str1[v12] --> ",str1[v12]); print("str1[::-1] --> ",str1[::-1],'\n')
print("str1[v13] --> ",str1[v13]); print("str1[:0:-1] --> ",str1[:0:-1],'\n')
print("str1[v13] --> ",str1[v13]); print("str1[::-1] --> ",str1[::-1],'\n')




# for list
lt1 = [1,2,53.665,'haider',34-42j,True]
lt2= [43,5,4,6.5,6,5.6,433.67,0,-445,-344,1,-1]
lt3= ['abc','wed','aaf','fd']
lt4 = ['A','B','C','D','E','F']

""" the slice() works as well as we do slicing in list """
v4=slice(5); v5=slice(2,7); v6=slice(-8,-4); v7=slice(2,8,2); v8=slice(5,30,3)
print("lt3[v4] --> ",lt3[v4]); print("lt3[:5:] --> ",lt3[:5:],'\n')
print("lt1[v5] --> ",lt1[v5]); print("lt1[2:7] --> ",lt1[2:7],'\n')
print("lt2[v6] --> ",lt2[v6]); print("lt2[-8:-4] --> ",lt2[-8:-4],'\n')
print("lt1[v7] --> ",lt1[v7]); print("lt1[2:8:2] --> ",lt1[2:8:2],'\n')
print("lt2[v8] --> ",lt2[v8]); print("lt2[5:30:3] --> ",lt2[5:30:3],'\n')
v9=slice(-2); v10=slice(-7,-2,2); v11=slice(-30,None,3); v12=slice(None,None,-1);v13=slice(None,0,-1)
print("lt4[v9] --> ",lt4[v9]); print("lt4[-2] --> ",lt4[:-2:],'\n')
print("lt3[v10] --> ",lt3[v10]); print("lt3[-7:-2:-2] --> ",lt3[-7:-2:2],'\n')
print("lt2[v11] --> ",lt2[v11]); print("lt2[-30::3] --> ",lt2[-30::3],'\n')
print("lt1[v12] --> ",lt1[v12]); print("lt1[::-1] --> ",lt1[::-1],'\n')
print("lt1[v13] --> ",lt1[v13]); print("lt1[:0:-1] --> ",lt1[:0:-1],'\n')
print("lt1[v13] --> ",lt1[v13]); print("lt1[::-1] --> ",lt1[::-1],'\n')




# for tuple
tp1 = (1,2,3,2,'haider','hanzala',9-45j,'haider')
tp2 = (34.34,123.0,232.565,789.433)
tp3 = ('wad','ajh','aafre','yakf')
tp4 = ('A','B','C','D','E','F')

""" the slice() works as well as we do slicing in tuple """
v4=slice(5); v5=slice(2,7); v6=slice(-8,-4); v7=slice(2,8,2); v8=slice(5,30,3)
print("tp3[v4] --> ",tp3[v4]); print("tp3[:5:] --> ",tp3[:5:],'\n')
print("tp1[v5] --> ",tp1[v5]); print("tp1[2:7] --> ",tp1[2:7],'\n')
print("tp2[v6] --> ",tp2[v6]); print("tp2[-8:-4] --> ",tp2[-8:-4],'\n')
print("tp1[v7] --> ",tp1[v7]); print("tp1[2:8:2] --> ",tp1[2:8:2],'\n')
print("tp2[v8] --> ",tp2[v8]); print("tp2[5:30:3] --> ",tp2[5:30:3],'\n')
v9=slice(-2); v10=slice(-7,-2,2); v11=slice(-30,None,3); v12=slice(None,None,-1);v13=slice(None,0,-1)
print("tp4[v9] --> ",tp4[v9]); print("tp4[-2] --> ",tp4[:-2:],'\n')
print("tp3[v10] --> ",tp3[v10]); print("tp3[-7:-2:-2] --> ",tp3[-7:-2:2],'\n')
print("tp2[v11] --> ",tp2[v11]); print("tp2[-30::3] --> ",tp2[-30::3],'\n')
print("tp1[v12] --> ",tp1[v12]); print("tp1[::-1] --> ",tp1[::-1],'\n')
print("tp1[v13] --> ",tp1[v13]); print("tp1[:0:-1] --> ",tp1[:0:-1],'\n')
print("tp1[v13] --> ",tp1[v13]); print("tp1[::-1] --> ",tp1[::-1],'\n')
