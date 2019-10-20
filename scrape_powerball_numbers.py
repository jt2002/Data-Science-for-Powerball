
# Scrape Powerball numbers from https://www.powerball.net/archive/

from requests_html import HTMLSession
import csv

csv_file = open('powerball_numbers.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['drawdate','ball1','ball2','ball3','ball4','ball5','powerball'])

# From years 1992 to 2019
for year in reversed(range(1992, 2020)):

    session = HTMLSession()
    r = session.get(f'https://www.powerball.net/archive/{year}')
    archive_boxes = r.html.find('.archive-box')

    for archive_box in archive_boxes:

        # Get draw date from 'href': '/numbers/1992-12-30'
        drawdate = archive_box.attrs['href'].split('/')[2]
        
        # List of 5 balls
        balls = [ball.text for ball in archive_box.find('.ball')]
        powerball = archive_box.find('.powerball', first=True).text
        
        csv_writer.writerow([drawdate, *balls, powerball])

csv_file.close()
      