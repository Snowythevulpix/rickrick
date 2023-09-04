import os
from bs4 import BeautifulSoup

# Define the HTML code you want to insert (excluding line 43)
inserted_code = """
    <!-- Your modified HTML code here -->
"""

# Get the current directory where the script is located
directory_path = os.path.dirname(os.path.abspath(__file__))

# List of files to ignore
ignore_files = ['index.html', 'discord.html', 'home.html', 'test.html']

# Function to modify an HTML file
def modify_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Check if the file should be ignored
    if os.path.basename(file_path) not in ignore_files:
        # Find line 43 and keep it as is
        for i, line in enumerate(lines):
            if i == 42:  # Line 43 (0-based index)
                continue
            # Insert the code at the desired location
            if '</head>' in line:
                lines.insert(i, inserted_code)
                break

    # Write the modified HTML back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Function to traverse the directory and modify HTML files
def modify_files_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith('.html'):
                file_path = os.path.join(root, filename)
                print(f'Modifying file: {file_path}')
                modify_html_file(file_path)

# Call the function to start modifying HTML files
modify_files_in_directory(directory_path)
