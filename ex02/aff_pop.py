import matplotlib.pyplot as plt
from load_csv import load


def parse_pop(val):
    """format population"""
    if isinstance(val, str):
        val_up = val.upper()
        if "M" in val_up:
            return float(val_up.replace("M", "")) * 1000000
        elif "K" in val_up:
            return float(val_up.replace("K", "")) * 1000
    return float(val)


def pick_some_country(df, my_country_name):
    """pick some country"""
    chosen_country = df[df["country"] == my_country_name]
    if chosen_country.empty:  # Empty if couldnt load bc not found
        print("Country not found in the dataset.")
        return None
    else:
        # t for transpose -> lign to column
        tab = chosen_country.drop(columns=["country"])
        tab = tab.loc[:, '1800':'2050'].T
        tab.columns = [my_country_name]
        tab.index = tab.index.astype(int)  # years in int
        tab[my_country_name] = tab[my_country_name].map(parse_pop)
        return tab.dropna()  # delete the empty values


def aff(path: str):
    """entry point to the programm"""
    df = load(path)
    name_one = "France"
    name_two = "Turkmenistan"
    country_one = pick_some_country(df, name_one)
    country_two = pick_some_country(df, name_two)
    if country_one is None or country_two is None:
        return
    else:
        tab = country_one.join(country_two)
        # the format -> pandas method calls matplotlib
        tab.plot(figsize=(10, 8))
        plt.title(f"{name_one} compared to {name_two}")
        plt.xlabel("Year")
        plt.ylabel("Population (millions)")
        plt.grid(True, alpha=0.3)  # create a background grid
        plt.tight_layout()
        # save the graph, define the resolution
        plt.savefig(f"{name_one}_vs_{name_two}population.png", dpi=150)
        # range-> start, end, step. rotate to avoid crushing infos
        plt.xticks(range(1800, 2050, 40), rotation=0)
        # put the pop in M format
        plt.gca().yaxis.set_major_formatter(
            plt.matplotlib.ticker.FuncFormatter(
                lambda x, _: f"{x / 1000000:.0f}M"))
        plt.show()


def main():
    """Entry point of the programm"""
    aff("population_total.csv")


if __name__ == "__main__":
    main()
