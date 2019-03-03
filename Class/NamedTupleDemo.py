from collections import namedtuple

stock = namedtuple("Stock","symbol current high low")
s1 = stock("MSFT",112.05,140,80)

stocks = []
stocks.append(s1)
s2= stock("AMZN",1600,2000,40)
stocks.append(s2)

print(s1.current)
