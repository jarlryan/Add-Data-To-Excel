"""
Please refer to README and main function documentation for a thourough description on this project.
:filename: ADTE.py
:author: Ryan Jarl
:date: July 31, 2023
"""


# Imports the pandas library and assigns it the alias 'pd'.
# Imports the 'List' attribute for specifying return type with a more narrow scope.
import pandas as pd
from typing import List


def read_in_excel() -> pd.DataFrame:
    """
    Reads data from an Excel file and returns it as a pandas DataFrame.
    :return: Pandas DataFrame object that represents read in file
    """
    df = pd.read_excel("Add Data To Excel/BlankADTE.xlsx")
    return df


def get_user_input(items) -> List[int]:
    """
    Takes user input, collecting data in a list, to enter a new piece of data, the
    user must hit enter, to exit the user must hit enter twice, list only accepts integers.
    :param items: A list that will store the integers entered by the user
    :return: A list of integers representing user input data
    """
    count = 0
    while 1:
        count += 1
        item = input('Enter item %d: '%count)
        if item == '':
            break
        try:
            items.append(int(item)) 
        except ValueError:
            count -= 1
            print("This is not an integer..Try Again!")
            continue
    return items


def new_column_builder(df_size, new_col_name) -> List[int]:
    """
    Allows the user to add data to a specified column of data.
    :param df_size: Represents the desired size of the data set in the Excel file
    :param new_col_name: The name of the new column that you want to add to your data set
    :return: Updated list of items with the new values added
    """
    items = []
    items_temp = []
    visited = 0
    while 1:
        s = str(input("Is there any data you need to add to the " + new_col_name + " data set? ('y'/'n') "))        
        if s == 'y':
            if visited != 0:
                items_temp.clear()
            items_temp = get_user_input(items_temp)
            for i in items_temp:
                items.append(i)
            visited += 1
            continue
        if s == 'n' and len(items) == 0:
            print("\nError: The data set is currently empty. Please enter atleast one value.\n")
            continue
        elif s == 'n' and len(items) != 0:
            items_size = len(items)
            size_difference = df_size - items_size
            for i in range(0, size_difference):
                items.append(0)
            return items
        else:
            print("\nError: Invalid entry. Please try again.\n")
            continue


def filter_zeros(list_containing_zeros) -> List[int]:
    """
    Takes a list as input and returns a new list with all the zeros removed.
    :param list_containing_zeros: A list that contains data with zeros that need to be filtered
    :return: A list with all the elements from the input list that are not equal to 0
    """
    return list(filter(lambda n: n!=0.0, list_containing_zeros))
        

def append_maximum_to_df(df, max_list, df_size) -> pd.DataFrame:
    """
    Append new dataframe containing maximum value for each individual data set from the user.
    :param df: Dataframe from input to which we want to append the maximum values
    :param max_list: A list containing the maximum values to be appended to the dataframe
    :param df_size: Represents the desired size of the dataframe 'df'
    :return: Modified dataframe with a new column 'Maximum Value' added, filled with the
    values from the max_list, any missing values in the dataframe are filled with 0
    """
    max_length_ = len(max_list)
    size_ = df_size - max_length_
    for data in range(0, size_):
        max_list.append(0)
    df['Maximum Valuue'] = max_list
    df = df.fillna(0.0)
    return df


def append_absolute_maximum_to_df(df, abolute_max_list, df_size):
    """
    Append the absolute maximum value of all data sets onto the dataframe.
    :param df: Pandas DataFrame that the user wants to modify
    :param abolute_max_list: A list of values to decipher absolute maximum from
    :param df_size: Represents the size of the dataframe 'df', it is used to
    determine the number of zeros to append to the 'abolute_max_list' before assigning it to the 'Absolute
    Maximum' column of the dataframe
    :return: Modified dataframe with a new column 'Absolute Maximum' added
    """
    absolute_maximum = max(abolute_max_list)
    abolute_max_list = []
    abolute_max_list.append(absolute_maximum)
    size_ = df_size - 1
    for data in range(0,size_):
        abolute_max_list.append(0)
    df['Absolute Maximum'] = abolute_max_list
    df = df.fillna(0.0)
    return df


def WriteToExcel(df):
    """
    Writes a Pandas DataFrame to an Excel file.
    :param df: Pandas DataFrame object that contains the data you want to write to an Excel file
    """
    df.to_excel("Add Data To Excel/ADTE.xlsx", sheet_name="ADTE", index=False)


def main():
    """
    The main function reads in data from an Excel file, prompts the user to create a new set of data,
    adds the new data to the dataframe, calculates the maximum value of each column, appends the maximum
    values to the dataframe, calculates the absolute maximum value of each column, appends the absolute
    maximum values to the dataframe, and saves the updated dataframe to a new Excel file.
    """
    maximum_list = []
    df = read_in_excel()
    df_size = len(df.index)
    if df_size < 1000:
        df_size += 800
    while 1:
        new_set_answer = input("Do you want to create a new set of data? ('y'/'n') ")
        if new_set_answer == 'y':
            new_column = []
            new_column_name = input("Enter name of new column: ")
            new_column = new_column_builder(df_size, new_column_name)
            new_column.sort(reverse=True)
            df[new_column_name] = pd.Series(new_column)
            df = df.fillna(0.0)
            new_column = filter_zeros(new_column)
            column_maximum = max(new_column)
            maximum_list.append(column_maximum)
            new_column_name=''
            continue
        if new_set_answer == 'n':
            df = append_maximum_to_df(df, maximum_list, df_size)
            df = append_absolute_maximum_to_df(df, (df[df.columns[-1]]), df_size)
            print('\n\n\nProcess Completed. Saved to: "ADTE.xlsx".')
            break
        else:
            print("\nError: Invalid entry. Please try again.\n")
            continue
    WriteToExcel(df)


# The 'if __name__ == "__main__":' statement is used to ensure that the code inside the 'main()'
# function is only executed if the script is run directly and not imported as a module. This is a
# common practice in Python to separate the code that should be run as a standalone script from the
# code that should be used as a module.
if __name__ == "__main__":
    main()