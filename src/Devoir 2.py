import pandas as pd

from CorrectionDatas import convert_data_float, clean_data, replace_missing_datas, describe_data, \
    filled_with_regression_multiple_time, duplicate_as_binairies_compare_to_median, find_delete_rows
from Correlation import find_biggest_correlation, order_correlation, make_histogram
from OutputJson import list_to_json
from reduction_dimension import execute_question4
from src.LinearRegression import find_best_linear_regression, normalize_regression

# Importe le premier facile, je le garde comme fonction de test pour imprimer une colonne

# url = "https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users"
# table = pd.read_html(url)[5]
# m = pd.read_csv("tableau.csv")
# print(m.columns)


# Implementation pour les quarante liens
# key == site, values == ( table position, column values position, column name position , ==4, ==20, == 32
dict_wiki = {
    'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita': (1, 6, 0, "PIB par capita"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_Internet_connection_speeds': (
        0, 2, 1, "Vitesse de téléchargement (Mb/s) moyenne"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption_per_capita': (
        0, 2, 0, "Litres d'alcool consommé par an, par capita chez 15+"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate': (
        1, 3, 0, "Homicide volontaire par 100k personnes"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures': (
        4, 2, 1, "%PIB dépensé dans le militaire"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index': (
        1, 3, 2, "Indice de développement humain"),
    'https://en.wikipedia.org/wiki/Democracy_Index': (5, 5, 2, "Indice de démocratie"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_tertiary_education_attainment': (
        1, 1, 0, "% d'éducation tertiare de 2 ans atteint"),
    'https://en.wikipedia.org/wiki/Importance_of_religion_by_country': (4, 2, 1, "% d'importance de la religion"),
    'https://en.wikipedia.org/wiki/Christianity_by_country': (7, 2, 0, "% de chrétiens"),
    'https://en.wikipedia.org/wiki/Islam_by_country': (3, 3, 0, "% de musulmans"),
    'https://en.wikipedia.org/wiki/Buddhism_by_country': (0, 2, 0, "% de bouddhistes"),
    'https://en.wikipedia.org/wiki/Jewish_population_by_country': (34, -1, 0, "% de juifs"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_infant_and_under-five_mortality_rates': (
        0, 1, 0, "Mortalité en dessous de 5 ans (mort/1k naissance)"),
    'https://en.wikipedia.org/wiki/Age_of_criminal_responsibility': (1, 1, 0, "Age de responsabilité criminelle"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_minimum_wage': (2, 2, 0, "Salaire minimum annuel"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_external_debt': (0, 4, 0, "Dette externe en % de PIB"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_income_equality': (1, 7, 0, "Indice de Gini en %"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_total_health_expenditure_per_capita': (
        0, 2, 0, "Dépense en santé par capita"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate': (1, 1, 0, "Taux de suicide"),
    'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependencies_by_total_fertility_rate': (
        2, 2, 1, "Taux de fertilité"),
    'https://en.wikipedia.org/wiki/Tobacco_consumption_by_country': (0, 1, 0, "Consommateur de tabac chez 15+"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate': (0, 1, 0, "Taux d'obésité"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users': (
        5, -1, 0, "Taux d'utilisateur d'Internet"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_median_age': (0, 3, 0, "Age médian"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_economic_freedom': (1, 2, 1, "Score de liberté économique"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_oil_production': (0, 2, 0, "Production de pétrole"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_population_growth_rate': (
        0, 6, 0, "Taux de croissance de population"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy': (1, 1, 0, "Espérance de vie"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_meat_consumption': (
        1, 1, 0, "Consommation de viande en kg par capita"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_incarceration_rate': (0, 3, 0, "Taux d'incarcération par 100k"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_literacy_rate': (1, 5, 0, "Taux d'alphabétisation"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_age_at_first_marriage': (0, 2, 0, "Age de premier marriage"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_spending_on_education_(%25_of_GDP)': (
        0, 1, 0, "Dépense en éducation, % du PIB"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_homeless_population': (0, 3, 0, "Taux d'itinérance par 100k"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_milk_consumption_per_capita': (
        0, 3, 2, "Consommation de lait par capita"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_number_of_scientific_and_technical_journal_articles': (
        0, 3, 1, "Nombre d'articles scientifique par capita"),
    'https://en.wikipedia.org/wiki/Books_published_per_country_per_year': (0, 3, 1, "Livres publiés par année"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_food_energy_intake': (
        0, 2, 1, "Consommation de nourriture en kilocalories"),
    'https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature': (
        0, 1, 0, "Température annuelle moyenne")
}


def get_colonnes():
    df = pd.DataFrame()
    # Prend la liste des pays et territoire de la page du pib commme label de depart pour les range
    table = pd.read_html(next(iter(dict_wiki)))[1]
    labels = table[table.columns[0]].truncate(1, 223)
    labels = labels.str.replace('[^a-zA-Z]', '', regex=True)
    labels = labels.truncate(1)
    df.index = labels

    manquant = pd.read_csv("tableau.csv")

    for key, values in dict_wiki.items():
        url = key
        table_i = values[0]
        colonne_i = values[1]
        table = pd.read_html(url)[table_i]
        label = table[table.columns[values[2]]]

        # Importe du csv les deux colonnes manquantes
        if colonne_i == -1:

            if values[3] == "% de juifs":
                label = label.str.replace('\[.*', '', regex=True)
                colonne = manquant[manquant.columns[0]]
                colonne = colonne.truncate(0, 111)

            elif values[3] == "Taux d'utilisateur d'Internet":
                colonne = manquant[manquant.columns[1]]

        else:

            # to do temporaire pour debugger, les noms doivent être corriger
            column_name = table.columns[colonne_i]

            # Va chercher le nom des pays pour la colonne que l'on extrait
            colonne = table[column_name]

            # Le truncate sert a enlever des colonnes nan vide et des index dupliques
            if values[3] == "%PIB dépensé dans le militaire":
                colonne = colonne.truncate(3, 17)
                label = label.truncate(3, 17)

            elif values[3] == "Taux de fertilité":
                colonne = colonne.truncate(0, 201)
                label = label.truncate(0, 201)

            elif values[3] == "% de chrétiens":
                label = label.str.replace('(details)', '', regex=True)

            # Ajoute les differents tableaux de la page en un, une des consignes du prof
            elif values[3] == "Age de premier marriage":
                url = key
                resultat = []
                label = []

                for j in range(5):
                    afr = pd.read_html(url)[j]
                    lab_df = afr[afr.columns[0]]
                    lab_df = lab_df.str.replace('\[.*', '', regex=True)
                    lab_df = lab_df.str.replace('\s\(.*', '', regex=True)
                    col_df = afr[afr.columns[2]]
                    lab_arr = lab_df.to_numpy()
                    col_arr = col_df.to_numpy()

                    for k in range(len(col_arr)):
                        label.append(lab_arr[k])
                        resultat.append(col_arr[k])

                colonne = pd.DataFrame({"Age de premier marriage": resultat})

        colonne.index = label
        colonne.index = colonne.index.str.replace('[^a-zA-Z]', '', regex=True)
        df[values[3]] = colonne

    convert_data_float(df)
    df_old = df.copy()
    df = clean_data(df)
    find_delete_rows(df, df_old)
    df_is_to_be_calculed = df.isna()
    replace_missing_datas(df)

    make_histogram(df)
    df = filled_with_regression_multiple_time(df, df_is_to_be_calculed, 2)

    df_as_binairies = duplicate_as_binairies_compare_to_median(df)

    # question 2
    biggest_corroletion_between_columns = find_biggest_correlation(df)
    order_of_average_correlation = order_correlation(df)

    list_to_json(biggest_corroletion_between_columns, "question2b")
    list_to_json(order_of_average_correlation, "question2c")

    # question3
    # partie linéaire
    find_best_linear_regression(df)
    normalize_regression(df)

    # question 4
    execute_question4(df)

    describe = describe_data(df)
    print(df.to_string())


if __name__ == '__main__':
    get_colonnes()
