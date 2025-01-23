def process_csv(input_file, output_file):
    # Read the original file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Process the lines
    processed_lines = []
    current_line = ""
    
    for line in lines:
        # Remove whitespace at the beginning and end
        line = line.strip()
        
        # If line is empty, continue
        if not line:
            continue
            
        # If line starts with a number
        if line[0].isdigit():
            # If there's a current line, save it
            if current_line:
                processed_lines.append(current_line)
            # Start a new line
            current_line = line
        else:
            # Add content to current line
            current_line += " " + line
    
    # Add the last line if it exists
    if current_line:
        processed_lines.append(current_line)
    
    # Write the result to the new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(processed_lines))

# Script usage
input_file = 'export.csv'
output_file = 'export_processed.csv'
process_csv(input_file, output_file)