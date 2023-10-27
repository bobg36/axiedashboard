import os
import pandas as pd
import csv



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

def get_csv_len(file_path):
    if file_path.lower().endswith('.csv'):
        count = 0
        with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                count = count + 1
        return count-1
    return

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
            count = get_csv_len(file_path)
            if filename.endswith('.csv'):
                title = os.path.splitext(filename)[0] + ": " + str(count)
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


def generate_html_page(directory_path, output_filename):
    all_html = ''
    
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            folder_html = generate_folder_html(item_path)
            all_html += folder_html

    all_html = f'<div class="content-wrapper">{all_html}</div>'
    
    html_page = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <div class="header">
            <a href="all_birds.html" class="button">all_birds</a>
            <a href="koi_aqua.html" class="button button1">koi_aqua</a>
            <a href="dusk_lunge.html" class="button button2">dusk_lunge</a>
            <a href="custom_breed.html" class="button button3">custom_breed</a>
        </div>
        <link rel="stylesheet" type="text/css" href="style.css">
    <body>
        {all_html}
    </body>
    </html>
    '''
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_page)
    print(f'{output_filename} generated')


# Generate HTML for 'all_birds'
generate_html_page('data/all_birds', 'all_birds.html')

# Generate HTML for 'koi_aqua'
generate_html_page('data/koi_aqua', 'koi_aqua.html')

# Generate HTML for 'dusk_lunge'
generate_html_page('data/dusk_lunge', 'dusk_lunge.html')

# Generate HTML for 'custom_breed'
generate_html_page('data/custom_breed', 'custom_breed.html')
