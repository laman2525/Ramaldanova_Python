def check_number(num):
    if num > 7:
        print("Hello")


def check_name(name):
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")


def filter_multiples_of_three(arr):
    multiples = [x for x in arr if x % 3 == 0]
    print("Elements that are multiples of 3:", multiples)


def main():
    try:
        num = int(input("Enter a number: "))
        check_number(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    name = input("Enter a name: ")
    check_name(name)

    try:
        arr_input = input("Enter numbers separated by spaces: ")
        arr = list(map(int, arr_input.strip().split()))
        filter_multiples_of_three(arr)
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")


if __name__ == "__main__":
    main()
