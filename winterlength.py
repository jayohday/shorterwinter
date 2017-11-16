import openpyxl
import numpy as np

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

s1 = []

for i in r:
    try:
        x = 365 - (i-1)
    except:
        x = None
    s1.append(x)

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
# next comes pulling out last spring freeze values for the first 30 years, then final winter length calculation for that season
# WL lists are all corresponding season lengths for all 24 stations
# station lists will include all season lengths for that particular station

station0 = []
station1 = []
station2 = []
station3 = []
station4 = []
station5 = []
station6 = []
station7 = []
station8 = []
station9 = []
station10 = []
station11 = []
station12 = []
station13 = []
station14 = []
station15 = []
station16 = []
station17 = []
station18 = []
station19 = []
station20 = []
station21 = []
station22 = []
station23 = []

#last spring freeze values for #1918

ba = []

for rowOfCellObjects in mosheet['DR2':'DR25']:
    for cellObj in rowOfCellObjects:
        ba.append(cellObj.value)

#final winter length calculation for 1917-1918 season for all of 24 Missouri stations

WL_0 = [] #all 1917-1918 winter lengths

try:
    winter_1917_1918_0 = l1[0] + ba[0]
except:
    winter_1917_1918_0 = None
WL_0.append(winter_1917_1918_0)
station0.append(winter_1917_1918_0)

try:
    winter_1917_1918_1 = l1[1] + ba[1]
except:
    winter_1917_1918_1 = None
WL_0.append(winter_1917_1918_1)
station1.append(winter_1917_1918_1)

try:
    winter_1917_1918_2 = l1[2] + ba[2]
except:
    winter_1917_1918_2 = None
WL_0.append(winter_1917_1918_2)
station2.append(winter_1917_1918_2)

try:
    winter_1917_1918_3 = l1[3] + ba[3]
except:
    winter_1917_1918_3 = None
WL_0.append(winter_1917_1918_3)
station3.append(winter_1917_1918_3)

try:
    winter_1917_1918_4 = l1[4] + ba[4]
except:
    winter_1917_1918_4 = None
WL_0.append(winter_1917_1918_4)
station4.append(winter_1917_1918_4)

try:
    winter_1917_1918_5 = l1[5] + ba[5]
except:
    winter_1917_1918_5 = None
WL_0.append(winter_1917_1918_5)
station5.append(winter_1917_1918_5)

try:
    winter_1917_1918_6 = l1[6] + ba[6]
except:
    winter_1917_1918_6 = None
WL_0.append(winter_1917_1918_6)
station6.append(winter_1917_1918_6)

try:
    winter_1917_1918_7 = l1[7] + ba[7]
except:
    winter_1917_1918_7 = None
WL_0.append(winter_1917_1918_7)
station7.append(winter_1917_1918_7)

try:
    winter_1917_1918_8 = l1[8] + ba[8]
except:
    winter_1917_1918_8 = None
WL_0.append(winter_1917_1918_8)
station8.append(winter_1917_1918_8)

try:
    winter_1917_1918_9 = l1[9] + ba[9]
except:
    winter_1917_1918_9 = None
WL_0.append(winter_1917_1918_9)
station9.append(winter_1917_1918_9)

try:
    winter_1917_1918_10 = l1[10] + ba[10]
except:
    winter_1917_1918_10 = None
WL_0.append(winter_1917_1918_10)
station10.append(winter_1917_1918_10)

try:
    winter_1917_1918_11 = l1[11] + ba[11]
except:
    winter_1917_1918_11 = None
WL_0.append(winter_1917_1918_11)
station11.append(winter_1917_1918_11)

try:
    winter_1917_1918_12 = l1[12] + ba[12]
except:
    winter_1917_1918_12 = None
WL_0.append(winter_1917_1918_12)
station12.append(winter_1917_1918_12)

try:
    winter_1917_1918_13 = l1[13] + ba[13]
except:
    winter_1917_1918_13 = None
WL_0.append(winter_1917_1918_13)
station13.append(winter_1917_1918_13)

try:
    winter_1917_1918_14 = l1[14] + ba[14]
except:
    winter_1917_1918_14 = None
WL_0.append(winter_1917_1918_14)
station14.append(winter_1917_1918_14)

try:
    winter_1917_1918_15 = l1[15] + ba[15]
except:
    winter_1917_1918_15 = None
WL_0.append(winter_1917_1918_15)
station15.append(winter_1917_1918_15)

try:
    winter_1917_1918_16 = l1[16] + ba[16]
except:
    winter_1917_1918_16 = None
WL_0.append(winter_1917_1918_16)
station16.append(winter_1917_1918_16)

try:
    winter_1917_1918_17 = l1[17] + ba[17]
except:
    winter_1917_1918_17 = None
WL_0.append(winter_1917_1918_17)
station17.append(winter_1917_1918_17)

try:
    winter_1917_1918_18 = l1[18] + ba[18]
except:
    winter_1917_1918_18 = None
WL_0.append(winter_1917_1918_18)
station18.append(winter_1917_1918_18)

try:
    winter_1917_1918_19 = l1[19] + ba[19]
except:
    winter_1917_1918_19 = None
WL_0.append(winter_1917_1918_19)
station19.append(winter_1917_1918_19)

try:
    winter_1917_1918_20 = l1[20] + ba[20]
except:
    winter_1917_1918_20 = None
WL_0.append(winter_1917_1918_20)
station20.append(winter_1917_1918_20)

try:
    winter_1917_1918_21 = l1[21] + ba[21]
except:
    winter_1917_1918_21 = None
WL_0.append(winter_1917_1918_21)
station21.append(winter_1917_1918_21)

try:
    winter_1917_1918_22 = l1[22] + ba[22]
except:
    winter_1917_1918_22 = None
WL_0.append(winter_1917_1918_22)
station22.append(winter_1917_1918_22)

try:
    winter_1917_1918_23 = l1[23] + ba[23]
except:
    winter_1917_1918_23 = None
WL_0.append(winter_1917_1918_23)
station23.append(winter_1917_1918_23)

#last spring freeze values for #1919

bb = []

for rowOfCellObjects in mosheet['DS2':'DS25']:
    for cellObj in rowOfCellObjects:
        bb.append(cellObj.value)

#final winter length calculation for 1918-1919 season for all of 24 Missouri stations

WL_1 = [] #all 1918-1919 winter lengths

try:
    winter_1918_1919_0 = m1[0] + bb[0]
except:
    winter_1918_1919_0 = None
WL_1.append(winter_1918_1919_0)
station0.append(winter_1918_1919_0)

try:
    winter_1918_1919_1 = m1[1] + bb[1]
except:
    winter_1918_1919_1 = None
WL_1.append(winter_1918_1919_1)
station1.append(winter_1918_1919_1)

try:
    winter_1918_1919_2 = m1[2] + bb[2]
except:
    winter_1918_1919_2 = None
WL_1.append(winter_1918_1919_2)
station2.append(winter_1918_1919_2)

try:
    winter_1918_1919_3 = m1[3] + bb[3]
except:
    winter_1918_1919_3 = None
WL_1.append(winter_1918_1919_3)
station3.append(winter_1918_1919_3)

try:
    winter_1918_1919_4 = m1[4] + bb[4]
except:
    winter_1918_1919_4 = None
WL_1.append(winter_1918_1919_4)
station4.append(winter_1918_1919_4)

try:
    winter_1918_1919_5 = m1[5] + bb[5]
except:
    winter_1918_1919_5 = None
WL_1.append(winter_1918_1919_5)
station5.append(winter_1918_1919_5)

try:
    winter_1918_1919_6 = m1[6] + bb[6]
except:
    winter_1918_1919_6 = None
WL_1.append(winter_1918_1919_0)
station6.append(winter_1918_1919_6)

try:
    winter_1918_1919_7 = m1[7] + bb[7]
except:
    winter_1918_1919_7 = None
WL_1.append(winter_1918_1919_7)
station7.append(winter_1918_1919_7)

try:
    winter_1918_1919_8 = m1[8] + bb[8]
except:
    winter_1918_1919_8 = None
WL_1.append(winter_1918_1919_8)
station8.append(winter_1918_1919_8)

try:
    winter_1918_1919_9 = m1[9] + bb[9]
except:
    winter_1918_1919_9 = None
WL_1.append(winter_1918_1919_9)
station9.append(winter_1918_1919_9)

try:
    winter_1918_1919_10 = m1[10] + bb[10]
except:
    winter_1918_1919_10 = None
WL_1.append(winter_1918_1919_10)
station10.append(winter_1918_1919_10)

try:
    winter_1918_1919_11 = m1[11] + bb[11]
except:
    winter_1918_1919_11 = None
WL_1.append(winter_1918_1919_11)
station11.append(winter_1918_1919_11)

try:
    winter_1918_1919_12 = m1[12] + bb[12]
except:
    winter_1918_1919_12 = None
WL_1.append(winter_1918_1919_12)
station12.append(winter_1918_1919_12)

try:
    winter_1918_1919_13 = m1[13] + bb[13]
except:
    winter_1918_1919_13 = None
WL_1.append(winter_1918_1919_13)
station13.append(winter_1918_1919_13)

try:
    winter_1918_1919_14 = m1[14] + bb[14]
except:
    winter_1918_1919_14 = None
WL_1.append(winter_1918_1919_14)
station14.append(winter_1918_1919_14)

try:
    winter_1918_1919_15 = m1[15] + bb[15]
except:
    winter_1918_1919_15 = None
WL_1.append(winter_1918_1919_15)
station15.append(winter_1918_1919_15)

try:
    winter_1918_1919_16 = m1[16] + bb[16]
except:
    winter_1918_1919_16 = None
WL_1.append(winter_1918_1919_16)
station16.append(winter_1918_1919_16)

try:
    winter_1918_1919_17 = m1[17] + bb[17]
except:
    winter_1918_1919_17 = None
WL_1.append(winter_1918_1919_17)
station17.append(winter_1918_1919_17)

try:
    winter_1918_1919_18 = m1[18] + bb[18]
except:
    winter_1918_1919_18 = None
WL_1.append(winter_1918_1919_18)
station18.append(winter_1918_1919_18)

try:
    winter_1918_1919_19 = m1[19] + bb[19]
except:
    winter_1918_1919_19 = None
WL_1.append(winter_1918_1919_19)
station19.append(winter_1918_1919_19)

try:
    winter_1918_1919_20 = m1[20] + bb[20]
except:
    winter_1918_1919_20 = None
WL_1.append(winter_1918_1919_20)
station20.append(winter_1918_1919_20)

try:
    winter_1918_1919_21 = m1[21] + bb[21]
except:
    winter_1918_1919_21 = None
WL_1.append(winter_1918_1919_21)
station21.append(winter_1918_1919_21)

try:
    winter_1918_1919_22 = m1[22] + bb[22]
except:
    winter_1918_1919_22 = None
WL_1.append(winter_1918_1919_22)
station22.append(winter_1918_1919_22)

try:
    winter_1918_1919_23 = m1[23] + bb[23]
except:
    winter_1918_1919_23 = None
WL_1.append(winter_1918_1919_23)
station23.append(winter_1918_1919_23)

#last spring freeze values for #1920

bc = []

for rowOfCellObjects in mosheet['DT2':'DT25']:
    for cellObj in rowOfCellObjects:
        bc.append(cellObj.value)


#final winter length calculation for 1919-1920 season for all of 24 Missouri stations

WL_2 = [] #all 1919-1920 winter lengths

try:
    winter_1919_1920_0 = n1[0] + bc[0]
except:
    winter_1919_1920_0 = None
WL_2.append(winter_1919_1920_0)
station0.append(winter_1919_1920_0)

try:
    winter_1919_1920_1 = n1[1] + bc[1]
except:
    winter_1919_1920_1 = None
WL_2.append(winter_1919_1920_1)
station1.append(winter_1919_1920_1)

try:
    winter_1919_1920_2 = n1[2] + bc[2]
except:
    winter_1919_1920_2 = None
WL_2.append(winter_1919_1920_2)
station2.append(winter_1919_1920_2)

try:
    winter_1919_1920_3 = n1[3] + bc[3]
except:
    winter_1919_1920_3 = None
WL_2.append(winter_1919_1920_3)
station3.append(winter_1919_1920_3)

try:
    winter_1919_1920_4 = n1[4] + bc[4]
except:
    winter_1919_1920_4 = None
WL_2.append(winter_1919_1920_4)
station4.append(winter_1919_1920_4)

try:
    winter_1919_1920_5 = n1[5] + bc[5]
except:
    winter_1919_1920_5 = None
WL_2.append(winter_1919_1920_5)
station5.append(winter_1919_1920_5)

try:
    winter_1919_1920_6 = n1[6] + bc[6]
except:
    winter_1919_1920_6 = None
WL_2.append(winter_1919_1920_6)
station6.append(winter_1919_1920_6)

try:
    winter_1919_1920_7 = n1[7] + bc[7]
except:
    winter_1919_1920_7 = None
