def calculatefinance (monthlyincome,taxrate,currency):
    monthlytax:float =monthlyincome*(taxrate/100)
    monthly_net_income:float = monthlyincome-monthlytax
    yearly_tax:float = monthlytax*12
    yearly_income:float = monthlyincome*12
    yearly_net_income:float = yearly_income-yearly_tax

    print(f'Monthly income: {currency}{monthlyincome:,.2f}')
    print(f'Tax rate: {taxrate:,.0f}%')
    print(f'Monthly tax: {currency}{monthlytax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency}{yearly_income:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')

def main() -> None:
    monthly_income = float(input('Enter your monthly income: '))
    tax_rate = float(input('Enter your tax rate (%): '))

    calculatefinance(monthly_income, tax_rate, currency='Rs')


if __name__ == "__main__":
    main()   
