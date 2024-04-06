import os
import random

from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def get_countries():
    return supabase.table('countries').select("*").limit(5).execute()


def get_data_by_country(country: str):
    return supabase.table('countries').select("*").eq("name", country).execute()


def add_country(name: str, continent: str):
    rng = random.randint(1, 100)
    return supabase.table('countries').insert({"id": rng, "name": name, "continent": continent}).execute()


def update_country(name: str, continent: str):
    return supabase.table('countries').update({"continent": continent}).eq("name", name).execute()


def delete_country(name: str):
    return supabase.table('countries').delete().eq("name", name).execute()


if __name__ == "__main__":
    print(get_countries())

    print(get_data_by_country("Brazil"))

    print(add_country("Brazil", "South America"))
    print(get_countries())

    print(update_country("Brazil", "Africa"))
    print(get_countries())

    print(delete_country("Brazil"))
    print(get_countries())


