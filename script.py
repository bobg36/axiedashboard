import os
import pandas as pd
import csv

# Define the path to the 'all_birds' directory
all_birds_path = 'data/all_birds'

file_order = ['virgin.csv', 'bred.csv', 'floor.csv', 'sales.csv', 'chart15.png', 'chart50.png']

# Function to convert a CSV file to an HTML table
def csv_to_html_table(csv_file_path):
    data = pd.read_csv(csv_file_path)
    html_table = data.to_html(classes='table table-bordered', index=False)
    return html_table

# Function to retrieve the image URL from sales.csv
def get_image_url_from_sales_csv(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for row in csv_reader:
            if row and len(row) > 0:
                axie_id = row[0]
                image_url = f'https://assets.axieinfinity.com/axies/{axie_id}/axie/axie-full-transparent.png'
                return image_url  # Return the URL as soon as it's found
    return ''

# Function to generate HTML code for a folder
def generate_folder_html(folder_path):
    folder_name = os.path.basename(folder_path)
    fallback_image_url = "https://assets.axieinfinity.com/axies/821/axie/axie-full-transparent.png"


    # Get the image URL from sales.csv
    sales_csv_path = os.path.join(folder_path, 'sales.csv')
    image_url = get_image_url_from_sales_csv(sales_csv_path)

    folder_html = f'<div class="table-container"><h2><img src="{image_url}" onerror="this.src=\'{fallback_image_url}\';"></h2>'
    
    for filename in file_order:
        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            if filename.endswith('.csv'):
                title = os.path.splitext(filename)[0]
                table = csv_to_html_table(file_path)
                if table:
                    # print('true')
                    if filename == 'bred.csv' or filename == 'virgin.csv':
                        folder_html += f'<div class="table-wrapper1"><div class="table-title">{title}</div>{table}</div>'
                    elif filename == 'floor.csv' or filename == 'sales.csv':
                        folder_html += f'<div class="table-wrapper2"><div class="table-title">{title}</div>{table}</div>'
            elif filename.endswith('.png'):
                folder_html += f'<img src="{file_path}" alt="{filename}">'
    
    folder_html += '</div>'
    return folder_html

# Generate HTML for all folders within 'all_birds'
all_birds_html = ''
for item in os.listdir(all_birds_path):
    item_path = os.path.join(all_birds_path, item)
    if os.path.isdir(item_path):
        folder_html = generate_folder_html(item_path)
        all_birds_html += folder_html

# Create a wrapper for 'all_birds'
all_birds_html = f'<div class="all-birds-wrapper">{all_birds_html}</div>'

# Create the final HTML page with the 'all_birds' content
html_page = f'''
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="style.css">
<body>
    <h1>'all_birds' Data</h1>
    {all_birds_html}
</body>
</html>
'''

# Save the HTML code to a file or serve it with a web framework
with open('all_birds_data.html', 'w', encoding='utf-8') as f:
    f.write(html_page)
