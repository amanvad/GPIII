import urllib.request

# log_raw_file = urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
# log_read = log_raw_file.read()
# log_file = open("log_read", "r")
# with urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log") as open_log:
#   log_file = open_log.read()
# with open("open_file") as log_file:
    # log_list = list(log_file)
   

   

get_file = urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "get_file")

open_file = open("get_file", "r")

read_file = open_file.read()

split_file = read_file.split("\n")

log_total = len(split_file)

six_month_start = False
six_month_total = 0
            
for log in splitfile:
    if "11/Apr/1995:00:00:16" in log:
        six_month_start = True
    if six_month_start == True:
        six_month_total += 1
            
print("This is how many total requests were made in the past 6 months: ", six_month_total)

print('/n')

print("This is how many total requests were made in the time period: ", log_total)


