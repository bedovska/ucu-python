
    
def get_epact(year):
    c = year // 100
    epact = (8 + c // 4 - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
    return epact



while True:
    year = input("enter a year:")
    
    year_is_valid = False
    if year.isdigit():
        year = int(year)
        year_is_valid = year > 999 and year <= 9999

    if year_is_valid:
        print(get_epact(year))

    else:
        print(f"wrong year value: {year}")