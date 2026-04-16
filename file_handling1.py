# Start a try block to safely handle potential file-reading errors
try:
    # Open 'sample.txt' in read-only mode ('r')
    # The 'with' statement ensures the file is automatically closed when we are done
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        
        # enumerate(file, 1) loops through the file and starts counting at 1
        for line_num, line in enumerate(file, 1):
            # .strip() removes the hidden newline character so prints don't double-space
            print(f"Line {line_num}: {line.strip()}")

# Catch the specific error if the file does not exist in the folder
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
    
# Catch general input/output errors (like file permission issues)
except IOError:
    print("Error: An IO error occurred while trying to read the file.")