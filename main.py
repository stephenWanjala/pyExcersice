def decode_message(message_file):
    # Define a dictionary to map numbers to words
    number_to_word = {}

    # Read the file line by line
    with open(message_file, 'r') as file:
        for line in file:
            # Split each line into number and word
            parts = line.strip().split()
            if len(parts) == 2:
                number = int(parts[0])  # Convert number to integer
                word = parts[1]

                # Map the number to the word
                number_to_word[number] = word

    sorted_keys = sorted(number_to_word.keys())
    # Initialize the counter
    counter = 0

    # Initialize a list to store the pyramid rows
    pyramid = []

    # Iterate over the sorted keys
    for i in range(1, len(sorted_keys)):
        # Initialize a list to store values for the current row
        row_values = []

        # Gather the corresponding number of elements for each line
        for j in range(i):
            if counter < len(sorted_keys):
                row_values.append(number_to_word[sorted_keys[counter]])
                counter += 1
        pyramid.append(row_values)
    last_elements = [inner_list[-1] for inner_list in pyramid if inner_list]
    print(" ".join(last_elements))


# Example usage:
file_path = 'encoded_message.txt'
decode_message(file_path)
