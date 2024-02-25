import random

# Define constants for minimum and maximum numbers in the lottery game
MIN_NUM = 1
MAX_NUM = 45
NUM_PER_QUICK_PICK = 6

# Function to generate a single quick pick
def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUM, MAX_NUM + 1), NUM_PER_QUICK_PICK))

def main():
    num_quick_picks = int(input("How many quick picks? "))

    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))

# Entry point of the program
if __name__ == "__main__":
    main()