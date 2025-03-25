import xlrd

xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter = True

loc=("storedata.xlsx")

sheet=xlrd.open_workbook(loc)
sheet=sheet.sheet_by_index(0)

# PRINT TOTAL NUMBER OF ROWS
print("Total number of row : ",sheet.nrows)

# PRINT TOTAL NUMBER OF COLUMNS
print("Total number of row : ",sheet.ncols)

# PRINT 61
print(sheet.cell_value(7,12))

# PRINT NAMES OF ALL MONTHS
for i in range(1,sheet.ncols):
    print("Month - ",sheet.cell_value(0,i))

# PRINT NAMES OF ALL PRODUCTS
for i in range(1,sheet.nrows):
    print("Products - ",sheet.cell_value(i,0))

# PRINT TOTAL NUMBER OF PRODUCTS SOLD IN MARCH MONTH
total= 0
for i in range(1, sheet.nrows):
    total = total+sheet.cell_value(i,3)

print("Total Products Sold in March:", total)

# WHICH PRODUCT SOLD HIGHEST IN MARCH MONTH.( ANS MOBILES )
high=0
for i in range(1,sheet.nrows):
    hp=sheet.cell_value(i,3)
    if hp>high:
        high=hp
        a=sheet.cell_value(i,0)
print(a)


# ALLOW USER TO INSERT NAME OF THE MONTH PRINT NAME OF HIGHEST AND LOWEST NUMBER OF PRODUCTS SOLD IN THAT MONTH
mdata=[]
user=input("Enter Month Name : ")
for i in range(1,sheet.ncols):
    for j in range(1, sheet.nrows):
        if user == sheet.cell_value(0,i):
            mdata.append(sheet.cell_value(j, i))
    break

print("Highest Number of Product Sold -", max(mdata))
print("Lowest Number of Product Sold -", min(mdata))

# IN WHICH MONTH REFRIGERATOR SOLD HIGHEST.
highref=0
for i in range(1,sheet.ncols):
    hs=sheet.cell_value(5,i)
    if hs>highref:
        highref=hs
        a=sheet.cell_value(0,i)
print("Refrigerator sold highest in ",a)
