import argparse
from dataframe import create_df, add_hwd_columns, create_histogram, create_column_area, filter_columns, sort_by_area


def parsing_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_csv", type = str, help="Path to csv file")
    arguments = parser.parse_args()
    return arguments


def main():
    arguments = parsing_arguments()
    try:
        df = create_df(arguments.path_csv)
        print('dataframe')
        print(df.head())
        print('new columns')
        add_hwd_columns(df)
        print(df.head())
        stats = df[['Height', 'Width', 'Depth']].describe()
        print(stats)
        print('filtered data')
        filtered_df = filter_columns(df, 1000, 1000)
        print(filtered_df.head())
        print('area')
        create_column_area(df)
        print(df.head())
        print('sort area')
        df_sort_by_value = sort_by_area(df)
        print(df_sort_by_value.head())
        create_histogram(df['Area'], 'Area')
    except Exception as e:
        print(f"Error: {e} ")


if __name__ == "__main__":
    main()