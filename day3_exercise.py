#greeting = "Hello, {}"

#concatenation:

#print(greeting + "!" )

#format:
#greeting2 ="Hello, world{}"

#output = "{0} is a Femal. she is a indepandent {1}. she wanna be a {2}.{0} want to go BD."
#print(output.format("arin", "women", "DevOps Engineer"))
#print(greeting2.format("!"))

#F-string:
"""character = "!"
print(f"Hallo, world{character}")"""
#2nd Task:
"""name = input("Enter the name:").strip().title()
character = "!"
print(f"Hallo,{name}{character}")

age = input(str("Enter the age please:"))
output1 = f"I am {age}. "
output2 = "MY mobile number is {}". format(input(str("enter the number:")))

print(output1 + output2)"""

#Task3 : Format and print the information below using string interpolation:
"""q:title = "Joker"
director = "Todd Phillips"
release_year = 2019

The output should look like this:

Joker (2019), directed by Todd Phillips"""


print("{title} ({release_year}) directed by {director}". format(title = "Joker",director = "Todd Phillips",release_year = 2019))


