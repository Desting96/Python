class Cars:
    color = ""
    brand = ""
    year = 0
    countrycar = ""

    def __init__(self, color, brand, year, countrycar):
        self.color = color
        self.brand = brand
        self.year = year
        self.countrycar = countrycar


class Person(Cars):
    name = ""
    years = 0
    country = ""

person = Person("green", "Mustang", 2006, "España")

print(person.countrycar)