import re

# Text data for parsing
text = "Sample text with a phone number: 123-456-7890 and an email address: example@email.com"

# Define patterns for phone number and email extraction
phone_pattern = r'\d{3}-\d{3}-\d{4}'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Search for phone number and email in the text
phone_number = re.search(phone_pattern, text)
email_address = re.search(email_pattern, text)

# Print the extracted phone number and email
if phone_number:
    print("Phone Number:", phone_number.group())

if email_address:
    print("Email Address:", email_address.group())