WL_2.append(winter_1919_1920_7)
station7.append(winter_1919_1920_7)

try:
    winter_1919_1920_8 = n1[8] + bc[8]
except:
    winter_1919_1920_8 = None
WL_2.append(winter_1919_1920_8)
station8.append(winter_1919_1920_8)

try:
    winter_1919_1920_9 = n1[9] + bc[9]
except:
    winter_1919_1920_9 = None
WL_2.append(winter_1919_1920_9)
station9.append(winter_1919_1920_9)

try:
    winter_1919_1920_10 = n1[10] + bc[10]
except:
    winter_1919_1920_10 = None
WL_2.append(winter_1919_1920_10)
station10.append(winter_1919_1920_10)

try:
    winter_1919_1920_11 = n1[11] + bc[11]
except:
    winter_1919_1920_11 = None
WL_2.append(winter_1919_1920_11)
station11.append(winter_1919_1920_11)

try:
    winter_1919_1920_12 = n1[12] + bc[12]
except:
    winter_1919_1920_12 = None
WL_2.append(winter_1919_1920_12)
station12.append(winter_1919_1920_12)

try:
    winter_1919_1920_13 = n1[13] + bc[13]
except:
    winter_1919_1920_13 = None
WL_2.append(winter_1919_1920_13)
station13.append(winter_1919_1920_13)

try:
    winter_1919_1920_14 = n1[14] + bc[14]
except:
    winter_1919_1920_14 = None
WL_2.append(winter_1919_1920_14)
station14.append(winter_1919_1920_14)

try:
    winter_1919_1920_15 = n1[15] + bc[15]
except:
    winter_1919_1920_15 = None
WL_2.append(winter_1919_1920_15)
station15.append(winter_1919_1920_15)

try:
    winter_1919_1920_16 = n1[16] + bc[16]
except:
    winter_1919_1920_16 = None
WL_2.append(winter_1919_1920_16)
station16.append(winter_1919_1920_16)

try:
    winter_1919_1920_17 = n1[17] + bc[17]
except:
    winter_1919_1920_17 = None
WL_2.append(winter_1919_1920_17)
station17.append(winter_1919_1920_17)

try:
    winter_1919_1920_18 = n1[18] + bc[18]
except:
    winter_1919_1920_18 = None
WL_2.append(winter_1919_1920_18)
station18.append(winter_1919_1920_18)

try:
    winter_1919_1920_19 = n1[19] + bc[19]
except:
    winter_1919_1920_19 = None
WL_2.append(winter_1919_1920_19)
station19.append(winter_1919_1920_19)

try:
    winter_1919_1920_20 = n1[20] + bc[20]
except:
    winter_1919_1920_20 = None
WL_2.append(winter_1919_1920_20)
station20.append(winter_1919_1920_20)

try:
    winter_1919_1920_21 = n1[21] + bc[21]
except:
    winter_1919_1920_21 = None
WL_2.append(winter_1919_1920_21)
station21.append(winter_1919_1920_21)

try:
    winter_1919_1920_22 = n1[22] + bc[22]
except:
    winter_1919_1920_22 = None
WL_2.append(winter_1919_1920_22)
station22.append(winter_1919_1920_22)

try:
    winter_1919_1920_23 = n1[23] + bc[23]
except:
    winter_1919_1920_23 = None
WL_2.append(winter_1919_1920_23)
station23.append(winter_1919_1920_23)

#last spring freeze values for #1921

bd = []

for rowOfCellObjects in mosheet['DU2':'DU25']:
    for cellObj in rowOfCellObjects:
        bd.append(cellObj.value)


#final winter length calculation for 1920-1921 season for all of 24 Missouri stations

WL_3 = [] #all 1920-1921 winter lengths

try:
    winter_1920_1921_0 = o1[0] + bd[0]
except:
    winter_1920_1921_0 = None
WL_3.append(winter_1920_1921_0)
station0.append(winter_1920_1921_0)

try:
    winter_1920_1921_1 = o1[1] + bd[1]
except:
    winter_1920_1921_1 = None
WL_3.append(winter_1920_1921_1)
station1.append(winter_1920_1921_1)

try:
    winter_1920_1921_2 = o1[2] + bd[2]
except:
    winter_1920_1921_2 = None
WL_3.append(winter_1920_1921_2)
station2.append(winter_1920_1921_2)

try:
    winter_1920_1921_3 = o1[3] + bd[3]
except:
    winter_1920_1921_3 = None
WL_3.append(winter_1920_1921_3)
station3.append(winter_1920_1921_3)

try:
    winter_1920_1921_4 = o1[4] + bd[4]
except:
    winter_1920_1921_4 = None
WL_3.append(winter_1920_1921_4)
station4.append(winter_1920_1921_4)

try:
    winter_1920_1921_5 = o1[5] + bd[5]
except:
    winter_1920_1921_5 = None
WL_3.append(winter_1920_1921_5)
station5.append(winter_1920_1921_5)

try:
    winter_1920_1921_6 = o1[6] + bd[6]
except:
    winter_1920_1921_6 = None
WL_3.append(winter_1920_1921_6)
station6.append(winter_1920_1921_6)

try:
    winter_1920_1921_7 = o1[7] + bd[7]
except:
    winter_1920_1921_7 = None
WL_3.append(winter_1920_1921_7)
station7.append(winter_1920_1921_7)

try:
    winter_1920_1921_8 = o1[8] + bd[8]
except:
    winter_1920_1921_8 = None
WL_3.append(winter_1920_1921_8)
station8.append(winter_1920_1921_8)

try:
    winter_1920_1921_9 = o1[9] + bd[9]
except:
    winter_1920_1921_9 = None
WL_3.append(winter_1920_1921_9)
station9.append(winter_1920_1921_9)

try:
    winter_1920_1921_10 = o1[10] + bd[10]
except:
    winter_1920_1921_10 = None
WL_3.append(winter_1920_1921_10)
station10.append(winter_1920_1921_10)

try:
    winter_1920_1921_11 = o1[11] + bd[11]
except:
    winter_1920_1921_11 = None
WL_3.append(winter_1920_1921_11)
station11.append(winter_1920_1921_11)

try:
    winter_1920_1921_12 = o1[12] + bd[12]
except:
    winter_1920_1921_12 = None
WL_3.append(winter_1920_1921_12)
station12.append(winter_1920_1921_12)

try:
    winter_1920_1921_13 = o1[13] + bd[13]
except:
    winter_1920_1921_13 = None
WL_3.append(winter_1920_1921_13)
station13.append(winter_1920_1921_13)

try:
    winter_1920_1921_14 = o1[14] + bd[14]
except:
    winter_1920_1921_14 = None
WL_3.append(winter_1920_1921_14)
station14.append(winter_1920_1921_14)

try:
    winter_1920_1921_15 = o1[15] + bd[15]
except:
    winter_1920_1921_15 = None
WL_3.append(winter_1920_1921_15)
station15.append(winter_1920_1921_15)

try:
    winter_1920_1921_16 = o1[16] + bd[16]
except:
    winter_1920_1921_16 = None
WL_3.append(winter_1920_1921_16)
station16.append(winter_1920_1921_16)

try:
    winter_1920_1921_17 = o1[17] + bd[17]
except:
    winter_1920_1921_17 = None
WL_3.append(winter_1920_1921_17)
station17.append(winter_1920_1921_17)

try:
    winter_1920_1921_18 = o1[18] + bd[18]
except:
    winter_1920_1921_18 = None
WL_3.append(winter_1920_1921_18)
station18.append(winter_1920_1921_18)

try:
    winter_1920_1921_19 = o1[19] + bd[19]
except:
    winter_1920_1921_19 = None
WL_3.append(winter_1920_1921_19)
station19.append(winter_1920_1921_19)

try:
    winter_1920_1921_20 = o1[20] + bd[20]
except:
    winter_1920_1921_20 = None
WL_3.append(winter_1920_1921_20)
station20.append(winter_1920_1921_20)

try:
    winter_1920_1921_21 = o1[21] + bd[21]
except:
    winter_1920_1921_21 = None
WL_3.append(winter_1920_1921_21)
station21.append(winter_1920_1921_21)

try:
    winter_1920_1921_22 = o1[22] + bd[22]
except:
    winter_1920_1921_22 = None
WL_3.append(winter_1920_1921_22)
station22.append(winter_1920_1921_22)

try:
    winter_1920_1921_23 = o1[23] + bd[23]
except:
    winter_1920_1921_23 = None
WL_3.append(winter_1920_1921_23)
station23.append(winter_1920_1921_23)

#last spring freeze values for #1922

be = []

for rowOfCellObjects in mosheet['DV2':'DV25']:
    for cellObj in rowOfCellObjects:
        be.append(cellObj.value)


#final winter length calculation for 1921-1922 season for all of 24 Missouri stations

WL_4 = [] #all 1921-1922 winter lengths

try:
    winter_1921_1922_0 = p1[0] + be[0]
except:
    winter_1921_1922_0 = None
WL_4.append(winter_1921_1922_0)
station0.append(winter_1921_1922_0)

try:
    winter_1921_1922_1 = p1[1] + be[1]
except:
    winter_1921_1922_1 = None
WL_4.append(winter_1921_1922_1)
station1.append(winter_1921_1922_1)

try:
    winter_1921_1922_2 = p1[2] + be[2]
except:
    winter_1921_1922_2 = None
WL_4.append(winter_1921_1922_2)
station2.append(winter_1921_1922_2)

try:
    winter_1921_1922_3 = p1[3] + be[3]
except:
    winter_1921_1922_3 = None
WL_4.append(winter_1921_1922_3)
station3.append(winter_1921_1922_3)

try:
    winter_1921_1922_4 = p1[4] + be[4]
except:
    winter_1921_1922_4 = None
WL_4.append(winter_1921_1922_4)
station4.append(winter_1921_1922_4)

try:
    winter_1921_1922_5 = p1[5] + be[5]
except:
    winter_1921_1922_5 = None
WL_4.append(winter_1921_1922_5)
station5.append(winter_1921_1922_5)

try:
    winter_1921_1922_6 = p1[6] + be[6]
except:
    winter_1921_1922_6 = None
WL_4.append(winter_1921_1922_6)
station6.append(winter_1921_1922_6)

try:
    winter_1921_1922_7 = p1[7] + be[7]
except:
    winter_1921_1922_7 = None
WL_4.append(winter_1921_1922_7)
station7.append(winter_1921_1922_7)

try:
    winter_1921_1922_8 = p1[8] + be[8]
except:
    winter_1921_1922_8 = None
WL_4.append(winter_1921_1922_8)
station8.append(winter_1921_1922_8)

try:
    winter_1921_1922_9 = p1[9] + be[9]
except:
    winter_1921_1922_9 = None
WL_4.append(winter_1921_1922_9)
station9.append(winter_1921_1922_9)

try:
    winter_1921_1922_10 = p1[10] + be[10]
except:
    winter_1921_1922_10 = None
WL_4.append(winter_1921_1922_10)
station10.append(winter_1921_1922_10)

try:
    winter_1921_1922_11 = p1[11] + be[11]
except:
    winter_1921_1922_11 = None
WL_4.append(winter_1921_1922_11)
station11.append(winter_1921_1922_11)

try:
    winter_1921_1922_12 = p1[12] + be[12]
except:
    winter_1921_1922_12 = None
WL_4.append(winter_1921_1922_12)
station12.append(winter_1921_1922_12)

try:
    winter_1921_1922_13 = p1[13] + be[13]
except:
    winter_1921_1922_13 = None
WL_4.append(winter_1921_1922_13)
station13.append(winter_1921_1922_13)

try:
    winter_1921_1922_14 = p1[14] + be[14]
except:
    winter_1921_1922_14 = None
WL_4.append(winter_1921_1922_14)
station14.append(winter_1921_1922_14)

try:
    winter_1921_1922_15 = p1[15] + be[15]
except:
    winter_1921_1922_15 = None
WL_4.append(winter_1921_1922_15)
station15.append(winter_1921_1922_15)

try:
    winter_1921_1922_16 = p1[16] + be[16]
except:
    winter_1921_1922_16 = None
WL_4.append(winter_1921_1922_16)
station16.append(winter_1921_1922_16)

try:
    winter_1921_1922_17 = p1[17] + be[17]
except:
    winter_1921_1922_17 = None
WL_4.append(winter_1921_1922_17)
station17.append(winter_1921_1922_17)

try:
    winter_1921_1922_18 = p1[18] + be[18]
except:
    winter_1921_1922_18 = None
WL_4.append(winter_1921_1922_18)
station18.append(winter_1921_1922_18)

try:
    winter_1921_1922_19 = p1[19] + be[19]
except:
    winter_1921_1922_19 = None
WL_4.append(winter_1921_1922_19)
station19.append(winter_1921_1922_19)

try:
    winter_1921_1922_20 = p1[20] + be[20]
except:
    winter_1921_1922_20 = None
WL_4.append(winter_1921_1922_20)
station20.append(winter_1921_1922_20)

try:
    winter_1921_1922_21 = p1[21] + be[21]
