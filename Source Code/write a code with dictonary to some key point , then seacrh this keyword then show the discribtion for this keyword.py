
def search_keyword(keyword):
    # Sample dictionary (replace with your actual data)
    knowledge_base = {
        "prime number": "A natural number greater than 1 that is not a product of two smaller natural numbers.",
        "even number": "An integer that is exactly divisible by 2.",
        "odd number": "An integer that is not exactly divisible by 2.",
        "dictionary": "A data structure in Python that stores key-value pairs.",
        "key-value pair":"A pair of data items, where the first item is a key and the second item is a value"
    }
    if keyword in knowledge_base:
      return knowledge_base[keyword]
    else:
      return "Keyword not found."
#Example usage
keyword_to_search = input("Enter the keyword you want to search for : ")

description = search_keyword(keyword_to_search)

print(description)