copy_local_data.py
the data and charts are generated locally
inventory: GraphQL endpoints
floor: GraphQL endpoints
sales history: local database SQL queries

generate_html.py
the html for every dashboard page is generated programatically

index.html
home page is not generated

style.css
css styles for the html

update_app_pushgit.py
performs a series of tasks required to sync the website
1. runs local scripts to generate up to date charts and data
2. runs 'generate_html.py' to generate html code
3. pushes changes to live if no errors occur
