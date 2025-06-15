# Laptop Data Gathering and Analysis from Flipkart

This project automates the process of scraping gaming laptop data from Flipkart, a major e-commerce website. It gathers detailed information about various laptops, stores it in a SQLite database, and provides an initial data analysis through a Jupyter Notebook.

### Project Title:
Flipkart Gaming Laptop Scraper and Analyzer

### Short Description:
A Python-based tool that uses Selenium to scrape gaming laptop data from Flipkart, saves it to a SQLite database, and includes a Jupyter Notebook for exploratory data analysis of the collected data, including price analysis by processor type.

---

## Features

- **Automated Web Scraping**: Scrapes multiple pages of gaming laptop listings from Flipkart.
- **Multi-Page Scraping**: The script is designed to navigate through multiple pages of search results to gather a more comprehensive dataset. This is achieved by iterating through a loop that modifies the page number in the URL.
- **Detailed Data Collection**: Extracts a wide range of data points for each laptop, including:
    - Name
    - Price
    - Rating
    - Processor
    - RAM
    - Operating System
    - Storage
    - Display
    - Included accessories/warranties
- **Database Storage**: Organizes and stores the scraped data in a SQLite database (`laptop.db`).
- **Data Analysis**: A Jupyter Notebook is included for data cleaning and exploratory data analysis (EDA).
- **Automation**: A simple batch script is provided to automate the entire data gathering process.

## Technologies Used

- **Programming Language**: Python
- **Web Scraping**: Selenium
- **Data Manipulation**: Pandas, NumPy
- **Database**: SQLite
- **Data Visualization**: Plotly Express, Matplotlib, Seaborn
- **Environment**: Jupyter Notebook, Anaconda
- **Automation**: Windows Batch Script

## Setup and Installation

To get this project up and running on your local machine, please follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    ```

2.  **Set up Conda Environment:**
    - It is recommended to use the Conda environment specified in the `app.txt` file (`B:\Mac_Learn2`). You can create a new one if needed:
    ```bash
    conda create --name laptop_analyzer python=3.9
    conda activate laptop_analyzer
    ```

3.  **Install Required Libraries:**
    - Create a `requirements.txt` file with the following content:
    ```
    pandas
    numpy
    selenium
    matplotlib
    seaborn
    plotly
    jupyter
    ```
    - Then, run the following command to install the libraries:
    ```bash
    pip install -r requirements.txt
    ```

4.  **WebDriver Setup:**
    - Make sure you have the correct WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and that it's accessible in your system's PATH.

## Usage

1.  **Run the Scraper:**
    -   Execute the `app.txt` batch file. This will automatically activate the specified Conda environment and run the `app.py` scraping script.
    -   The script will scrape the first two pages of gaming laptops sorted by price (descending) and store the data in `laptop.db`.
    -   The core of the multi-page scraping is handled by the following loop in `app.py`, which can be adjusted to scrape more pages:
    ```python
    for page_num in range(1,3):
        page_url = f'[https://www.flipkart.com/search?q=gaming+laptop&...&page=](https://www.flipkart.com/search?q=gaming+laptop&...&page=){page_num}'
        driver.get(page_url)
        # ... scraping logic ...
    ```

2.  **Analyze the Data:**
    -   After the scraper has finished, open the `Data Analysis Example.ipynb` file in a Jupyter Notebook environment.
    -   You can run the cells in the notebook to perform data cleaning, analysis, and generate visualizations, such as a bar chart showing the average laptop price by processor type.

## Project Structure


. <br>
├── app.py                      # Main Python script for web scraping <br>
├── app.txt                     # Batch script to automate the scraping process <br>
├── Data Analysis Example.ipynb # Jupyter Notebook for data analysis <br>
└── laptop.db                   # SQLite database to store scraped data <br>


## Data Analysis Insights

The initial data analysis performed in the Jupyter Notebook provides insights into the gaming laptop market on Flipkart, including:

-   A breakdown of the most common processor types available.
-   A comparison of laptop prices based on the processor type, which can help in identifying price trends and value for money.

## Author

- **ASHNER_NOVILLA**
