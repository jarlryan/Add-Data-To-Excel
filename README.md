# Add Data To Excel (ADTE)
## Author: Ryan Jarl
## Date: July 31, 2023

This program prompts the user for input on whether or not the user wants to add 
a new data set, if 'y', the program prompts the user for the desired name of the data 
set. The program then asks the user if the user has any data to add to the current
data set, if 'y',  the user enters data until the user enters enter/return twice in a 
row. The program will ask once again if there is any more data for that set, if 'n', the 
program will ask the user if the user needs to add any more data sets, this process
will repeat itself until the user responds to this prompt with 'n'. The program then 
appends a new column with all of the entered data set's maximum values, then appends
another column with the absolute largest value within all data entered entirely, aka the
abosulte maximum.

The significance of this program is being able to append as much data as the
user wants to as many data sets as the user wants, and being able to work with this data 
via dictionaries and dataframes, converting all data to excel in a neat fashion.
This program can be extended to calculate different things about the entered data sets for
a session and can also be extended in the sense that a front end application/manager has not
been presented quite yet in this model.


## Copy Of Terminal For Existing Sample Output:
- Do you want to create a new set of data? ('y'/'n') y
- Enter name of new column: Set 1
- Is there any data you need to add to the Set 1 data set? ('y'/'n') y
- Enter item 1: 1
- Enter item 2: 3
- Enter item 3: 5
- Enter item 4: 
- Is there any data you need to add to the Set 1 data set? ('y'/'n') n
- Do you want to create a new set of data? ('y'/'n') y
- Enter name of new column: Set 2
- Is there any data you need to add to the Set 2 data set? ('y'/'n') y
- Enter item 1: 2 
- Enter item 2: 4
- Enter item 3: 6
- Enter item 4: asdf
- This is not an integer..Try Again!
- Enter item 4: 8
- Enter item 5: 
- Is there any data you need to add to the Set 2 data set? ('y'/'n') r
- 
- Error: Invalid entry. Please try again.
- 
- Is there any data you need to add to the Set 2 data set? ('y'/'n') n
- Do you want to create a new set of data? ('y'/'n') y
- Enter name of new column: Set 3
- Is there any data you need to add to the Set 3 data set? ('y'/'n') y
- Enter item 1: 9
- Enter item 2: 13
- Enter item 3: 17
- Enter item 4: fdsa
- This is not an integer..Try Again!
- Enter item 4: ds
- This is not an integer..Try Again!
- Enter item 4: a
- This is not an integer..Try Again!
- Enter item 4: 4000000234234229
- Enter item 5: 
- Is there any data you need to add to the Set 3 data set? ('y'/'n') n
- Do you want to create a new set of data? ('y'/'n') n
- 
- 
- 
- Process Completed. Saved to: "ADTE.xlsx".
