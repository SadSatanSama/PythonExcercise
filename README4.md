# Assignment: File Handling in Python

## Description
This repository contains two Python scripts demonstrating secure file handling operations, including reading, writing, and appending data, with comprehensive `try...except` error management.

### Task 1: Read a File and Handle Errors
This script safely opens a local file (`sample.txt`) in read mode and iterates through its contents. It prints each line alongside its corresponding line number and includes specific error handling for missing files (`FileNotFoundError`) and general input/output issues (`IOError`).

### Task 2: Write and Append Data to a File
This script interactively prompts the user for text and writes it to a new file (`output.txt`). It includes a custom loop that asks the user if they wish to append additional lines. Finally, it reads and displays the complete file contents to verify the operations were successful.

---

## How to Run
1. Ensure Python 3 is installed on your machine.
2. Extract the ZIP folder and open the directory in your terminal.
3. To run Task 1, execute: `file_handling1.py` *(Note: Ensure a `sample.txt` file exists in the same folder to see the success output, or run it without one to test the error handling).*
4. To run Task 2, execute: `file_handling2.py`

---

## Example Outputs

### Task 1 Example
> Reading file content:
> Line 1: This is a sample text file.
> Line 2: It contains multiple lines.

### Task 2 Example
> Enter text to write to the file: Hello, Python!
> Data successfully written to output.txt.
>
> Do you want to add anything else to this file? (y/n): y
> Enter additional text to append to the file: Learning file handling in Python.
> Data successfully appended to output.txt.
>
> Final content of output.txt:
> Hello, Python!
> Learning file handling in Python.