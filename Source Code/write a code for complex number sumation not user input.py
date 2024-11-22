def complex_sum(c1, c2):
  """Adds two complex numbers."""
  real_part = c1.real + c2.real
  imaginary_part = c1.imag + c2.imag
  return complex(real_part, imaginary_part)

# Example usage with pre-defined complex numbers
complex_num1 = 2 + 3j
complex_num2 = 1 - 1j

sum_result = complex_sum(complex_num1, complex_num2)
print(f"The sum of {complex_num1} and {complex_num2} is: {sum_result}")