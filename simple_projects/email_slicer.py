input_email = input("Please provide your email: ")

(username, domain_name) = input_email.split("@")
(email_provider, extension) = domain_name.split(".")

print(f"Your username is '{username}'.")
print(f"You email provider is {email_provider}.")
print(f"The extension being used is {extension}.")