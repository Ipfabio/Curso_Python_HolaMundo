def get_product(**datos):  # Siempre que utilicemos esto, al pasarle el parametro necesitamos ponerle un nombre al parametro
    print(datos["id"], datos["name"]) # 'datos'


get_product(id="23", name="Iphone", desc="Esto es un iphone")
