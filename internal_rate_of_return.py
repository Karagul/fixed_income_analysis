def present_value(futureValue, interestRate, numOfYears):
  return futureValue * (1 / pow(1 + interestRate, numOfYears))

def yield_calc(calcInfo, price, interestAssumption):
  interestAssumption = interestAssumption
  calcAmount = 0.00

  for cashFlow in calcInfo:
    calcAmount += present_value(cashFlow[1], interestAssumption/100, cashFlow[0])
  
  return round(calcAmount)

def calcMultipleYield(cashFlow, price):
  initialYield = 1.00

  # assuming the yield will be always less than 20.00
  while initialYield < 20.00:
    trialYield = yield_calc(cashFlow, price, initialYield)

    if trialYield - price <= 1 and trialYield - price >= -1:
      return round(initialYield, 2)
    
    initialYield += 0.01

# Input cash flow and the price
print(calcMultipleYield([[1, 2000], [2, 2000], [3, 2500], [4, 4000]], 7077))
