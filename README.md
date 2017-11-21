# shorterwinter

This project forks data from the Associated Press on data.world, the platform the AP is using to distribute data to its member newsrooms.
The AP story concludes nationwide that winter has shortened by about a month. I wanted to see what the Missouri data showed, so I wrote this script.
The AP data comes from National Weather Service Stations across the country. 
There are 24 Missouri stations included in the data, and they're spread throughout different regions of the state. A source at NOAA who works with freeze data often said for this kind of data, 24 stations is enough for a representative sample for Missouri.
The script calculates winter lengths for the first 30 seasons of the 100-year data, and winter lengths for the last 30 seasons.
The Missouri state climatologist, based out of the University of Missouri, advised a 30-year comparison would be fair.

The data include the dates of the first fall frost and the last spring frost for nearly a century. The dates are not in date format; rather the number of the day of year that the frost occurred; ie day 279 for the first frost and day 115 for the last frost. 

The script, written in Python (winterlength.py) uses these numbers to calculate winter lengths. The script is written to calculate for including the day of the first frost (ie subtracting (279-1) from 365 instead of subtracting 279 from 365. It also calculates for leap years.
Two sets of lists are created by the end; a list for each station and a list for each season. 
The script uses csv.writer to create a file with winter lengths for each of the 60 seasons in a row, and each station is a column. 
As of 11/20, the script does not write headers for the columns or labels for the rows. I intend to write this in. 
