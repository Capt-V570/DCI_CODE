import time                   # import Time module

start_time = time.time()      # current time in seconds (since start of UNIX Epoch)
y = time.ctime(start_time)    # x converted to human readable time format

stop_time = int(input("Enter a Time for the Stopwatch: "))      # request input 'stop time' from user
end_time = time.ctime(stop_time)    # convert Stop_time to readable format

print()
print(y)