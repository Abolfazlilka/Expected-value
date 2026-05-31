# Expected Value

A Python-based statistical analysis project for calculating **mean**, **variance**, and **standard deviation**, with optional visualizations such as **histograms**, **normal distribution samples**, and **sample means plots**.

This project is designed as a simple educational tool to help understand descriptive statistics and the concept of **expected value** through interactive user input and visualization.

## Features

- Calculate:
  - Mean
  - Variance
  - Standard Deviation
- Accept data input in three ways:
  - Manual input
  - From a `data.txt` file
  - Default built-in dataset
- Draw a histogram of the input data
- Generate and visualize normally distributed random data based on the dataset
- Draw a sample means plot using random resampling
- Colored terminal output using `colorama`
- Error handling with fallback to default data

## Technologies Used

- Python 3
- NumPy
- Matplotlib
- Colorama
- OS / Platform modules

## Project Structure
```bash
Expected-value/
├── Expected-value.py
├── data.txt
└── README.md

## How It Works

When the program starts, it asks the user to choose one of the following input methods:

1. **Manual input**  
   Enter data one by one from the keyboard.

2. **Text file input**  
   Load data from `data.txt`.

3. **Default data**  
   Use the predefined dataset included in the program.

After receiving the data, the program calculates:

- Mean
- Variance
- Standard Deviation

Then the user can choose to:

- Draw a histogram of the original data
- Generate a normal sample based on the data's mean and standard deviation
- Draw a sample averages plot using bootstrap-style resampling

## Installation

Clone the repository:

bash
git clone https://github.com/Abolfazlilka/Expected-value.git
cd Expected-value

Install the required libraries:

bash
pip install numpy matplotlib colorama

## Usage

Run the script with:

bash
python Expected-value.py

Then follow the interactive prompts in the terminal.

## Example Workflow

- Choose data input method
- View calculated statistics
- Decide whether to draw a histogram
- Optionally generate a normal sample plot
- Optionally draw a sample averages plot

## Example Output

The program displays statistical results such as:

text
Data Summary:
Mean: 78.54
Variance: 33.12
Standard Deviation: 5.75

It can also display plots such as:

- Histogram of the original dataset
- Histogram of generated normal data
- Sample means distribution plot

## Purpose of the Project

This project was created to practice Python programming and apply basic statistical concepts in a practical and visual way. It is especially useful for students and beginners who want to better understand:

- Expected value
- Variance
- Standard deviation
- Sampling and distribution behavior

## Notes

- If an error occurs during input, the program automatically falls back to the default dataset.
- The script clears the terminal screen depending on the operating system.
- The banner is displayed using colored text for a better terminal experience.

## Future Improvements

- Add support for CSV file input
- Improve plot styling and labeling
- Add median, mode, and other descriptive statistics
- Create a GUI version
- Add unit tests
- Refactor the code into functions and modules

## Author

**Abolfazl Ilka**

## License

This project is open source and available for educational and personal use.
