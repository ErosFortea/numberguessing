import random
random_number = random.randint(1, 10)
user_number = input('elige un numero')

if random_number == int(user_number):
  print(f'you won!! the machine number was{random_number}')
else:
  print(f"the machine number was {random_number} looooser")  
  
