import mysql.connector

#connect = mysql.connector.connect(hostname ="localhost", username="root", password ="root", databasename= "abc")

#mycursor = connect.cursor();
#mycursor.execute("Select all statments")




# Zip

names = ["nayeem", "John","Dinesh", "Vinoth"]
comps = ["Cognizant", "IBM", "Cognizant", "Capgemini"]


for (a,b) in zip(names, comps):
    print(a,b)

for (a,b) in zip(comps, names):
    print(a,b)

print(list(zip(names, comps)))
print(set(zip(comps, names)))
print(dict(zip(comps, names)))