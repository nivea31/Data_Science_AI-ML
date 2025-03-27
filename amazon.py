import xlrd
# 1) Load amazon categories dataset.
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter = True

loc=("amazon_categories.xlsx")
sheet=xlrd.open_workbook(loc)
sheet=sheet.sheet_by_index(0)

# 2) Print total number of rows.
print("Total number of rows - ",sheet.nrows)

# 3) Print total number of Columns.
print("Total number of columns - ",sheet.ncols)

# 4) Print names of all columns.
print("Name of all columns - ")
for i in range(0,sheet.ncols):
    print(sheet.cell_value(0,i))
