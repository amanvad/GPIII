import urllib.request

# log_raw_file = urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
# log_read = log_raw_file.read()
# log_file = open("log_read", "r")
# with urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log") as open_log:
#   log_file = open_log.read()
   

open_file = urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "open_file")

with open(open_file) as log_file:
    log_list = list(log_file)

# log_file = open("open_file", "r")

# split_file = log_file.split("\n")

log_total = len(split_file)

print(split_file[0])

print("This is how many total requests were made in the past 6 months: ",)

print("This is how many total requests were made in the time period: ", log_total)


