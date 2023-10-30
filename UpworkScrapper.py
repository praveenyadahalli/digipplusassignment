import requests
from bs4 import BeautifulSoup
import csv

# Upwork URL to scrape
upwork_url = 'https://www.upwork.com/'

# Make a request to the Upwork website
response = requests.get(upwork_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find and filter project details
projects = soup.find_all('div', class_='job-title')

# Create and open a CSV file
csv_file_path = 'upwork_projects.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer
    csv_writer = csv.writer(csv_file)
    
    # Write header row
    csv_writer.writerow(['Title', 'Description', 'Budget', 'Link'])

    for project in projects:
        title = project.find('h4', class_='job-title')
        description = project.find('p', class_='description')
        budget = project.find('span', class_='js-budget')
        link = project.find('a', class_='job-title-link')

        # Check if all elements are found before extracting text
        if title and description and budget and link:
            title_text = title.text.strip()
            description_text = description.text.strip()
            budget_text = budget.text.strip()
            link_text = link['href']

            # Write data to CSV file
            csv_writer.writerow([title_text, description_text, budget_text, link_text])

print(f"Scraping and writing to CSV file '{csv_file_path}' completed.")
