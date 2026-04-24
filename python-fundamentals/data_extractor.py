import re

text = """
Hello TEAM,

Please contact us at support@gmail.com or admin123@company.co.in for assistance.
You can also reach out to john.doe@service.org for technical queries.

Call us at +91-9876543210, 98765 43210, or (123) 456-7890 for immediate help.

Visit our websites:
https://www.example.com
http://testsite.org/page
https://sub.domain.co.in/home

Important dates:
Project start: 01/09/2025
Deadline: 2025-12-31
Meeting: 15/08/2024

Pricing details:
Basic plan: ₹499
Premium plan: ₹1,999
International plan: $49.99
Discount offer: $10

IMPORTANT NOTICE:
ALL USERS MUST VERIFY THEIR EMAIL BEFORE ACCESS.
SYSTEM MAINTENANCE WILL OCCUR AT MIDNIGHT.

Thank you,
ADMIN TEAM
CUSTOMER SUPPORT
"""

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email = re.findall(email_pattern, text)
    return email

def extract_phone_numbers(text): #+91-9876543210, 98765 43210, or (123) 456-7890
    phone_pattern = r'(?:\+\d{1,3}[- ]?)?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}|\d{5}[- ]?\d{5}'
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers

def urls(text):
    url_pattern = r'https?://[^\s]+'
    urls = re.findall(url_pattern, text)
    return urls

def dates(text):
    date_pattern = r'\b\d{2}[/-]\d{2}[/-]\d{4}\b|\b\d{4}-\d{2}-\d{2}\b'
    dates = re.findall(date_pattern, text)
    return dates

def prices(text):
    price_pattern = r'₹\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    prices = re.findall(price_pattern, text)
    return prices

def all_caps(text):
    all_caps_pattern = r'\b[A-Z\s]+\b'
    all_caps_words = re.findall(all_caps_pattern, text)
    return all_caps_words

d_email = extract_emails(text)
d_phone = extract_phone_numbers(text)
d_urls = urls(text)
d_dates = dates(text)
d_prices = prices(text)
d_all_caps = all_caps(text)

print(f"Extracted Emails: {d_email}")
print(f"Extracted Phone Numbers: {d_phone}")
print(f"Extracted URLs: {d_urls}")
print(f"Extracted Dates: {d_dates}")
print(f"Extracted Prices: {d_prices}")
print(f"Extracted All Caps Words: {d_all_caps}")

def redact(text):
    redacted_text = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[REDACTED]', text)
    redacted_text = re.sub(r'(?:\+\d{1,3}[- ]?)?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}|\d{5}[- ]?\d{5}', '[REDACTED]', redacted_text)
    redacted_text = re.sub(r'₹\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?', '[REDACTED]', redacted_text)
    return redacted_text

redacted_text = redact(text)
print("\nRedacted Text:\n", redacted_text)