except:
    winter_1921_1922_21 = None
WL_4.append(winter_1921_1922_21)
station21.append(winter_1921_1922_21)

try:
    winter_1921_1922_22 = p1[22] + be[22]
except:
    winter_1921_1922_22 = None
WL_4.append(winter_1921_1922_22)
station22.append(winter_1921_1922_22)

try:
    winter_1921_1922_23 = p1[23] + be[23]
except:
    winter_1921_1922_23 = None
WL_4.append(winter_1921_1922_23)
station23.append(winter_1921_1922_23)

#last spring freeze values for #1923

bf = []

for rowOfCellObjects in mosheet['DW2':'DW25']:
    for cellObj in rowOfCellObjects:
        bf.append(cellObj.value)


#final winter length calculation for 1922-1923 season for all of 24 Missouri stations

WL_5 = [] #all 1922-1923 winter lengths

try:
    winter_1922_1923_0 = q1[0] + bf[0]
except:
    winter_1922_1923_0 = None
WL_5.append(winter_1922_1923_0)
station0.append(winter_1922_1923_0)

try:
    winter_1922_1923_1 = q1[1] + bf[1]
except:
    winter_1922_1923_1 = None
WL_5.append(winter_1922_1923_1)
station1.append(winter_1922_1923_1)

try:
    winter_1922_1923_2 = q1[2] + bf[2]
except:
    winter_1922_1923_2 = None
WL_5.append(winter_1922_1923_2)
station2.append(winter_1922_1923_2)

try:
    winter_1922_1923_3 = q1[3] + bf[3]
except:
    winter_1922_1923_3 = None
WL_5.append(winter_1922_1923_3)
station3.append(winter_1922_1923_3)

try:
    winter_1922_1923_4 = q1[4] + bf[4]
except:
    winter_1922_1923_4 = None
WL_5.append(winter_1922_1923_4)
station4.append(winter_1922_1923_4)

try:
    winter_1922_1923_5 = q1[5] + bf[5]
except:
    winter_1922_1923_5 = None
WL_5.append(winter_1922_1923_5)
station5.append(winter_1922_1923_5)

try:
    winter_1922_1923_6 = q1[6] + bf[6]
except:
    winter_1922_1923_6 = None
WL_5.append(winter_1922_1923_6)
station6.append(winter_1922_1923_6)

try:
    winter_1922_1923_7 = q1[7] + bf[7]
except:
    winter_1922_1923_7 = None
WL_5.append(winter_1922_1923_7)
station7.append(winter_1922_1923_7)

try:
    winter_1922_1923_8 = q1[8] + bf[8]
except:
    winter_1922_1923_8 = None
WL_5.append(winter_1922_1923_8)
station8.append(winter_1922_1923_8)

try:
    winter_1922_1923_9 = q1[9] + bf[9]
except:
    winter_1922_1923_9 = None
WL_5.append(winter_1922_1923_9)
station9.append(winter_1922_1923_9)

try:
    winter_1922_1923_10 = q1[10] + bf[10]
except:
    winter_1922_1923_10 = None
WL_5.append(winter_1922_1923_10)
station10.append(winter_1922_1923_10)

try:
    winter_1922_1923_11 = q1[11] + bf[11]
except:
    winter_1922_1923_11 = None
WL_5.append(winter_1922_1923_11)
station11.append(winter_1922_1923_11)

try:
    winter_1922_1923_12 = q1[12] + bf[12]
except:
    winter_1922_1923_12 = None
WL_5.append(winter_1922_1923_12)
station12.append(winter_1922_1923_12)

try:
    winter_1922_1923_13 = q1[13] + bf[13]
except:
    winter_1922_1923_13 = None
WL_5.append(winter_1922_1923_13)
station13.append(winter_1922_1923_13)

try:
    winter_1922_1923_14 = q1[14] + bf[14]
except:
    winter_1922_1923_14 = None
WL_5.append(winter_1922_1923_14)
station14.append(winter_1922_1923_14)

try:
    winter_1922_1923_15 = q1[15] + bf[15]
except:
    winter_1922_1923_15 = None
WL_5.append(winter_1922_1923_15)
station15.append(winter_1922_1923_15)

try:
    winter_1922_1923_16 = q1[16] + bf[16]
except:
    winter_1922_1923_16 = None
WL_5.append(winter_1922_1923_16)
station16.append(winter_1922_1923_16)

try:
    winter_1922_1923_17 = q1[17] + bf[17]
except:
    winter_1922_1923_17 = None
WL_5.append(winter_1922_1923_17)
station17.append(winter_1922_1923_17)

try:
    winter_1922_1923_18 = q1[18] + bf[18]
except:
    winter_1922_1923_18 = None
WL_5.append(winter_1922_1923_18)
station18.append(winter_1922_1923_18)

try:
    winter_1922_1923_19 = q1[19] + bf[19]
except:
    winter_1922_1923_19 = None
WL_5.append(winter_1922_1923_19)
station19.append(winter_1922_1923_19)

try:
    winter_1922_1923_20 = q1[20] + bf[20]
except:
    winter_1922_1923_20 = None
WL_5.append(winter_1922_1923_20)
station20.append(winter_1922_1923_20)

try:
    winter_1922_1923_21 = q1[21] + bf[21]
except:
    winter_1922_1923_21 = None
WL_5.append(winter_1922_1923_21)
station21.append(winter_1922_1923_21)

try:
    winter_1922_1923_22 = q1[22] + bf[22]
except:
    winter_1922_1923_22 = None
WL_5.append(winter_1922_1923_22)
station22.append(winter_1922_1923_22)

try:
    winter_1922_1923_23 = q1[23] + bf[23]
except:
    winter_1922_1923_23 = None
WL_5.append(winter_1922_1923_23)
station23.append(winter_1922_1923_23)

#last spring freeze values for #1924

bg = []

for rowOfCellObjects in mosheet['DX2':'DX25']:
    for cellObj in rowOfCellObjects:
        bg.append(cellObj.value)


#final winter length calculation for 1923-1924 season for all of 24 Missouri stations

WL_6 = [] #all 1923-1924 winter lengths

try:
    winter_1923_1924_0 = s1[0] + bg[0]
except:
    winter_1923_1924_0 = None
WL_6.append(winter_1923_1924_0)
station0.append(winter_1923_1924_0)

try:
    winter_1923_1924_1 = s1[1] + bg[1]
except:
    winter_1923_1924_1 = None
WL_6.append(winter_1923_1924_1)
station1.append(winter_1923_1924_1)

try:
    winter_1923_1924_2 = s1[2] + bg[2]
except:
    winter_1923_1924_2 = None
WL_6.append(winter_1923_1924_2)
station2.append(winter_1923_1924_2)

try:
    winter_1923_1924_3 = s1[3] + bg[3]
except:
    winter_1923_1924_3 = None
WL_6.append(winter_1923_1924_3)
station3.append(winter_1923_1924_3)

try:
    winter_1923_1924_4 = s1[4] + bg[4]
except:
    winter_1923_1924_4 = None
WL_6.append(winter_1923_1924_4)
station4.append(winter_1923_1924_4)

try:
    winter_1923_1924_5 = s1[5] + bg[5]
except:
    winter_1923_1924_5 = None
WL_6.append(winter_1923_1924_5)
station5.append(winter_1923_1924_5)

try:
    winter_1923_1924_6 = s1[6] + bg[6]
except:
    winter_1923_1924_6 = None
WL_6.append(winter_1923_1924_6)
station6.append(winter_1923_1924_6)

try:
    winter_1923_1924_7 = s1[7] + bg[7]
except:
    winter_1923_1924_7 = None
WL_6.append(winter_1923_1924_7)
station7.append(winter_1923_1924_7)

try:
    winter_1923_1924_8 = s1[8] + bg[8]
except:
    winter_1923_1924_8 = None
WL_6.append(winter_1923_1924_8)
station8.append(winter_1923_1924_8)

try:
    winter_1923_1924_9 = s1[9] + bg[9]
except:
    winter_1923_1924_9 = None
WL_6.append(winter_1923_1924_9)
station9.append(winter_1923_1924_9)

try:
    winter_1923_1924_10 = s1[10] + bg[10]
except:
    winter_1923_1924_10 = None
WL_6.append(winter_1923_1924_10)
station10.append(winter_1923_1924_10)

try:
    winter_1923_1924_11 = s1[11] + bg[11]
except:
    winter_1923_1924_11 = None
WL_6.append(winter_1923_1924_11)
station11.append(winter_1923_1924_11)

try:
    winter_1923_1924_12 = s1[12] + bg[12]
except:
    winter_1923_1924_12 = None
WL_6.append(winter_1923_1924_12)
station12.append(winter_1923_1924_12)

try:
    winter_1923_1924_13 = s1[13] + bg[13]
except:
    winter_1923_1924_13 = None
WL_6.append(winter_1923_1924_13)
station13.append(winter_1923_1924_13)

try:
    winter_1923_1924_14 = s1[14] + bg[14]
except:
    winter_1923_1924_14 = None
WL_6.append(winter_1923_1924_14)
station14.append(winter_1923_1924_14)

try:
    winter_1923_1924_15 = s1[15] + bg[15]
except:
    winter_1923_1924_15 = None
WL_6.append(winter_1923_1924_15)
station15.append(winter_1923_1924_15)

try:
    winter_1923_1924_16 = s1[16] + bg[16]
except:
    winter_1923_1924_16 = None
WL_6.append(winter_1923_1924_16)
station16.append(winter_1923_1924_16)

try:
    winter_1923_1924_17 = s1[17] + bg[17]
except:
    winter_1923_1924_17 = None
WL_6.append(winter_1923_1924_17)
station17.append(winter_1923_1924_17)

try:
    winter_1923_1924_18 = s1[18] + bg[18]
except:
    winter_1923_1924_18 = None
WL_6.append(winter_1923_1924_18)
station18.append(winter_1923_1924_18)

try:
    winter_1923_1924_19 = s1[19] + bg[19]
except:
    winter_1923_1924_19 = None
WL_6.append(winter_1923_1924_19)
station19.append(winter_1923_1924_19)

try:
    winter_1923_1924_20 = s1[20] + bg[20]
except:
    winter_1923_1924_20 = None
WL_6.append(winter_1923_1924_20)
station20.append(winter_1923_1924_20)

try:
    winter_1923_1924_21 = s1[21] + bg[21]
except:
    winter_1923_1924_21 = None
WL_6.append(winter_1923_1924_21)
station21.append(winter_1923_1924_21)

try:
    winter_1923_1924_22 = s1[22] + bg[22]
except:
    winter_1923_1924_22 = None
WL_6.append(winter_1923_1924_22)
station22.append(winter_1923_1924_22)

try:
    winter_1923_1924_23 = s1[23] + bg[23]
except:
    winter_1923_1924_23 = None
WL_6.append(winter_1923_1924_23)
station23.append(winter_1923_1924_23)

#last spring freeze values for #1925

bh = []

for rowOfCellObjects in mosheet['DY2':'DY25']:
    for cellObj in rowOfCellObjects:
        bh.append(cellObj.value)

#final winter length calculation for 1924-1925 season for all of 24 Missouri stations

WL_7 = [] #all 1924-1925 winter lengths

try:
    winter_1924_1925_0 = s1[0] + bh[0]
except:
    winter_1924_1925_0 = None
WL_7.append(winter_1924_1925_0)
station0.append(winter_1924_1925_0)

try:
    winter_1924_1925_1 = s1[1] + bh[1]
except:
    winter_1924_1925_1 = None
WL_7.append(winter_1924_1925_1)
station1.append(winter_1924_1925_1)

try:
    winter_1924_1925_2 = s1[2] + bh[2]
except:
    winter_1924_1925_2 = None
WL_7.append(winter_1924_1925_2)
station2.append(winter_1924_1925_2)

try:
    winter_1924_1925_3 = s1[3] + bh[3]
except:
    winter_1924_1925_3 = None
WL_7.append(winter_1924_1925_3)
station3.append(winter_1924_1925_3)

try:
    winter_1924_1925_4 = s1[4] + bh[4]
except:
    winter_1924_1925_4 = None
WL_7.append(winter_1924_1925_4)
station4.append(winter_1924_1925_4)

try:
    winter_1924_1925_5 = s1[5] + bh[5]
except:
    winter_1924_1925_5 = None
WL_7.append(winter_1924_1925_5)
station5.append(winter_1924_1925_5)

try:
    winter_1924_1925_6 = s1[6] + bh[6]
except:
    winter_1924_1925_6 = None
WL_7.append(winter_1924_1925_6)
station6.append(winter_1924_1925_6)

try:
    winter_1924_1925_7 = s1[7] + bh[7]
except:
    winter_1924_1925_7 = None
WL_7.append(winter_1924_1925_7)
station7.append(winter_1924_1925_7)

try:
    winter_1924_1925_8 = s1[8] + bh[8]
except:
    winter_1924_1925_8 = None
WL_7.append(winter_1924_1925_8)
station8.append(winter_1924_1925_8)

