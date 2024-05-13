def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def findNextPrime(curr):
        next_prime = curr + 1
        while not isPrime(next_prime):
            next_prime += 1
        return next_prime

    # Helper function to simulate the game for a given round
    def simulateGame(num):
        # If the number is even, Maria wins
        if num % 2 == 0:
            return "Maria"
        # If the number is odd and prime, Ben wins
        if isPrime(num):
            return "Ben"
        # Otherwise, determine the winner based on the next prime number
        next_prime = findNextPrime(num)
        # If the next prime is odd, Maria wins
        if next_prime % 2 != 0:
            return "Maria"
        # Otherwise, Ben wins
        return "Ben"

    # Count the number of wins for each player
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        winner = simulateGame(num)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: "Ben"

