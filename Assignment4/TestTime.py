from Time import Time 

t = Time()
print("Time class created")

print ("Current time :", t.getHour(),":",t.getMinute(),":",t.getSecond())
elapseTime = eval(input("Enter the elapsed time:"))
t.setTime(elapseTime)
print ("The hour:minute:second for the elapsed time is :", t.getHour(),":",t.getMinute(),":",t.getSecond())
