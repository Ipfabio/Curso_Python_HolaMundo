mascotas = ["Pelusa", "Wolfgang", "Pulga",
            "Felipe", "Wolfgang", "Chanchito feliz"]

print(mascotas.count("Wolfgang"))
if "Wolfgang" in mascotas:  # Lo metemos dentro de un 'if' para evitar que tire error
    print(mascotas.index("Wolfgang"))
