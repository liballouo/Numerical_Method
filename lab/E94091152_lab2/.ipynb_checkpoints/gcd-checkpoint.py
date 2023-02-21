def gcd(m:int ,n:int) -> int:
    """ function of finding a greatest common divisor """
    if (n == 0):
        return m
    else:
        return gcd(n, m%n)

if __name__ == "__main__":
    input_data = str(input(''))
    if (input_data == "?gcd"):
        help("gcd")
    else:
        m = int(input_data.split(',', -1))
        n = int(input_data.split(',', 0))
        # input two integers to do the gcd
        m = int(input("Enter the first positive integer (m):"))
        n = int(input("Enter the second positive integer (n):"))
        # the error situation
        if (m == 0 or n == 0):
            print("--------------------------------------\nPlease enter a number greater than 0\n--------------------------------------")
            continue

        print("Greatest common divisor:" + str(gcd(m,n)))
