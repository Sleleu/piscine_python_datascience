from load_csv import load
import matplotlib.pyplot as plt


def projection_life(df_life, df_gdp, year) -> None:
    """
    Displays a scatter plot connecting life expectancy and
    gross domestic product (GDP) for the given year.

    Args:
        df_life (DataFrame): life expectancy data by year.
        df_gdp (DataFrame): GDP data by year.
        year (int): The year for which you want to display the projection.

    Returns:
        None
    """
    life_year = df_life[str(year)]
    gdp_year = df_gdp[str(year)]
    gdp_year = [int(float(gdp_year[i].replace('k', '')) * 1e3)
                if str(gdp_year[i]).endswith('k')
                else int(gdp_year[i]) for i in gdp_year.index]
    plt.scatter(gdp_year, life_year)
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks([300, 1e3, 1e4], ["300", "1k", "10k"])
    plt.show()


def main():
    """
    Main function that loads life expectancy and GDP data,
    and then displays the projection for the year 1900.
    In case of an error, it prints an appropriate error message.
    """
    df_life = load("life_expectancy_years.csv")
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    try:
        projection_life(df_life, df_gdp, 1900)
    except (KeyError, TypeError, ValueError, AttributeError) as error:
        print(f"{__name__}: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
