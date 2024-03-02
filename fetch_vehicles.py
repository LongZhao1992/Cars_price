import requests
from bs4 import BeautifulSoup
import csv
import argparse

def fetch_and_save_vehicle_data(url, csv_file_name):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            vehicles = soup.find_all('div', class_='vehicle-details')
            
            with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'Year', 'Mileage', 'Price'])
                
                for vehicle in vehicles:
                    title = vehicle.find('h2', class_='title').text.strip()
                    mileage = vehicle.find('div', class_='mileage').text.strip().replace(' mi.', '').replace(',', '')
                    price = vehicle.find('span', class_='primary-price').text.strip().replace('$', '').replace(',', '')
                    year = title.split(' ')[0]
                    
                    writer.writerow([title, year, mileage, price])
            print(f"Data successfully written to {csv_file_name}")
        else:
            print('Failed to retrieve the webpage. Please check the URL and try again.')
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Fetch vehicle details from a specified URL and save the data in a CSV file.")
    parser.add_argument("url", help="The target URL to fetch vehicle data from")
    parser.add_argument("csv_file_name", help="The name of the output CSV file (e.g., output.csv)")

    args = parser.parse_args()
    
    fetch_and_save_vehicle_data(args.url, args.csv_file_name)

if __name__ == '__main__':
    main()
