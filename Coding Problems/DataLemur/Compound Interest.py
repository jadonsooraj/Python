# create a compound interest calculator,calculate the final amount you’ll have after the specified number of years, with annual compounding. In other words, at the end of each year, you’ll earn interest on your current balance, then make an additional contribution.
def compound_vale(data:list)-> float:
    principal=data[0]
    rate=data[1]/100
    contribution=data[2]
    years=data[3]

    principal_growth=principal*((1+rate)**years)
    
    # contributions form a geometric series, not simple compound interest
    contribution_growth = contribution * (((1 + rate) ** years - 1) / rate)

    return round(principal_growth + contribution_growth, 2)

if __name__=='__main__':
    
    # principal, rate, contribution at end of year, years
    investment_data=[500,10,50,3]
    print(f'Investment value: {compound_vale(investment_data)}')