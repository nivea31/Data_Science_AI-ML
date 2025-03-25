import requests
#Allow user to insert word, print meaning found or not found
url2=input("Enter Word : ")
url1= "https://api.dictionaryapi.dev/api/v2/entries/en/"
url=url1+url2
print(url)

data=requests.get(url)
mydata=data.json()

if data.status_code == 200:
    meanings = mydata[0]["meanings"]
    if meanings:
        print("Meaning Found.")
else:
    print("Meaning not found.")

#Allow the user to insert a word, print url of audio pronunciation of that word.
url2=input("Enter Word : ")
url1= "https://api.dictionaryapi.dev/api/v2/entries/en/"
url=url1+url2

data=requests.get(url)
mydata=data.json()

if url2==mydata[0]["word"]:
    print("URL of audio - ",mydata[0]["phonetics"][0]["audio"])

# Print the first meaning of that word.
    print("First Meaning - ", "\n", mydata[0]["meanings"][0]["definitions"][0]["definition"])

#Print all meanings of that word.
print("All meanings of this word is - ")
for i in range(0,len(mydata[0]["meanings"])):
    print(mydata[0]["meanings"][i]["definitions"][0]["definition"])
for i in range(1,len(mydata[0]["meanings"][2]["definitions"])): #api has 2nd list in 3rd definition which has no end so starting 2nd loop from 2nd index and start loop from 1 skipping 0th meaning.
    print(mydata[0]["meanings"][2]["definitions"][i]["definition"])
