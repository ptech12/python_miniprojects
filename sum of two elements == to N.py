# Python program to find if there are
# two elements wtih given sum

# function to check for the given sum
# in the array
def printPairs(arr, arr_size, sum):
    # Create an empty hash set
    s = set()

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp in s):
            print("Pair with given sum " + str(sum) +
                  " is (" + str(arr[i]) + ", " + str(temp) + ")")
        s.add(arr[i])


# driver code
N = int(input())
arr = list(map(int, input().strip().split()))[:N]
n = int(input())
printPairs(arr, len(arr), n)

# This code is contributed by __Devesh Agrawal__
