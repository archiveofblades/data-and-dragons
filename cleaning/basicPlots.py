


from pandas import read_csv

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



def plot_race(data):
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=data["processedRace"],
        histnorm="percent",
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
        xaxis_title="Race",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(
            color="#000",
            gridcolor="rgba(0,0,0,0)",
            linecolor="#000",
            range=[0,30]
        ),
        xaxis=dict(color="#000", linecolor="#000"),
        title=dict(
            text="Race of Unqiue Characters",
            font=dict(size=24, color="#000"), xanchor="center", x=0.5
        )
    )
    return fig

def plot_class(data):
    # ignore multiclass
    data = data[data["justClass"].isin(cclass)]
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=data["justClass"],
        histnorm="percent",
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
        xaxis_title="Class",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(
            color="#000",
            gridcolor="rgba(0,0,0,0)",
            linecolor="#000",
            range=[0,30]
        ),
        xaxis=dict(color="#000", linecolor="#000"),
        title=dict(
            text="Class of Unqiue Single-Class Characters",
            font=dict(size=24, color="#000"), xanchor="center", x=0.5
        )
    )
    return fig

def plot_level(data):
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=data["level"],
        histnorm="percent",
        marker_color="rgba(0,0,0,0)",
        marker_line=dict(
            width=4,
            color="#000"
        )
        ))
    fig.update_layout(
        font_family="Garamond",   
        font_size=16,
        yaxis_title="Percent",
        xaxis_title="Level",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(
            color="#000",
            gridcolor="rgba(0,0,0,0)",
            linecolor="#000",
            range=[0,30]
        ),
        xaxis=dict(color="#000", linecolor="#000"),
        title=dict(
            text="Level of All Characters",
            font=dict(size=24, color="#000"), xanchor="center", x=0.5
        )
    )
    return fig

if __name__ == "__main__":
    data = read_csv("data/dnd_chars_processed.csv")
    race = plot_race(data[~data["duplicated"]])
    cclass = plot_class(data[~data["duplicated"]])
    level = plot_level(data)
    
    show = False
    if show:
        race.show()
        cclass.show()
        level.show()
    else:
        race.write_image("img/basic/race.png", scale=3)
        cclass.write_image("img/basic/class.png", scale=3)
        level.write_image("img/basic/level.png", scale=3)
    
