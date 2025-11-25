# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
result = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(result)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first = 'Coding'
second = 'For'
third = 'All'
all_sum = first + ' ' + second + ' '+ third
print(all_sum)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.title())
print(company.swapcase())
print(company.capitalize())

# 9. Cut(slice) out the first word of Coding For All string.
first_word = company[:6]
print(first_word)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))
print(company.index('Coding'))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12. Change Python for All to Python for Everyone using the replace method or other methods.
text = 'Python For All'
print(text.replace('Python For All', 'Python For Everyone'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
new_text = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(new_text.split(','))

# 15. What is the character at index 0 in the string Coding For All.
print(company[0])

# 16. What is the last index of the string Coding For All.
last_index = len(company) -1
print(last_index)

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = ''.join(word[0].upper() for word in text.split())
print(acronym) 

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
abb = ''.join(word[0].upper() for word in company.split())
print(abb)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
new_company = 'Coding For All People'
print(new_company.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = 'You cannot end a sentence with because because because is a conjunction'
print(text.find('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(text.rindex('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase = 'because because because'
start = text.index(phrase)
end = start + len(phrase)
print(text[start:end])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(text.find('because'))

# 27. Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# 29. Does 'Coding For All' end with a substring coding?
print(company.endswith('Coding'))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
given_string = '    Coding For All    '
print(given_string.strip())

# 31. Which one of the following variables return True when we use the method isidentifier():
#  - 30DaysOfPython
#  - thirty_days_of_python
value1 = '30DaysOfPython'
value2 = 'thirty_days_of_python'
print(value1.isidentifier())
print(value2.isidentifier())

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list_of =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '#'.join(list_of)
print(result)

# 33. Use the new line escape sequence to separate the following sentences.
#  - I am enjoying this challenge.
#  - I just wonder what is next.
sentence1 = '\n I am enjoying this challenge.'
sentence2 = '\n I just wonder what is next.'
print(sentence1)
print(sentence2)

# 34. Use a tab escape sequence to write the following lines
#  - Name      Age     Country   City
#  - Asabeneh  250     Finland   Helsinki
sentence1 = 'Name\tAge\tCountry\tCity'
sentence2 = 'Asabeneh\t250\tFinland\tHelsinki'
print(sentence1)
print(sentence2)

# 35. Use the string formatting method to display the following:
#   - radius = 10
#   - area = 3.14 * radius ** 2
#   - The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
result = 'The area of the circle with radius {} is {} meters square.'.format(10,area)
print(result)

# 36. Make the following using string formatting methods:
#   - 8 + 6 = 14
#   - 8 - 6 = 2
#   - 8 * 6 = 48
#   - 8 / 6 = 1.33
#   - 8 % 6 = 2
#   - 8 // 6 = 1
#   - 8 ** 6 = 262144
print('{0} + {1} = {result}'.format(8,6,result=8+6))
print('{0} - {1} = {result}'.format(8,6,result=8-6))
print('{0} * {1} = {result}'.format(8,6,result=8*6))
print('{0} / {1} = {result}'.format(8,6,result=8/6))
print('{0} % {1} = {result}'.format(8,6,result=8%6))
print('{0} // {1} = {result}'.format(8,6,result=8//6))
print('{0} ** {1} = {result}'.format(8,6,result=8**6))