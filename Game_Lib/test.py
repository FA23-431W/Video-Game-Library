from itertools import permutations
from fractions import Fraction

# Define the characteristic function for the game as a dictionary for easy access
V_game_dict = {
    (): Fraction(0),
    (1,): Fraction(0),
    (2,): Fraction(0),
    (3,): Fraction(0),
    (1, 2): Fraction(3, 4),
    (1, 3): Fraction(3, 4),
    (2, 3): Fraction(1, 4),
    (1, 2, 3): Fraction(1)
}

# Define the permutations of players joining the coalition
player_permutations = list(permutations([1, 2, 3]))

# Initialize the sums of marginal contributions for each player
marginal_contributions = {1: 0, 2: 0, 3: 0}

# Helper function to calculate the marginal contribution of a player
def calculate_marginal_contribution(player, coalition, V_game):
    # Ensure the coalition is sorted for consistent key access
    coalition_sorted = tuple(sorted(coalition))
    coalition_without_player = tuple(sorted(set(coalition_sorted) - {player}))
    # Calculate and return the marginal contribution
    return V_game[coalition_sorted] - V_game.get(coalition_without_player, 0)

# Calculate the marginal contributions for each player in each permutation
for perm in player_permutations:
    coalition = ()
    for player in perm:
        # Calculate the marginal contribution for the current player
        marginal_contribution = calculate_marginal_contribution(player, coalition + (player,), V_game_dict)
        marginal_contributions[player] += marginal_contribution
        # Add the current player to the coalition
        coalition += (player,)

# Calculate the Shapley values by averaging the sums of the marginal contributions
shapley_values_corrected = {player: Fraction(marginal_contributions[player], len(player_permutations)) for player in marginal_contributions}

# Print the Shapley values
print(shapley_values_corrected)
