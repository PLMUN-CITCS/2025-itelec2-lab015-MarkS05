# Filename: while_loop_sentinel.py

# Step 1: Initialize the sum variable
total_sum = 0

# Step 2: Start a while loop that continues indefinitely
while True:
    
    # Step 3: Prompt the user for input
    user_input = input("Enter a number (or 'stop' to finish): ")
    
    # Step 4: Check if the sentinel value 'stop' is entered
    if user_input.strip().lower() == "stop":
        break  # Exit the loop
    
    # Step 5: Convert input to a number and add to total_sum (with error handling)
    try:
        number = float(user_input)  # Convert user input to a float
        total_sum += number  # Add the number to the total sum
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")
        continue  # Skip the rest of the loop and prompt for input again

# Step 6: Print the final total sum
print("The total sum