import xlrd #pip install xlrd==1.2.0

xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter = True

loc=("cricket.xlsx")
#object
sheet=xlrd.open_workbook(loc)
sheet=sheet.sheet_by_index(0)

#print(sheet)
#print(sheet.cell_value(0,0))

#total no. of rows
print("Total number of row : ",sheet.nrows)

#total no. of columns
print("Total number of row : ",sheet.ncols)

#total number of matches
print("Total number of matches : ",sheet.ncols-1)

#total number of players
print("Total number of players : ",sheet.nrows-1)

#name of all players
for i in range(1,sheet.nrows):
    print("Players name - ",sheet.cell_value(i,0))

#score of all matches of VIRAT
for i in range(1,sheet.ncols):
    print("Virat's score of all matches - ",sheet.cell_value(2,i))

#Allow user to insert player name, print found or not found
user=input("Enter player name - ")
for i in range(1,sheet.nrows):
    if sheet.cell_value(i,0)==user:
        print("Player Found")
        break
else:
    print("Player Not Found")


#Allow user to insert player name, print latest score of that player
user1=input("Enter player name - ")
for i in range(1,sheet.nrows):
    if user1==sheet.cell_value(i,0):
        print(sheet.cell_value(i,sheet.ncols-1))
        break
else:
    print("Player Not Found")

#Allow user to insert name of player, print score of all matches of that player.
user2=input("Enter player name - ")
for i in range(1,sheet.nrows):
    for j in range(1,sheet.ncols):
        if user2==sheet.cell_value(i,0):
            print(sheet.cell_value(i,j))
            break
else:
    print("Player Not Found")

#Allow user to insert player name, store all matches data of that player in a list.
data=[]
user3=input("Enter Player Name : ")

for i in range(1,sheet.nrows):
    if user3==sheet.cell_value(i,0):
        for j in range(1,sheet.ncols):
            data.append(sheet.cell_value(i,j))
        break
else:
    print("Player Not Found")

print("PlayerScore-",data)

#Allow user to insert player name, print High score, Low Score, Average score of that player.

data1=0
data3=[]

user4=input("Enter Player Name - ")

for i in range(1,sheet.nrows):
    if user4==sheet.cell_value(i,0):
        for j in range(1, sheet.ncols):
            data2=data1+sheet.cell_value(i,j)
            data3.append(sheet.cell_value(i, j))
        break
else:
    print("Player Not Found")

print("Highest Score of Player -", max(data3))
print("Lowest Score of Player -", min(data3))
print("Average Score of Player -", data2/sheet.ncols-1)



