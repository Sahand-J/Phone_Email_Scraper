#!/bin/bash
import re,pyperclip

# Creating regex for phone numbers
phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-000, 555-0000 ext 123, ext. 1234, x1234
(

((\d\d\d)|(\(\d\d\d\)))?    #area code (optional with or w/out parens)

(\s|-)                      #first dash (or space)

\d\d\d                      #first 3 digits

-                           #second dash

\d\d\d\d                    #last 4 digits

(((ext(\.)?\s)|x)           #extention (optional)

(\d{2,5}))?                 #extention number

)

''', re.VERBOSE)

# Create a regex for emails
emailRegex= re.compile(r'''
#something._+@somethings.com/edu/gov/net

[a-zA-Z0-9_.+]+       #name (alphabet group of text symbols and numbers)

@                     #@

[a-zA-Z0-9_.+]+       #domain name (alphabet group of text symbols and numbers)

''',re.VERBOSE)

#Getting the text off the clipboard
text = pyperclip.paste()

#Extracting the emails/phone nums from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

#extracting the first phone number in each touple for a cleaner output
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmail)

#Copy the extracted phones/emails to clipboard
#joins everything onto one string, one phone number per line
result ='\n'.join(allPhoneNumbers) +'\n'+'\n'.join(extractedEmail)
pyperclip.copy(result) #can paste result

