# ### 10 Hard Python List Questions (No Loops)

# 1. **Remove consecutive duplicate elements**

# ```python
# lst = [1, 1, 1, 2, 2, 3, 1, 1, 4]
# ```
lst = [1, 1, 1, 2, 2, 3, 1, 1, 4]

if lst.count(1) > 1 :
    lst.pop(1)
if lst.count(1) > 1 :
    lst.pop(1)
if lst.count(1) > 1 :
    lst.pop(1)
if lst.count(1) > 1 :
    lst.pop(1)

# 2. **Find the second largest unique element**

# ```python
# lst = [5, 8, 3, 8, 9, 9, 2]
# ```
lst_2 = [5, 8, 3, 8, 9, 9, 2]

lst2=sorted(lst_2)
set_list = set(lst2)
lst2 = list(set_list)
print(lst2[-2])




# 3. **Rotate the list to the right by `k` positions**

# ```python
# lst = [1, 2, 3, 4, 5]
# k = 2
# ```

# 4. **Find all elements that appear exactly once**

# ```python
# lst = [1, 2, 2, 3, 4, 4, 5]
# ```


# 5. **Find the missing number from the sequence**

# ```python
# lst = [1, 2, 3, 5, 6, 7]
# ```

# 6. **Find the three largest unique values**

# ```python
# lst = [5, 7, 2, 7, 9, 1, 9, 8]
# ```
lst_3 = [5, 7, 2, 7, 9, 1, 9, 8]
lst_3 = set(sorted(lst_3))
lst_3 = list(lst_3)
print(f'{lst_3[-1]},{lst_3[-2]},{lst_3[-3]}')

# 7. **Rearrange the list by taking elements alternately from the start and end**

# ```python
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ```

# 8. **Find the median of the list**

# ```python
# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# ```

# 9. **Create a new list containing cumulative sums**

# ```python
# lst = [1, 2, 3, 4, 5]
# ```
lst = [1, 2, 3, 4, 5]

lst_new = []



# 10. **Find the third smallest unique element**

# ```python
# lst = [4, 2, 7, 1, 9, 3]
# ```

# **Rule:** No `for` loops, `while` loops, list comprehensions, `map()`, or `filter()`.
