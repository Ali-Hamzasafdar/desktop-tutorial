import pandas as pd
print('1')
US_data = pd.read_csv("Pandas/us data.csv",delimiter=',',index_col='Serial Number')

print(US_data)
print("US_Data .info :",US_data.info)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print("US-data .dtype :",US_data.dtypes)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print("US_data .describe :",US_data.describe)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print("US_data .describe :",US_data.shape)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')



#3.  Use , DataFrame method -  .to_string() 


US_1 = pd.DataFrame({
    'Name ': ['Ali', 'hamza', 'Arslan', 'Usman', 'Qasim', 'Noor', 'Ali', 'hamza', 'Arslan', 'Usman', 'Qasim', 'Noor'],
    'Age': [17, 20, 18, 21, 23, 25, 19, 30, 16, 25, 22, 24],
    'DOB': [2003, 1997, 1999, 2001, 2000, 2002, 2004, 1998, 1995, 2001, 2003, 2002]
})

print(US_1.to_string(index=False))


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# 4. On given DataFrame – select top 7 rows, and print 


US_2 =US_1.head(7)
print(US_1)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# 5. On given DataFrame – select bottom 9 rows, and print 

US_3 = US_1.tail(9)
print(US_3)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# 6. On Given DataFrame – access the Name column for “Town” and print whole column 
# Then next, access the name column for “Residential Type” and print whole column


town = US_data['Town']
residential = US_data['Residential Type']



print('US_data All Towns      :', town)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print('US_data Residential      :', residential)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# On Given DataFrame – access access multiple columns like “Town” and “Date Recorded” 

town_datarecord =US_data[['Town','Date Recorded']]

print(town_datarecord)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 8. Selecting a single row using .loc 
# With index – “Serial Number” value “200008” , print the returned row and analyze results.


Single_row=US_data.loc[200008]
print(Single_row)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# 9. Selecting multiple rows using .loc 
# With index – “Serial Number” value “200305” and “200207”,”20000048”  , print the returned 
# rows and analyze results.

Multi_Row = US_data.loc[[200305,200207,20000048]]
print (Multi_Row)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


#  Selecting a slice of rows using .loc 
# With index – “Serial Number” value range of “2020090” and “200121” , print the returned row 
# and analyze results.

Slice = US_data.loc[2020090:200121]
print(Slice)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# 11. Conditional selection of rows using .loc 
# “Sale Amount” greater then “202500” 
# , print the returned row and analyze results. 


greater=US_data.loc[US_data['Sale Amount']>202500]
print(greater)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 12. Conditional selection of rows using .loc 
# “Town” equal to “Ansonia” 
# , print the returned row and analyze results.



equal =US_data.loc[US_data['Town']=='Ansonia']
print('“Town” equal to “Ansonia” ',equal)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 13. Conditional selection of rows using .loc 
# “Residential Type” equal to “Condo” and “Assessed Value” is equal to - less then 180500 
# , print the returned row and analyze results.

Equal_less= US_data.loc[(US_data['Residential Type'] =='Condo')&(US_data['Assessed Value']<=180500)]
print('“Residential Type” equal to “Condo” and “Assessed Value” is equal to - less then 180500 :' ,Equal_less)



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# 14. Selecting a single column using .loc 
# With index – “Serial Number” value “201354” , only select following columns 
# “Address”,” Assessed Value” , ”Sale Amount” , ”Sales Ratio” , ”Property Type” 
Single_column = US_data.loc[201354, ['Address', 'Assessed Value', 'Sale Amount', 'Sales Ratio', 'Property Type']]
print(Single_column)

print()



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 15. Selecting a slice of columns using .loc 
# Form “Date Recorded” to “Sale Amount”
# 
Slice_column = US_data.loc[:, 'Date Recorded':'Sale Amount']
print(Slice_column)
print()


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
#  
# 16. Combined row and column selection using .loc 
# “Residential Type” equal to “Condo” and Columns th  “Date Recorded” to “Assessed Value”
Combin = US_data.loc[US_data['Residential Type'] == 'condo', ['Date Recorded', 'Assessed Value']]
print(Combin)
print()


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 17. Selecting a single row using .iloc 
# Select 5th row 

Row_5 =US_data.iloc[4]
print(Row_5)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# 18. Selecting multiple rows using .iloc 
# Select – 7th row, 9th row and 15th row

Row_6 = US_data.iloc[[-8,8,14]]
print(Row_6)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 19. Selecting a slice of rows using .iloc 
# Select from 5th to 13th row 

Slice_Row= US_data.iloc[5:13]
print(Slice_Row)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# 20. Selecting a single column using .iloc 
# Select 3rd column

Select_Column= US_data .iloc[:,2]
print(Select_Column)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 21. Selecting multiple columns using .iloc 
# Select 2nd column, 4th column,  7th columns 

Select_Multi= US_data.iloc[:,[1,3,6]]
print(Select_Multi)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 22. Selecting a slice of columns using .iloc 
# Range: Select from 2nd column to 5th columns  

Select_Range = US_data.iloc[range(1,4)]
print(Select_Range)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# 23. Combined row and column selection using .iloc 
# Select – 7th row, 9th row and 15th row 
# Select 2nd column, 4th column 

Select_Multi_row_column = US_data.iloc[[-8,8,14],[1,3]]
print(Select_Multi_row_column )

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 24. Combined row and column selection using .iloc 
# Select range : 2nd  row, 6th  row 
# Select range : 2nd column to 4th column 

Combin_row_column = US_data.iloc[1:6, 1:4]
print(Combin_row_column)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 25. Add a New Row to a Pandas DataFrame


# print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# 26. delete row with index 2 

Multi_Rows = US_data.drop(US_data.index[2])
print(Multi_Rows)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 27. delete row with index from 4 to 7th row

Del_row = US_data.drop(US_data.index[4:7])
print(Del_row)



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# 28.  Delete “Residential Type” column
 
 
Del_Column = US_data.drop(columns=['Residential Type'])
print(Del_Column)




print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# 29. Delete “Assessor Remarks” and “Location” columns 

Multi_del = US_data.drop(columns=['Assessor Remarks','Location'])
print(Multi_del)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# 30. Rename column “List Year:  to “List_Year_Changed” 

Rename = US_data.rename(columns={'List Year':'List Year_Changed'})
print(Rename)



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
# 31. Rename label from “200400” to “20040333” 

Rename_index = US_data.rename(index={200400:20040333})
print(Rename_index)



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 32. query() to Select Data 
# where: "Assessed Value” < 127400 
# “Property Type”  = “Commercial” 
# “Residential Type” not equal to “Single Family”


# print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
#  
# 33. sort DataFrame by price in ascending order column “Assessed Value” 
ascending_sort= US_data.sort_values(by='Assessed Value', ascending=True)
print(ascending_sort)



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 34. “group the DataFrame by the “Property Type” column and calculate the sum of “Sale Amount” 
# for each category 

Sum_row=US_data.groupby('Property Type')['Sale Amount'].sum()
print(Sum_row)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 35. use dropna() to remove rows with any missing values 


Remove_row = US_data.dropna()
print(Remove_row)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# 36. filling NaN values with 0 

nan = US_data.fillna
print(nan)
# print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