try:
    winter_1924_1925_9 = s1[9] + bh[9]
except:
    winter_1924_1925_9 = None
WL_7.append(winter_1924_1925_9)
station9.append(winter_1924_1925_9)

try:
    winter_1924_1925_10 = s1[10] + bh[10]
except:
    winter_1924_1925_10 = None
WL_7.append(winter_1924_1925_10)
station10.append(winter_1924_1925_10)

try:
    winter_1924_1925_11 = s1[11] + bh[11]
except:
    winter_1924_1925_11 = None
WL_7.append(winter_1924_1925_11)
station11.append(winter_1924_1925_11)

try:
    winter_1924_1925_12 = s1[12] + bh[12]
except:
    winter_1924_1925_12 = None
WL_7.append(winter_1924_1925_12)
station12.append(winter_1924_1925_12)

try:
    winter_1924_1925_13 = s1[13] + bh[13]
except:
    winter_1924_1925_13 = None
WL_7.append(winter_1924_1925_13)
station13.append(winter_1924_1925_13)

try:
    winter_1924_1925_14 = s1[14] + bh[14]
except:
    winter_1924_1925_14 = None
WL_7.append(winter_1924_1925_14)
station14.append(winter_1924_1925_14)

try:
    winter_1924_1925_15 = s1[15] + bh[15]
except:
    winter_1924_1925_15 = None
WL_7.append(winter_1924_1925_15)
station15.append(winter_1924_1925_15)

try:
    winter_1924_1925_16 = s1[16] + bh[16]
except:
    winter_1924_1925_16 = None
WL_7.append(winter_1924_1925_16)
station16.append(winter_1924_1925_16)

try:
    winter_1924_1925_17 = s1[17] + bh[17]
except:
    winter_1924_1925_17 = None
WL_7.append(winter_1924_1925_17)
station17.append(winter_1924_1925_17)

try:
    winter_1924_1925_18 = s1[18] + bh[18]
except:
    winter_1924_1925_18 = None
WL_7.append(winter_1924_1925_18)
station18.append(winter_1924_1925_18)

try:
    winter_1924_1925_19 = s1[19] + bh[19]
except:
    winter_1924_1925_19 = None
WL_7.append(winter_1924_1925_19)
station19.append(winter_1924_1925_19)

try:
    winter_1924_1925_20 = s1[20] + bh[20]
except:
    winter_1924_1925_20 = None
WL_7.append(winter_1924_1925_20)
station20.append(winter_1924_1925_20)

try:
    winter_1924_1925_21 = s1[21] + bh[21]
except:
    winter_1924_1925_21 = None
WL_7.append(winter_1924_1925_21)
station21.append(winter_1924_1925_21)

try:
    winter_1924_1925_22 = s1[22] + bh[22]
except:
    winter_1924_1925_22 = None
WL_7.append(winter_1924_1925_22)
station22.append(winter_1924_1925_22)

try:
    winter_1924_1925_23 = s1[23] + bh[23]
except:
    winter_1924_1925_23 = None
WL_7.append(winter_1924_1925_23)
station23.append(winter_1924_1925_23)

#last spring freeze values for #1926

bi = []

for rowOfCellObjects in mosheet['DZ2':'DZ25']:
    for cellObj in rowOfCellObjects:
        bi.append(cellObj.value)

#final winter length calculation for 1925-1926 season for all of 24 Missouri stations

WL_8 = [] #all 1925-1926 winter lengths

try:
    winter_1925_1926_0 = t1[0] + bi[0]
except:
    winter_1925_1926_0 = None
WL_8.append(winter_1925_1926_0)
station0.append(winter_1925_1926_0)

try:
    winter_1925_1926_1 = t1[1] + bi[1]
except:
    winter_1925_1926_1 = None
WL_8.append(winter_1925_1926_1)
station1.append(winter_1925_1926_1)

try:
    winter_1925_1926_2 = t1[2] + bi[2]
except:
    winter_1925_1926_2 = None
WL_8.append(winter_1925_1926_2)
station2.append(winter_1925_1926_2)

try:
    winter_1925_1926_3 = t1[3] + bi[3]
except:
    winter_1925_1926_3 = None
WL_8.append(winter_1925_1926_3)
station3.append(winter_1925_1926_3)

try:
    winter_1925_1926_4 = t1[4] + bi[4]
except:
    winter_1925_1926_4 = None
WL_8.append(winter_1925_1926_4)
station4.append(winter_1925_1926_4)

try:
    winter_1925_1926_5 = t1[5] + bi[5]
except:
    winter_1925_1926_5 = None
WL_8.append(winter_1925_1926_5)
station5.append(winter_1925_1926_5)

try:
    winter_1925_1926_6 = t1[6] + bi[6]
except:
    winter_1925_1926_6 = None
WL_8.append(winter_1925_1926_6)
station6.append(winter_1925_1926_6)

try:
    winter_1925_1926_7 = t1[7] + bi[7]
except:
    winter_1925_1926_7 = None
WL_8.append(winter_1925_1926_7)
station7.append(winter_1925_1926_7)

try:
    winter_1925_1926_8 = t1[8] + bi[8]
except:
    winter_1925_1926_8 = None
WL_8.append(winter_1925_1926_8)
station8.append(winter_1925_1926_8)

try:
    winter_1925_1926_9 = t1[9] + bi[9]
except:
    winter_1925_1926_9 = None
WL_8.append(winter_1925_1926_9)
station9.append(winter_1925_1926_9)

try:
    winter_1925_1926_10 = t1[10] + bi[10]
except:
    winter_1925_1926_10 = None
WL_8.append(winter_1925_1926_10)
station10.append(winter_1925_1926_10)

try:
    winter_1925_1926_11 = t1[11] + bi[11]
except:
    winter_1925_1926_11 = None
WL_8.append(winter_1925_1926_11)
station11.append(winter_1925_1926_11)

try:
    winter_1925_1926_12 = t1[12] + bi[12]
except:
    winter_1925_1926_12 = None
WL_8.append(winter_1925_1926_12)
station12.append(winter_1925_1926_12)

try:
    winter_1925_1926_13 = t1[13] + bi[13]
except:
    winter_1925_1926_13 = None
WL_8.append(winter_1925_1926_13)
station13.append(winter_1925_1926_13)

try:
    winter_1925_1926_14 = t1[14] + bi[14]
except:
    winter_1925_1926_14 = None
WL_8.append(winter_1925_1926_14)
station14.append(winter_1925_1926_14)

try:
    winter_1925_1926_15 = t1[15] + bi[15]
except:
    winter_1925_1926_15 = None
WL_8.append(winter_1925_1926_15)
station15.append(winter_1925_1926_15)

try:
    winter_1925_1926_16 = t1[16] + bi[16]
except:
    winter_1925_1926_16 = None
WL_8.append(winter_1925_1926_16)
station16.append(winter_1925_1926_16)

try:
    winter_1925_1926_17 = t1[17] + bi[17]
except:
    winter_1925_1926_17 = None
WL_8.append(winter_1925_1926_17)
station17.append(winter_1925_1926_17)

try:
    winter_1925_1926_18 = t1[18] + bi[18]
except:
    winter_1925_1926_18 = None
WL_8.append(winter_1925_1926_18)
station18.append(winter_1925_1926_18)

try:
    winter_1925_1926_19 = t1[19] + bi[19]
except:
    winter_1925_1926_19 = None
WL_8.append(winter_1925_1926_19)
station19.append(winter_1925_1926_19)

try:
    winter_1925_1926_20 = t1[20] + bi[20]
except:
    winter_1925_1926_20 = None
WL_8.append(winter_1925_1926_20)
station20.append(winter_1925_1926_20)

try:
    winter_1925_1926_21 = t1[21] + bi[21]
except:
    winter_1925_1926_21 = None
WL_8.append(winter_1925_1926_21)
station21.append(winter_1925_1926_21)

try:
    winter_1925_1926_22 = t1[22] + bi[22]
except:
    winter_1925_1926_22 = None
WL_8.append(winter_1925_1926_22)
station22.append(winter_1925_1926_22)

try:
    winter_1925_1926_23 = t1[23] + bi[23]
except:
    winter_1925_1926_23 = None
WL_8.append(winter_1925_1926_23)
station23.append(winter_1925_1926_23)

#last spring freeze values for #1927

bj = []

for rowOfCellObjects in mosheet['EA2':'EA25']:
    for cellObj in rowOfCellObjects:
        bj.append(cellObj.value)

#final winter length calculation for 1926-1927 season for all of 24 Missouri stations

WL_9 = [] #all 1926-1927 winter lengths

try:
    winter_1926_1927_0 = u1[0] + bj[0]
except:
    winter_1926_1927_0 = None
WL_9.append(winter_1926_1927_0)
station0.append(winter_1926_1927_0)

try:
    winter_1926_1927_1 = u1[1] + bj[1]
except:
    winter_1926_1927_1 = None
WL_9.append(winter_1926_1927_1)
station1.append(winter_1926_1927_1)

try:
    winter_1926_1927_2 = u1[2] + bj[2]
except:
    winter_1926_1927_2 = None
WL_9.append(winter_1926_1927_2)
station2.append(winter_1926_1927_2)

try:
    winter_1926_1927_3 = u1[3] + bj[3]
except:
    winter_1926_1927_3 = None
WL_9.append(winter_1926_1927_3)
station3.append(winter_1926_1927_3)

try:
    winter_1926_1927_4 = u1[4] + bj[4]
except:
    winter_1926_1927_4 = None
WL_9.append(winter_1926_1927_4)
station4.append(winter_1926_1927_4)

try:
    winter_1926_1927_5 = u1[5] + bj[5]
except:
    winter_1926_1927_5 = None
WL_9.append(winter_1926_1927_5)
station5.append(winter_1926_1927_5)

try:
    winter_1926_1927_6 = u1[6] + bj[6]
except:
    winter_1926_1927_6 = None
WL_9.append(winter_1926_1927_6)
station6.append(winter_1926_1927_6)

try:
    winter_1926_1927_7 = u1[7] + bj[7]
except:
    winter_1926_1927_7 = None
WL_9.append(winter_1926_1927_7)
station7.append(winter_1926_1927_7)

try:
    winter_1926_1927_8 = u1[8] + bj[8]
except:
    winter_1926_1927_8 = None
WL_9.append(winter_1926_1927_8)
station8.append(winter_1926_1927_8)

try:
    winter_1926_1927_9 = u1[9] + bj[9]
except:
    winter_1926_1927_9 = None
WL_9.append(winter_1926_1927_9)
station9.append(winter_1926_1927_9)

try:
    winter_1926_1927_10 = u1[10] + bj[10]
except:
    winter_1926_1927_10 = None
WL_9.append(winter_1926_1927_10)
station10.append(winter_1926_1927_10)

try:
    winter_1926_1927_11 = u1[11] + bj[11]
except:
    winter_1926_1927_11 = None
WL_9.append(winter_1926_1927_11)
station11.append(winter_1926_1927_11)

try:
    winter_1926_1927_12 = u1[12] + bj[12]
except:
    winter_1926_1927_12 = None
WL_9.append(winter_1926_1927_12)
station12.append(winter_1926_1927_12)

try:
    winter_1926_1927_13 = u1[13] + bj[13]
except:
    winter_1926_1927_13 = None
WL_9.append(winter_1926_1927_13)
station13.append(winter_1926_1927_13)

try:
    winter_1926_1927_14 = u1[14] + bj[14]
except:
    winter_1926_1927_14 = None
WL_9.append(winter_1926_1927_14)
station14.append(winter_1926_1927_14)

try:
    winter_1926_1927_15 = u1[15] + bj[15]
except:
    winter_1926_1927_15 = None
WL_9.append(winter_1926_1927_15)
station15.append(winter_1926_1927_15)

try:
    winter_1926_1927_16 = u1[16] + bj[16]
except:
    winter_1926_1927_16 = None
WL_9.append(winter_1926_1927_16)
station16.append(winter_1926_1927_16)

try:
    winter_1926_1927_17 = u1[17] + bj[17]
except:
    winter_1926_1927_17 = None
WL_9.append(winter_1926_1927_17)
station17.append(winter_1926_1927_17)

try:
    winter_1926_1927_18 = u1[18] + bj[18]
except:
    winter_1926_1927_18 = None
WL_9.append(winter_1926_1927_18)
station18.append(winter_1926_1927_18)

try:
    winter_1926_1927_19 = u1[19] + bj[19]
except:
    winter_1926_1927_19 = None
WL_9.append(winter_1926_1927_19)
station19.append(winter_1926_1927_19)

try:
    winter_1926_1927_20 = u1[20] + bj[20]
except:
    winter_1926_1927_20 = None
WL_9.append(winter_1926_1927_20)
station20.append(winter_1926_1927_20)

try:
    winter_1926_1927_21 = u1[21] + bj[21]
except:
    winter_1926_1927_21 = None
WL_9.append(winter_1926_1927_21)
station21.append(winter_1926_1927_21)

