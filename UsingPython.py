from urllib.request import urlopen

log_raw_file = urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")

log_file = log_raw_file.read()

log_total = len(log_file)


print("This is how many total requests were made in the past 6 months: ",)

print("This is how many total requests were made in the time period: ", log_total)

print(log_file[0])
