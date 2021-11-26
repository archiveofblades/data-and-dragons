


from pandas import read_csv

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

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



def plot_weapons(data):
    weapons = []
    for pw in data["processedWeapons"]:
        if (not pd.isna(pw)):
            # ignore duplicate weapons
            pw_list = set(pw.split("|"))
            weapons.extend(pw_list)
            # weapons.append(pw)
    
    weapons = list(filter(
        lambda a: a != "Dagger" and a != "Blowgun" and a != "",
         weapons ))
    
    # Do some kind of weapon filtering:
    # ranged, simple, etc. ?
    # do stuff by class for validation
    
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=weapons,
        # histnorm="percent",
        marker_color="rgba(0,0,0,0)",
        marker_line=dict(
            width=4,
            color="#000"
        )
        ))
    fig.update_layout(
        xaxis_categoryorder="min descending",
        font_family="Garamond",   
        font_size=16,
        yaxis_title="Percent",
        xaxis_title="Weapon",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(
            color="#000",
            gridcolor="rgba(0,0,0,0)",
            linecolor="#000",
            # range=[0,30]
        ),
        xaxis=dict(color="#000", linecolor="#000"),
        title=dict(
            text="Weapons of Unqiue Characters",
            font=dict(size=24, color="#000"), xanchor="center", x=0.5
        )
    )
    return fig


if __name__ == "__main__":
    print("Weapons")
    data = read_csv("data/dnd_chars_processed.csv")
    data = data[~data["duplicated"]]
    
    total = len(data)
    

    weapons = [
        "Rapier", 
        "Morningstar", 
        "Crossbow, Light", 
        "War pick", 
        "Warhammer", 
        "Battleaxe", 
        "Flail", 
        "Longsword", 
        "Greatclub", 
        "Longbow", 
        "Shortbow", 
        "Scimitar", 
        "Mace", 
        "Handaxe", 
        "Spear", 
        "Javelin", 
        "Trident", 
        "Quarterstaff", 
        "Crossbow, hand", 
        "Shortsword", 
        "Crossbow, Heavy", 
        "Maul", 
        "Glaive", 
        "Halberd", 
        "Dagger", 
        "Blowgun", 
        "Greataxe", 
        "Sickle", 
        "Pike", 
        "Light hammer", 
        "Net", 
        "Lance", 
        "Sling", 
        "Club", 
        "Unarmed Strike", 
        "Whip", 
        "Greatsword", 
        "Dart", 
    ]
    counts = {x:0 for x in weapons}
    
    
    empty = 0
    for pw in data["processedWeapons"]:
        if (not pd.isna(pw)):
            if (pd == ""):
                empty += 1
            for k in counts.keys():
                if (k in pw):
                    counts[k] += 1
        else:
            empty += 1
    
    print("Characters: {0}".format(total))
    total = total - empty
    print("With Weapons: {0}".format(total))
    print("With:")
    counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])} 
    totalw = 0
    for (k,v) in counts.items():
        print("\t{0}:\t{1} / {2:.2f}%".format(k, v, 100 * v/total))
        totalw += v
    # print("\tDagger:\t{0}".format())
    # print(data["processedWeapons"])
    
    # Plot barchar for all weapons (do filtering before selecting)
    weapons = plot_weapons(data)
    
    print("Total Weapons:\t{0}".format(totalw))
    
    
    # import sys
    # sys.exit()
    
    # race = plot_race(data[~data["duplicated"]])
    # cclass = plot_class(data[~data["duplicated"]])
    # level = plot_level(data)
    
    show = True
    if show:
        weapons.show()
    else:
        weapons.write_image("img/weapons/weapons.png", scale=3)
    
