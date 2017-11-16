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

#1937

g = []
for rowOfCellObjects in mosheet['AF2':'AF25']:
    for cellObj in rowOfCellObjects:
        g.append(cellObj.value)

g1 = []

for i in g:
    try:
        x = 365 - (i-1)
    except:
        x = None
    g1.append(x)

#1938

h = []
for rowOfCellObjects in mosheet['AG2':'AG25']:
    for cellObj in rowOfCellObjects:
        h.append(cellObj.value)

h1 = []

for i in h:
    try:
        x = 365 - (i-1)
    except:
        x = None
    h1.append(x)

#1939
#skipping using i for lists because used elsewhere

j = []
for rowOfCellObjects in mosheet['AH2':'AH25']:
    for cellObj in rowOfCellObjects:
        j.append(cellObj.value)

j1 = []

for i in j:
    try:
        x = 365 - (i-1)
    except:
        x = None
    j1.append(x)

#1940

k = []
for rowOfCellObjects in mosheet['AI2':'AI25']:
    for cellObj in rowOfCellObjects:
        k.append(cellObj.value)

k1 = []

for i in k:
    try:
        x = 366 - (i-1)
    except:
        x = None
    k1.append(x)

#1941

aa = []
for rowOfCellObjects in mosheet['AJ2':'AJ25']:
    for cellObj in rowOfCellObjects:
        aa.append(cellObj.value)

aa1 = []

for i in aa:
    try:
        x = 365 - (i-1)
    except:
        x = None
    aa1.append(x)

#1942

ab = []
for rowOfCellObjects in mosheet['AK2':'AK25']:
    for cellObj in rowOfCellObjects:
        ab.append(cellObj.value)

ab1 = []

for i in ab:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ab1.append(x)

#1943

ac = []
for rowOfCellObjects in mosheet['AL2':'AL25']:
    for cellObj in rowOfCellObjects:
        ac.append(cellObj.value)

ac1 = []

for i in ac:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ac1.append(x)

#1944

ad = []
for rowOfCellObjects in mosheet['AM2':'AM25']:
    for cellObj in rowOfCellObjects:
        ad.append(cellObj.value)

ad1 = []

for i in ad:
    try:
        x = 366 - (i-1)
    except:
        x = None
    ad1.append(x)

#1945

ae = []
for rowOfCellObjects in mosheet['AN2':'AN25']:
    for cellObj in rowOfCellObjects:
        ae.append(cellObj.value)

ae1 = []

for i in ae:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ae1.append(x)

#1946

af = []
for rowOfCellObjects in mosheet['AO2':'AO25']:
    for cellObj in rowOfCellObjects:
        af.append(cellObj.value)

af1 = []

for i in af:
    try:
        x = 365 - (i-1)
    except:
        x = None
    af1.append(x)

#1947

ag = []
for rowOfCellObjects in mosheet['AP2':'AP25']:
    for cellObj in rowOfCellObjects:
        ag.append(cellObj.value)

ag1 = []

for i in ag:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ag1.append(x)

# all of the above loops calculate the first part of winter for the first 30 years in this dataset. next, we'll calculate the last part of winter for the first 30 years, minus 1917, because winter of 1917 spans 1917-1918. then, we'll do the all of the same for the last 30 years in the dataset.

# pulling out last spring freeze values, then final winter length calculation for that season

#last spring freeze values for #1918

ba = []

for rowOfCellObjects in mosheet['DR2':'DR25']:
    for cellObj in rowOfCellObjects:
        ba.append(cellObj.value)

#final winter length calculation for that season for all of 24 Missouri stations

try:
    winter_1917_1918_0 = l1[0] + ba[0]
except:
    winter_1917_1918_0 = None

try:
    winter_1917_1918_1 = l1[1] + ba[1]
except:
    winter_1917_1918_1 = None

try:
    winter_1917_1918_2 = l1[2] + ba[2]
except:
    winter_1917_1918_2 = None

try:
    winter_1917_1918_3 = l1[3] + ba[3]
except:
    winter_1917_1918_3 = None

try:
    winter_1917_1918_4 = l1[4] + ba[4]
except:
    winter_1917_1918_4 = None

try:
    winter_1917_1918_5 = l1[5] + ba[5]
except:
    winter_1917_1918_5 = None

try:
    winter_1917_1918_6 = l1[6] + ba[6]
except:
    winter_1917_1918_6 = None

try:
    winter_1917_1918_7 = l1[7] + ba[7]
except:
    winter_1917_1918_7 = None

try:
    winter_1917_1918_8 = l1[8] + ba[8]
except:
    winter_1917_1918_8 = None

try:
    winter_1917_1918_9 = l1[9] + ba[9]
except:
    winter_1917_1918_9 = None

try:
    winter_1917_1918_10 = l1[10] + ba[10]
except:
    winter_1917_1918_10 = None

try:
    winter_1917_1918_11 = l1[11] + ba[11]
except:
    winter_1917_1918_11 = None

try:
    winter_1917_1918_12 = l1[12] + ba[12]
except:
    winter_1917_1918_12 = None

try:
    winter_1917_1918_13 = l1[13] + ba[13]
except:
    winter_1917_1918_13 = None

try:
    winter_1917_1918_14 = l1[14] + ba[14]
except:
    winter_1917_1918_14 = None

try:
    winter_1917_1918_15 = l1[15] + ba[15]
except:
    winter_1917_1918_15 = None

try:
    winter_1917_1918_16 = l1[16] + ba[16]
except:
    winter_1917_1918_16 = None

try:
    winter_1917_1918_17 = l1[17] + ba[17]
except:
    winter_1917_1918_17 = None

try:
    winter_1917_1918_18 = l1[18] + ba[18]
except:
    winter_1917_1918_18 = None

try:
    winter_1917_1918_19 = l1[19] + ba[19]
except:
    winter_1917_1918_19 = None

try:
    winter_1917_1918_20 = l1[20] + ba[20]
except:
    winter_1917_1918_20 = None

try:
    winter_1917_1918_21 = l1[21] + ba[21]
except:
    winter_1917_1918_21 = None

try:
    winter_1917_1918_22 = l1[22] + ba[22]
except:
    winter_1917_1918_22 = None

try:
    winter_1917_1918_23 = l1[23] + ba[23]
except:
    winter_1917_1918_23 = None

#last spring freeze values for #1919

bb = []

for rowOfCellObjects in mosheet['DS2':'DS25']:
    for cellObj in rowOfCellObjects:
        bb.append(cellObj.value)

#final winter length calculation for that season





