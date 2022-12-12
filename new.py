import random

# Function to generate a random phone number
def generate_phone_number():
  # Randomize the first three digits
  first_digits = str(random.randint(100, 999))
  
  # Randomize the last seven digits
  last_digits = str(random.randint(1000000, 9999999))
  
  # Return the phone number in the format "XXX-YYYYYYY"
  return first_digits + "-" + last_digits
  
# Generate 1000 phone numbers
phone_numbers = []
for i in range(1000):
  phone_number = generate_phone_number()
  phone_numbers.append(phone_number)
  
# Print the first 10 phone numbers
print(phone_numbers[:10])
