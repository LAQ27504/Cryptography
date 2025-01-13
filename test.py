import time
import random
number = [52, 2, 39, 17]
result = random.randint(0, 100)
print(result)
while result not in number:
   result = random.randint(0,100)
   print(result)
print(f"Congratulations to number {result}.")
