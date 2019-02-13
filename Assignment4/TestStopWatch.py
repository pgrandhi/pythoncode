from StopWatch import StopWatch 

stopwatch = StopWatch()
print("Stopwatch created")
sum = 0
stopwatch.start()
for i in range(1, 1000000):
  sum +=i
stopwatch.stop()

print ("sum of 1 to 1,000,000 :", sum)
print ("time taken to add 1 to 1,000,000 :", stopwatch.getElapsedTime())
