# 1. Load above CVS file above, into separate – Array , with NUMPY, following columns 
import numpy as np

Sale_Amount,Serial_Number,List_Year,Town,Assessed_Value = np.genfromtxt('Numpy/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter =',',usecols=(6,0,1,3,5),unpack=True,dtype=None,skip_header=1,invalid_raise=False)

print (Sale_Amount)
print (Serial_Number)
print (List_Year)
print (Town)
print (Assessed_Value)


print('<========================================================================>')

#2. Perform following operation on array of ““Sale Amount”: 

print("RealEstate.com Sale_Amount mean : " ,np.mean(Sale_Amount))
print("RealEstate.com Sale_Amount Median: " ,np.median(Sale_Amount))
print("RealEstate.com Sale_Amount SD : ",np.std(Sale_Amount))
print ("RealEsate.com Sale_Amount Max : ",np.max(Sale_Amount))
print("RealEsate.com Sale_Amount Min :",np.min(Sale_Amount))

print('<========================================================================>')

# 3. Perform following operation on array of “Assessed Value”: 

print("RealEstae.com Assessed Value mean :",np.mean(Assessed_Value))
print("RealEstae.com Assessed Value Median :",np.median(Assessed_Value))
print("RealEstae.com Assessed Value SD :",np.std(Assessed_Value))
print("RealEstae.com Assessed Value max :",np.max(Assessed_Value))
print("RealEstae.com Assessed Value min :",np.min(Assessed_Value))

print('<========================================================================>')

# 4. Perform following operations on  - array of [array of ““Sale Amount”] and [array of “Assessed 
# Value”] 

addition = Sale_Amount + Assessed_Value
Sub     = Sale_Amount - Assessed_Value
Multiply = Sale_Amount * Assessed_Value
Division = Sale_Amount / Assessed_Value

print('Addition :',addition)
print('Subtraction :',Sub)
print('Multiply :',Multiply)
print('Division :',Division)

print('<========================================================================>')

# 5, 7 . Create a “2D array” based on array of [array of ““Sale Amount”] and [array of “Assessed Value”] 

D2_Arrays= np.array([Sale_Amount,Assessed_Value])

print('2 dimentional Array ,Number of Dimintons :',D2_Arrays.ndim)
print('2 dimentional Array , Total Number of Elements:',D2_Arrays.size)
print('2 dimentional Array , Data Type:',D2_Arrays.dtype)
print('2 dimentional Array , Tuple:',D2_Arrays.shape)



print('<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')


#6. Create a “3D array” based on array of [array of ““Sale Amount”] and [array of “Assessed Value”] 
# and [array of “List Year”]


D3_Array = np.array([Sale_Amount,Assessed_Value,List_Year])

print ('3 dimentional Array ,Number of Dimentional : ',D3_Array.ndim)
print ('3 dimentional Array ,total Number of Element : ',D3_Array.size)
print ('3 dimentional Array ,Data Types : ',D3_Array.dtype)
print ('3 dimentional Array ,Tuple : ',D3_Array.shape)

print('<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')


#7. Iterate the array - of [array of ““Sale Amount”] 
# With function  of “np.nditer"

Iterate_arr = np.array([[Sale_Amount],[Assessed_Value]])
print( "NumPy n-dimensional iterator:",Iterate_arr)

for x in np.nditer(Iterate_arr):
 print(x)


print('<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')



# 8. Iterate the array - of [array of ““Sale Amount”] 
# With function  of “np.ndenumerate


Iterate_arr2 = np.array([[Sale_Amount]])

print("NumPy n-dimensional enumerate : " ,Iterate_arr2)

for y in (Iterate_arr2):
  print(y)

print('<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')


#9 . Slice array of [Question 5, as - “2D array” based on array of [array of “Sale Amount”] and [array 
# of “Assessed Value”] ] 
# Row : from 3th value to 7th value 
# Column: from 2nd value to 4th value


D2_Slice= D2_Arrays[2:7 ,1:4]
print ("D2 Slices : ",D2_Slice)


print('<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')

# 11. Slice array of [Question 5, as - “2D array” based on array of [array of  “Assessed Value”] and 
# [array of “Assessed Value”] ] 
# Row : from 2nd  value to 8th value 
# Column: from 3rd value to 5th value

D2_Slice_2 = D2_Arrays[1:8 ,2:5]
print("D2_Slice_2 :",D2_Slice_2)



print('<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')

# 12. Learn – what are geometric operation in NUMPY. 
# np.sin , np.cos 
# apply common 6 to - “2D array” based on array of [array of  “Assessed Value”] and [array of 
# “Assessed Value”] , created in Question  5.

SIN = np.sin("RealEstate .com in Sin :",D2_Arrays)
COS = np.cos("RealEstate . com in cos :",D2_Arrays)
TAN = np.tan("RealEstate. com in Tangent :",D2_Arrays)


print('<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')
print('<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')
print('<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')
