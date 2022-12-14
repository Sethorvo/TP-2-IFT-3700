import pandas as pd

from CorrectionDatas import convert_data_float, clean_data, replace_missing_datas

# Importe le premier facile, je le garde comme fonction de test pour imprimer une colonne

# url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita"
# table = pd.read_html(url)[1]
# colonne = table[table.columns[6]]
# colonne = colonne.truncate(1,223)
# colonne.index = table[table.columns[0]].truncate(1,223)
# colonne.index = colonne.index.str.replace('[^a-zA-Z]', '', regex=True)


# Implementation pour les quarante liens
# key == site, values == ( table position, column values position, column name position , ==4, ==20, == 32
dict_wiki = {
    'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita': (1, 6, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_Internet_connection_speeds': (0, 2, 1, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption_per_capita': (0, 2, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate': (1, 3, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures': (4, 2, 1, True, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index': (1, 3, 2, False, False, False),
    'https://en.wikipedia.org/wiki/Democracy_Index': (5, 5, 2, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_tertiary_education_attainment': (1, 1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/Importance_of_religion_by_country': (4, 2, 1, False, False, False),
    'https://en.wikipedia.org/wiki/Christianity_by_country': (7, 2, 0, False, False, False),
    'https://en.wikipedia.org/wiki/Islam_by_country': (3, 3, 0, False, False, False),
    'https://en.wikipedia.org/wiki/Buddhism_by_country': (0, 2, 0, False, False, False),
    'https://en.wikipedia.org/wiki/Jewish_population_by_country': (34, -1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_infant_and_under-five_mortality_rates': (
        0, 1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/Age_of_criminal_responsibility': (1, 1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_minimum_wage': (2, 2, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_external_debt': (0, 4, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_income_equality': (1, 7, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_total_health_expenditure_per_capita': (
        0, 2, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate': (1, 1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependencies_by_total_fertility_rate': (
        2, 2, 1, False, True, False),
    'https://en.wikipedia.org/wiki/Tobacco_consumption_by_country': (0, 1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate': (0, 1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users': (5, -1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_median_age': (0, 3, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_economic_freedom': (1, 2, 1, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_oil_production': (0, 2, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_population_growth_rate': (0, 6, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy': (1, 1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_meat_consumption': (1, 1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_incarceration_rate': (0, 3, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_literacy_rate': (1, 5, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_age_at_first_marriage': (0, 2, 0, False, False, True),
    'https://en.wikipedia.org/wiki/List_of_countries_by_spending_on_education_(%25_of_GDP)': (
        0, 1, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_homeless_population': (0, 3, 0, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_milk_consumption_per_capita': (0, 3, 2, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_number_of_scientific_and_technical_journal_articles': (
        0, 3, 1, False, False, False),
    'https://en.wikipedia.org/wiki/Books_published_per_country_per_year': (0, 3, 1, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_food_energy_intake': (0, 2, 1, False, False, False),
    'https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature': (0, 1, 0, False, False, False)}


def get_colonnes():
    df = pd.DataFrame()
    # Prend la liste des pays et territoire de la page du pib commme label de depart pour les range
    table = pd.read_html(next(iter(dict_wiki)))[1]
    labels = table[table.columns[0]].truncate(1, 223)
    labels = labels.str.replace('[^a-zA-Z]', '', regex=True)
    labels = labels.truncate(1)
    df.index = labels

    for key, values in dict_wiki.items():
        url = key
        table_i = values[0]
        colonne_i = values[1]

        # Saute les deux liens ou je n'arrive a pas a obtenir les colonnes
        if colonne_i == -1:
            continue

        else:
            table = pd.read_html(url)[table_i]

            # to do temporaire pour debugger, les noms doivent être corriger
            column_name = table.columns[colonne_i]

            # Va chercher le nom des pays pour la colonne que l'on extrait
            label = table[table.columns[values[2]]]
            colonne = table[column_name]

            # Le truncate sert a enlever des colonnes nan vide et des index dupliques
            if values[3]:
                colonne = colonne.truncate(3, 17)
                label = label.truncate(3, 17)

            elif values[4]:
                colonne = colonne.truncate(0, 201)
                label = label.truncate(0, 201)

            # Ajoute les differents tableaux de la page en un, une des consignes du prof
            elif values[5]:
                # Pour l'instant les labels sont pas reconnus comme des strings je sais pas pourquoi, a voir
                continue
                url = key
                resultat = []
                label_r = []

                for j in range(5):
                    afr = pd.read_html(url)[j]

                    lab_df = afr[afr.columns[0]]
                    col_df = afr[afr.columns[2]]

                    lab_arr = lab_df.to_numpy()
                    col_arr = col_df.to_numpy()

                    for k in range(len(col_arr)):
                        label_r.append(lab_arr[k])
                        resultat.append(col_arr[k])

                colonne = pd.DataFrame({'col': resultat})
                label = pd.DataFrame({'id': label_r})
                label = label.str.replace('[^a-zA-Z]', '', regex=True)
                colonne.index = label
                df[str(i)] = colonne
                continue

            colonne.index = label
            colonne.index = colonne.index.str.replace('[^a-zA-Z]', '', regex=True)
            df[column_name] = colonne

    convert_data_float(df)
    df = clean_data(df)
    replace_missing_datas(df)
    print(df.to_string())


if __name__ == '__main__':
    get_colonnes()
