import pandas as pd


def load(path: str):
    """import a database from a string and return a csv"""
    try:
        if isinstance(path, str):
            load_csv = pd.read_csv(path)
            print(f"Loading dataset of dimensions {load_csv.shape}")
            return (load_csv)
        else:
            raise TypeError("Error : Path must be a string")
    except FileNotFoundError:
        print("Error : bad path")
    except TypeError as e:
        print(f"{e}")
    except Exception as e:
        print(f"{e}")
    return (None)


def main():
    """Entry point of the programm"""
    print(load("life_expectancy_years.txt"))
    print(load("life_expectancy_years.jpg"))
    print(load(""))
    print(load(7))
    print(load("banniere.jpg"))


if __name__ == "__main__":
    main()
