    
username = "Stefnaos"
has_upper = any(letter.isupper() for letter in username)
has_lower = any(letter.islower() for letter in username)

print(has_lower) ## Got it so this returns a True statement
print(has_upper) ##
if not (has_upper and has_lower): # So this is saying if Not True
    raise ValueError("Issue here with casing")
else:
    print("Nice")
