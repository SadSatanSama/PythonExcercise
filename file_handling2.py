# --- Step 1: Initial File Writing ---
# Use a try block to catch any issues (like permission errors) when creating the file
try:
    # Open 'output.txt' in write mode ('w'). 
    # Warning: 'w' will create the file if it doesn't exist, but it will OVERWRITE any existing data!
    with open('output.txt', 'w') as file:
        text = input("Enter text to write to the file: ")
        file.write(text)
    print("Data successfully written to output.txt.")
except IOError:
    print("Error: An IO error occurred while trying to write to the file.")

# --- Step 2: Interactive Append Feature ---
# Ask the user if they want to continue interacting with the file
choice = input("Do you want to add anything else to this file? (y/n): ")

if choice == 'y':
    # Use a fresh try block for the append operation in case the file got locked or deleted
    try:
        # Open in append mode ('a'). This adds new data to the very end without erasing the old data.
        with open('output.txt', 'a') as file:  
            additional_text = input("Enter additional text to append to the file: ")
            # Add a newline character (\n) so the new text doesn't get mashed into the old text
            file.write("\n" + additional_text)  
        print("Data successfully appended to output.txt.")
    except IOError:
        print("Error: An IO error occurred while trying to append to the file.\n")

    # --- Step 3: Read and Display ---
    # Open the file one last time in read-only mode ('r') to verify what we saved
with open('output.txt', 'r') as file:
    # .read() grabs the entire file contents as one large string
    final_content = file.read()
print("Final content of output.txt:")
# .strip() cleans up any accidental blank lines or spaces at the very beginning or end of the text
print(final_content.strip())        
    