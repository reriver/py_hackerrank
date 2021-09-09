def solve(meal_cost, tip_percent, tax_percent):
    tip_p = float(tip_percent) / 100.0
    tip = meal_cost * tip_p
    tax_p = float(tax_percent) / 100.0
    tax = meal_cost * tax_p
    total = meal_cost + tip + tax
    int_total = int(round(total))
    print(int_total)


if __name__ == '__main__':
    main_cost = float(input())
    main_tip = int(input())
    main_tax = int(input())
    solve(main_cost, main_tip, main_tax)

