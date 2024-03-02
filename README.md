
# Vehicle Data Fetcher

## Description

This script, `fetch_vehicles.py`, is designed to scrape vehicle information from a specified webpage and save the data in a CSV format. It captures details such as the vehicle's title, year, mileage, and price from the given URL. This tool is useful for anyone looking to compile vehicle listings from specific online sources into an easily manageable format. Only [cars.com](https://www.cars.com/) has been test now.

[阅读中文版本](./README_zh.md)

## Features

- Fetch vehicle details including title, year, mileage, and price
- Output data in CSV format for easy analysis and manipulation
- Command-line interface for straightforward usage

## Installation

Before running the script, ensure you have Python installed on your system. This script was developed with Python 3.x in mind.

You will also need to install the following Python packages: `requests` and `beautifulsoup4`. You can install these using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

To use the script, navigate to the directory where `fetch_vehicles.py` is located and run the following command in your terminal:

```bash
python fetch_vehicles.py [URL] [OUTPUT_CSV_FILE_NAME]
```

Replace `[URL]` with the target webpage URL from which you wish to scrape vehicle data, and `[OUTPUT_CSV_FILE_NAME]` with the desired name of your output CSV file.

### Example

```bash
python fetch_vehicles.py "http://example.com/vehicles" "vehicles.csv"
```

This command fetches vehicle data from `http://example.com/vehicles` and saves it to `vehicles.csv`.

## Parameters

- `URL`: The target webpage URL containing vehicle listings.
- `OUTPUT_CSV_FILE_NAME`: The name of the output CSV file where the data will be saved.

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository, make changes, and submit a pull request. Your contributions are highly appreciated!

## License

This project is open source and available under the [MIT License](LICENSE).
