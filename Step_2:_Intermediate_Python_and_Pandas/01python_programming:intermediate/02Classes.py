#coding: UTF-8
#class black_honda_accordというオブジェクトを作成するとした時、black_honda_accordはcolor,make,modelという変数を持っており、
#これらが車を表現するときに役立つ。これらの変数はpropertiesと呼ばれる。
#オブジェクトを作成するときにはある種のテンプレートが必要で、それはどのようなpropertiesを持つかを決めることである。
#classは、オブジェクトを作成するときにそのオブジェクトが従うテンプレートである。
#またこのclass（テンプレート）から作成されたオブジェクトのことをinstancesと呼ぶ。つまり
#black_honda_accordはCar classのinstanceである。
import csv
f = open("nfl.csv","r")
nfl = list(csv.reader(f))

#class sytax
class Team():
    def __init__(self,name): #この２行はおまじない
        #self.name = "Tampa Bay Buccaneers"
        self.name = name
        #can load data inside the class
        f = open("nfl.csv","r")
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def print_name(self):
        print(self.name)
#More instance methods
    def count_total_wins(self):
        count = 0
        for win in self.nfl:
            if self.name == win[4]:
                count += 1
        return count

giants = Team("New York Giants")
print(giants.name)

broncos = Team("Denver Broncos")
broncos_wins = broncos.count_total_wins()

chiefs = Team("Kansas City Chiefs")
chiefs_wins = chiefs.count_total_wins()

print("\ncount of broncos win is %d" %broncos_wins)
print("\ncount of chiefs win is %d" %chiefs_wins)
