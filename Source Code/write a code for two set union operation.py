def set_union(set1, set2):
  """Performs the union operation on two sets."""
  return set1 | set2

# Example usage:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_result = set_union(set1, set2)
print("Union of set1 and set2:", union_result)