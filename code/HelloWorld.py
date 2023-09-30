def check_dir(variable):
    print(dir(variable))

def return_multiple():
    """ Returnerar 3 variabler av olika typer """
    a = "anka"
    b = 3
    c = ['Tre ankor i kostym']

    return a, b, c



    #added_digits = perform_addition(a=10, b=11)
    a = []
    b = 5
    print(f"This is my variable value: {a}, and this is the variable b: {b}")


    my_string, my_digit, my_list = return_multiple()
    print(my_string, my_digit, my_list) 
  


def main():
    my_dict = {"key1": 1, "key2": 1337}
 

    for i in range(1, 10):
        #print(i)
        pass

    for key, value in my_dict.items():
        #print(key)
        #print(value)
        pass

    my_list = ["Anton", "Adrian", "Anna"]

    for i, e in enumerate(my_list):
        print(i)
        print(e)
if __name__ == "__main__":
    main()
