def playSegments(coins):
    n = len(coins)
    
    # Calculate Player 2's final score
    player2_score = sum(1 if coin == 1 else -1 for coin in coins)
    
    # Initialize variables to determine the minimum segments Player 1 needs to play
    min_segments = float('inf')
    current_score = 0
    
    # Iterate over segments and calculate Player 1's score
    for i in range(n):
        if coins[i] == 1:
            current_score += 1
        else:
            current_score -= 1
        
        # Check if Player 1's score is greater than Player 2's score
        if current_score > player2_score:
            min_segments = min(min_segments, i + 1)
    
    return min_segments if min_segments != float('inf') else 0

# Sample input
coins = [1, 0, 0, 1, 0]
print(playSegments(coins))  # Output: 2