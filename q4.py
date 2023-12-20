def generate_bruckner(n):
    # Base case, if n < 2
    if n < 2:
        return []

    # Initialize variables
    output = []

    # Initialize an empty list of lists with n rows and n columns
    for i in range(n):
        output.append([])

    # Updated first row of output to be from n to 1
    for i in range(n, 0, -1):
        output[0].append(i)

    # Loop for each row (1 to n)
    for CurrentRow in range(1, n):
        currentIndex = 0  # Reset currentIndex at the beginning of each row

        # Loop for each column (0 to n-1)
        for j in range(n):
            # Check if current index is at the end of the row
            if currentIndex == n:
                break  # Break the column loop if currentIndex exceeds n

            # Initialize tempValue to n (largest value)
            tempValue = n

            # Check if tempValue exists in the same index as currentIndex in all the previous lists within the list
            while any(tempValue == output[i][currentIndex] for i in range(CurrentRow)):
                # If it does, decrement tempValue until it doesn't
                tempValue -= 1

            # Check if tempValue exists in rows above (same index)
            while tempValue in output[:CurrentRow]:
                # If it does, decrement tempValue until it doesn't
                tempValue -= 1

            # Check if tempValue exists in indices before currentIndex in the current row
            while tempValue in output[CurrentRow][:currentIndex]:
                # If it does, decrement tempValue until it doesn't
                tempValue -= 1

            # Append tempValue to output list with the correct index and row (which list within the list)
            output[CurrentRow].append(tempValue)

            # Increment index for the next column
            currentIndex += 1

    # Return the output
    return output

print(generate_bruckner(4))
