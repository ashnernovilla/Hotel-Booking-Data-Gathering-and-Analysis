# Hotel Booking Data Gathering and Analysis

### Short Description

This project scrapes hotel data (prices, ratings, location) from booking.com for specified cities, stores it in a SQLite database, and then uses a Jupyter Notebook to perform exploratory data analysis and visualize key findings.

---

This project is designed to scrape hotel data from booking.com for specific cities (Manila and Davao), store the information in a SQLite database, and then perform an Exploratory Data Analysis (EDA) to uncover insights about hotel pricing, ratings, and locations.

## Features

- **Web Scraping**: Dynamically scrapes hotel data, including names, prices, distances from the city center, and user ratings.
- **Data Storage**: Stores the collected data in a structured SQLite database (`hotels.db`).
- **ETL and EDA**: Cleans and transforms the raw data, and performs a detailed exploratory data analysis.
- **Data Visualization**: Generates visualizations to understand the distribution of prices and ratings, and the correlation between different data points.

## Technologies Used

- **Programming Language**: Python
- **Web Scraping**: Selenium
- **Data Manipulation**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **Database**: SQLite
- **Environment**: Jupyter Notebook, Anaconda
- **Automation**: Windows Batch Script

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    ```

2.  **Create and activate a Conda environment:**
    ```bash
    conda create --name hotel_scraper python=3.9
    conda activate hotel_scraper
    ```

3.  **Install the required libraries.** Create a `requirements.txt` file with the following content:
    ```
    pandas
    numpy
    selenium
    matplotlib
    seaborn
    jupyter
    ```
    Then, install the libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download WebDriver**: Make sure you have the correct WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and that it is in your system's PATH.

## Usage

1.  **Run the Scraper**:
    -   Execute the `app.bat` batch file. This will activate the Conda environment and run the `app_scrape.py` script.
    -   You will be prompted to enter a city (**Manila** or **Davao**) and the **check-in** and **check-out dates** in `YYYY-MM-DD` format.
    -   The script will then scrape the data and save it to `hotels.db`.

2.  **Analyze the Data**:
    -   Once the scraping is complete, open the `ETL_EDA.ipynb` Jupyter Notebook.
    -   You can run the cells in the notebook to see the data cleaning, analysis, and visualizations.

## Project Structure
. <br>
├── app_scrape.py       # The main web scraping script <br>
├── ETL_EDA.ipynb       # Jupyter Notebook for data analysis <br>
├── app.bat             # Batch script to run the scraper <br>
└── hotels.db           # SQLite database for storing data <br>


## Data Analysis and Findings

The exploratory data analysis reveals several key insights:

-   **Hotel prices are highly variable**, ranging from affordable to very expensive.
-   **Hotel ratings are generally high**, with most hotels scoring between 7 and 9.
-   There is a **weak correlation between price and rating**, meaning a higher price does not always guarantee a better rating.
-   The **distance from the city center has a weak correlation with the price** of the hotel.

## Author

-   **ASHNER_NOVILLA**
