import random

def coin_toss(num_coins):
    results = []
    for _ in range(num_coins):
        result = random.choice(['Heads', 'Tails'])
        results.append(result)
    return results

while True:
    try:
        num_coins = int(input("Enter the number of coins to toss: "))
        if num_coins <= 0:
            print("Number of coins must be positive.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

toss_results = coin_toss(num_coins)
print(f"Coin toss results: {toss_results}")

