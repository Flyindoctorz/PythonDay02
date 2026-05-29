import matplotlib.pyplot as plt
from load_csv import load


def aff(path: str):
    """entry point to the programm"""
    aff = load(path)
    country_name = "France"
    # select the lign in "country"
    chosen_country = aff[aff["country"] == country_name]
    if chosen_country.empty:  # Empty if couldnt load bc not found
        print("Country not found in the dataset.")
        return
    else:
        # t for transpose -> lign to column
        tab = chosen_country.drop(columns=["country"]).T
        tab.columns = ["life_expectancy"]
        tab.index = tab.index.astype(int)  # years in int
        tab = tab.dropna()  # delete the empty values
        print(tab)
        # the format -> pandas method calls matplotlib
        tab.plot(figsize=(10, 8))
        plt.title(f"{country_name} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.grid(True, alpha=0.3)  # create a background grid
        plt.tight_layout()
        # save the graph, define the resolution
        plt.savefig(f"{country_name}_Life_expectancy_Projections.png", dpi=150)
        # range-> start, end, step. rotate to avoid crushing infos
        plt.xticks(range(1800, 2120, 20), rotation=0)
        plt.show()


def main():
    """Entry point of the programm"""
    aff("life_expectancy_years.csv")


if __name__ == "__main__":
    main()
