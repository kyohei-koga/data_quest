#coding: UTF-8
#time module
import time
current_time = time.time()
print(current_time)

current_struct_time = time.gmtime(current_time) #Convert time.time() to be readable
print(current_struct_time)
current_year = current_struct_time.tm_year #extract year from current_struct_time
current_month = current_struct_time.tm_mon #extract month from current_struct_time
current_day = current_struct_time.tm_mday #extract day from current_struct_time
current_hour = current_struct_time.tm_hour #extract hour from current_struct_time
current_min = current_struct_time.tm_min ##extract min from current_struct_time

print('%d/%d/%d %d:%d') %(current_year, current_month, current_day, current_hour, current_min)

#datetime module
#this module is more convenient than time module
import datetime
current_time = datetime.datetime.now()
current_year = current_time.year
current_month = current_time.month
print(current_time)
print(current_year)

#substracting and adding time. use timedelta class
diff = datetime.timedelta(weeks=3,days=2) #span of 3weeeks plus 2days
result_feature = current_time + diff
result_past = current_time - diff
print("feature result is %s, past result is %s") %(result_feature,result_past)
