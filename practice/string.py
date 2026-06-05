# Here are **10 carefully chosen questions** that cover most of the important string methods 

# ### 1. Customer Name Cleaning

# A dataset contains customer names with extra spaces and inconsistent capitalization.

# ```python
# name = "   jOhN smITh   "
# ```

# Clean the name so it is properly formatted.

# ---

name = "   jOhN smITh   "

proper_name=name.strip().title()
print(f'This is a proper name {proper_name}')

# ### 2. Email Standardization

# A dataset contains email addresses in different cases.

# ```python
# email = "John.Smith@GMAIL.COM"
# ```

# Convert the email into a standard format and extract the username and domain separately.
email = "John.Smith@GMAIL.COM"
convert=email.lower()
print(convert)

username,domain = convert.split('@')

print(username)
print(domain)

# ---

# ### 3. Product Category Processing

# You receive product categories as a comma-separated string.

# ```python
# categories = "Electronics,Mobile,Accessories,Laptop"
# ```

# Convert it into a list and determine how many categories exist.

categories = "Electronics,Mobile,Accessories,Laptop"

categories_ls = categories.split(',')
print(categories_ls)

# ---

# ### 4. Customer Review Analysis

# A review is given as:

# ```python
# review = "good product good quality good service"
# ```

# Find how many times the word `"good"` appears and determine whether the review contains the word `"service"`.
review = "good product good quality good service"

c=review.count('good')
d = "service" in review
print(c)
print(d)

# ---

# ### 5. Date Processing

# A dataset contains dates in the format:

# ```python
# date = "2025-08-15"
# ```

# Extract the year, month, and day separately.
date = "2025-08-15"
year,month,day = date.split('-')
print(year)
print(month)
print(day)
# ---

# ### 6. Product Code Cleaning

# A dataset contains product codes like:

# ```python
# code = "prd-001"
# ```

# Convert the code into a standardized format by removing special characters and making all letters uppercase.
code = "prd-001"
codes=code.upper()
codes = codes.replace('-','')
print(codes)
# ---

# ### 7. Phone Number Validation

# A dataset contains phone numbers stored as strings.

# ```python
# phone = "9841234567"
# ```

# Check whether the value contains only digits and whether its length is valid.
phone = "9841234567"
phone.isdigit()

if len(phone) == 10:
    print('It is valid')

# ---

# ### 8. File Name Validation

# A list of files contains:

# ```python
# file_name = "sales_data_2025.csv"
# ```

# Check whether the file starts with `"sales"` and ends with `".csv"`.
file_name = "sales_data_2025.csv"
starrt_file =file_name.startswith('sales')
print(starrt_file)
end_file = file_name.endswith('.csv')
print(end_file)
# ---

# ### 9. Text Cleaning for NLP

# A customer feedback text contains extra spaces and punctuation.

# ```python
# text = "  Data Science is AWESOME!!!  "
# ```

# Clean the text by removing spaces, converting it to lowercase, and removing the exclamation marks.
text = "  Data Science is AWESOME!!!  "
cleaned_text = text.strip().lower().replace('!','')
cleaned_texts = text.strip().capitalize().replace('!','')

print(cleaned_text)
print(cleaned_texts)

# ---

# ### 10. Word Frequency Analysis

# A text dataset contains:

# ```python
# text = "python data science python analytics python"
# ```

# Split the text into words and create a frequency count for each word.

# ---
text = "python data science python analytics python"

split_text = text.split(" ")
print(split_text)

count = 0


 


