from datetime import datetime as dt
import time as ti

'''

    strftime() is a method in Python that formats date and time objects into readable strings based on specified format codes. It is part of the datetime module.

'''

now = dt.now()
print(now)

# hour = int(ti.strftime('%H'))
timecycle = ti.strftime('%p')

print(timecycle)

if(timecycle=="PM"):
    print("Buneos noches! Senior")

else:
    print("Buneos dias! Senior")