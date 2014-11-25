Email
=====

To check whether the email is exist or Not?


For this you have to import the module name called validate_email.

$ pip install validate_email

$ pip install pyDNS


USAGE

Basic usage:

from validate_email import validate_email
is_valid = validate_email('example@example.com')

Checking domain has SMTP Server

Check if the host has SMTP Server:

from validate_email import validate_email
is_valid = validate_email('example@example.com',check_mx=True)

Verify email exists

Check if the host has SMTP Server and the email really exists:

from validate_email import validate_email
is_valid = validate_email('example@example.com',verify=True)

In my program you can include lot of email address in input.csv file, After run the py file you will get the output file asap.

Thanks
Ref:https://pypi.python.org/pypi/validate_email
