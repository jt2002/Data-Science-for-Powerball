# Data Science for Powerball

Implementation of Reinforcement Learning to pick Powerball winning numbers

Two Python scripts:
1. Pull historical Powerball winning numbers
2. Learn from the data and pick the next winning number

### 1. Historical Powerball Numbers

The script `powerball_numbers.py` scrapes the winning numbers from [PowerBall.net](https://www.powerball.net/archive) 
using [Request-HTML](https://requests-html.kennethreitz.org/).  
```
	$ pip install requests-html
```
It writes the numbers to a CSV file `powerball_numbers.csv`.  The winning numbers from April 22, 1992 to October 16, 2019 `powerball_numbers_since_1992.csv` is available for download.

### 2. Predict the Next Winning Numbers

On October 4, 2015, the Powerball format was updated to use a 5/69 (white balls) + 1/26 (Powerballs).  The data to feed the script should start from October 7, 2015.

The script pre-processes the winning numbers to 2 matrices:
1. A 69-columns matrix
2. A 26-columns matrix 

Each row represents one draw where the columns of the winning number is 1 and 0 otherwise. 

Then, the script picks 5 white balls and 1 powerball and prints the predicts winning number.  

When using `random.seed(0)`, Powerball to play is `[9, 33, 41, 48, 56] [24]`
