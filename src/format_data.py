import csv
import re

def format_data(data_file_name: str) -> str:
    file_name = data_file_name[:-4]
    csv_file_name = file_name + '.csv'
    # Open the input file and create a new CSV file
    with open(data_file_name, 'r') as input_file, open('csv_data/{}'.format(csv_file_name), 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        
        # Process each line in the input file
        for line in input_file:
            # Use a regular expression to extract the numeric values from the line
            values = re.findall(r'\d+(?:\.\d+)?', line)
            
            # Write the numeric values to the CSV file
            writer.writerow(values)

    return csv_file_name



