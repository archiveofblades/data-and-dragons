"""Load and clean the data."""


from pandas import read_csv

# Permitted character classes
cclass = [
    "Fighter",
    "Ranger",
    "Paladin",
    "Barbarian",
    "Monk",
    "Warlock",
    "Sorcerer",
    "Wizard",
    "Druid",
    "Cleric",
    "Bard",
    "Rogue"
]
# Permitted race
race = [
    "Dragonborn",
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling",
    "Half-Orc",
    "Human",
    "Tiefling",
]
# Fields of interest
fields = [
    "background",
    "class",
    "justClass",
    "subclass",
    "level",
    "feats",
    "HP",
    "AC",
    "Str",
    "Dex",
    "Con",
    "Wis",
    "Int",
    "Cha",
    "skills",
    "castingStat",
    "choices",
    "processedAlignment",
    "processedRace",
    "processedSpells",
    "processedWeapons",
    "duplicated"
]



def load_data():
    """Load tsv to dataframe."""
    return read_csv("data/dnd_chars_all.tsv", sep="\t")

if __name__=="__main__":
    df = load_data()
    print("Total Characters: {0}".format(df.shape[0]))
    print("Earliest Entry: {0}".format(df["date"].min()[:10]))
    print("Latest Entry: {0}".format(df["date"].max()[:10]))


    # Sanity Checks
    df = df[df["level"] <= 20]
    df = df[df["level"] >= 1]
    df = df[df["HP"] <= 300]
    df = df[df["HP"] >= 1]
    for ability in ["Str", "Dex", "Con", "Wis", "Int", "Cha"]:
        df = df[df[ability] <= 30]
        df = df[df[ability] >= 3]
    
    # Race
    df = df[df["processedRace"].isin(race)]

    # Class
    mclass= []
    for v in df["justClass"].unique():
        if v != v:  # catch NaN
            continue
        count = 0
        for c in v.split("|"):
            count += 1
            if count > 3 or c not in cclass:
                break
        else:
            mclass.append(v)
    df = df[df["justClass"].isin(cclass + mclass)]
    
    # Drop non-unique same-level characters
    df = df.drop_duplicates(["name", "level"], keep='first')
    
    # Add `unique` field that is true for the first entry with unique name/justClass
    # df = df.drop_duplicates(["name", "justClass"], keep='first')
    # df["unique"] = false
    df["duplicated"] = df.duplicated(["name", "justClass"], keep='first')
    
    # Select only certain fields
    df = df[fields]
    
    # Store results
    print("Filtered Characters: {0}".format(df.shape[0]))
    df.to_csv("data/dnd_chars_processed.csv")