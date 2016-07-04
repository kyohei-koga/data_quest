#coding: UTF-8

r = open("unisex_names_table.csv","r")
data = r.read()
#Convert the string to a list
data_list = data.split("\n")
print(data_list[0:5])
string_data = []
for data in data_list:
    data_comma = data.split(",")
    string_data.append(data_comma)
print(string_data[0:5])
string_data = string_data[1:len(string_data)-1]
print(string_data[0:5])
#Convert numerical values
numerical_data=[]
for row in string_data:
    newlist = [row[1],float(row[2])]
    numerical_data.append(newlist)
print(numerical_data[0:5])

#Filter the list
#あるしきい値より多いデータセットを抽出する
thousand_or_greater = []
for numerical in numerical_data:
    if numerical[1] >= 1000:
        thousand_or_greater.append(numerical)
print("\nmore than 1000 people share list below")
print(thousand_or_greater[:10])
