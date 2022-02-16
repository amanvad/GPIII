import urllib.request

get_file = urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "get_file")
open_file = open("get_file", "r")
read_file = open_file.read()
split_file = read_file.split('\n')

log_total = len(split_file)

six_month_start = False
six_month_total = 0
            
for log in split_file:
    if "11/Apr/1995:00:00:16" in log:
        six_month_start = True
    if six_month_start == True:
        six_month_total += 1
        
print(/n)            
print("This is how many total requests were made in the past 6 months: ", six_month_total)
print("This is how many total requests were made in the time period: ", log_total)
