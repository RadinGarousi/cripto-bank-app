import sqlite3
import pathlib

translation_dir = pathlib.Path(__file__).parent     # Detect folder path

# Connect database for  collection languages
conn = sqlite3.connect(database="languages_list.db", autocommit=False)
cur = conn.cursor()

# Collection rtl, ltr languages
ltr_languages = cur.execute("SELECT DISTINCT country_language FROM languages WHERE direction='ltr'").fetchall()
rtl_languages = cur.execute("SELECT DISTINCT country_language FROM languages WHERE direction='rtl'").fetchall()

# Create ltr and rtl folders to sparat left-to-right and right-to-left languages
(translation_dir / "ltr").mkdir(exist_ok=True)
(translation_dir / "rtl").mkdir(exist_ok=True)

# Crate database for language
[(translation_dir / "ltr" / f"{lrt_languages_file[0]}.db").touch(exist_ok=True) for lrt_languages_file in ltr_languages]
[(translation_dir / "rtl" / f"{rtl_languages_file[0]}.db").touch(exist_ok=True) for rtl_languages_file in rtl_languages]