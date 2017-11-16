import openpyxl

#open and load workbook
mo = openpyxl.load_workbook('missouri.xlsx')

#open and load sheet
mosheet = mo.get_sheet_by_name('missouri')

#calculating fall part of winter with first fall freeze dates

#1917

#getting cell values out of each column; each column is a year
l = []
for rowOfCellObjects in mosheet['L2':'L25']:
    for cellObj in rowOfCellObjects:
        l.append(cellObj.value)

#making list of winter lengths from each column/year for later use in final winter length calculations
l1 = []
for i in l:
    try:
        x = 365 - (i-1)
    except:
    	x = None
    l1.append(x)

#1918

m = []
for rowOfCellObjects in mosheet['M2':'M25']:
    for cellObj in rowOfCellObjects:
        m.append(cellObj.value)

m1 = []

for i in m:
    try:
        x = 365 - (i-1)
    except:
        x = None
    m1.append(x)

#1919

n = []
for rowOfCellObjects in mosheet['N2':'N25']:
    for cellObj in rowOfCellObjects:
        n.append(cellObj.value)

n1 = []

for i in n:
    try:
        x = 365 - (i-1)
    except:
        x = None
    n1.append(x)

#1920

o = []
for rowOfCellObjects in mosheet['O2':'O25']:
    for cellObj in rowOfCellObjects:
        o.append(cellObj.value)

o1 = []

for i in o:
    try:
        x = 366 - (i-1)
    except:
        x = None
    o1.append(x)

#1921

p = []
for rowOfCellObjects in mosheet['P2':'P25']:
    for cellObj in rowOfCellObjects:
        p.append(cellObj.value)

p1 = []

for i in p:
    try:
        x = 365 - (i-1)
    except:
        x = None
    p1.append(x)

#1922

q = []
for rowOfCellObjects in mosheet['Q2':'Q25']:
    for cellObj in rowOfCellObjects:
        q.append(cellObj.value)

q1 = []

for i in q:
    try:
        x = 365 - (i-1)
    except:
        x = None
    q1.append(x)

#1923

r = []
for rowOfCellObjects in mosheet['R2':'R25']:
    for cellObj in rowOfCellObjects:
        r.append(cellObj.value)

r1 = []

for i in r:
    try:
        x = 365 - (i-1)
    except:
        x = None
    r1.append(x)

#1924

s = []
for rowOfCellObjects in mosheet['S2':'S25']:
    for cellObj in rowOfCellObjects:
        s.append(cellObj.value)

s1 = []

for i in s:
    try:
        x = 366 - (i-1)
    except:
        x = None
    s1.append(x)

#1925

t = []
for rowOfCellObjects in mosheet['T2':'T25']:
    for cellObj in rowOfCellObjects:
        t.append(cellObj.value)

t1 = []

for i in t:
    try:
        x = 365 - (i-1)
    except:
        x = None
    t1.append(x)

#1926

u = []
for rowOfCellObjects in mosheet['U2':'U25']:
    for cellObj in rowOfCellObjects:
        u.append(cellObj.value)

u1 = []

for i in u:
    try:
        x = 365 - (i-1)
    except:
        x = None
    u1.append(x)

#1927

v = []
for rowOfCellObjects in mosheet['V2':'V25']:
    for cellObj in rowOfCellObjects:
        v.append(cellObj.value)

v1 = []

for i in v:
    try:
        x = 365 - (i-1)
    except:
        x = None
    v1.append(x)

#1928

w = []
for rowOfCellObjects in mosheet['W2':'W25']:
    for cellObj in rowOfCellObjects:
        w.append(cellObj.value)

w1 = []

for i in w:
    try:
        x = 366 - (i-1)
    except:
        x = None
    w1.append(x)

#1929
#have to skip using x here as variable for lists because of use as variable elsewhere

y = []
for rowOfCellObjects in mosheet['X2':'X25']:
    for cellObj in rowOfCellObjects:
        y.append(cellObj.value)

y1 = []

for i in y:
    try:
        x = 365 - (i-1)
    except:
        x = None
    y1.append(x)

#1930

z = []
for rowOfCellObjects in mosheet['Y2':'Y25']:
    for cellObj in rowOfCellObjects:
        z.append(cellObj.value)

z1 = []

for i in z:
    try:
        x = 365 - (i-1)
    except:
        x = None
    z1.append(x)

#1931

a = []
for rowOfCellObjects in mosheet['Z2':'Z25']:
    for cellObj in rowOfCellObjects:
        a.append(cellObj.value)

a1 = []

for i in a:
    try:
        x = 365 - (i-1)
    except:
        x = None
    a1.append(x)

#1932

b = []
for rowOfCellObjects in mosheet['AA2':'AA25']:
    for cellObj in rowOfCellObjects:
        b.append(cellObj.value)

b1 = []

for i in b:
    try:
        x = 366 - (i-1)
    except:
        x = None
    b1.append(x)

#1933

c = []
for rowOfCellObjects in mosheet['AB2':'AB25']:
    for cellObj in rowOfCellObjects:
        c.append(cellObj.value)

c1 = []

for i in c:
    try:
        x = 365 - (i-1)
    except:
        x = None
    c1.append(x)

#1934

d = []
for rowOfCellObjects in mosheet['AC2':'AC25']:
    for cellObj in rowOfCellObjects:
        d.append(cellObj.value)

d1 = []

for i in d:
    try:
        x = 365 - (i-1)
    except:
        x = None
    d1.append(x)

#1935

e = []
for rowOfCellObjects in mosheet['AD2':'AD25']:
    for cellObj in rowOfCellObjects:
        e.append(cellObj.value)

e1 = []

for i in e:
    try:
        x = 365 - (i-1)
    except:
        x = None
    e1.append(x)

#1936

f = []
for rowOfCellObjects in mosheet['AE2':'AE25']:
    for cellObj in rowOfCellObjects:
        f.append(cellObj.value)

f1 = []

for i in f:
    try:
        x = 366 - (i-1)
    except:
        x = None
    f1.append(x)



