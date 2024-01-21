from datetime import datetime, timedelta

ost_lab = datetime(2024, 1, 15)

kol = datetime(2024, 2, 12)

dni = (datetime.now() - ost_lab).days

czas = kol - datetime.now()

print(f"Od ostatnich laboratoriów minęło {dni} dni.")
print(f"Do kolokwium pozostało {czas.days} dni i {czas.seconds // 3600} godzin.")
