import cv2
import pandas as pd
import matplotlib.pyplot as plt


def create_df(path_csv: str) -> pd.DataFrame:
    df = pd.read_csv(path_csv)
    return df


def add_hwd_columns(df: pd.DataFrame) -> pd.DataFrame:
    heights, widths, depths = [], [], []
    for abspath in df["Absolute path"]:
        img = cv2.imread(abspath)
        height, width, depth = img.shape
        heights.append(height)
        widths.append(width)
        depths.append(depth)
    df["Height"] = heights
    df["Width"] = widths
    df["Depth"] = depths
    return df


def filter_columns(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    return df[(df['Height'] <= max_height) & (df['Width'] <= max_width)]


def create_column_area(df: pd.DataFrame) -> None:
    df['Area'] = df['Height'] * df['Width']


def create_histogram(column: pd.Series, column_name: str) -> None:
    plt.figure(figsize=(9, 5))
    plt.hist(column, bins=30, edgecolor='black')
    plt.title('Распределение площадей изображений')
    plt.xlabel(column_name)
    plt.ylabel('Количество изображений')
    plt.grid(True)
    plt.show()


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by='Area', ascending=True)
