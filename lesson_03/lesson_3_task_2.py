from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79261234567"),
    Smartphone("Xiaomi", "Redmi Note 11", "+79361234567"),
    Smartphone("Huawei", "P40", "+79461234567"),
    Smartphone("Nokia", "G10", "+79561234567"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
