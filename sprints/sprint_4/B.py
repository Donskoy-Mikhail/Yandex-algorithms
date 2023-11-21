from A import calculate_polynomial_hash
a = 1000
m = 123987123
#
#
# def modinv(a, m):
#     return pow(a, -1, m)  # Calculate modular inverse using built-in pow function
#
#
# x = 342525  # You can choose any value from 1 to m-1
# y = (x * modinv(a, m)) % m
#
# string_x = 's' + 'a' * 999  # Create a string with first character x mod 128 and 999 'a' characters
# string_y = 's' + 'b' * 999  # Create a string with first character y mod 128 and 999 'b' characters
#
# print(string_x)
# print(string_y)
print(calculate_polynomial_hash("ezhgeljkablzwnvuwqvp", a, m))
print(calculate_polynomial_hash("gbpdcvkumyfxilrgnqrv", a, m))