from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def find_country_stat(df: pd.DataFrame, country: str, c_color):
    country_data = df[df["country"] == country].squeeze()
    country_years = country_data.drop("country")
    country_years = country_years.loc[country_years.index <= '2050']
    index = [int(year) for year in country_years.index]
    values = [float(value.replace('M', '')) for value in country_years.values]
    plt.plot(index, values, label=country, color=c_color)


def aff_pop(df: pd.DataFrame, country1: str, country2):
    df = df.loc[df.index <= 2050]
    find_country_stat(df, country2, "red")
    find_country_stat(df, country1, "blue")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.yticks([20, 40, 60],labels=['20M','40M','60M'])
    plt.xticks(range(1800, 2050, 40))
    plt.legend([country2, country1])
    plt.show()


def main():
    df = load("population_total.csv")
    try:
        aff_pop(df, "France", "Belgium")
    except (KeyError, TypeError, ValueError) as error:
        print(f"{__name__}: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
