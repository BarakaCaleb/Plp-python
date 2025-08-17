#File Read & Write Challenge: Create a program that read a file and writes a modified version of it.
#Error Handling Lab: Ask the user for a filename and handle errors if it exist or can't be read.


def file_handler(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.readlines()
        modified_file = ' '.join(word.capitalize() for word in content.split())

        with open(output_file, 'w') as outfile:
            outfile.write(modified_file)
        print(f"File '{input_file}' sucessfully modified and saved to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file '{input_file}' or '{output_file}'.")


input_file = str(input("Enter the input file name eg (file.txt): "))

output_file = str(input("Enter the output file name eg (output.txt): "))

print("Processing the file...")
file_handler(input_file, output_file)
print("File processing complete.")

