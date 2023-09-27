from re import findall


class NameTooShortError(Exception):  # Note (Exception) inherits all the functionality of the Exception class
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH_NAME_MAIL = 4
VALID_DOMAINS = (".com", ".bg", ".org", "net")
pattern_name = r"\w+"
pattern_domain = r"\.[a-z]+"

email = input()
while email != "End":
    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Valid email contains only one @ symbol!")
    if len(email.split("@")[0]) < MIN_LENGTH_NAME_MAIL:
        raise NameTooShortError("Name must be more than 4 characters!")
    if findall(pattern_name, email)[0] != email.split("@")[0]:  # [name; domain_name; domain]
        raise InvalidNameError("Name may contain only letters, digits and underscores!")
    if "@" not in email:
        raise MoreThanOneAtSymbolError("Email must contain @ symbol")
    if findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    email = input()
