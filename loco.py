from bs4 import BeautifulSoup

# Cargar HTML guardado
with open("loco.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

localizadores_vcc = []

# Recorrer cada fila de la tabla
for fila in soup.select("tr.bui-table__row"):
    # Si la fila contiene una tarjeta virtual
    if fila.select_one("span.vcc_active_status_txt"):
        # Buscar el enlace que lleva al número de reserva
        enlace_reserva = fila.select_one('td[data-heading="Número de reserva"] a.bui-link.bui-link--primary span')
        if enlace_reserva:
            localizadores_vcc.append(enlace_reserva.get_text(strip=True))

# Mostrar resultados
print("Localizadores con Tarjeta Virtual encontrados:")
for loc in localizadores_vcc:
    print(loc)

# Guardar en TXT
with open("localizadores_vcc.txt", "w", encoding="utf-8") as f:
    for loc in localizadores_vcc:
        f.write(loc + "\n")

print(f"Total encontrados: {len(localizadores_vcc)}")