try:
    winter_1926_1927_22 = u1[22] + bj[22]
except:
    winter_1926_1927_22 = None
WL_9.append(winter_1926_1927_22)
station22.append(winter_1926_1927_22)

try:
    winter_1926_1927_23 = u1[23] + bj[23]
except:
    winter_1926_1927_23 = None
WL_9.append(winter_1926_1927_23)
station23.append(winter_1926_1927_23)

#last spring freeze values for #1928

bk = []

for rowOfCellObjects in mosheet['EB2':'EB25']:
    for cellObj in rowOfCellObjects:
        bk.append(cellObj.value)

#final winter length calculation for 1927-1928 season for all of 24 Missouri stations

WL_10 = [] #all 1927-1928 winter lengths

try:
    winter_1927_1928_0 = v1[0] + bk[0]
except:
    winter_1927_1928_0 = None
WL_10.append(winter_1927_1928_0)
station0.append(winter_1927_1928_0)

try:
    winter_1927_1928_1 = v1[1] + bk[1]
except:
    winter_1927_1928_1 = None
WL_10.append(winter_1927_1928_1)
station1.append(winter_1927_1928_1)

try:
    winter_1927_1928_2 = v1[2] + bk[2]
except:
    winter_1927_1928_2 = None
WL_10.append(winter_1927_1928_2)
station2.append(winter_1927_1928_2)

try:
    winter_1927_1928_3 = v1[3] + bk[3]
except:
    winter_1927_1928_3 = None
WL_10.append(winter_1927_1928_3)
station3.append(winter_1927_1928_3)

try:
    winter_1927_1928_4 = v1[4] + bk[4]
except:
    winter_1927_1928_4 = None
WL_10.append(winter_1927_1928_4)
station4.append(winter_1927_1928_4)

try:
    winter_1927_1928_5 = v1[5] + bk[5]
except:
    winter_1927_1928_5 = None
WL_10.append(winter_1927_1928_5)
station5.append(winter_1927_1928_5)

try:
    winter_1927_1928_6 = v1[6] + bk[6]
except:
    winter_1927_1928_6 = None
WL_10.append(winter_1927_1928_6)
station6.append(winter_1927_1928_6)

try:
    winter_1927_1928_7 = v1[7] + bk[7]
except:
    winter_1927_1928_7 = None
WL_10.append(winter_1927_1928_7)
station7.append(winter_1927_1928_7)

try:
    winter_1927_1928_8 = v1[8] + bk[8]
except:
    winter_1927_1928_8 = None
WL_10.append(winter_1927_1928_8)
station8.append(winter_1927_1928_8)

try:
    winter_1927_1928_9 = v1[9] + bk[9]
except:
    winter_1927_1928_9 = None
WL_10.append(winter_1927_1928_9)
station9.append(winter_1927_1928_9)

try:
    winter_1927_1928_10 = v1[10] + bk[10]
except:
    winter_1927_1928_10 = None
WL_10.append(winter_1927_1928_10)
station10.append(winter_1927_1928_10)

try:
    winter_1927_1928_11 = v1[11] + bk[11]
except:
    winter_1927_1928_11 = None
WL_10.append(winter_1927_1928_11)
station11.append(winter_1927_1928_11)

try:
    winter_1927_1928_12 = v1[12] + bk[12]
except:
    winter_1927_1928_12 = None
WL_10.append(winter_1927_1928_12)
station12.append(winter_1927_1928_12)

try:
    winter_1927_1928_13 = v1[13] + bk[13]
except:
    winter_1927_1928_13 = None
WL_10.append(winter_1927_1928_13)
station13.append(winter_1927_1928_13)

try:
    winter_1927_1928_14 = v1[14] + bk[14]
except:
    winter_1927_1928_14 = None
WL_10.append(winter_1927_1928_14)
station14.append(winter_1927_1928_14)

try:
    winter_1927_1928_15 = v1[15] + bk[15]
except:
    winter_1927_1928_15 = None
WL_10.append(winter_1927_1928_15)
station15.append(winter_1927_1928_15)

try:
    winter_1927_1928_16 = v1[16] + bk[16]
except:
    winter_1927_1928_16 = None
WL_10.append(winter_1927_1928_16)
station16.append(winter_1927_1928_16)

try:
    winter_1927_1928_17 = v1[17] + bk[17]
except:
    winter_1927_1928_17 = None
WL_10.append(winter_1927_1928_17)
station17.append(winter_1927_1928_17)

try:
    winter_1927_1928_18 = v1[18] + bk[18]
except:
    winter_1927_1928_18 = None
WL_10.append(winter_1927_1928_18)
station18.append(winter_1927_1928_18)

try:
    winter_1927_1928_19 = v1[19] + bk[19]
except:
    winter_1927_1928_19 = None
WL_10.append(winter_1927_1928_19)
station19.append(winter_1927_1928_19)

try:
    winter_1927_1928_20 = v1[20] + bk[20]
except:
    winter_1927_1928_20 = None
WL_10.append(winter_1927_1928_20)
station20.append(winter_1927_1928_20)

try:
    winter_1927_1928_21 = v1[21] + bk[21]
except:
    winter_1927_1928_21 = None
WL_10.append(winter_1927_1928_21)
station21.append(winter_1927_1928_21)

try:
    winter_1927_1928_22 = v1[22] + bk[22]
except:
    winter_1927_1928_22 = None
WL_10.append(winter_1927_1928_22)
station22.append(winter_1927_1928_22)

try:
    winter_1927_1928_23 = v1[23] + bk[23]
except:
    winter_1927_1928_23 = None
WL_10.append(winter_1927_1928_23)
station23.append(winter_1927_1928_23)

#last spring freeze values for #1929

bl = []

for rowOfCellObjects in mosheet['EC2':'EC25']:
    for cellObj in rowOfCellObjects:
        bl.append(cellObj.value)

#final winter length calculation for 1928-1929 season for all of 24 Missouri stations

WL_11 = [] #all 1928-1929 winter lengths

try:
    winter_1928_1929_0 = w1[0] + bl[0]
except:
    winter_1928_1929_0 = None
WL_11.append(winter_1928_1929_0)
station0.append(winter_1928_1929_0)

try:
    winter_1928_1929_1 = w1[1] + bl[1]
except:
    winter_1928_1929_1 = None
WL_11.append(winter_1928_1929_1)
station1.append(winter_1928_1929_1)

try:
    winter_1928_1929_2 = w1[2] + bl[2]
except:
    winter_1928_1929_2 = None
WL_11.append(winter_1928_1929_2)
station2.append(winter_1928_1929_2)

try:
    winter_1928_1929_3 = w1[3] + bl[3]
except:
    winter_1928_1929_3 = None
WL_11.append(winter_1928_1929_3)
station3.append(winter_1928_1929_3)

try:
    winter_1928_1929_4 = w1[4] + bl[4]
except:
    winter_1928_1929_4 = None
WL_11.append(winter_1928_1929_4)
station4.append(winter_1928_1929_4)

try:
    winter_1928_1929_5 = w1[5] + bl[5]
except:
    winter_1928_1929_5 = None
WL_11.append(winter_1928_1929_5)
station5.append(winter_1928_1929_5)

try:
    winter_1928_1929_6 = w1[6] + bl[6]
except:
    winter_1928_1929_6 = None
WL_11.append(winter_1928_1929_6)
station6.append(winter_1928_1929_6)

try:
    winter_1928_1929_7 = w1[7] + bl[7]
except:
    winter_1928_1929_7 = None
WL_11.append(winter_1928_1929_7)
station7.append(winter_1928_1929_7)

try:
    winter_1928_1929_8 = w1[8] + bl[8]
except:
    winter_1928_1929_8 = None
WL_11.append(winter_1928_1929_8)
station8.append(winter_1928_1929_8)

try:
    winter_1928_1929_9 = w1[9] + bl[9]
except:
    winter_1928_1929_9 = None
WL_11.append(winter_1928_1929_9)
station9.append(winter_1928_1929_9)

try:
    winter_1928_1929_10 = w1[10] + bl[10]
except:
    winter_1928_1929_10 = None
WL_11.append(winter_1928_1929_10)
station10.append(winter_1928_1929_10)

try:
    winter_1928_1929_11 = w1[11] + bl[11]
except:
    winter_1928_1929_11 = None
WL_11.append(winter_1928_1929_11)
station11.append(winter_1928_1929_11)

try:
    winter_1928_1929_12 = w1[12] + bl[12]
except:
    winter_1928_1929_12 = None
WL_11.append(winter_1928_1929_12)
station12.append(winter_1928_1929_12)

try:
    winter_1928_1929_13 = w1[13] + bl[13]
except:
    winter_1928_1929_13 = None
WL_11.append(winter_1928_1929_13)
station13.append(winter_1928_1929_13)

try:
    winter_1928_1929_14 = w1[14] + bl[14]
except:
    winter_1928_1929_14 = None
WL_11.append(winter_1928_1929_14)
station14.append(winter_1928_1929_14)

try:
    winter_1928_1929_15 = w1[15] + bl[15]
except:
    winter_1928_1929_15 = None
WL_11.append(winter_1928_1929_15)
station15.append(winter_1928_1929_15)

try:
    winter_1928_1929_16 = w1[16] + bl[16]
except:
    winter_1928_1929_16 = None
WL_11.append(winter_1928_1929_16)
station16.append(winter_1928_1929_16)

try:
    winter_1928_1929_17 = w1[17] + bl[17]
except:
    winter_1928_1929_17 = None
WL_11.append(winter_1928_1929_17)
station17.append(winter_1928_1929_17)

try:
    winter_1928_1929_18 = w1[18] + bl[18]
except:
    winter_1928_1929_18 = None
WL_11.append(winter_1928_1929_18)
station18.append(winter_1928_1929_18)

try:
    winter_1928_1929_19 = w1[19] + bl[19]
except:
    winter_1928_1929_19 = None
WL_11.append(winter_1928_1929_19)
station19.append(winter_1928_1929_19)

try:
    winter_1928_1929_20 = w1[20] + bl[20]
except:
    winter_1928_1929_20 = None
WL_11.append(winter_1928_1929_20)
station20.append(winter_1928_1929_20)

try:
    winter_1928_1929_21 = w1[21] + bl[21]
except:
    winter_1928_1929_21 = None
WL_11.append(winter_1928_1929_21)
station21.append(winter_1928_1929_21)

try:
    winter_1928_1929_22 = w1[22] + bl[22]
except:
    winter_1928_1929_22 = None
WL_11.append(winter_1928_1929_22)
station22.append(winter_1928_1929_22)

try:
    winter_1928_1929_23 = w1[23] + bl[23]
except:
    winter_1928_1929_23 = None
WL_11.append(winter_1928_1929_23)
station23.append(winter_1928_1929_23)

#last spring freeze values for #1930

bm = []

for rowOfCellObjects in mosheet['ED2':'ED25']:
    for cellObj in rowOfCellObjects:
        bm.append(cellObj.value)

#final winter length calculation for 1929-1930 season for all of 24 Missouri stations

WL_12 = [] #all 1929-1930 winter lengths

try:
    winter_1929_1930_0 = y1[0] + bm[0]
except:
    winter_1929_1930_0 = None
WL_12.append(winter_1929_1930_0)
station0.append(winter_1929_1930_0)

try:
    winter_1929_1930_1 = y1[1] + bm[1]
except:
    winter_1929_1930_1 = None
WL_12.append(winter_1929_1930_1)
station1.append(winter_1929_1930_1)

try:
    winter_1929_1930_2 = y1[2] + bm[2]
except:
    winter_1929_1930_2 = None
WL_12.append(winter_1929_1930_2)
station2.append(winter_1929_1930_2)

try:
    winter_1929_1930_3 = y1[3] + bm[3]
except:
    winter_1929_1930_3 = None
WL_12.append(winter_1929_1930_3)
station3.append(winter_1929_1930_3)

try:
    winter_1929_1930_4 = y1[4] + bm[4]
except:
    winter_1929_1930_4 = None
WL_12.append(winter_1929_1930_4)
station4.append(winter_1929_1930_4)

try:
    winter_1929_1930_5 = y1[5] + bm[5]
except:
    winter_1929_1930_5 = None
WL_12.append(winter_1929_1930_5)
station5.append(winter_1929_1930_5)

try:
    winter_1929_1930_6 = y1[6] + bm[6]
except:
    winter_1929_1930_6 = None
WL_12.append(winter_1929_1930_6)
station6.append(winter_1929_1930_6)

try:
    winter_1929_1930_7 = y1[7] + bm[7]
except:
    winter_1929_1930_7 = None
WL_12.append(winter_1929_1930_7)
station7.append(winter_1929_1930_7)

try:
    winter_1929_1930_8 = y1[8] + bm[8]
except:
    winter_1929_1930_8 = None
WL_12.append(winter_1929_1930_8)
station8.append(winter_1929_1930_8)

try:
    winter_1929_1930_9 = y1[9] + bm[9]
except:
    winter_1929_1930_9 = None
