def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with special characters: @$#!\n")
        print("File 'my_file.txt' has been created and initial content written.")
    except IOError as e:
        print(f"Error: {e}")
    finally:
        file.close()

def read_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print("Error: File 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied while accessing 'my_file.txt'.")

def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("New line appended 1\n")
            file.write("789\n")
            file.write("Final line appended!\n")
        print("Content appended to 'my_file.txt'.")
    except IOError as e:
        print(f"Error: {e}")
    finally:
        file.close()

# Main function to execute tasks
def main():
    create_file()       # Task: Create a new file with initial content
    read_file()         # Task: Read and display file contents
    append_to_file()    # Task: Append new content to the file

if __name__ == "__main__":
    main()
