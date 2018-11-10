#ask for email id

email=input("Please enter your email address: ").strip()

#slice out username

user=email[:email.index("@")]

#slice out domain name

domain=email[email.index("@")+ 1:]

#format message

output="Your username is {} and your email domain is {} ".format(user,domain)

#display message

print(output)
