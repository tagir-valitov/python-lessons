def is_even(number):
    return number % 2 == 0
if __name__ == '__main__':
    print(is_even(7))
    print(is_even(8))
    numbers = [100, 107, -83, 0]
    for i in numbers:
        print(is_even(i))

    list_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in list_numbers:
        for j in i:
            print(j, end=', ')
        print()


    def matrix(mat):
        for i in mat:
            for j in i:
                print(j, end=', ')
            print()
    print(matrix([[1, 2, 38], [0], [7, 8, 9]]))


    def is_palindrome(number):
        return str(number) == str(number)[::-1]
    print(is_palindrome(121))
    print(is_palindrome(456))




    class Solution(object):
        def climbStairs(self, n):
            if n <= 2:
                return n
            x= 1
            y = 2
            z= 0
            for i in range(2, n):
                z=x+y
                x=y
                y=z
                return z


    a = -24
    b = -52
    a += b
    b = a - b
    a = a - b
    print(a, b)
