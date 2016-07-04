# coding: UTF-8
#type function
a = type(50)
print(a)

#converting types
ten = '10'
eight = 8
int_ten = int(ten)
str_eight = str(eight)
print type(ten) ,type(eight)

#Lists
#リスト型は値の列を表す：l=[]
#値を加えるときは.append()を利用する。
l = []
print(type(l))
l.append("January")
l.append("February")
l.append("March")
l.append("April")
print(l)

#別のやり方で上記と同じ結果

L = ["January","February","March","April"]
print(L)

#Multiple types in list
o = ["Jan",5.0,"uary",10]
print(o)

#list index
print(o[3])

#List length
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
second_last = months[len(months)-2]
print(second_last)

#List slicing
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
eight_eleven = months[8:12]
print(months[0:5])
