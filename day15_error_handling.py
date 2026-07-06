 # error handling

'''
NameError
ValueError
TypeError
IndexError
AttributesError
'''

# a = 10
# print(A)

try:
    a = 10
    print(a)

except NameError as e:
    print(e)

except TypeError as e:
    print(e)
except Exception as e:
    print(e)
    print("Something went wrong")
finally:
    print("Succesfully called")

