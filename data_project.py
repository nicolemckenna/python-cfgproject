import csv

# define function for reading spreadsheet
def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


# using read function to print each month and sale value
def run():
    data = read_data()

    for row in data:
        print(row['sales'], row['month'])
run()


# Calculation to get total sales
def run():
    data = read_data()

    sales =[]
    for row in data:
        sale =int(row['sales'])
        sales.append(sale)
    total = sum(sales)
    print('Total sales: {}'.format(total))
run()


# calculation of average sale value
def run():
    data = read_data()

    sales =[]
    for row in data:
        sale =int(row['sales'])
        sales.append(sale)
    average = sum(sales)/12
    print('Average sale: {}'.format(round(average)))
run()

# minimum and maximum sale values
def run():
    data = read_data()

    sales =[]
    for row in data:
        monthly_sales = row['sales']
        sales.append(monthly_sales)
    min_sales = min(sales)
    print('Minimum sale value: {}'.format(min_sales))
run()


def run():
    data = read_data()

    sales =[]
    for row in data:
        monthly_sales = row['sales']
        sales.append(monthly_sales)
    max_sales = max(sales)
    print('Maximum sale value: {}'.format(max_sales))
run()

# calculating if there was a profit or loss
def run():
    data = read_data()

    for row in data:
        monthly_sales = int(row['sales'])
        monthly_expenditure = int(row['expenditure'])
        monthly_profit_or_loss = monthly_sales - monthly_expenditure

        if monthly_profit_or_loss > 0:
            print('There was a profit of {}'.format(monthly_profit_or_loss), 'during', row['month'])

        elif monthly_profit_or_loss < int('0'):
            print('There was a loss of {}'.format(monthly_profit_or_loss), 'during', row['month'])
run()


# calculating profit/loss percentage
def run():
    data = read_data()

    for row in data:
        monthly_sales = int(row['sales'])
        monthly_expenditure = int(row['expenditure'])
        monthly_profit_or_loss = monthly_sales - monthly_expenditure
        profit_percent = monthly_profit_or_loss / int(row['sales'])
        profit_percentage = profit_percent *100
        loss_percent = monthly_profit_or_loss / int(row['expenditure'])
        loss_percentage = loss_percent *100

        if monthly_profit_or_loss > 0:
            print('The profit margin is {} %'.format(round(profit_percentage)), row['month'])
        elif monthly_profit_or_loss < 0:
            print('There was a loss of {} %'.format(round(loss_percentage)), 'during', row['month'])
run()
