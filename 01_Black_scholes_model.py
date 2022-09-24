import numpy as np
from scipy.stats import norm

r = float(input("Enter the interest rate="))
S = float(input("Enter the spot price of the asset="))
K = float(input("Enter the strike price ="))
time = int(input("Enter the number of days the asset is present in the market="))
T = time/365
volatility = float(input("Ente the volatility rate in % ="))
sigma = volatility/100

def blackscholes(r, S, K, T, sigma, type="C"):
    # Calculating the BlackScholes option price for call/put
    d1 = (np.log(S/K) + (r + (sigma**2/2))*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))
    if type == "C":
        price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        return price
    elif type == "P":
        price2 = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price2
    else:
        print("Please repeat the program again!!!")
option = input("Enter C for call and P for put:")
a = blackscholes(r,S,K,T,sigma, option)
print(f"The option price is: {round(a,2)}")