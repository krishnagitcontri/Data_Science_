# @author: 22000214 - Abhiraj Chaudhuri
# @description: Program No. 7. Create a function that grabs the email website domain from a string in the form:
# "user@domain.com"
# So for example, passing "user@domain.com" would return: domain.com

def get_domain(email):
    user, domain = email.split("@")
    return domain

email_address = "user@domain.com"
result = get_domain(email_address)
print(result)

#output: domain.com