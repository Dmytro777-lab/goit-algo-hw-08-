import heapq


def minimize_connection_cost(cables):
    # Turn the list of cables into a min-heap
    heapq.heapify(cables)

    total_cost = 0  # Total cost of connecting all cables

    # Continue until there's only one cable left in the heap
    while len(cables) > 1:
        # Extract the two smallest cables from the heap
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Calculate the cost of connecting these two cables
        cost = first + second
        total_cost += cost  # Add the cost to the total

        # Add the new connected cable back into the heap
        heapq.heappush(cables, cost)

    return total_cost


# Example input
cables = [4, 3, 2, 6]  # Array of cable lengths
result = minimize_connection_cost(cables)
print(f"Minimum connection cost: {result}")