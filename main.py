import json
import os

# Function to extract code from a notebook file and save it to a text file
def extract_code_from_notebook(notebook_file, output_file):
    try:
        # Open the notebook file with utf-8 encoding to avoid decoding errors
        with open(notebook_file, 'r', encoding='utf-8') as f:
            notebook_data = f.read()
        
        notebook_json = json.loads(notebook_data)
        
        # Extract code from all code cells
        all_code_cells = []
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'code':
                code = ''.join(cell['source'])
                all_code_cells.append(code)
        
        # Join all the extracted code into a single string
        extracted_code = "\n".join(all_code_cells)
        
        # Save the extracted code to the specified output file
        with open(output_file, 'w', encoding='utf-8') as output_f:
            output_f.write(extracted_code)
        
        # Notify the user that the code has been saved
        print(f"Entire notebook code has been extracted and saved to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The notebook file '{notebook_file}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to parse the notebook. It may not be a valid .ipynb file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to run the script
def main():
    # Ask for the path of the downloaded notebook file
    notebook_file = input("Enter the full path to the downloaded Kaggle notebook file: ").strip()
    
    if os.path.exists(notebook_file):
        # Ask for the output file name where the code should be saved
        output_file = input("Enter the desired output file name (e.g., extracted_code.py): ").strip()
        
        # Extract code from the notebook and save it to the output file
        extract_code_from_notebook(notebook_file, output_file)
    else:
        print(f"Error: The file at {notebook_file} does not exist.")

if __name__ == "__main__":
    main()
