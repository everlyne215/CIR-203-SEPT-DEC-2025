routes = [
    "Nairobi-Ruaraka",
    "Mombasa-Bamburi",
    "Nakuru-Shabab",
    "Kisumu-Milimani",
    "Eldoret-Kapsoya",
    "Thika-Makongeni",
    "Nanyuki-MeruRoad",
    "Nyeri-Mathari",
    "Malindi-Shela",
    "Naivasha-Maraigushu"
]

routes.append("Kitengela-AthiRiver")
routes.remove("Kisumu-Milimani")

routes.sort()
routes.reverse()

num_starting_N = sum(r[0] == "N" for r in routes)
print(num_starting_N)

long_named_routes = [r for r in routes if len(r) >= 12]
print(long_named_routes)