WL_12.append(winter_1929_1930_9)
station9.append(winter_1929_1930_9)

try:
    winter_1929_1930_10 = y1[10] + bm[10]
except:
    winter_1929_1930_10 = None
WL_12.append(winter_1929_1930_10)
station10.append(winter_1929_1930_10)

try:
    winter_1929_1930_11 = y1[11] + bm[11]
except:
    winter_1929_1930_11 = None
WL_12.append(winter_1929_1930_11)
station11.append(winter_1929_1930_11)

try:
    winter_1929_1930_12 = y1[12] + bm[12]
except:
    winter_1929_1930_12 = None
WL_12.append(winter_1929_1930_12)
station12.append(winter_1929_1930_12)

try:
    winter_1929_1930_13 = y1[13] + bm[13]
except:
    winter_1929_1930_13 = None
WL_12.append(winter_1929_1930_13)
station13.append(winter_1929_1930_13)

try:
    winter_1929_1930_14 = y1[14] + bm[14]
except:
    winter_1929_1930_14 = None
WL_12.append(winter_1929_1930_14)
station14.append(winter_1929_1930_14)

try:
    winter_1929_1930_15 = y1[15] + bm[15]
except:
    winter_1929_1930_15 = None
WL_12.append(winter_1929_1930_15)
station15.append(winter_1929_1930_15)

try:
    winter_1929_1930_16 = y1[16] + bm[16]
except:
    winter_1929_1930_16 = None
WL_12.append(winter_1929_1930_16)
station16.append(winter_1929_1930_16)

try:
    winter_1929_1930_17 = y1[17] + bm[17]
except:
    winter_1929_1930_17 = None
WL_12.append(winter_1929_1930_17)
station17.append(winter_1929_1930_17)

try:
    winter_1929_1930_18 = y1[18] + bm[18]
except:
    winter_1929_1930_18 = None
WL_12.append(winter_1929_1930_18)
station18.append(winter_1929_1930_18)

try:
    winter_1929_1930_19 = y1[19] + bm[19]
except:
    winter_1929_1930_19 = None
WL_12.append(winter_1929_1930_19)
station19.append(winter_1929_1930_19)

try:
    winter_1929_1930_20 = y1[20] + bm[20]
except:
    winter_1929_1930_20 = None
WL_12.append(winter_1929_1930_20)
station20.append(winter_1929_1930_20)

try:
    winter_1929_1930_21 = y1[21] + bm[21]
except:
    winter_1929_1930_21 = None
WL_12.append(winter_1929_1930_21)
station21.append(winter_1929_1930_21)

try:
    winter_1929_1930_22 = y1[22] + bm[22]
except:
    winter_1929_1930_22 = None
WL_12.append(winter_1929_1930_22)
station22.append(winter_1929_1930_22)

try:
    winter_1929_1930_23 = y1[23] + bm[23]
except:
    winter_1929_1930_23 = None
WL_12.append(winter_1929_1930_23)
station23.append(winter_1929_1930_23)

#last spring freeze values for #1931

bn = []

for rowOfCellObjects in mosheet['EE2':'EE25']:
    for cellObj in rowOfCellObjects:
        bn.append(cellObj.value)

#final winter length calculation for 1930-1931 season for all of 24 Missouri stations

WL_13 = [] #all 1930-1931 winter lengths

try:
    winter_1930_1931_0 = z1[0] + bn[0]
except:
    winter_1930_1931_0 = None
WL_13.append(winter_1930_1931_0)
station0.append(winter_1930_1931_0)

try:
    winter_1930_1931_1 = z1[1] + bn[1]
except:
    winter_1930_1931_1 = None
WL_13.append(winter_1930_1931_1)
station1.append(winter_1930_1931_1)

try:
    winter_1930_1931_2 = z1[2] + bn[2]
except:
    winter_1930_1931_2 = None
WL_13.append(winter_1930_1931_2)
station2.append(winter_1930_1931_2)

try:
    winter_1930_1931_3 = z1[3] + bn[3]
except:
    winter_1930_1931_3 = None
WL_13.append(winter_1930_1931_3)
station3.append(winter_1930_1931_3)

try:
    winter_1930_1931_4 = z1[4] + bn[4]
except:
    winter_1930_1931_4 = None
WL_13.append(winter_1930_1931_4)
station4.append(winter_1930_1931_4)

try:
    winter_1930_1931_5 = z1[5] + bn[5]
except:
    winter_1930_1931_5 = None
WL_13.append(winter_1930_1931_5)
station5.append(winter_1930_1931_5)

try:
    winter_1930_1931_6 = z1[6] + bn[6]
except:
    winter_1930_1931_6 = None
WL_13.append(winter_1930_1931_6)
station6.append(winter_1930_1931_6)

try:
    winter_1930_1931_7 = z1[7] + bn[7]
except:
    winter_1930_1931_7 = None
WL_13.append(winter_1930_1931_7)
station7.append(winter_1930_1931_7)

try:
    winter_1930_1931_8 = z1[8] + bn[8]
except:
    winter_1930_1931_8 = None
WL_13.append(winter_1930_1931_8)
station8.append(winter_1930_1931_8)

try:
    winter_1930_1931_9 = z1[9] + bn[9]
except:
    winter_1930_1931_9 = None
WL_13.append(winter_1930_1931_9)
station9.append(winter_1930_1931_9)

try:
    winter_1930_1931_10 = z1[10] + bn[10]
except:
    winter_1930_1931_10 = None
WL_13.append(winter_1930_1931_10)
station10.append(winter_1930_1931_10)

try:
    winter_1930_1931_11 = z1[11] + bn[11]
except:
    winter_1930_1931_11 = None
WL_13.append(winter_1930_1931_11)
station11.append(winter_1930_1931_11)

try:
    winter_1930_1931_12 = z1[12] + bn[12]
except:
    winter_1930_1931_12 = None
WL_13.append(winter_1930_1931_12)
station12.append(winter_1930_1931_12)

try:
    winter_1930_1931_13 = z1[13] + bn[13]
except:
    winter_1930_1931_13 = None
WL_13.append(winter_1930_1931_13)
station13.append(winter_1930_1931_13)

try:
    winter_1930_1931_14 = z1[14] + bn[14]
except:
    winter_1930_1931_14 = None
WL_13.append(winter_1930_1931_14)
station14.append(winter_1930_1931_14)

try:
    winter_1930_1931_15 = z1[15] + bn[15]
except:
    winter_1930_1931_15 = None
WL_13.append(winter_1930_1931_15)
station15.append(winter_1930_1931_15)

try:
    winter_1930_1931_16 = z1[16] + bn[16]
except:
    winter_1930_1931_16 = None
WL_13.append(winter_1930_1931_16)
station16.append(winter_1930_1931_16)

try:
    winter_1930_1931_17 = z1[17] + bn[17]
except:
    winter_1930_1931_17 = None
WL_13.append(winter_1930_1931_17)
station17.append(winter_1930_1931_17)

try:
    winter_1930_1931_18 = z1[18] + bn[18]
except:
    winter_1930_1931_18 = None
WL_13.append(winter_1930_1931_18)
station18.append(winter_1930_1931_18)

try:
    winter_1930_1931_19 = z1[19] + bn[19]
except:
    winter_1930_1931_19 = None
WL_13.append(winter_1930_1931_19)
station19.append(winter_1930_1931_19)

try:
    winter_1930_1931_20 = z1[20] + bn[20]
except:
    winter_1930_1931_20 = None
WL_13.append(winter_1930_1931_20)
station20.append(winter_1930_1931_20)

try:
    winter_1930_1931_21 = z1[21] + bn[21]
except:
    winter_1930_1931_21 = None
WL_13.append(winter_1930_1931_21)
station21.append(winter_1930_1931_21)

try:
    winter_1930_1931_22 = z1[22] + bn[22]
except:
    winter_1930_1931_22 = None
WL_13.append(winter_1930_1931_22)
station22.append(winter_1930_1931_22)

try:
    winter_1930_1931_23 = z1[23] + bn[23]
except:
    winter_1930_1931_23 = None
WL_13.append(winter_1930_1931_23)
station23.append(winter_1930_1931_23)

#last spring freeze values for #1932

bo = []

for rowOfCellObjects in mosheet['EF2':'EF25']:
    for cellObj in rowOfCellObjects:
        bo.append(cellObj.value)

#final winter length calculation for 1931-1932 season for all of 24 Missouri stations

WL_14 = [] #all 1931-1932 winter lengths

try:
    winter_1931_1932_0 = a1[0] + bo[0]
except:
    winter_1931_1932_0 = None
WL_14.append(winter_1931_1932_0)
station0.append(winter_1931_1932_0)

try:
    winter_1931_1932_1 = a1[1] + bo[1]
except:
    winter_1931_1932_1 = None
WL_14.append(winter_1931_1932_1)
station1.append(winter_1931_1932_1)

try:
    winter_1931_1932_2 = a1[2] + bo[2]
except:
    winter_1931_1932_2 = None
WL_14.append(winter_1931_1932_2)
station2.append(winter_1931_1932_2)

try:
    winter_1931_1932_3 = a1[3] + bo[3]
except:
    winter_1931_1932_3 = None
WL_14.append(winter_1931_1932_3)
station3.append(winter_1931_1932_3)

try:
    winter_1931_1932_4 = a1[4] + bo[4]
except:
    winter_1931_1932_4 = None
WL_14.append(winter_1931_1932_4)
station4.append(winter_1931_1932_4)

try:
    winter_1931_1932_5 = a1[5] + bo[5]
except:
    winter_1931_1932_5 = None
WL_14.append(winter_1931_1932_5)
station5.append(winter_1931_1932_5)

try:
    winter_1931_1932_6 = a1[6] + bo[6]
except:
    winter_1931_1932_6 = None
WL_14.append(winter_1931_1932_6)
station6.append(winter_1931_1932_6)

try:
    winter_1931_1932_7 = a1[7] + bo[7]
except:
    winter_1931_1932_7 = None
WL_14.append(winter_1931_1932_7)
station7.append(winter_1931_1932_7)

try:
    winter_1931_1932_8 = a1[8] + bo[8]
except:
    winter_1931_1932_8 = None
WL_14.append(winter_1931_1932_8)
station8.append(winter_1931_1932_8)

try:
    winter_1931_1932_9 = a1[9] + bo[9]
except:
    winter_1931_1932_9 = None
WL_14.append(winter_1931_1932_9)
station9.append(winter_1931_1932_9)

try:
    winter_1931_1932_10 = a1[10] + bo[10]
except:
    winter_1931_1932_10 = None
WL_14.append(winter_1931_1932_10)
station10.append(winter_1931_1932_10)

try:
    winter_1931_1932_11 = a1[11] + bo[11]
except:
    winter_1931_1932_11 = None
WL_14.append(winter_1931_1932_11)
station11.append(winter_1931_1932_11)

try:
    winter_1931_1932_12 = a1[12] + bo[12]
except:
    winter_1931_1932_12 = None
WL_14.append(winter_1931_1932_12)
station12.append(winter_1931_1932_12)

try:
    winter_1931_1932_13 = a1[13] + bo[13]
except:
    winter_1931_1932_13 = None
WL_14.append(winter_1931_1932_13)
station13.append(winter_1931_1932_13)

try:
    winter_1931_1932_14 = a1[14] + bo[14]
except:
    winter_1931_1932_14 = None
WL_14.append(winter_1931_1932_14)
station14.append(winter_1931_1932_14)

try:
    winter_1931_1932_15 = a1[15] + bo[15]
except:
    winter_1931_1932_15 = None
WL_14.append(winter_1931_1932_15)
station15.append(winter_1931_1932_15)

try:
    winter_1931_1932_16 = a1[16] + bo[16]
except:
    winter_1931_1932_16 = None
WL_14.append(winter_1931_1932_16)
station16.append(winter_1931_1932_16)

try:
    winter_1931_1932_17 = a1[17] + bo[17]
except:
    winter_1931_1932_17 = None
WL_14.append(winter_1931_1932_17)
station17.append(winter_1931_1932_17)

try:
    winter_1931_1932_18 = a1[18] + bo[18]
except:
    winter_1931_1932_18 = None
WL_14.append(winter_1931_1932_18)
station18.append(winter_1931_1932_18)

try:
    winter_1931_1932_19 = a1[19] + bo[19]
except:
    winter_1931_1932_19 = None
WL_14.append(winter_1931_1932_19)
station19.append(winter_1931_1932_19)

try:
    winter_1931_1932_20 = a1[20] + bo[20]
except:
    winter_1931_1932_20 = None
WL_14.append(winter_1931_1932_20)
station20.append(winter_1931_1932_20)

try:
    winter_1931_1932_21 = a1[21] + bo[21]
except:
    winter_1931_1932_21 = None
WL_14.append(winter_1931_1932_21)
station21.append(winter_1931_1932_21)

try:
    winter_1931_1932_22 = a1[22] + bo[22]
except:
    winter_1931_1932_22 = None
WL_14.append(winter_1931_1932_22)
station22.append(winter_1931_1932_22)

