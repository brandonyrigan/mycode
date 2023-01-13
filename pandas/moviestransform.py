#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Challenge Solution 01 - JSON to CSV"""

import pandas

def main():

    # create a dataframe from json
    dfjson = pandas.read_json("5movies.json")

    # writeout dataframe to CSV
    dfjson.to_csv("5movies-translated-from-json.csv")

    # create a dataframe from csv
    dfcsv = pandas.read_csv("5movies.csv")

    # writeout dataframe to excel
    dfcsv.to_excel("5movies-translated-from-csv.xlsx")

    # writeout dataframe to excel
    dfjson.to_excel("5movies-translated-from-json.xlsx")


if __name__ == "__main__":
    main()

