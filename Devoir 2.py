import pandas as pd

#Importe le premier facile, je le garde comme exemple
url = "https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature"
table = pd.read_html(url)[0]
colonne = table[table.columns[1]]
print(colonne)

#Implementation pour les quarante liens

url_array = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita", "https://en.wikipedia.org/wiki/List_of_countries_by_Internet_connection_speeds",
             "https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption_per_capita","https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate",
             "https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures","https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",
             "https://en.wikipedia.org/wiki/Democracy_Index","https://en.wikipedia.org/wiki/List_of_countries_by_tertiary_education_attainment",
             "https://en.wikipedia.org/wiki/Importance_of_religion_by_country","https://en.wikipedia.org/wiki/Christianity_by_country",
             "https://en.wikipedia.org/wiki/Islam_by_country","https://en.wikipedia.org/wiki/Buddhism_by_country",
             "https://en.wikipedia.org/wiki/Jewish_population_by_country","https://en.wikipedia.org/wiki/List_of_countries_by_infant_and_under-five_mortality_rates",
             "https://en.wikipedia.org/wiki/Age_of_criminal_responsibility","https://en.wikipedia.org/wiki/List_of_countries_by_minimum_wage",
             "https://en.wikipedia.org/wiki/List_of_countries_by_external_debt","https://en.wikipedia.org/wiki/List_of_countries_by_income_equality",
             "https://en.wikipedia.org/wiki/List_of_countries_by_total_health_expenditure_per_capita","https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate",
             "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependencies_by_total_fertility_rate","https://en.wikipedia.org/wiki/Tobacco_consumption_by_country",
             "https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate","https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users",
             "https://en.wikipedia.org/wiki/List_of_countries_by_median_age","https://en.wikipedia.org/wiki/List_of_countries_by_economic_freedom",
             "https://en.wikipedia.org/wiki/List_of_countries_by_oil_production","https://en.wikipedia.org/wiki/List_of_countries_by_population_growth_rate",
             "https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy","https://en.wikipedia.org/wiki/List_of_countries_by_meat_consumption",
             "https://en.wikipedia.org/wiki/List_of_countries_by_incarceration_rate","https://en.wikipedia.org/wiki/List_of_countries_by_literacy_rate",
             "https://en.wikipedia.org/wiki/List_of_countries_by_age_at_first_marriage","https://en.wikipedia.org/wiki/List_of_countries_by_spending_on_education_(%25_of_GDP)",
             "https://en.wikipedia.org/wiki/List_of_countries_by_homeless_population","https://en.wikipedia.org/wiki/List_of_countries_by_milk_consumption_per_capita",
             "https://en.wikipedia.org/wiki/List_of_countries_by_food_energy_intake","https://en.wikipedia.org/wiki/Books_published_per_country_per_year",
             "https://en.wikipedia.org/wiki/List_of_countries_by_food_energy_intake","https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature",
]

# table_array = [0,0,0,1,4,1,5,1,4,7,
# 3,0,34,0,1,2,0,1,0,1,
# 2,0,0,5,0,1,0,1,1,1,
# 0,1,0,0,0,0,0,0,0,0]
# colonne_array = [6,2,2,3,2,3,5,1,2,2,
# 3,2,?,2,1,2,4,7,2,1,
# 2,1,1,?,3,2,2,6,1,1,
# 3,5,2,1,3,3,3,3,2,1]

# df = pd.DataFrame()
# #Rappel : la liste de dev humain a plus les données de 2019
# for i in range(40):
#     url = url_array[i]
#     table_i = table_array[i]
#     colonne_i = colonne_array[i]

#     table = pd.read_html(url)[table_i]
#     colonne = table[table.columns[colonne_i]]


# if i == 4 :
# colonne = colonne.truncate(3,17)

# if i == 32:
#     url = url_array[i]
#     resultat = []

#     for j in range(5):
#         afr = pd.read_html(url)[j]
#         col_df = afr[afr.columns[2]]
#         resultat.append(col_df)
#     colonne = pd.concat(resultat, axis=0)


#   df.insert(i,"colonne", colonne)

