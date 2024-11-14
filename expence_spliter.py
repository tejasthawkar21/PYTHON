def calcsplit(total_amount, no_of_people):
    if no_of_people<1:
        raise ValueError("number of people must be greater than 1.")
    
    share_per_person: float = total_amount/no_of_people

    print(f'Total Expense:{total_amount:,.2f}')
    print(f'Total No. of people:{no_of_people}')
    print(f'Share of Each Person:{share_per_person:,.2f}')

def main():
    try:
        total_amount= float (input("enter the amount of the expense:"))
        no_of_people= int(input("enter the no. of people:"))

        calcsplit(total_amount,no_of_people)

    except ValueError as e:
        print(f'Error:{e}')

if __name__ == '__main__':
    main()
