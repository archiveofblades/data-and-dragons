

import plotly.express as px

def test(straight, contested, mod):
    dc = 10+mod
    for i in range(20):
        straight.append([])
        contested.append([])
        for j in range(20):
            if i+1 > dc:
                straight[i].append(1)
            else:
                straight[i].append(0)
            if i+1 > j+1+mod:
                contested[i].append(1)
            else:
                contested[i].append(0)

if __name__ == "__main__":
    mod = 2
    s = []
    c = []
    for mod in range(-11,11):
        straight = []
        contested = []
        test(straight, contested, mod)
        s.append(sum(x.count(1) for x in straight))
        c.append(sum(x.count(1) for x in contested))
        print("{0}//{1}".format(
        sum(x.count(1) for x in straight),
        sum(x.count(1) for x in contested)
        ))
    fig1 = px.line(s)
    fig1.show()
    fig2 = px.line(c)
    fig2.show()