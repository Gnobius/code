def main():
    sum_variable_plus_one(0)


def sum_variable_plus_one(x=5):  #  du kan sätta x=5 så vet du värdet på x
    """Denna funktion summerar x med sina 3 efterföljande values"""
    increment_by_one_x_times = 4
    sum = 0
    for i in range(increment_by_one_x_times):
        sum = sum + x + i
        print(sum)
    return sum
if __name__=="__main__":
    main()