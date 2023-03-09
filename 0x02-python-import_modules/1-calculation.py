#!/usr/bin/python3

if __name__ == '__main__':
    # import module
    import calculator_1 as cal

    a = 10
    b = 5

    print(f"{a} + {b} = {cal.add(a, b)}")
    print(f"{a} - {b} = {cal.sub(a, b)}")
    print(f"{a} * {b} = {cal.mul(a, b)}")
    print(f"{a} / {b} = {cal.div(a, b)}")

