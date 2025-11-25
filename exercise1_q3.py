routes = [
    "Nairobi-Westlands",
    "Mombasa-Bamburi",
    "Nakuru-Pipeline",
    "Kisumu-Milimani",
    "Eldoret-Kapsoya",
    "Thika-Makongeni",
    "Nanyuki-King'uru",
    "Nyeri-Ruring'u",
    "Malindi-Vipingo",
    "Naivasha-MaiMahiu"
]

routes.append("Kajiado-Ngong")
routes.remove("Kisumu-Milimani")

routes.sort()
routes.reverse()

num_starting_N = sum(r.startswith("N") for r in routes)
print(num_starting_N)

long_route_names = [r for r in routes if len(r) > 12]
print(long_route_names)
