BIRTH = 7
DEATH = 13
IMMIGRANT = 35
SECONDS_IN_YEAR = 31536000

years = int(input("Years: "))

population_now = 307357870

births_per_year = SECONDS_IN_YEAR / BIRTH
deaths_per_year = SECONDS_IN_YEAR / DEATH
immigrants_per_year = SECONDS_IN_YEAR / IMMIGRANT

if years < 0:
    print("Invalid input!")

else:
    new_population = int(population_now + (births_per_year + immigrants_per_year - deaths_per_year) * years)

    print("New population after", years, "years is", new_population)