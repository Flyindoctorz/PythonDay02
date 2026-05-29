import matplotlib.pyplot as plt
from load_csv import load


def stats(path, papath):
	incper = load_csv(path)
	lifexpec = load_csv(papath)
	if incper is None or lifexpec is None:
		print("Error: Couldnt load the documents")
		return
	col = incper["country"]

def main():
    """Entry point of the programm"""
    stats("income_per_person_gdppercapita_ppp_inflation_adjusted.csv", "life_expectancy_years.csv")


if __name__ == "__main__":
    main()