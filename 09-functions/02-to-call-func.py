# first remove '01-' from '01-uer_difined'
from user_difined import*

""" print cost to make a tent """

height = float(input("enter height: "))
radius = float(input("enter radius: "))
slant_height = float(input("enter slant_height: "))
print("\n\n\n")

csa_cone = cone(slant_height,height)
csa_cylinder = cylinder(height,radius)

total_area = csa_cone+csa_cylinder
print("total area: ",total_area)

length_fabric = len_feb(total_area,20)
print("length of the fabric required is: ",length_fabric)
print("................................................\n")

rate = float(input("enter rate: "))
print("\n................................................\n")
cost_exc_tax = cost(length_fabric,rate)

cost_inc_tax = amount(cost_exc_tax)
print("cost excl. of tax: ",cost_exc_tax)
print("cost incl. of tax: ",cost_inc_tax)
print("\n\n\n")


# to know what does a function do ?, we use --> function_name.__doc__ 
print("len_feb -->",len_feb.__doc__)
print("cylinder -->",cylinder.__doc__)
print("cost -->",cost.__doc__)
print("\n\n\n")
