def format_into_groups(filtered_lines):
    formatted_lines = []
    buffer = []
    found_first_group_start = False  # Flag to indicate when we've found the first "01"

    for line in filtered_lines:
        if not found_first_group_start:
            if line == "01":  # Look for the first "01" to start grouping
                found_first_group_start = True
                buffer.append(line)
            else:  # If it's before the first "01", it's incomplete
                formatted_lines.append(line)
        else:
            buffer.append(line)
            if len(buffer) == 6:  # If buffer size is 6, it's a complete group
                formatted_lines.append(' '.join(buffer))
                buffer = []  # Reset for the next group

    # Append any remaining incomplete group at the end
    if buffer:
        formatted_lines.append(' '.join(buffer))

    return formatted_lines

# Ask the user for the location of the txt file
file_location = input("Please provide the path to the txt file: ").strip('\"')

try:
    with open(file_location, 'r') as file:
        lines = file.readlines()

    # Strip "uart-1: " from each line and filter by the exact content length (adjust if necessary)
    content_length = 2  # Adjust this based on your needs
    filtered_lines = [line.replace("uart-1: ", "").strip() for line in lines if len(line.replace("uart-1: ", "").strip()) == content_length]

    # Format the cleaned lines into 6-byte groups
    formatted_lines = format_into_groups(filtered_lines)

    # Create a new file with "_formatted" at the end of the original file name
    output_file_location = file_location[:-4] + "_formatted.txt"

    # Write the formatted lines to the new file
    with open(output_file_location, 'w') as output_file:
        for line in formatted_lines:
            output_file.write(line + '\n')

    print(f"Formatted lines have been written to {output_file_location}.")

except FileNotFoundError:
    print("File not found. Please provide a valid file location.")
except Exception as e:
    print(f"An error occurred: {e}")
