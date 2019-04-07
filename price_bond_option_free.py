def pvCoupon(coupon, numOfYears, parValue, reqYield):
    semiAnnualCouponPayment = (coupon / 200)
    interestPayment = semiAnnualCouponPayment * parValue

    numOfInterestPayments = numOfYears * 2
    sixMonthInterestRate = (reqYield / 200)

    fractionCalculation = (1 - ( 1 / (pow(1 + sixMonthInterestRate, numOfInterestPayments)) )) / sixMonthInterestRate

    return semiAnnualCouponPayment * fractionCalculation * 1000

def pvMaturity (coupon, numOfYears, maturity, reqYield):
    return maturity * ( 1 / (pow(1 + (reqYield / 200), numOfYears * 2)))

# Assumes the coupon payment is semi annual
def calc_price(coupon, numOfYears, parValue, reqYield):
    return pvCoupon(coupon, numOfYears, parValue, reqYield) + pvMaturity(coupon, numOfYears, parValue, reqYield)

print(calc_price(9, 14, 1000, 7))