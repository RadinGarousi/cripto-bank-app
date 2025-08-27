import pathlib as pl
import json

json_directory = pl.Path(__file__).parent.parent.parent / "files"

def insert(them_mode, color_mode, user_device, last_device):
    with open(json_directory / "signup_page_base_data.json", "w") as json_file:
        json.dump({"them_mode": them_mode, "color_mode": color_mode, "user_device": user_device, "last_device": last_device}, json_file)

def reade():
    with open(json_directory / "signup_page_base_data.json", "r") as json_file:
        file_read = json.load(json_file)
    return file_read