import random

# Generate random phone number
area_code = random.randint(100, 999)
first_three = random.randint(100, 999)
last_four = random.randint(1000, 9999)

phone_number = f"({area_code}) {first_three}-{last_four}"

# Print the phone number
print(phone_number)
