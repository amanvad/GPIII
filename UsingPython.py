import urllib.request

# log_raw_file = urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
# log_read = log_raw_file.read()
# log_file = open("log_read", "r")
# with urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log") as open_log:
#   log_file = open_log.read()
   

open_file = urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "open_file")

log_file = open("open_file", "r")

log_file = log_file.split("\n")

log_total = len(log_file)

print(log_file[0])

print("This is how many total requests were made in the past 6 months: ",)

print("This is how many total requests were made in the time period: ", log_total)


