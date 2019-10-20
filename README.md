# Data Science for Powerball

Apply Reinforcement Learning to pick Powerball winning numbers

Two Python scripts:
1. Pull historical Powerball winning numbers
2. Learn from the data and pick the next winning number

### 1. Historical Powerball Winning Numbers

The script `powerball_numbers.py` scrapes the winning numbers from [PowerBall.net](https://www.powerball.net/archive) 
using [Request-HTML](https://requests-html.kennethreitz.org/).  
```
	$ pip install requests-html
```
Then, it writes the numbers to a CSV file `powerball_numbers.csv`.  

The winning numbers from April 22, 1992 to October 16, 2019 is available for download `powerball_numbers_since_1992.csv`.

### 2. Reinforcement Learning to Predict the Next Powerball Numbers

On October 4, 2015, the Powerball format was updated and used a 5/69 (white balls) + 1/26 (Powerballs).  The data should starts from October 7, 2015.
