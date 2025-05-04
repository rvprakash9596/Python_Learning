# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.
input_str = "teeter"
# isme first non-repeated character r hai , remaing characters are repeating , but r is non repeated
print(input_str)
for i in input_str:
    if input_str.count(i)==1:
        print("Non-Repeated Character is :",i)
        break


