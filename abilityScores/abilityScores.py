

import pandas as pd
from pandas import read_csv
import numpy as np
import plotly.graph_objects as go

import plotly.express as px


deck = [9,8,8,8,8,7,6,6,4,4,3,3]
def cards():
    return cardDraft(deck, [])


# Method:
# Pick a pair, then recursivly pick the next

def cardDraft(cards, notin):
    if len(cards) == 0:
        return [[]]
    scores = []
    for c in range(12):
        if c in notin:
            continue
        for c2 in range(12):
            if c2 in notin or c == c2:
                continue
            ab = cards[c] + cards[c2]
            rest = cardDraft(cards, notin+[c,c2])
            for s in rest:
                scores.append([ab] + s)
    return scores

def plotPB(data, title):

    fig = go.Figure(
        data=[go.Box(
            
        y=data[i],
        marker_color="#b8b894",
        # marker_line=dict(
        #     width=2,
        #     color="#000"
        # )
        showlegend=False,
        boxpoints=False,
        whiskerwidth=1,
        width=1,
        ) for i in range(65)]
    )
    fig.update_layout(
        font_family="Garamond",   
        font_size=16,
        yaxis_title="Ability Score",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(
            color="#000",
            gridcolor="rgba(0,0,0,0)",
            linecolor="#000",
        ),
        xaxis=dict(
            showticklabels=False,
            color="#000",
            linecolor="rgba(0,0,0,0)",
        ),
        title=dict(
            text=title, 
            font=dict(size=24, color="#000"), xanchor="center", x=0.5
        )
    )
    return fig

def pointbuy():
    # return pointbuy_next(5, 27, 15)
    scores = pointbuy_next(5, 27, 15)
    trimmed = [scores[0]]
    for s in scores[1:]:
        # add to trimmed only if better in some way that what is there
        worse = True
        for t in trimmed:
            worse = True
            for i in range(len(s)):
                if s[i] > t[i]:
                    worse = False
                    break
            # discard if worse
            if worse:
                break
        if not worse:
            trimmed.append(s)            
        
    return trimmed

pb_costs = [
    (15, 9),
    (14, 7),
    (13, 5),
    (12, 4),
    (11, 3),
    (10, 2),
    (9, 1),
    (8, 0),
]

def pointbuy_next(n, points, last):
    # pick a value that we can afford that is at most as big as the previous
    scores = []
    for (score, cost) in pb_costs:
        if score <= last and cost <= points:
            if n > 0:
                for x in pointbuy_next(n-1, points-cost, score):
                    scores.append([score] + x)
            else:
                scores.append([score])
                
    # return a list of possible scores from here on
    # remove scores that are strictly worse than others
    # sets are in descending order
    trimmed = [scores[0]]
    for s in scores[1:]:
        # add to trimmed only if better in some way that what is there
        better = False
        for t in trimmed:
            for i in range(len(s)):
                if s[i] > t[i]:
                    better = True
                    break
            if better:
                break
        if better:
            trimmed.append(s)            
        
    return trimmed
    


def roll4d6():
    rolls = []
    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                for d in range(1,7):
                    rolls.append(a+b+c+d-min([a,b,c,d]))
    return rolls

def roll3d6():
    rolls = []
    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                rolls.append(a+b+c)
    return rolls


def plot(data, title, top):
    mean = np.mean(data)
    std = np.std(data)
    print(title)
    print("Mean: {0}".format(mean))    
    print("Std: {0}".format(std))    
    print("Low: {0}".format(mean-std))    
    print("High: {0}".format(mean+std))    
    
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=data,
        histnorm="probability",
        marker_color="#b8b894",
        # marker_line=dict(
        xbins=dict(size=1),
        #     width=2,
        #     color="#000"
        # )
        ))
    fig.add_shape(type="line", x0=mean, x1=mean, y0=0, y1=top,
        xref="x", yref="y", line=dict(width=3, color="black"))
    fig.add_shape(type="line", x0=mean-std, x1=mean-std, y0=0, y1=top,
        xref="x", yref="y", line=dict(color="black", dash="dash"))
    fig.add_shape(type="line", x0=mean+std, x1=mean+std, y0=0, y1=top,
        xref="x", yref="y", line=dict(color="black", dash="dash"))
    fig.update_layout(
        font_family="Garamond",   
        font_size=16,
        yaxis_title="Probability",
        xaxis_title="Ability Score",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(
            color="#000",
            gridcolor="rgba(0,0,0,0)",
            linecolor="#000",
        ),
        xaxis=dict(
            color="#000",
            linecolor="#000",
            linewidth=2,
            range=[2.5, 18.5],
        ),
        title=dict(
            text=title, 
            font=dict(size=24, color="#000"), xanchor="center", x=0.5
        )
    )
    return fig

if __name__ == "__main__":
    # data = cards()
    # print("Card Combos: {0}".format(len(data)))
    
    # means = [np.mean(d) for d in data]
    # print("Mean mean: {0}".format(np.mean(means)))    
    # print("Deviation in mean: {0}".format(np.std(means)))    
    # std = [np.std(d) for d in data]
    # print("Mean deviation: {0}".format(np.mean(std)))    
    # print("Deviation in deviation: {0}".format(np.std(std)))    

    data = pointbuy()
    print("Point Buy Possibilities: {0}".format(len(data)))
    
    means = [np.mean(d) for d in data]
    print("Mean mean: {0}".format(np.mean(means)))    
    print("Deviation in mean: {0}".format(np.std(means)))    
    std = [np.std(d) for d in data]
    print("Mean deviation: {0}".format(np.mean(std)))    
    print("Deviation in deviation: {0}".format(np.std(std)))    
    
    data = sorted(data,
        reverse=True,
        key=lambda x: (np.quantile(
                x,
                q=0.75
            ),
            np.quantile(
                x,
                q=0.25)
            ))
    
    df = pd.DataFrame(data).T
    fig = plotPB(df, "Point Buy Distributions")
    
    figs = [
        (plot(roll4d6(), "Roll 4d6, Drop Lowest", 0.15), "r4d6"),
        (plot(roll3d6(), "Roll 3d6", 0.15), "r3d6"),
        (plot([15,14,13,12,10,8], "Standard Array", 0.2), "std"),
        (fig, "pb")        
    ]
    
    show = True 
    store = True
    
    for (fig, fname) in figs: 
        if show:
            fig.show()
        if store:
            fig.write_image("img/ability/{0}.png".format(fname), scale=3)
    
