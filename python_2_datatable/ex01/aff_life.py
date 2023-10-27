from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def aff_life(df: pd.DataFrame, country: str):
    country_data = df[df["country"] == country].squeeze()
    country_years = country_data.drop("country")
    plt.plot(country_years.index, country_years.values)
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(range(0, 360, 40))
    plt.show()

def main():
    df = load("life_expectancy_years.csv")
    try:
        aff_life(df, "France")
    except (KeyError, TypeError) as error:
        print(f"{__name__}: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()