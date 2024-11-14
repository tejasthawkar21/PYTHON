from forex_python.converter import CurrencyRates

def currency_convertor(amount,from_currency,to_currency):
    c = CurrencyRates()
    rate=c.convert(from_currency,to_currency,amount)
    return rate

def main():
    amount=int(input("Enter the Amount :"))
    from_currency=input("From Currency :").upper()
    to_currency=input("To Currency :").upper()

    converted_amount=currency_convertor(amount,from_currency,to_currency)

    print(f'{amount}{from_currency} is equal to {converted_amount}{to_currency}')
    
if __name__=='__main__':
    main()
