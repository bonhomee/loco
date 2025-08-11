from bs4 import BeautifulSoup

# Cargar HTML de reservas
with open("booking_reservas.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

cobradas = []
pendientes = []

for fila in soup.select("tr.bui-table__row"):
    # Comprobar si tiene tarjeta virtual
    if fila.select_one("span.vcc_active_status_txt"):
        # Localizador (número de reserva)
        loc_elem = fila.select_one('td[data-heading="Número de reserva"] a.bui-link.bui-link--primary span')
        if not loc_elem:
            continue
        localizador = loc_elem.get_text(strip=True)

        # Texto que describe el método de pago o estado
        estado_pago = fila.get_text(" ", strip=True).lower()

        # Clasificar según estado
        if "pagado" in estado_pago or "pago online" in estado_pago or "cliente ha pagado" in estado_pago:
            cobradas.append(localizador)
        else:
            pendientes.append(localizador)

# Guardar resultados en ficheros
with open("localizadores_vcc_cobradas.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cobradas))

with open("localizadores_vcc_pendientes.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(pendientes))

print("Localizadores cobradas:", cobradas)
print("Localizadores pendientes:", pendientes)
