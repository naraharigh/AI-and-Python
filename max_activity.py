def max_activities(start, end):
    # Combine start and end into a list of activities and sort by end time
    activities = sorted(zip(start, end), key=lambda x: x[1])

    print(activities)
    
    # Initialize variables
    count = 0
    last_end_time = -1
    
    # Iterate through sorted activities
    for s, e in activities:
        print('s,e',s,e)
        if s >= last_end_time:  # Check if activity can be selected
            count += 1
            last_end_time = e  # Update the last selected activity's end time
    
    return count

# Example usage
start = [1, 3, 2, 5]
end = [2, 4, 3, 6]
print(max_activities(start, end))  # Output: 3
