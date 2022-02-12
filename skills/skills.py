


from pandas import read_csv, isna

import plotly.express as px
import plotly.graph_objects as go

skills = [
    "Survival",
    "Stealth",
    "Sleight of Hand",
    "Religion",
    "Persuasion",
    "Performance",
    "Perception",
    "Nature",
    "Medicine",
    "Investigation",
    "Intimidation",
    "Insight",
    "History",
    "Deception",
    "Athletics",
    "Arcana",
    "Animal Handling",
    "Acrobatics",
]



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
c_prof = {
    "Fighter": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
    "Ranger": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
    "Paladin": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
    "Barbarian": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
    "Monk": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
    "Warlock": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
    "Sorcerer": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
    "Wizard": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
    "Druid": ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
    "Cleric": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
    "Bard": skills,
    "Rogue": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
}

def plot_skills(data, title, profs):
    all = []
    for r in data.skills:
        if not isna(r):
            all.extend(r.split("|"))

    freq = [100*all.count(s)/len(data) for s in skills]

    cols = [
        "rgba(0,0,0,0)" if s not in profs else "black" 
         for s in skills
    ]

    fig = go.Figure()
    fig.add_bar(
        x=freq,
        y=skills,
        orientation='h',
        marker_color=cols,
        marker_line=dict(
            width=4,
            color="#000"
        )
        )
    fig.update_layout(
        font_family="Garamond",   
        font_size=16,
        yaxis_title="Skill Proficiency",
        xaxis_title="Frequency (%)",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            size=10,
        ),
        xaxis=dict(
            color="#000",
            gridcolor="rgba(0,0,0,0)",
            linecolor="#000",
            range=[0, 100],# len(data)]
        ),
        yaxis=dict(color="#000", linecolor="#000"),
        title=dict(
            text=title,
            font=dict(size=24, color="#000"), xanchor="center", x=0.5
        )
    )
    return fig

if __name__ == "__main__":
    data = read_csv("data/dnd_chars_processed.csv")
    data= data[~data["duplicated"]]
    
    # filter data
    
    # Get list of skills
    figs = []
    figs.append((
        plot_skills(data, "Skill Proficiencies of All Characters", []),
        "all"))
    for cc in cclass:
        figs.append((
            plot_skills(
                data[data["justClass"] == cc],
                "{0} Skills".format(cc),
                c_prof[cc]),
            cc.lower()
        ))
    
    show = False
    if show:
        for f, _ in figs:
            f.show()
    else:
        for f, name in figs:
            f.write_image("img/skills/{0}.png".format(name), height=400, scale=3)
    