try:
    winter_1931_1932_23 = a1[23] + bo[23]
except:
    winter_1931_1932_23 = None
WL_14.append(winter_1931_1932_23)
station23.append(winter_1931_1932_23)

#last spring freeze values for #1933

bp = []

for rowOfCellObjects in mosheet['EG2':'EG25']:
    for cellObj in rowOfCellObjects:
        bp.append(cellObj.value)

#final winter length calculation for 1932-1933 season for all of 24 Missouri stations

WL_15 = [] #all 1932-1933 winter lengths

try:
    winter_1932_1933_0 = b1[0] + bp[0]
except:
    winter_1932_1933_0 = None
WL_15.append(winter_1932_1933_0)
station0.append(winter_1932_1933_0)

try:
    winter_1932_1933_1 = b1[1] + bp[1]
except:
    winter_1932_1933_1 = None
WL_15.append(winter_1932_1933_1)
station1.append(winter_1932_1933_1)

try:
    winter_1932_1933_2 = b1[2] + bp[2]
except:
    winter_1932_1933_2 = None
WL_15.append(winter_1932_1933_2)
station2.append(winter_1932_1933_2)

try:
    winter_1932_1933_3 = b1[3] + bp[3]
except:
    winter_1932_1933_3 = None
WL_15.append(winter_1932_1933_3)
station3.append(winter_1932_1933_3)

try:
    winter_1932_1933_4 = b1[4] + bp[4]
except:
    winter_1932_1933_4 = None
WL_15.append(winter_1932_1933_4)
station4.append(winter_1932_1933_4)

try:
    winter_1932_1933_5 = b1[5] + bp[5]
except:
    winter_1932_1933_5 = None
WL_15.append(winter_1932_1933_5)
station5.append(winter_1932_1933_5)

try:
    winter_1932_1933_6 = b1[6] + bp[6]
except:
    winter_1932_1933_6 = None
WL_15.append(winter_1932_1933_6)
station6.append(winter_1932_1933_6)

try:
    winter_1932_1933_7 = b1[7] + bp[7]
except:
    winter_1932_1933_7 = None
WL_15.append(winter_1932_1933_7)
station7.append(winter_1932_1933_7)

try:
    winter_1932_1933_8 = b1[8] + bp[8]
except:
    winter_1932_1933_8 = None
WL_15.append(winter_1932_1933_8)
station8.append(winter_1932_1933_8)

try:
    winter_1932_1933_9 = b1[9] + bp[9]
except:
    winter_1932_1933_9 = None
WL_15.append(winter_1932_1933_9)
station9.append(winter_1932_1933_9)

try:
    winter_1932_1933_10 = b1[10] + bp[10]
except:
    winter_1932_1933_10 = None
WL_15.append(winter_1932_1933_10)
station10.append(winter_1932_1933_10)

try:
    winter_1932_1933_11 = b1[11] + bp[11]
except:
    winter_1932_1933_11 = None
WL_15.append(winter_1932_1933_11)
station11.append(winter_1932_1933_11)

try:
    winter_1932_1933_12 = b1[12] + bp[12]
except:
    winter_1932_1933_12 = None
WL_15.append(winter_1932_1933_12)
station12.append(winter_1932_1933_12)

try:
    winter_1932_1933_13 = b1[13] + bp[13]
except:
    winter_1932_1933_13 = None
WL_15.append(winter_1932_1933_13)
station13.append(winter_1932_1933_13)

try:
    winter_1932_1933_14 = b1[14] + bp[14]
except:
    winter_1932_1933_14 = None
WL_15.append(winter_1932_1933_14)
station14.append(winter_1932_1933_14)

try:
    winter_1932_1933_15 = b1[15] + bp[15]
except:
    winter_1932_1933_15 = None
WL_15.append(winter_1932_1933_15)
station15.append(winter_1932_1933_15)

try:
    winter_1932_1933_16 = b1[16] + bp[16]
except:
    winter_1932_1933_16 = None
WL_15.append(winter_1932_1933_16)
station16.append(winter_1932_1933_16)

try:
    winter_1932_1933_17 = b1[17] + bp[17]
except:
    winter_1932_1933_17 = None
WL_15.append(winter_1932_1933_17)
station17.append(winter_1932_1933_17)

try:
    winter_1932_1933_18 = b1[18] + bp[18]
except:
    winter_1932_1933_18 = None
WL_15.append(winter_1932_1933_18)
station18.append(winter_1932_1933_18)

try:
    winter_1932_1933_19 = b1[19] + bp[19]
except:
    winter_1932_1933_19 = None
WL_15.append(winter_1932_1933_19)
station19.append(winter_1932_1933_19)

try:
    winter_1932_1933_20 = b1[20] + bp[20]
except:
    winter_1932_1933_20 = None
WL_15.append(winter_1932_1933_20)
station20.append(winter_1932_1933_20)

try:
    winter_1932_1933_21 = b1[21] + bp[21]
except:
    winter_1932_1933_21 = None
WL_15.append(winter_1932_1933_21)
station21.append(winter_1932_1933_21)

try:
    winter_1932_1933_22 = b1[22] + bp[22]
except:
    winter_1932_1933_22 = None
WL_15.append(winter_1932_1933_22)
station22.append(winter_1932_1933_22)

try:
    winter_1932_1933_23 = b1[23] + bp[23]
except:
    winter_1932_1933_23 = None
WL_15.append(winter_1932_1933_23)
station23.append(winter_1932_1933_23)

#last spring freeze values for #1934

bq = []

for rowOfCellObjects in mosheet['EH2':'EH25']:
    for cellObj in rowOfCellObjects:
        bq.append(cellObj.value)

#final winter length calculation for 1933-1934 season for all of 24 Missouri stations

WL_16 = [] #all 1933-1934 winter lengths

try:
    winter_1933_1934_0 = c1[0] + bq[0]
except:
    winter_1933_1934_0 = None
WL_16.append(winter_1933_1934_0)
station0.append(winter_1933_1934_0)

try:
    winter_1933_1934_1 = c1[1] + bq[1]
except:
    winter_1933_1934_1 = None
WL_16.append(winter_1933_1934_1)
station1.append(winter_1933_1934_1)

try:
    winter_1933_1934_2 = c1[2] + bq[2]
except:
    winter_1933_1934_2 = None
WL_16.append(winter_1933_1934_2)
station2.append(winter_1933_1934_2)

try:
    winter_1933_1934_3 = c1[3] + bq[3]
except:
    winter_1933_1934_3 = None
WL_16.append(winter_1933_1934_3)
station3.append(winter_1933_1934_3)

try:
    winter_1933_1934_4 = c1[4] + bq[4]
except:
    winter_1933_1934_4 = None
WL_16.append(winter_1933_1934_4)
station4.append(winter_1933_1934_4)

try:
    winter_1933_1934_5 = c1[5] + bq[5]
except:
    winter_1933_1934_5 = None
WL_16.append(winter_1933_1934_5)
station5.append(winter_1933_1934_5)

try:
    winter_1933_1934_6 = c1[6] + bq[6]
except:
    winter_1933_1934_6 = None
WL_16.append(winter_1933_1934_6)
station6.append(winter_1933_1934_6)

try:
    winter_1933_1934_7 = c1[7] + bq[7]
except:
    winter_1933_1934_7 = None
WL_16.append(winter_1933_1934_7)
station7.append(winter_1933_1934_7)

try:
    winter_1933_1934_8 = c1[8] + bq[8]
except:
    winter_1933_1934_8 = None
WL_16.append(winter_1933_1934_8)
station8.append(winter_1933_1934_8)

try:
    winter_1933_1934_9 = c1[9] + bq[9]
except:
    winter_1933_1934_9 = None
WL_16.append(winter_1933_1934_9)
station9.append(winter_1933_1934_9)

try:
    winter_1933_1934_10 = c1[10] + bq[10]
except:
    winter_1933_1934_10 = None
WL_16.append(winter_1933_1934_10)
station10.append(winter_1933_1934_10)

try:
    winter_1933_1934_11 = c1[11] + bq[11]
except:
    winter_1933_1934_11 = None
WL_16.append(winter_1933_1934_11)
station11.append(winter_1933_1934_11)

try:
    winter_1933_1934_12 = c1[12] + bq[12]
except:
    winter_1933_1934_12 = None
WL_16.append(winter_1933_1934_12)
station12.append(winter_1933_1934_12)

try:
    winter_1933_1934_13 = c1[13] + bq[13]
except:
    winter_1933_1934_13 = None
WL_16.append(winter_1933_1934_13)
station13.append(winter_1933_1934_13)

try:
    winter_1933_1934_14 = c1[14] + bq[14]
except:
    winter_1933_1934_14 = None
WL_16.append(winter_1933_1934_14)
station14.append(winter_1933_1934_14)

try:
    winter_1933_1934_15 = c1[15] + bq[15]
except:
    winter_1933_1934_15 = None
WL_16.append(winter_1933_1934_15)
station15.append(winter_1933_1934_15)

try:
    winter_1933_1934_16 = c1[16] + bq[16]
except:
    winter_1933_1934_16 = None
WL_16.append(winter_1933_1934_16)
station16.append(winter_1933_1934_16)

try:
    winter_1933_1934_17 = c1[17] + bq[17]
except:
    winter_1933_1934_17 = None
WL_16.append(winter_1933_1934_17)
station17.append(winter_1933_1934_17)

try:
    winter_1933_1934_18 = c1[18] + bq[18]
except:
    winter_1933_1934_18 = None
WL_16.append(winter_1933_1934_18)
station18.append(winter_1933_1934_18)

try:
    winter_1933_1934_19 = c1[19] + bq[19]
except:
    winter_1933_1934_19 = None
WL_16.append(winter_1933_1934_19)
station19.append(winter_1933_1934_19)

try:
    winter_1933_1934_20 = c1[20] + bq[20]
except:
    winter_1933_1934_20 = None
WL_16.append(winter_1933_1934_20)
station20.append(winter_1933_1934_20)

try:
    winter_1933_1934_21 = c1[21] + bq[21]
except:
    winter_1933_1934_21 = None
WL_16.append(winter_1933_1934_21)
station21.append(winter_1933_1934_21)

try:
    winter_1933_1934_22 = c1[22] + bq[22]
except:
    winter_1933_1934_22 = None
WL_16.append(winter_1933_1934_22)
station22.append(winter_1933_1934_22)

try:
    winter_1933_1934_23 = c1[23] + bq[23]
except:
    winter_1933_1934_23 = None
WL_16.append(winter_1933_1934_23)
station23.append(winter_1933_1934_23)

#last spring freeze values for #1935

br = []

for rowOfCellObjects in mosheet['EI2':'EI25']:
    for cellObj in rowOfCellObjects:
        br.append(cellObj.value)

#final winter length calculation for 1934-1935 season for all of 24 Missouri stations

WL_17 = [] #all 1934-1935 winter lengths

try:
    winter_1934_1935_0 = d1[0] + br[0]
except:
    winter_1934_1935_0 = None
WL_17.append(winter_1934_1935_0)
station0.append(winter_1934_1935_0)

try:
    winter_1934_1935_1 = d1[1] + br[1]
except:
    winter_1934_1935_1 = None
WL_17.append(winter_1934_1935_1)
station1.append(winter_1934_1935_1)

try:
    winter_1934_1935_2 = d1[2] + br[2]
except:
    winter_1934_1935_2 = None
WL_17.append(winter_1934_1935_2)
station2.append(winter_1934_1935_2)

try:
    winter_1934_1935_3 = d1[3] + br[3]
except:
    winter_1934_1935_3 = None
WL_17.append(winter_1934_1935_3)
station3.append(winter_1934_1935_3)

try:
    winter_1934_1935_4 = d1[4] + br[4]
except:
    winter_1934_1935_4 = None
WL_17.append(winter_1934_1935_4)
station4.append(winter_1934_1935_4)

try:
    winter_1934_1935_5 = d1[5] + br[5]
except:
    winter_1934_1935_5 = None
WL_17.append(winter_1934_1935_5)
station5.append(winter_1934_1935_5)

try:
    winter_1934_1935_6 = d1[6] + br[6]
except:
    winter_1934_1935_6 = None
WL_17.append(winter_1934_1935_6)
station6.append(winter_1934_1935_6)

try:
    winter_1934_1935_7 = d1[7] + br[7]
except:
    winter_1934_1935_7 = None
WL_17.append(winter_1934_1935_7)
station7.append(winter_1934_1935_7)

try:
    winter_1934_1935_8 = d1[8] + br[8]
except:
    winter_1934_1935_8 = None
WL_17.append(winter_1934_1935_8)
station8.append(winter_1934_1935_8)

try:
    winter_1934_1935_9 = d1[9] + br[9]
except:
    winter_1934_1935_9 = None
WL_17.append(winter_1934_1935_9)
station9.append(winter_1934_1935_9)

try:
    winter_1934_1935_10 = d1[10] + br[10]
except:
    winter_1934_1935_10 = None
