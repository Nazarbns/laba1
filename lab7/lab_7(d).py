import pandas as pd
data = {'Imię': ['Robert', 'Magda', 'Tomasz', 'Zosia'],
        'nazwisko': ['Nowak', 'Kowalska', 'Lewandoski', 'Szpilewski'],
        'nr_albumu': [70532, 70256, 70712, 70402],
        'ocena_z_kolokwium': [4.0, 3.0, 5.0, 3.5]}
df = pd.DataFrame(data)
# a.
oceny_wieksze_niz_4 = df[df['ocena_z_kolokwium'] > 4]

# b.
posortowani_studenci = df.sort_values(by='ocena_z_kolokwium')

srednia_ocena_w_grupach = df.groupby('ocena_z_kolokwium')['ocena_z_kolokwium'].mean()

merged_df = pd.merge(df, df1, on='nr_albumu', how='left')

print(df)

print("\nStudenci z oceną większą niż 4:")
print(oceny_wieksze_niz_4)
print("\nStudenci posortowani według ocen:")
print(posortowani_studenci)

print("\nŚrednia ocena w każdej grupie:")
print(srednia_ocena_w_grupach)

print("\nPołączona ramka danych:")
print(merged_df)