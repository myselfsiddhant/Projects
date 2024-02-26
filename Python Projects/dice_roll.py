import random

def dice(num_dice, num_sides):
      return [random.randint(1, num_sides) for _ in range(num_dice)]
  
while True:
  try:
    num_dice = int(input("Enter the number of dice to roll: "))
    num_sides = int(input("Enter the number of sides in the dice: "))
    break
  except ValueError:
    print("Invalid input. Please enter positive integers only.")

dice_results = dice(num_dice, num_sides)
print(f"Dice roll results: {dice_results}")
