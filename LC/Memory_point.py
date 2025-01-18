def maximizeTotalMemoryPoints(memory):
    # Step 1: Sort memory points in descending order
    memory.sort(reverse=True)

    # Step 2: Calculate prefix sums and total memory points
    total_points = 0
    prefix_sum = 0
    for points in memory:
        prefix_sum += points
        total_points += prefix_sum

    return total_points

# Example usage
memory = [3, 4, 5]
print(maximizeTotalMemoryPoints(memory))  # Output: 26
# Step 1: Sort memory points in descending order memory = [5, 4, 3]
# Step 2: 5 + (5+4) + (5+4+3) = 26