def tip_calculator():
    # 1º passo: welcome
    print('Welcome to the tip calculator.')
    # 2º passo: perguntar total a pagar
    total_pay = float(input('What was the total bill? $'))
    # 3º passo: escolher percentagem
    percentage = int(input('What percentage tip would you like to give? '))
    # total with percentage
    total_with_percentage = round(total_pay * (1 + (percentage / 100)), 2)
    # 4º passo: dividir o valor em quantas pessoas
    split_bill = int(input('How many people to split the bill? '))
    total_with_split = None
    # Result

    if split_bill == 0:
        return f'The amount to be paid is ${total_with_percentage}'
    else:
        total_with_split = round((total_with_percentage / split_bill), 2)
        return f'Each person should pay: ${total_with_split}'



