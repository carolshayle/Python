import json
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Define the input and output file paths
input_file = os.path.join(script_dir, 'Complete_Satellite_Data.json') 
output_file = os.path.join(script_dir, 'ca_data.json')

try:
    # Read the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Initialize a list to store CA data
    ca_data = []

    # Check if the loaded data is a list
    if isinstance(data, list):
        # Iterate through the list of countries
        for item in data:
            # Assuming each item is a dictionary and has a 'country_code' key
            if item.get('country_code') == 'CA':
                ca_data.append(item)
    else:
        # If it's not a list, it might be a dictionary with country codes as keys (original assumption)
        # This part handles the original dictionary format as a fallback
        if data.get('CA'):
            ca_data.append(data.get('CA')) # Append the dictionary directly

    # Save the extracted 'CA' data to a new JSON file
    # If ca_data is a list of one item, you might want to save just that item if that's the desired output.
    # For now, it will save a list, which is safer if there could be multiple CA entries.
    with open(output_file, 'w') as f:
        json.dump(ca_data, f, indent=4)

    print(f"Successfully extracted 'CA' data and saved to {output_file}")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from '{input_file}'. Please check the file's format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")