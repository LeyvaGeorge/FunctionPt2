# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3=0):
    x = max(num1, num2, num3)
    return x


# print(max_num(5,56,23))


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(*nums):
    ans = 0

    def multiply(x, y):
        return x * y

    for number in nums:
        if ans == 0:
            ans = number
        else:
            ans = multiply(ans, number)
    return ans


# print( mult_list(4,3,5))
# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    list = ""
    for letter in str:
        list = letter + list
    return list


# print(rev_string("This needs to be reversed"))


# Write a Python function called num_within() to check whether a number falls in a given range.
#    The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#    Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(*nums):
    success = True

    for number in nums:
        if number > 5 and number < 10:
            success = success
        else:
            success = False
    return success


# print(num_within(7,8,6))

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    # fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
       # create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev) + 1
      for i in range(length):
        # first number is 1
        if i == 0:
          row.append(1)
          # intermediate nunmbers get added from previous rows
        elif i > 0 and i < length - 1:
          row.append(
          triangle[row_number - 1][i - 1] + triangle[row_number - 1][i]
          )
          # last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    # print triangle
    for row in triangle:
      print(row)
