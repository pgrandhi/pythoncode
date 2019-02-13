from Stock import Stock 

stock1 = Stock("INTC","Intel Corporation",20.50,20.35)


print("Stock name:",stock1.getName(),"Symbol:",stock1.getSymbol(), "previous closing price",stock1.getPreviousClosingPrice(),"current price:",stock1.getCurrentPrice(),"change Percent:",stock1.getChangePercent())
