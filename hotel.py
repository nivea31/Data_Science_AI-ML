import xlrd
from matplotlib import pyplot as plt

# Load hotel reviews dataset and Print first hotel’s name.
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter = True

loc=("hotel_revies.xlsx")
sheet=xlrd.open_workbook(loc)
sheet=sheet.sheet_by_index(0)

print("First hotel’s name - ",sheet.cell_value(1,11))

# Print total number of rows.
print("Total number of rows",sheet.nrows)

# Print total number of Columns.
print("Total number of columns",sheet.ncols)

# Allow user to insert hotel Name, Print hotel found or Not found
user = input("Enter Hotel name to found hotel is there or not-")
for i in range (1,sheet.nrows):
    if user == sheet.cell_value(i,11):
        print("Hotel Found")
        break
else:
    print("Hotel not found")

# Allow user to insert hotel name, print hotel's details. For example Categories, city, state province ‘ address etc.
user=input("Enter Hotel name to get details-")
for i in range (1,sheet.nrows):
    if user==sheet.cell_value(i,11):
        for j in range(1,sheet.ncols):
            print(sheet.cell_value(i,j))
        break
else:
    print("Hotel not found")

# Allow user to insert hotel name print total rating average of that hotel.
total=0
user=input("Enter Hotel name to get review ratings-")
for i in range (1,sheet.nrows):
    if user==sheet.cell_value(i,11):
        print(sheet.cell_value(i,17))
        total=total+sheet.cell_value(i,17)
        avg=total/sheet.nrows
        print("Total",total)
        print(avg)
    #     break
    # else:
    #     print("Hotel Not Found")

# For Example 1 star - 12, 2 star - 8, 3 star - 23, 4 star - 35, 5 star - 120.Bar graph and pie graph of above counts.
ratings=[]
user=input("Enter Hotel name to print bar and piechart-")
for i in range (1,sheet.nrows):
    star = ["1-star", "2-star", "3-star", "4-star", "5-star"]

    if user==sheet.cell_value(i,11):
        #print("Ratings",sheet.cell_value(i,17))
        ratings.append(sheet.cell_value(i,17))

print(ratings)

plt.pie(ratings,labels=star,autopct="%.2f%%")
plt.show()

# Allow user to insert hotel names until User inserts stop. Print bar graph of Average rating of those entered hotel's.
hotel=[]
average=[]
total=0
while True:
    user = input("Enter Hotel name-")
    if user == "stop":
        break
    for i in range(1, sheet.nrows):
        if user == sheet.cell_value(i, 11):
            hotel.append(user)
            #print(sheet.cell_value(i, 17))
            total = total + sheet.cell_value(i, 17)
            avg = total / sheet.nrows
            #print("Total", total)
            average.append(avg)
    #print(average)
plt.bar(hotel,average)
plt.show()

# Allow user to insert any 3 hotel names. Print pie chart of all 3 hotel's rating wise count ( same as question  7 ) in single frame. ( 3 pie chart of 3 hotels for comparison  ).
ratings1=[]
ratings2=[]
ratings3=[]
while True:
    for user in range(0,3):
        user=input("Enter any three Hotel name-")

    for i in range (1,sheet.nrows):
        if user==sheet.cell_value(i,11):
            #print("Ratings",sheet.cell_value(i,17))
            ratings1.append(sheet.cell_value(i,17))
            ratings2.append(sheet.cell_value(i, 17))
            ratings3.append(sheet.cell_value(i, 17))

    print(ratings1)
    fig,axes=plt.subplots(1,3)
    axes[0].pie(ratings1,autopct="%.2f%%")
    axes[1].pie(ratings2, autopct="%.2f%%")
    axes[2].pie(ratings3, autopct="%.2f%%")
    plt.show()