WL_17.append(winter_1934_1935_10)
station10.append(winter_1934_1935_10)

try:
    winter_1934_1935_11 = d1[11] + br[11]
except:
    winter_1934_1935_11 = None
WL_17.append(winter_1934_1935_11)
station11.append(winter_1934_1935_11)

try:
    winter_1934_1935_12 = d1[12] + br[12]
except:
    winter_1934_1935_12 = None
WL_17.append(winter_1934_1935_12)
station12.append(winter_1934_1935_12)

try:
    winter_1934_1935_13 = d1[13] + br[13]
except:
    winter_1934_1935_13 = None
WL_17.append(winter_1934_1935_13)
station13.append(winter_1934_1935_13)

try:
    winter_1934_1935_14 = d1[14] + br[14]
except:
    winter_1934_1935_14 = None
WL_17.append(winter_1934_1935_14)
station14.append(winter_1934_1935_14)

try:
    winter_1934_1935_15 = d1[15] + br[15]
except:
    winter_1934_1935_15 = None
WL_17.append(winter_1934_1935_15)
station15.append(winter_1934_1935_15)

try:
    winter_1934_1935_16 = d1[16] + br[16]
except:
    winter_1934_1935_16 = None
WL_17.append(winter_1934_1935_16)
station16.append(winter_1934_1935_16)

try:
    winter_1934_1935_17 = d1[17] + br[17]
except:
    winter_1934_1935_17 = None
WL_17.append(winter_1934_1935_17)
station17.append(winter_1934_1935_17)

try:
    winter_1934_1935_18 = d1[18] + br[18]
except:
    winter_1934_1935_18 = None
WL_17.append(winter_1934_1935_18)
station18.append(winter_1934_1935_18)

try:
    winter_1934_1935_19 = d1[19] + br[19]
except:
    winter_1934_1935_19 = None
WL_17.append(winter_1934_1935_19)
station19.append(winter_1934_1935_19)

try:
    winter_1934_1935_20 = d1[20] + br[20]
except:
    winter_1934_1935_20 = None
WL_17.append(winter_1934_1935_20)
station20.append(winter_1934_1935_20)

try:
    winter_1934_1935_21 = d1[21] + br[21]
except:
    winter_1934_1935_21 = None
WL_17.append(winter_1934_1935_21)
station21.append(winter_1934_1935_21)

try:
    winter_1934_1935_22 = d1[22] + br[22]
except:
    winter_1934_1935_22 = None
WL_17.append(winter_1934_1935_22)
station22.append(winter_1934_1935_22)

try:
    winter_1934_1935_23 = d1[23] + br[23]
except:
    winter_1934_1935_23 = None
WL_17.append(winter_1934_1935_23)
station23.append(winter_1934_1935_23)

#last spring freeze values for #1936

bs = []

for rowOfCellObjects in mosheet['EJ2':'EJ25']:
    for cellObj in rowOfCellObjects:
        bs.append(cellObj.value)

#final winter length calculation for 1935-1936 season for all of 24 Missouri stations

WL_18 = [] #all 1935-1936 winter lengths

try:
    winter_1935_1936_0 = e1[0] + bs[0]
except:
    winter_1935_1936_0 = None
WL_18.append(winter_1935_1936_0)
station0.append(winter_1935_1936_0)

try:
    winter_1935_1936_1 = e1[1] + bs[1]
except:
    winter_1935_1936_1 = None
WL_18.append(winter_1935_1936_1)
station1.append(winter_1935_1936_1)

try:
    winter_1935_1936_2 = e1[2] + bs[2]
except:
    winter_1935_1936_2 = None
WL_18.append(winter_1935_1936_2)
station2.append(winter_1935_1936_2)

try:
    winter_1935_1936_3 = e1[3] + bs[3]
except:
    winter_1935_1936_3 = None
WL_18.append(winter_1935_1936_3)
station3.append(winter_1935_1936_3)

try:
    winter_1935_1936_4 = e1[4] + bs[4]
except:
    winter_1935_1936_4 = None
WL_18.append(winter_1935_1936_4)
station4.append(winter_1935_1936_4)

try:
    winter_1935_1936_5 = e1[5] + bs[5]
except:
    winter_1935_1936_5 = None
WL_18.append(winter_1935_1936_5)
station5.append(winter_1935_1936_5)

try:
    winter_1935_1936_6 = e1[6] + bs[6]
except:
    winter_1935_1936_6 = None
WL_18.append(winter_1935_1936_6)
station6.append(winter_1935_1936_6)

try:
    winter_1935_1936_7 = e1[7] + bs[7]
except:
    winter_1935_1936_7 = None
WL_18.append(winter_1935_1936_7)
station7.append(winter_1935_1936_7)

try:
    winter_1935_1936_8 = e1[8] + bs[8]
except:
    winter_1935_1936_8 = None
WL_18.append(winter_1935_1936_8)
station8.append(winter_1935_1936_8)

try:
    winter_1935_1936_9 = e1[9] + bs[9]
except:
    winter_1935_1936_9 = None
WL_18.append(winter_1935_1936_9)
station9.append(winter_1935_1936_9)

try:
    winter_1935_1936_10 = e1[10] + bs[10]
except:
    winter_1935_1936_10 = None
WL_18.append(winter_1935_1936_10)
station10.append(winter_1935_1936_10)

try:
    winter_1935_1936_11 = e1[11] + bs[11]
except:
    winter_1935_1936_11 = None
WL_18.append(winter_1935_1936_11)
station11.append(winter_1935_1936_11)

try:
    winter_1935_1936_12 = e1[12] + bs[12]
except:
    winter_1935_1936_12 = None
WL_18.append(winter_1935_1936_12)
station12.append(winter_1935_1936_12)

try:
    winter_1935_1936_13 = e1[13] + bs[13]
except:
    winter_1935_1936_13 = None
WL_18.append(winter_1935_1936_13)
station13.append(winter_1935_1936_13)

try:
    winter_1935_1936_14 = e1[14] + bs[14]
except:
    winter_1935_1936_14 = None
WL_18.append(winter_1935_1936_14)
station14.append(winter_1935_1936_14)

try:
    winter_1935_1936_15 = e1[15] + bs[15]
except:
    winter_1935_1936_15 = None
WL_18.append(winter_1935_1936_15)
station15.append(winter_1935_1936_15)

try:
    winter_1935_1936_16 = e1[16] + bs[16]
except:
    winter_1935_1936_16 = None
WL_18.append(winter_1935_1936_16)
station16.append(winter_1935_1936_16)

try:
    winter_1935_1936_17 = e1[17] + bs[17]
except:
    winter_1935_1936_17 = None
WL_18.append(winter_1935_1936_17)
station17.append(winter_1935_1936_17)

try:
    winter_1935_1936_18 = e1[18] + bs[18]
except:
    winter_1935_1936_18 = None
WL_18.append(winter_1935_1936_18)
station18.append(winter_1935_1936_18)

try:
    winter_1935_1936_19 = e1[19] + bs[19]
except:
    winter_1935_1936_19 = None
WL_18.append(winter_1935_1936_19)
station19.append(winter_1935_1936_19)

try:
    winter_1935_1936_20 = e1[20] + bs[20]
except:
    winter_1935_1936_20 = None
WL_18.append(winter_1935_1936_20)
station20.append(winter_1935_1936_20)

try:
    winter_1935_1936_21 = e1[21] + bs[21]
except:
    winter_1935_1936_21 = None
WL_18.append(winter_1935_1936_21)
station21.append(winter_1935_1936_21)

try:
    winter_1935_1936_22 = e1[22] + bs[22]
except:
    winter_1935_1936_22 = None
WL_18.append(winter_1935_1936_22)
station22.append(winter_1935_1936_22)

try:
    winter_1935_1936_23 = e1[23] + bs[23]
except:
    winter_1935_1936_23 = None
WL_18.append(winter_1935_1936_23)
station23.append(winter_1935_1936_23)

#last spring freeze values for #1937

bt = []

for rowOfCellObjects in mosheet['EK2':'EK25']:
    for cellObj in rowOfCellObjects:
        bt.append(cellObj.value)

#final winter length calculation for 1936-1937 season for all of 24 Missouri stations

WL_19 = [] #all 1936-1937 winter lengths

try:
    winter_1936_1937_0 = f1[0] + bt[0]
except:
    winter_1936_1937_0 = None
WL_19.append(winter_1936_1937_0)
station0.append(winter_1936_1937_0)

try:
    winter_1936_1937_1 = f1[1] + bt[1]
except:
    winter_1936_1937_1 = None
WL_19.append(winter_1936_1937_1)
station1.append(winter_1936_1937_1)

try:
    winter_1936_1937_2 = f1[2] + bt[2]
except:
    winter_1936_1937_2 = None
WL_19.append(winter_1936_1937_2)
station2.append(winter_1936_1937_2)

try:
    winter_1936_1937_3 = f1[3] + bt[3]
except:
    winter_1936_1937_3 = None
WL_19.append(winter_1936_1937_3)
station3.append(winter_1936_1937_3)

try:
    winter_1936_1937_4 = f1[4] + bt[4]
except:
    winter_1936_1937_4 = None
WL_19.append(winter_1936_1937_4)
station4.append(winter_1936_1937_4)

try:
    winter_1936_1937_5 = f1[5] + bt[5]
except:
    winter_1936_1937_5 = None
WL_19.append(winter_1936_1937_5)
station5.append(winter_1936_1937_5)

try:
    winter_1936_1937_6 = f1[6] + bt[6]
except:
    winter_1936_1937_6 = None
WL_19.append(winter_1936_1937_6)
station6.append(winter_1936_1937_6)

try:
    winter_1936_1937_7 = f1[7] + bt[7]
except:
    winter_1936_1937_7 = None
WL_19.append(winter_1936_1937_7)
station7.append(winter_1936_1937_7)

try:
    winter_1936_1937_8 = f1[8] + bt[8]
except:
    winter_1936_1937_8 = None
WL_19.append(winter_1936_1937_8)
station8.append(winter_1936_1937_8)

try:
    winter_1936_1937_9 = f1[9] + bt[9]
except:
    winter_1936_1937_9 = None
WL_19.append(winter_1936_1937_9)
station9.append(winter_1936_1937_9)

try:
    winter_1936_1937_10 = f1[10] + bt[10]
except:
    winter_1936_1937_10 = None
WL_19.append(winter_1936_1937_10)
station10.append(winter_1936_1937_10)

try:
    winter_1936_1937_11 = f1[11] + bt[11]
except:
    winter_1936_1937_11 = None
WL_19.append(winter_1936_1937_11)
station11.append(winter_1936_1937_11)

try:
    winter_1936_1937_12 = f1[12] + bt[12]
except:
    winter_1936_1937_12 = None
WL_19.append(winter_1936_1937_12)
station12.append(winter_1936_1937_12)

try:
    winter_1936_1937_13 = f1[13] + bt[13]
except:
    winter_1936_1937_13 = None
WL_19.append(winter_1936_1937_13)
station13.append(winter_1936_1937_13)

try:
    winter_1936_1937_14 = f1[14] + bt[14]
except:
    winter_1936_1937_14 = None
WL_19.append(winter_1936_1937_14)
station14.append(winter_1936_1937_14)

try:
    winter_1936_1937_15 = f1[15] + bt[15]
except:
    winter_1936_1937_15 = None
WL_19.append(winter_1936_1937_15)
station15.append(winter_1936_1937_15)

try:
    winter_1936_1937_16 = f1[16] + bt[16]
except:
    winter_1936_1937_16 = None
WL_19.append(winter_1936_1937_16)
station16.append(winter_1936_1937_16)

try:
    winter_1936_1937_17 = f1[17] + bt[17]
except:
    winter_1936_1937_17 = None
WL_19.append(winter_1936_1937_17)
station17.append(winter_1936_1937_17)

try:
    winter_1936_1937_18 = f1[18] + bt[18]
except:
    winter_1936_1937_18 = None
WL_19.append(winter_1936_1937_18)
station18.append(winter_1936_1937_18)

try:
    winter_1936_1937_19 = f1[19] + bt[19]
except:
    winter_1936_1937_19 = None
WL_19.append(winter_1936_1937_19)
station19.append(winter_1936_1937_19)

try:
    winter_1936_1937_20 = f1[20] + bt[20]
except:
    winter_1936_1937_20 = None
WL_19.append(winter_1936_1937_20)
station20.append(winter_1936_1937_20)

try:
    winter_1936_1937_21 = f1[21] + bt[21]
except:
    winter_1936_1937_21 = None
WL_19.append(winter_1936_1937_21)
station21.append(winter_1936_1937_21)

try:
    winter_1936_1937_22 = f1[22] + bt[22]
except:
    winter_1936_1937_22 = None
WL_19.append(winter_1936_1937_22)
station22.append(winter_1936_1937_22)

try:
    winter_1936_1937_23 = f1[23] + bt[23]
except:
    winter_1936_1937_23 = None
WL_19.append(winter_1936_1937_23)
station23.append(winter_1936_1937_23)

