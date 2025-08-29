import sqlite3
import countryinfo
import langcodes

# connect dtabase
conn = sqlite3.connect(
    database="languages_list.db",
    autocommit=False
)

cur = conn.cursor()


# create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS languages
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT NOT NULL,
    country_language TEXT NOT NULL,
    direction TEXT NOT NULL
)
""")

conn.commit()

# list all country with country language

language_directions = {
    "Arabic": "rtl",
    "Persian": "rtl",
    "Hebrew": "rtl",
    "Urdu": "rtl",
    "Pashto": "rtl",
    "Divehi": "rtl",
    "Yiddish": "rtl",
    "Sindhi": "rtl",

    "English": "ltr",
    "French": "ltr",
    "German": "ltr",
    "Spanish": "ltr",
    "Italian": "ltr",
    "Portuguese": "ltr",
    "Dutch": "ltr",
    "Swedish": "ltr",
    "Norwegian": "ltr",
    "Danish": "ltr",
    "Finnish": "ltr",
    "Russian": "ltr",
    "Chinese": "ltr",
    "Japanese": "ltr",
    "Korean": "ltr",
    "Hindi": "ltr",
    "Bengali": "ltr",
    "Turkish": "ltr",
    "Greek": "ltr",
    "Thai": "ltr",
    "Armenian": "ltr",
    "Georgian": "ltr",
    "Amharic": "ltr",
    "Tigrinya": "ltr",
    "Malay": "ltr",
    "Samoan": "ltr",
    "Fijian": "ltr",
    "Dzongkha": "ltr",
    "Swahili": "ltr",
    "Afrikaans": "ltr",
    "Maltese": "ltr",
    "Albanian": "ltr",
    "Belarusian": "ltr",
    "Croatian": "ltr",
    "Czech": "ltr",
    "Slovak": "ltr",
    "Slovenian": "ltr",
    "Hungarian": "ltr",
    "Icelandic": "ltr",
    "Irish": "ltr",
    "Lithuanian": "ltr",
    "Latvian": "ltr",
    "Estonian": "ltr",
    "Macedonian": "ltr",
    "Romanian": "ltr",
    "Serbian": "ltr",
    "Bulgarian": "ltr",
    "Kazakh": "ltr",
    "Uzbek": "ltr",
    "Turkmen": "ltr",
    "Kyrgyz": "ltr",
    "Tajik": "ltr",
    "Nepali": "ltr",
    "Māori": "ltr",
    "Chamorro": "ltr",
    "Guarani": "ltr",
    "Aymara": "ltr",
    "Quechua": "ltr",
}

country_language = []
dict = countryinfo.CountryInfo()
countries = dict.all()

for country_name in countries.keys():
    try:
        for language_code in countries[country_name]["languages"]:
            language_name = langcodes.get(language_code).display_name()
            country_language.append((countries[country_name]["name"] , language_name, language_directions[language_name]))
    except Exception as e:
        print(e)
        continue

# insert data
sql_languages_params = []
for x in range(len(country_language)):
    sql_languages_params.clear()
    for sql_params in country_language[x]:
        sql_languages_params.append(sql_params)

    cur.execute("""
        INSERT INTO languages(country, country_language, direction)
        VALUES (?, ?, ?)
    """, (sql_languages_params[0], sql_languages_params[1], sql_languages_params[2]))

    conn.commit()
conn.close()