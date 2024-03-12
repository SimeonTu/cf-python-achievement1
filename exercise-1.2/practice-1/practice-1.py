f = open('practice-1.txt', 'r') #read text file
lines = f.readlines() #[1000\n, 0.145\n, 3]
[principal, rate, time_period] = [x.strip('\n') for x in lines] #equivalent to "lines[0].strip('\n'), lines[1].strip('\n'), lines[2].strip('\n')
f.close()

principal = float(principal) #1000 - initial amonut borrowed
rate = float(rate) #0.145 - interest rate
time_period = float(time_period) #3 - amount of time in years over which the borrowed amount is repaid

ratePercent = rate / 100

compound = 1

compounded_principal = principal * (1 + ratePercent / compound) ** (compound * time_period)

print(round(compounded_principal, 2)) # 1004.36