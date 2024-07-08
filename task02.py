import random

def get_numbers_ticket(min, max, quantity):
  unique_num = set()

  if min >= 1 and max <= 1000:

    while len(unique_num) != quantity:
      for i in range(quantity):
        random_num = random.randint(min, max)
        random_num * i

      unique_num.add(random_num)

      if len(unique_num) == quantity:
        print(unique_num)

  else:
    print('Min number must be >= 1 ant Max number must be <= 1000')

get_numbers_ticket(1, 1001, 6)