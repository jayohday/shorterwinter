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

#making list of fall part of winter lengths from each column/year for later use in final winter length calculations
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
for rowOfCellObjects in mosheet['cr2':'cr25']:
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

cr = []
for rowOfCellObjects in mosheet['AP2':'AP25']:
    for cellObj in rowOfCellObjects:
        cr.append(cellObj.value)

cr1 = []

for i in cr:
    try:
        x = 365 - (i-1)
    except:
        x = None
    cr1.append(x)

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
    winter_1923_1924_0 = r1[0] + bg[0]
except:
    winter_1923_1924_0 = None
WL_6.append(winter_1923_1924_0)
station0.append(winter_1923_1924_0)

try:
    winter_1923_1924_1 = r1[1] + bg[1]
except:
    winter_1923_1924_1 = None
WL_6.append(winter_1923_1924_1)
station1.append(winter_1923_1924_1)

try:
    winter_1923_1924_2 = r1[2] + bg[2]
except:
    winter_1923_1924_2 = None
WL_6.append(winter_1923_1924_2)
station2.append(winter_1923_1924_2)

try:
    winter_1923_1924_3 = r1[3] + bg[3]
except:
    winter_1923_1924_3 = None
WL_6.append(winter_1923_1924_3)
station3.append(winter_1923_1924_3)

try:
    winter_1923_1924_4 = r1[4] + bg[4]
except:
    winter_1923_1924_4 = None
WL_6.append(winter_1923_1924_4)
station4.append(winter_1923_1924_4)

try:
    winter_1923_1924_5 = r1[5] + bg[5]
except:
    winter_1923_1924_5 = None
WL_6.append(winter_1923_1924_5)
station5.append(winter_1923_1924_5)

try:
    winter_1923_1924_6 = r1[6] + bg[6]
except:
    winter_1923_1924_6 = None
WL_6.append(winter_1923_1924_6)
station6.append(winter_1923_1924_6)

try:
    winter_1923_1924_7 = r1[7] + bg[7]
except:
    winter_1923_1924_7 = None
WL_6.append(winter_1923_1924_7)
station7.append(winter_1923_1924_7)

try:
    winter_1923_1924_8 = r1[8] + bg[8]
except:
    winter_1923_1924_8 = None
WL_6.append(winter_1923_1924_8)
station8.append(winter_1923_1924_8)

try:
    winter_1923_1924_9 = r1[9] + bg[9]
except:
    winter_1923_1924_9 = None
WL_6.append(winter_1923_1924_9)
station9.append(winter_1923_1924_9)

try:
    winter_1923_1924_10 = r1[10] + bg[10]
except:
    winter_1923_1924_10 = None
WL_6.append(winter_1923_1924_10)
station10.append(winter_1923_1924_10)

try:
    winter_1923_1924_11 = r1[11] + bg[11]
except:
    winter_1923_1924_11 = None
WL_6.append(winter_1923_1924_11)
station11.append(winter_1923_1924_11)

try:
    winter_1923_1924_12 = r1[12] + bg[12]
except:
    winter_1923_1924_12 = None
WL_6.append(winter_1923_1924_12)
station12.append(winter_1923_1924_12)

try:
    winter_1923_1924_13 = r1[13] + bg[13]
except:
    winter_1923_1924_13 = None
WL_6.append(winter_1923_1924_13)
station13.append(winter_1923_1924_13)

try:
    winter_1923_1924_14 = r1[14] + bg[14]
except:
    winter_1923_1924_14 = None
WL_6.append(winter_1923_1924_14)
station14.append(winter_1923_1924_14)

try:
    winter_1923_1924_15 = r1[15] + bg[15]
except:
    winter_1923_1924_15 = None
WL_6.append(winter_1923_1924_15)
station15.append(winter_1923_1924_15)

try:
    winter_1923_1924_16 = r1[16] + bg[16]
except:
    winter_1923_1924_16 = None
WL_6.append(winter_1923_1924_16)
station16.append(winter_1923_1924_16)

try:
    winter_1923_1924_17 = r1[17] + bg[17]
except:
    winter_1923_1924_17 = None
WL_6.append(winter_1923_1924_17)
station17.append(winter_1923_1924_17)

try:
    winter_1923_1924_18 = r1[18] + bg[18]
except:
    winter_1923_1924_18 = None
WL_6.append(winter_1923_1924_18)
station18.append(winter_1923_1924_18)

try:
    winter_1923_1924_19 = r1[19] + bg[19]
except:
    winter_1923_1924_19 = None
WL_6.append(winter_1923_1924_19)
station19.append(winter_1923_1924_19)

try:
    winter_1923_1924_20 = r1[20] + bg[20]
except:
    winter_1923_1924_20 = None
WL_6.append(winter_1923_1924_20)
station20.append(winter_1923_1924_20)

try:
    winter_1923_1924_21 = r1[21] + bg[21]
except:
    winter_1923_1924_21 = None
WL_6.append(winter_1923_1924_21)
station21.append(winter_1923_1924_21)

try:
    winter_1923_1924_22 = r1[22] + bg[22]
except:
    winter_1923_1924_22 = None
WL_6.append(winter_1923_1924_22)
station22.append(winter_1923_1924_22)

try:
    winter_1923_1924_23 = r1[23] + bg[23]
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

#last spring freeze values for #1938

bu = []

for rowOfCellObjects in mosheet['EL2':'EL25']:
    for cellObj in rowOfCellObjects:
        bu.append(cellObj.value)

#final winter length calculation for 1937-1938 season for all of 24 Missouri stations

WL_20 = [] #all 1937-1938 winter lengths

try:
    winter_1937_1938_0 = g1[0] + bu[0]
except:
    winter_1937_1938_0 = None
WL_20.append(winter_1937_1938_0)
station0.append(winter_1937_1938_0)

try:
    winter_1937_1938_1 = g1[1] + bu[1]
except:
    winter_1937_1938_1 = None
WL_20.append(winter_1937_1938_1)
station1.append(winter_1937_1938_1)

try:
    winter_1937_1938_2 = g1[2] + bu[2]
except:
    winter_1937_1938_2 = None
WL_20.append(winter_1937_1938_2)
station2.append(winter_1937_1938_2)

try:
    winter_1937_1938_3 = g1[3] + bu[3]
except:
    winter_1937_1938_3 = None
WL_20.append(winter_1937_1938_3)
station3.append(winter_1937_1938_3)

try:
    winter_1937_1938_4 = g1[4] + bu[4]
except:
    winter_1937_1938_4 = None
WL_20.append(winter_1937_1938_4)
station4.append(winter_1937_1938_4)

try:
    winter_1937_1938_5 = g1[5] + bu[5]
except:
    winter_1937_1938_5 = None
WL_20.append(winter_1937_1938_5)
station5.append(winter_1937_1938_5)

try:
    winter_1937_1938_6 = g1[6] + bu[6]
except:
    winter_1937_1938_6 = None
WL_20.append(winter_1937_1938_6)
station6.append(winter_1937_1938_6)

try:
    winter_1937_1938_7 = g1[7] + bu[7]
except:
    winter_1937_1938_7 = None
WL_20.append(winter_1937_1938_7)
station7.append(winter_1937_1938_7)

try:
    winter_1937_1938_8 = g1[8] + bu[8]
except:
    winter_1937_1938_8 = None
WL_20.append(winter_1937_1938_8)
station8.append(winter_1937_1938_8)

try:
    winter_1937_1938_9 = g1[9] + bu[9]
except:
    winter_1937_1938_9 = None
WL_20.append(winter_1937_1938_9)
station9.append(winter_1937_1938_9)

try:
    winter_1937_1938_10 = g1[10] + bu[10]
except:
    winter_1937_1938_10 = None
WL_20.append(winter_1937_1938_10)
station10.append(winter_1937_1938_10)

try:
    winter_1937_1938_11 = g1[11] + bu[11]
except:
    winter_1937_1938_11 = None
WL_20.append(winter_1937_1938_11)
station11.append(winter_1937_1938_11)

try:
    winter_1937_1938_12 = g1[12] + bu[12]
except:
    winter_1937_1938_12 = None
WL_20.append(winter_1937_1938_12)
station12.append(winter_1937_1938_12)

try:
    winter_1937_1938_13 = g1[13] + bu[13]
except:
    winter_1937_1938_13 = None
WL_20.append(winter_1937_1938_13)
station13.append(winter_1937_1938_13)

try:
    winter_1937_1938_14 = g1[14] + bu[14]
except:
    winter_1937_1938_14 = None
WL_20.append(winter_1937_1938_14)
station14.append(winter_1937_1938_14)

try:
    winter_1937_1938_15 = g1[15] + bu[15]
except:
    winter_1937_1938_15 = None
WL_20.append(winter_1937_1938_15)
station15.append(winter_1937_1938_15)

try:
    winter_1937_1938_16 = g1[16] + bu[16]
except:
    winter_1937_1938_16 = None
WL_20.append(winter_1937_1938_16)
station16.append(winter_1937_1938_16)

try:
    winter_1937_1938_17 = g1[17] + bu[17]
except:
    winter_1937_1938_17 = None
WL_20.append(winter_1937_1938_17)
station17.append(winter_1937_1938_17)

try:
    winter_1937_1938_18 = g1[18] + bu[18]
except:
    winter_1937_1938_18 = None
WL_20.append(winter_1937_1938_18)
station18.append(winter_1937_1938_18)

try:
    winter_1937_1938_19 = g1[19] + bu[19]
except:
    winter_1937_1938_19 = None
WL_20.append(winter_1937_1938_19)
station19.append(winter_1937_1938_19)

try:
    winter_1937_1938_20 = g1[20] + bu[20]
except:
    winter_1937_1938_20 = None
WL_20.append(winter_1937_1938_20)
station20.append(winter_1937_1938_20)

try:
    winter_1937_1938_21 = g1[21] + bu[21]
except:
    winter_1937_1938_21 = None
WL_20.append(winter_1937_1938_21)
station21.append(winter_1937_1938_21)

try:
    winter_1937_1938_22 = g1[22] + bu[22]
except:
    winter_1937_1938_22 = None
WL_20.append(winter_1937_1938_22)
station22.append(winter_1937_1938_22)

try:
    winter_1937_1938_23 = g1[23] + bu[23]
except:
    winter_1937_1938_23 = None
WL_20.append(winter_1937_1938_23)
station23.append(winter_1937_1938_23)

#last spring freeze values for #1939

bv = []

for rowOfCellObjects in mosheet['EM2':'EM25']:
    for cellObj in rowOfCellObjects:
        bv.append(cellObj.value)

#final winter length calculation for 1938-1939 season for all of 24 Missouri stations

WL_21 = [] #all 1938-1939 winter lengths

try:
    winter_1938_1939_0 = h1[0] + bv[0]
except:
    winter_1938_1939_0 = None
WL_21.append(winter_1938_1939_0)
station0.append(winter_1938_1939_0)

try:
    winter_1938_1939_1 = h1[1] + bv[1]
except:
    winter_1938_1939_1 = None
WL_21.append(winter_1938_1939_1)
station1.append(winter_1938_1939_1)

try:
    winter_1938_1939_2 = h1[2] + bv[2]
except:
    winter_1938_1939_2 = None
WL_21.append(winter_1938_1939_2)
station2.append(winter_1938_1939_2)

try:
    winter_1938_1939_3 = h1[3] + bv[3]
except:
    winter_1938_1939_3 = None
WL_21.append(winter_1938_1939_3)
station3.append(winter_1938_1939_3)

try:
    winter_1938_1939_4 = h1[4] + bv[4]
except:
    winter_1938_1939_4 = None
WL_21.append(winter_1938_1939_4)
station4.append(winter_1938_1939_4)

try:
    winter_1938_1939_5 = h1[5] + bv[5]
except:
    winter_1938_1939_5 = None
WL_21.append(winter_1938_1939_5)
station5.append(winter_1938_1939_5)

try:
    winter_1938_1939_6 = h1[6] + bv[6]
except:
    winter_1938_1939_6 = None
WL_21.append(winter_1938_1939_6)
station6.append(winter_1938_1939_6)

try:
    winter_1938_1939_7 = h1[7] + bv[7]
except:
    winter_1938_1939_7 = None
WL_21.append(winter_1938_1939_7)
station7.append(winter_1938_1939_7)

try:
    winter_1938_1939_8 = h1[8] + bv[8]
except:
    winter_1938_1939_8 = None
WL_21.append(winter_1938_1939_8)
station8.append(winter_1938_1939_8)

try:
    winter_1938_1939_9 = h1[9] + bv[9]
except:
    winter_1938_1939_9 = None
WL_21.append(winter_1938_1939_9)
station9.append(winter_1938_1939_9)

try:
    winter_1938_1939_10 = h1[10] + bv[10]
except:
    winter_1938_1939_10 = None
WL_21.append(winter_1938_1939_10)
station10.append(winter_1938_1939_10)

try:
    winter_1938_1939_11 = h1[11] + bv[11]
except:
    winter_1938_1939_11 = None
WL_21.append(winter_1938_1939_11)
station11.append(winter_1938_1939_11)

try:
    winter_1938_1939_12 = h1[12] + bv[12]
except:
    winter_1938_1939_12 = None
WL_21.append(winter_1938_1939_12)
station12.append(winter_1938_1939_12)

try:
    winter_1938_1939_13 = h1[13] + bv[13]
except:
    winter_1938_1939_13 = None
WL_21.append(winter_1938_1939_13)
station13.append(winter_1938_1939_13)

try:
    winter_1938_1939_14 = h1[14] + bv[14]
except:
    winter_1938_1939_14 = None
WL_21.append(winter_1938_1939_14)
station14.append(winter_1938_1939_14)

try:
    winter_1938_1939_15 = h1[15] + bv[15]
except:
    winter_1938_1939_15 = None
WL_21.append(winter_1938_1939_15)
station15.append(winter_1938_1939_15)

try:
    winter_1938_1939_16 = h1[16] + bv[16]
except:
    winter_1938_1939_16 = None
WL_21.append(winter_1938_1939_16)
station16.append(winter_1938_1939_16)

try:
    winter_1938_1939_17 = h1[17] + bv[17]
except:
    winter_1938_1939_17 = None
WL_21.append(winter_1938_1939_17)
station17.append(winter_1938_1939_17)

try:
    winter_1938_1939_18 = h1[18] + bv[18]
except:
    winter_1938_1939_18 = None
WL_21.append(winter_1938_1939_18)
station18.append(winter_1938_1939_18)

try:
    winter_1938_1939_19 = h1[19] + bv[19]
except:
    winter_1938_1939_19 = None
WL_21.append(winter_1938_1939_19)
station19.append(winter_1938_1939_19)

try:
    winter_1938_1939_20 = h1[20] + bv[20]
except:
    winter_1938_1939_20 = None
WL_21.append(winter_1938_1939_20)
station20.append(winter_1938_1939_20)

try:
    winter_1938_1939_21 = h1[21] + bv[21]
except:
    winter_1938_1939_21 = None
WL_21.append(winter_1938_1939_21)
station21.append(winter_1938_1939_21)

try:
    winter_1938_1939_22 = h1[22] + bv[22]
except:
    winter_1938_1939_22 = None
WL_21.append(winter_1938_1939_22)
station22.append(winter_1938_1939_22)

try:
    winter_1938_1939_23 = h1[23] + bv[23]
except:
    winter_1938_1939_23 = None
WL_21.append(winter_1938_1939_23)
station23.append(winter_1938_1939_23)

#last spring freeze values for #1940

bw = []

for rowOfCellObjects in mosheet['EN2':'EN25']:
    for cellObj in rowOfCellObjects:
        bw.append(cellObj.value)

#final winter length calculation for 1939-1940 season for all of 24 Missouri stations

WL_22 = [] #all 1939-1940 winter lengths

try:
    winter_1939_1940_0 = j1[0] + bw[0]
except:
    winter_1939_1940_0 = None
WL_22.append(winter_1939_1940_0)
station0.append(winter_1939_1940_0)

try:
    winter_1939_1940_1 = j1[1] + bw[1]
except:
    winter_1939_1940_1 = None
WL_22.append(winter_1939_1940_1)
station1.append(winter_1939_1940_1)

try:
    winter_1939_1940_2 = j1[2] + bw[2]
except:
    winter_1939_1940_2 = None
WL_22.append(winter_1939_1940_2)
station2.append(winter_1939_1940_2)

try:
    winter_1939_1940_3 = j1[3] + bw[3]
except:
    winter_1939_1940_3 = None
WL_22.append(winter_1939_1940_3)
station3.append(winter_1939_1940_3)

try:
    winter_1939_1940_4 = j1[4] + bw[4]
except:
    winter_1939_1940_4 = None
WL_22.append(winter_1939_1940_4)
station4.append(winter_1939_1940_4)

try:
    winter_1939_1940_5 = j1[5] + bw[5]
except:
    winter_1939_1940_5 = None
WL_22.append(winter_1939_1940_5)
station5.append(winter_1939_1940_5)

try:
    winter_1939_1940_6 = j1[6] + bw[6]
except:
    winter_1939_1940_6 = None
WL_22.append(winter_1939_1940_6)
station6.append(winter_1939_1940_6)

try:
    winter_1939_1940_7 = j1[7] + bw[7]
except:
    winter_1939_1940_7 = None
WL_22.append(winter_1939_1940_7)
station7.append(winter_1939_1940_7)

try:
    winter_1939_1940_8 = j1[8] + bw[8]
except:
    winter_1939_1940_8 = None
WL_22.append(winter_1939_1940_8)
station8.append(winter_1939_1940_8)

try:
    winter_1939_1940_9 = j1[9] + bw[9]
except:
    winter_1939_1940_9 = None
WL_22.append(winter_1939_1940_9)
station9.append(winter_1939_1940_9)

try:
    winter_1939_1940_10 = j1[10] + bw[10]
except:
    winter_1939_1940_10 = None
WL_22.append(winter_1939_1940_10)
station10.append(winter_1939_1940_10)

try:
    winter_1939_1940_11 = j1[11] + bw[11]
except:
    winter_1939_1940_11 = None
WL_22.append(winter_1939_1940_11)
station11.append(winter_1939_1940_11)

try:
    winter_1939_1940_12 = j1[12] + bw[12]
except:
    winter_1939_1940_12 = None
WL_22.append(winter_1939_1940_12)
station12.append(winter_1939_1940_12)

try:
    winter_1939_1940_13 = j1[13] + bw[13]
except:
    winter_1939_1940_13 = None
WL_22.append(winter_1939_1940_13)
station13.append(winter_1939_1940_13)

try:
    winter_1939_1940_14 = j1[14] + bw[14]
except:
    winter_1939_1940_14 = None
WL_22.append(winter_1939_1940_14)
station14.append(winter_1939_1940_14)

try:
    winter_1939_1940_15 = j1[15] + bw[15]
except:
    winter_1939_1940_15 = None
WL_22.append(winter_1939_1940_15)
station15.append(winter_1939_1940_15)

try:
    winter_1939_1940_16 = j1[16] + bw[16]
except:
    winter_1939_1940_16 = None
WL_22.append(winter_1939_1940_16)
station16.append(winter_1939_1940_16)

try:
    winter_1939_1940_17 = j1[17] + bw[17]
except:
    winter_1939_1940_17 = None
WL_22.append(winter_1939_1940_17)
station17.append(winter_1939_1940_17)

try:
    winter_1939_1940_18 = j1[18] + bw[18]
except:
    winter_1939_1940_18 = None
WL_22.append(winter_1939_1940_18)
station18.append(winter_1939_1940_18)

try:
    winter_1939_1940_19 = j1[19] + bw[19]
except:
    winter_1939_1940_19 = None
WL_22.append(winter_1939_1940_19)
station19.append(winter_1939_1940_19)

try:
    winter_1939_1940_20 = j1[20] + bw[20]
except:
    winter_1939_1940_20 = None
WL_22.append(winter_1939_1940_20)
station20.append(winter_1939_1940_20)

try:
    winter_1939_1940_21 = j1[21] + bw[21]
except:
    winter_1939_1940_21 = None
WL_22.append(winter_1939_1940_21)
station21.append(winter_1939_1940_21)

try:
    winter_1939_1940_22 = j1[22] + bw[22]
except:
    winter_1939_1940_22 = None
WL_22.append(winter_1939_1940_22)
station22.append(winter_1939_1940_22)

try:
    winter_1939_1940_23 = j1[23] + bw[23]
except:
    winter_1939_1940_23 = None
WL_22.append(winter_1939_1940_23)
station23.append(winter_1939_1940_23)

#last spring freeze values for #1941

bx = []

for rowOfCellObjects in mosheet['EO2':'EO25']:
    for cellObj in rowOfCellObjects:
        bx.append(cellObj.value)

#final winter length calculation for 1940-1941 season for all of 24 Missouri stations

WL_23 = [] #all 1940-1941 winter lengths

try:
    winter_1940_1941_0 = k1[0] + bx[0]
except:
    winter_1940_1941_0 = None
WL_23.append(winter_1940_1941_0)
station0.append(winter_1940_1941_0)

try:
    winter_1940_1941_1 = k1[1] + bx[1]
except:
    winter_1940_1941_1 = None
WL_23.append(winter_1940_1941_1)
station1.append(winter_1940_1941_1)

try:
    winter_1940_1941_2 = k1[2] + bx[2]
except:
    winter_1940_1941_2 = None
WL_23.append(winter_1940_1941_2)
station2.append(winter_1940_1941_2)

try:
    winter_1940_1941_3 = k1[3] + bx[3]
except:
    winter_1940_1941_3 = None
WL_23.append(winter_1940_1941_3)
station3.append(winter_1940_1941_3)

try:
    winter_1940_1941_4 = k1[4] + bx[4]
except:
    winter_1940_1941_4 = None
WL_23.append(winter_1940_1941_4)
station4.append(winter_1940_1941_4)

try:
    winter_1940_1941_5 = k1[5] + bx[5]
except:
    winter_1940_1941_5 = None
WL_23.append(winter_1940_1941_5)
station5.append(winter_1940_1941_5)

try:
    winter_1940_1941_6 = k1[6] + bx[6]
except:
    winter_1940_1941_6 = None
WL_23.append(winter_1940_1941_6)
station6.append(winter_1940_1941_6)

try:
    winter_1940_1941_7 = k1[7] + bx[7]
except:
    winter_1940_1941_7 = None
WL_23.append(winter_1940_1941_7)
station7.append(winter_1940_1941_7)

try:
    winter_1940_1941_8 = k1[8] + bx[8]
except:
    winter_1940_1941_8 = None
WL_23.append(winter_1940_1941_8)
station8.append(winter_1940_1941_8)

try:
    winter_1940_1941_9 = k1[9] + bx[9]
except:
    winter_1940_1941_9 = None
WL_23.append(winter_1940_1941_9)
station9.append(winter_1940_1941_9)

try:
    winter_1940_1941_10 = k1[10] + bx[10]
except:
    winter_1940_1941_10 = None
WL_23.append(winter_1940_1941_10)
station10.append(winter_1940_1941_10)

try:
    winter_1940_1941_11 = k1[11] + bx[11]
except:
    winter_1940_1941_11 = None
WL_23.append(winter_1940_1941_11)
station11.append(winter_1940_1941_11)

try:
    winter_1940_1941_12 = k1[12] + bx[12]
except:
    winter_1940_1941_12 = None
WL_23.append(winter_1940_1941_12)
station12.append(winter_1940_1941_12)

try:
    winter_1940_1941_13 = k1[13] + bx[13]
except:
    winter_1940_1941_13 = None
WL_23.append(winter_1940_1941_13)
station13.append(winter_1940_1941_13)

try:
    winter_1940_1941_14 = k1[14] + bx[14]
except:
    winter_1940_1941_14 = None
WL_23.append(winter_1940_1941_14)
station14.append(winter_1940_1941_14)

try:
    winter_1940_1941_15 = k1[15] + bx[15]
except:
    winter_1940_1941_15 = None
WL_23.append(winter_1940_1941_15)
station15.append(winter_1940_1941_15)

try:
    winter_1940_1941_16 = k1[16] + bx[16]
except:
    winter_1940_1941_16 = None
WL_23.append(winter_1940_1941_16)
station16.append(winter_1940_1941_16)

try:
    winter_1940_1941_17 = k1[17] + bx[17]
except:
    winter_1940_1941_17 = None
WL_23.append(winter_1940_1941_17)
station17.append(winter_1940_1941_17)

try:
    winter_1940_1941_18 = k1[18] + bx[18]
except:
    winter_1940_1941_18 = None
WL_23.append(winter_1940_1941_18)
station18.append(winter_1940_1941_18)

try:
    winter_1940_1941_19 = k1[19] + bx[19]
except:
    winter_1940_1941_19 = None
WL_23.append(winter_1940_1941_19)
station19.append(winter_1940_1941_19)

try:
    winter_1940_1941_20 = k1[20] + bx[20]
except:
    winter_1940_1941_20 = None
WL_23.append(winter_1940_1941_20)
station20.append(winter_1940_1941_20)

try:
    winter_1940_1941_21 = k1[21] + bx[21]
except:
    winter_1940_1941_21 = None
WL_23.append(winter_1940_1941_21)
station21.append(winter_1940_1941_21)

try:
    winter_1940_1941_22 = k1[22] + bx[22]
except:
    winter_1940_1941_22 = None
WL_23.append(winter_1940_1941_22)
station22.append(winter_1940_1941_22)

try:
    winter_1940_1941_23 = k1[23] + bx[23]
except:
    winter_1940_1941_23 = None
WL_23.append(winter_1940_1941_23)
station23.append(winter_1940_1941_23)

#last spring freeze values for #1942

by = []

for rowOfCellObjects in mosheet['EP2':'EP25']:
    for cellObj in rowOfCellObjects:
        by.append(cellObj.value)

#final winter length calculation for 1941-1942 season for all of 24 Missouri stations

WL_24 = [] #all 1941-1942 winter lengths

try:
    winter_1941_1942_0 = aa1[0] + by[0]
except:
    winter_1941_1942_0 = None
WL_24.append(winter_1941_1942_0)
station0.append(winter_1941_1942_0)

try:
    winter_1941_1942_1 = aa1[1] + by[1]
except:
    winter_1941_1942_1 = None
WL_24.append(winter_1941_1942_1)
station1.append(winter_1941_1942_1)

try:
    winter_1941_1942_2 = aa1[2] + by[2]
except:
    winter_1941_1942_2 = None
WL_24.append(winter_1941_1942_2)
station2.append(winter_1941_1942_2)

try:
    winter_1941_1942_3 = aa1[3] + by[3]
except:
    winter_1941_1942_3 = None
WL_24.append(winter_1941_1942_3)
station3.append(winter_1941_1942_3)

try:
    winter_1941_1942_4 = aa1[4] + by[4]
except:
    winter_1941_1942_4 = None
WL_24.append(winter_1941_1942_4)
station4.append(winter_1941_1942_4)

try:
    winter_1941_1942_5 = aa1[5] + by[5]
except:
    winter_1941_1942_5 = None
WL_24.append(winter_1941_1942_5)
station5.append(winter_1941_1942_5)

try:
    winter_1941_1942_6 = aa1[6] + by[6]
except:
    winter_1941_1942_6 = None
WL_24.append(winter_1941_1942_6)
station6.append(winter_1941_1942_6)

try:
    winter_1941_1942_7 = aa1[7] + by[7]
except:
    winter_1941_1942_7 = None
WL_24.append(winter_1941_1942_7)
station7.append(winter_1941_1942_7)

try:
    winter_1941_1942_8 = aa1[8] + by[8]
except:
    winter_1941_1942_8 = None
WL_24.append(winter_1941_1942_8)
station8.append(winter_1941_1942_8)

try:
    winter_1941_1942_9 = aa1[9] + by[9]
except:
    winter_1941_1942_9 = None
WL_24.append(winter_1941_1942_9)
station9.append(winter_1941_1942_9)

try:
    winter_1941_1942_10 = aa1[10] + by[10]
except:
    winter_1941_1942_10 = None
WL_24.append(winter_1941_1942_10)
station10.append(winter_1941_1942_10)

try:
    winter_1941_1942_11 = aa1[11] + by[11]
except:
    winter_1941_1942_11 = None
WL_24.append(winter_1941_1942_11)
station11.append(winter_1941_1942_11)

try:
    winter_1941_1942_12 = aa1[12] + by[12]
except:
    winter_1941_1942_12 = None
WL_24.append(winter_1941_1942_12)
station12.append(winter_1941_1942_12)

try:
    winter_1941_1942_13 = aa1[13] + by[13]
except:
    winter_1941_1942_13 = None
WL_24.append(winter_1941_1942_13)
station13.append(winter_1941_1942_13)

try:
    winter_1941_1942_14 = aa1[14] + by[14]
except:
    winter_1941_1942_14 = None
WL_24.append(winter_1941_1942_14)
station14.append(winter_1941_1942_14)

try:
    winter_1941_1942_15 = aa1[15] + by[15]
except:
    winter_1941_1942_15 = None
WL_24.append(winter_1941_1942_15)
station15.append(winter_1941_1942_15)

try:
    winter_1941_1942_16 = aa1[16] + by[16]
except:
    winter_1941_1942_16 = None
WL_24.append(winter_1941_1942_16)
station16.append(winter_1941_1942_16)

try:
    winter_1941_1942_17 = aa1[17] + by[17]
except:
    winter_1941_1942_17 = None
WL_24.append(winter_1941_1942_17)
station17.append(winter_1941_1942_17)

try:
    winter_1941_1942_18 = aa1[18] + by[18]
except:
    winter_1941_1942_18 = None
WL_24.append(winter_1941_1942_18)
station18.append(winter_1941_1942_18)

try:
    winter_1941_1942_19 = aa1[19] + by[19]
except:
    winter_1941_1942_19 = None
WL_24.append(winter_1941_1942_19)
station19.append(winter_1941_1942_19)

try:
    winter_1941_1942_20 = aa1[20] + by[20]
except:
    winter_1941_1942_20 = None
WL_24.append(winter_1941_1942_20)
station20.append(winter_1941_1942_20)

try:
    winter_1941_1942_21 = aa1[21] + by[21]
except:
    winter_1941_1942_21 = None
WL_24.append(winter_1941_1942_21)
station21.append(winter_1941_1942_21)

try:
    winter_1941_1942_22 = aa1[22] + by[22]
except:
    winter_1941_1942_22 = None
WL_24.append(winter_1941_1942_22)
station22.append(winter_1941_1942_22)

try:
    winter_1941_1942_23 = aa1[23] + by[23]
except:
    winter_1941_1942_23 = None
WL_24.append(winter_1941_1942_23)
station23.append(winter_1941_1942_23)

#last spring freeze values for #1943

bz = []

for rowOfCellObjects in mosheet['EQ2':'EQ25']:
    for cellObj in rowOfCellObjects:
        bz.append(cellObj.value)

#final winter length calculation for 1942-1943 season for all of 24 Missouri stations

WL_25 = [] #all 1942-1943 winter lengths

try:
    winter_1942_1943_0 = ab1[0] + bz[0]
except:
    winter_1942_1943_0 = None
WL_25.append(winter_1942_1943_0)
station0.append(winter_1942_1943_0)

try:
    winter_1942_1943_1 = ab1[1] + bz[1]
except:
    winter_1942_1943_1 = None
WL_25.append(winter_1942_1943_1)
station1.append(winter_1942_1943_1)

try:
    winter_1942_1943_2 = ab1[2] + bz[2]
except:
    winter_1942_1943_2 = None
WL_25.append(winter_1942_1943_2)
station2.append(winter_1942_1943_2)

try:
    winter_1942_1943_3 = ab1[3] + bz[3]
except:
    winter_1942_1943_3 = None
WL_25.append(winter_1942_1943_3)
station3.append(winter_1942_1943_3)

try:
    winter_1942_1943_4 = ab1[4] + bz[4]
except:
    winter_1942_1943_4 = None
WL_25.append(winter_1942_1943_4)
station4.append(winter_1942_1943_4)

try:
    winter_1942_1943_5 = ab1[5] + bz[5]
except:
    winter_1942_1943_5 = None
WL_25.append(winter_1942_1943_5)
station5.append(winter_1942_1943_5)

try:
    winter_1942_1943_6 = ab1[6] + bz[6]
except:
    winter_1942_1943_6 = None
WL_25.append(winter_1942_1943_6)
station6.append(winter_1942_1943_6)

try:
    winter_1942_1943_7 = ab1[7] + bz[7]
except:
    winter_1942_1943_7 = None
WL_25.append(winter_1942_1943_7)
station7.append(winter_1942_1943_7)

try:
    winter_1942_1943_8 = ab1[8] + bz[8]
except:
    winter_1942_1943_8 = None
WL_25.append(winter_1942_1943_8)
station8.append(winter_1942_1943_8)

try:
    winter_1942_1943_9 = ab1[9] + bz[9]
except:
    winter_1942_1943_9 = None
WL_25.append(winter_1942_1943_9)
station9.append(winter_1942_1943_9)

try:
    winter_1942_1943_10 = ab1[10] + bz[10]
except:
    winter_1942_1943_10 = None
WL_25.append(winter_1942_1943_10)
station10.append(winter_1942_1943_10)

try:
    winter_1942_1943_11 = ab1[11] + bz[11]
except:
    winter_1942_1943_11 = None
WL_25.append(winter_1942_1943_11)
station11.append(winter_1942_1943_11)

try:
    winter_1942_1943_12 = ab1[12] + bz[12]
except:
    winter_1942_1943_12 = None
WL_25.append(winter_1942_1943_12)
station12.append(winter_1942_1943_12)

try:
    winter_1942_1943_13 = ab1[13] + bz[13]
except:
    winter_1942_1943_13 = None
WL_25.append(winter_1942_1943_13)
station13.append(winter_1942_1943_13)

try:
    winter_1942_1943_14 = ab1[14] + bz[14]
except:
    winter_1942_1943_14 = None
WL_25.append(winter_1942_1943_14)
station14.append(winter_1942_1943_14)

try:
    winter_1942_1943_15 = ab1[15] + bz[15]
except:
    winter_1942_1943_15 = None
WL_25.append(winter_1942_1943_15)
station15.append(winter_1942_1943_15)

try:
    winter_1942_1943_16 = ab1[16] + bz[16]
except:
    winter_1942_1943_16 = None
WL_25.append(winter_1942_1943_16)
station16.append(winter_1942_1943_16)

try:
    winter_1942_1943_17 = ab1[17] + bz[17]
except:
    winter_1942_1943_17 = None
WL_25.append(winter_1942_1943_17)
station17.append(winter_1942_1943_17)

try:
    winter_1942_1943_18 = ab1[18] + bz[18]
except:
    winter_1942_1943_18 = None
WL_25.append(winter_1942_1943_18)
station18.append(winter_1942_1943_18)

try:
    winter_1942_1943_19 = ab1[19] + bz[19]
except:
    winter_1942_1943_19 = None
WL_25.append(winter_1942_1943_19)
station19.append(winter_1942_1943_19)

try:
    winter_1942_1943_20 = ab1[20] + bz[20]
except:
    winter_1942_1943_20 = None
WL_25.append(winter_1942_1943_20)
station20.append(winter_1942_1943_20)

try:
    winter_1942_1943_21 = ab1[21] + bz[21]
except:
    winter_1942_1943_21 = None
WL_25.append(winter_1942_1943_21)
station21.append(winter_1942_1943_21)

try:
    winter_1942_1943_22 = ab1[22] + bz[22]
except:
    winter_1942_1943_22 = None
WL_25.append(winter_1942_1943_22)
station22.append(winter_1942_1943_22)

try:
    winter_1942_1943_23 = ab1[23] + bz[23]
except:
    winter_1942_1943_23 = None
WL_25.append(winter_1942_1943_23)
station23.append(winter_1942_1943_23)

#last spring freeze values for #1944

ca = []

for rowOfCellObjects in mosheet['ER2':'ER25']:
    for cellObj in rowOfCellObjects:
        ca.append(cellObj.value)

#final winter length calculation for 1943-1944 season for all of 24 Missouri stations

WL_26 = [] #all 1943-1944 winter lengths

try:
    winter_1943_1944_0 = ac1[0] + ca[0]
except:
    winter_1943_1944_0 = None
WL_26.append(winter_1943_1944_0)
station0.append(winter_1943_1944_0)

try:
    winter_1943_1944_1 = ac1[1] + ca[1]
except:
    winter_1943_1944_1 = None
WL_26.append(winter_1943_1944_1)
station1.append(winter_1943_1944_1)

try:
    winter_1943_1944_2 = ac1[2] + ca[2]
except:
    winter_1943_1944_2 = None
WL_26.append(winter_1943_1944_2)
station2.append(winter_1943_1944_2)

try:
    winter_1943_1944_3 = ac1[3] + ca[3]
except:
    winter_1943_1944_3 = None
WL_26.append(winter_1943_1944_3)
station3.append(winter_1943_1944_3)

try:
    winter_1943_1944_4 = ac1[4] + ca[4]
except:
    winter_1943_1944_4 = None
WL_26.append(winter_1943_1944_4)
station4.append(winter_1943_1944_4)

try:
    winter_1943_1944_5 = ac1[5] + ca[5]
except:
    winter_1943_1944_5 = None
WL_26.append(winter_1943_1944_5)
station5.append(winter_1943_1944_5)

try:
    winter_1943_1944_6 = ac1[6] + ca[6]
except:
    winter_1943_1944_6 = None
WL_26.append(winter_1943_1944_6)
station6.append(winter_1943_1944_6)

try:
    winter_1943_1944_7 = ac1[7] + ca[7]
except:
    winter_1943_1944_7 = None
WL_26.append(winter_1943_1944_7)
station7.append(winter_1943_1944_7)

try:
    winter_1943_1944_8 = ac1[8] + ca[8]
except:
    winter_1943_1944_8 = None
WL_26.append(winter_1943_1944_8)
station8.append(winter_1943_1944_8)

try:
    winter_1943_1944_9 = ac1[9] + ca[9]
except:
    winter_1943_1944_9 = None
WL_26.append(winter_1943_1944_9)
station9.append(winter_1943_1944_9)

try:
    winter_1943_1944_10 = ac1[10] + ca[10]
except:
    winter_1943_1944_10 = None
WL_26.append(winter_1943_1944_10)
station10.append(winter_1943_1944_10)

try:
    winter_1943_1944_11 = ac1[11] + ca[11]
except:
    winter_1943_1944_11 = None
WL_26.append(winter_1943_1944_11)
station11.append(winter_1943_1944_11)

try:
    winter_1943_1944_12 = ac1[12] + ca[12]
except:
    winter_1943_1944_12 = None
WL_26.append(winter_1943_1944_12)
station12.append(winter_1943_1944_12)

try:
    winter_1943_1944_13 = ac1[13] + ca[13]
except:
    winter_1943_1944_13 = None
WL_26.append(winter_1943_1944_13)
station13.append(winter_1943_1944_13)

try:
    winter_1943_1944_14 = ac1[14] + ca[14]
except:
    winter_1943_1944_14 = None
WL_26.append(winter_1943_1944_14)
station14.append(winter_1943_1944_14)

try:
    winter_1943_1944_15 = ac1[15] + ca[15]
except:
    winter_1943_1944_15 = None
WL_26.append(winter_1943_1944_15)
station15.append(winter_1943_1944_15)

try:
    winter_1943_1944_16 = ac1[16] + ca[16]
except:
    winter_1943_1944_16 = None
WL_26.append(winter_1943_1944_16)
station16.append(winter_1943_1944_16)

try:
    winter_1943_1944_17 = ac1[17] + ca[17]
except:
    winter_1943_1944_17 = None
WL_26.append(winter_1943_1944_17)
station17.append(winter_1943_1944_17)

try:
    winter_1943_1944_18 = ac1[18] + ca[18]
except:
    winter_1943_1944_18 = None
WL_26.append(winter_1943_1944_18)
station18.append(winter_1943_1944_18)

try:
    winter_1943_1944_19 = ac1[19] + ca[19]
except:
    winter_1943_1944_19 = None
WL_26.append(winter_1943_1944_19)
station19.append(winter_1943_1944_19)

try:
    winter_1943_1944_20 = ac1[20] + ca[20]
except:
    winter_1943_1944_20 = None
WL_26.append(winter_1943_1944_20)
station20.append(winter_1943_1944_20)

try:
    winter_1943_1944_21 = ac1[21] + ca[21]
except:
    winter_1943_1944_21 = None
WL_26.append(winter_1943_1944_21)
station21.append(winter_1943_1944_21)

try:
    winter_1943_1944_22 = ac1[22] + ca[22]
except:
    winter_1943_1944_22 = None
WL_26.append(winter_1943_1944_22)
station22.append(winter_1943_1944_22)

try:
    winter_1943_1944_23 = ac1[23] + ca[23]
except:
    winter_1943_1944_23 = None
WL_26.append(winter_1943_1944_23)
station23.append(winter_1943_1944_23)

#last spring freeze values for #1945

cb = []

for rowOfCellObjects in mosheet['ES2':'ES25']:
    for cellObj in rowOfCellObjects:
        cb.append(cellObj.value)

#final winter length cblculation for 1944-1945 season for all of 24 Missouri stations

WL_27 = [] #all 1944-1945 winter lengths

try:
    winter_1944_1945_0 = ad1[0] + cb[0]
except:
    winter_1944_1945_0 = None
WL_27.append(winter_1944_1945_0)
station0.append(winter_1944_1945_0)

try:
    winter_1944_1945_1 = ad1[1] + cb[1]
except:
    winter_1944_1945_1 = None
WL_27.append(winter_1944_1945_1)
station1.append(winter_1944_1945_1)

try:
    winter_1944_1945_2 = ad1[2] + cb[2]
except:
    winter_1944_1945_2 = None
WL_27.append(winter_1944_1945_2)
station2.append(winter_1944_1945_2)

try:
    winter_1944_1945_3 = ad1[3] + cb[3]
except:
    winter_1944_1945_3 = None
WL_27.append(winter_1944_1945_3)
station3.append(winter_1944_1945_3)

try:
    winter_1944_1945_4 = ad1[4] + cb[4]
except:
    winter_1944_1945_4 = None
WL_27.append(winter_1944_1945_4)
station4.append(winter_1944_1945_4)

try:
    winter_1944_1945_5 = ad1[5] + cb[5]
except:
    winter_1944_1945_5 = None
WL_27.append(winter_1944_1945_5)
station5.append(winter_1944_1945_5)

try:
    winter_1944_1945_6 = ad1[6] + cb[6]
except:
    winter_1944_1945_6 = None
WL_27.append(winter_1944_1945_6)
station6.append(winter_1944_1945_6)

try:
    winter_1944_1945_7 = ad1[7] + cb[7]
except:
    winter_1944_1945_7 = None
WL_27.append(winter_1944_1945_7)
station7.append(winter_1944_1945_7)

try:
    winter_1944_1945_8 = ad1[8] + cb[8]
except:
    winter_1944_1945_8 = None
WL_27.append(winter_1944_1945_8)
station8.append(winter_1944_1945_8)

try:
    winter_1944_1945_9 = ad1[9] + cb[9]
except:
    winter_1944_1945_9 = None
WL_27.append(winter_1944_1945_9)
station9.append(winter_1944_1945_9)

try:
    winter_1944_1945_10 = ad1[10] + cb[10]
except:
    winter_1944_1945_10 = None
WL_27.append(winter_1944_1945_10)
station10.append(winter_1944_1945_10)

try:
    winter_1944_1945_11 = ad1[11] + cb[11]
except:
    winter_1944_1945_11 = None
WL_27.append(winter_1944_1945_11)
station11.append(winter_1944_1945_11)

try:
    winter_1944_1945_12 = ad1[12] + cb[12]
except:
    winter_1944_1945_12 = None
WL_27.append(winter_1944_1945_12)
station12.append(winter_1944_1945_12)

try:
    winter_1944_1945_13 = ad1[13] + cb[13]
except:
    winter_1944_1945_13 = None
WL_27.append(winter_1944_1945_13)
station13.append(winter_1944_1945_13)

try:
    winter_1944_1945_14 = ad1[14] + cb[14]
except:
    winter_1944_1945_14 = None
WL_27.append(winter_1944_1945_14)
station14.append(winter_1944_1945_14)

try:
    winter_1944_1945_15 = ad1[15] + cb[15]
except:
    winter_1944_1945_15 = None
WL_27.append(winter_1944_1945_15)
station15.append(winter_1944_1945_15)

try:
    winter_1944_1945_16 = ad1[16] + cb[16]
except:
    winter_1944_1945_16 = None
WL_27.append(winter_1944_1945_16)
station16.append(winter_1944_1945_16)

try:
    winter_1944_1945_17 = ad1[17] + cb[17]
except:
    winter_1944_1945_17 = None
WL_27.append(winter_1944_1945_17)
station17.append(winter_1944_1945_17)

try:
    winter_1944_1945_18 = ad1[18] + cb[18]
except:
    winter_1944_1945_18 = None
WL_27.append(winter_1944_1945_18)
station18.append(winter_1944_1945_18)

try:
    winter_1944_1945_19 = ad1[19] + cb[19]
except:
    winter_1944_1945_19 = None
WL_27.append(winter_1944_1945_19)
station19.append(winter_1944_1945_19)

try:
    winter_1944_1945_20 = ad1[20] + cb[20]
except:
    winter_1944_1945_20 = None
WL_27.append(winter_1944_1945_20)
station20.append(winter_1944_1945_20)

try:
    winter_1944_1945_21 = ad1[21] + cb[21]
except:
    winter_1944_1945_21 = None
WL_27.append(winter_1944_1945_21)
station21.append(winter_1944_1945_21)

try:
    winter_1944_1945_22 = ad1[22] + cb[22]
except:
    winter_1944_1945_22 = None
WL_27.append(winter_1944_1945_22)
station22.append(winter_1944_1945_22)

try:
    winter_1944_1945_23 = ad1[23] + cb[23]
except:
    winter_1944_1945_23 = None
WL_27.append(winter_1944_1945_23)
station23.append(winter_1944_1945_23)

#last spring freeze values for #1946

cc = []

for rowOfCellObjects in mosheet['ET2':'ET25']:
    for cellObj in rowOfCellObjects:
        cc.append(cellObj.value)

#final winter length cclculation for 1945-1946 season for all of 24 Missouri stations

WL_28 = [] #all 1945-1946 winter lengths

try:
    winter_1945_1946_0 = ae1[0] + cc[0]
except:
    winter_1945_1946_0 = None
WL_28.append(winter_1945_1946_0)
station0.append(winter_1945_1946_0)

try:
    winter_1945_1946_1 = ae1[1] + cc[1]
except:
    winter_1945_1946_1 = None
WL_28.append(winter_1945_1946_1)
station1.append(winter_1945_1946_1)

try:
    winter_1945_1946_2 = ae1[2] + cc[2]
except:
    winter_1945_1946_2 = None
WL_28.append(winter_1945_1946_2)
station2.append(winter_1945_1946_2)

try:
    winter_1945_1946_3 = ae1[3] + cc[3]
except:
    winter_1945_1946_3 = None
WL_28.append(winter_1945_1946_3)
station3.append(winter_1945_1946_3)

try:
    winter_1945_1946_4 = ae1[4] + cc[4]
except:
    winter_1945_1946_4 = None
WL_28.append(winter_1945_1946_4)
station4.append(winter_1945_1946_4)

try:
    winter_1945_1946_5 = ae1[5] + cc[5]
except:
    winter_1945_1946_5 = None
WL_28.append(winter_1945_1946_5)
station5.append(winter_1945_1946_5)

try:
    winter_1945_1946_6 = ae1[6] + cc[6]
except:
    winter_1945_1946_6 = None
WL_28.append(winter_1945_1946_6)
station6.append(winter_1945_1946_6)

try:
    winter_1945_1946_7 = ae1[7] + cc[7]
except:
    winter_1945_1946_7 = None
WL_28.append(winter_1945_1946_7)
station7.append(winter_1945_1946_7)

try:
    winter_1945_1946_8 = ae1[8] + cc[8]
except:
    winter_1945_1946_8 = None
WL_28.append(winter_1945_1946_8)
station8.append(winter_1945_1946_8)

try:
    winter_1945_1946_9 = ae1[9] + cc[9]
except:
    winter_1945_1946_9 = None
WL_28.append(winter_1945_1946_9)
station9.append(winter_1945_1946_9)

try:
    winter_1945_1946_10 = ae1[10] + cc[10]
except:
    winter_1945_1946_10 = None
WL_28.append(winter_1945_1946_10)
station10.append(winter_1945_1946_10)

try:
    winter_1945_1946_11 = ae1[11] + cc[11]
except:
    winter_1945_1946_11 = None
WL_28.append(winter_1945_1946_11)
station11.append(winter_1945_1946_11)

try:
    winter_1945_1946_12 = ae1[12] + cc[12]
except:
    winter_1945_1946_12 = None
WL_28.append(winter_1945_1946_12)
station12.append(winter_1945_1946_12)

try:
    winter_1945_1946_13 = ae1[13] + cc[13]
except:
    winter_1945_1946_13 = None
WL_28.append(winter_1945_1946_13)
station13.append(winter_1945_1946_13)

try:
    winter_1945_1946_14 = ae1[14] + cc[14]
except:
    winter_1945_1946_14 = None
WL_28.append(winter_1945_1946_14)
station14.append(winter_1945_1946_14)

try:
    winter_1945_1946_15 = ae1[15] + cc[15]
except:
    winter_1945_1946_15 = None
WL_28.append(winter_1945_1946_15)
station15.append(winter_1945_1946_15)

try:
    winter_1945_1946_16 = ae1[16] + cc[16]
except:
    winter_1945_1946_16 = None
WL_28.append(winter_1945_1946_16)
station16.append(winter_1945_1946_16)

try:
    winter_1945_1946_17 = ae1[17] + cc[17]
except:
    winter_1945_1946_17 = None
WL_28.append(winter_1945_1946_17)
station17.append(winter_1945_1946_17)

try:
    winter_1945_1946_18 = ae1[18] + cc[18]
except:
    winter_1945_1946_18 = None
WL_28.append(winter_1945_1946_18)
station18.append(winter_1945_1946_18)

try:
    winter_1945_1946_19 = ae1[19] + cc[19]
except:
    winter_1945_1946_19 = None
WL_28.append(winter_1945_1946_19)
station19.append(winter_1945_1946_19)

try:
    winter_1945_1946_20 = ae1[20] + cc[20]
except:
    winter_1945_1946_20 = None
WL_28.append(winter_1945_1946_20)
station20.append(winter_1945_1946_20)

try:
    winter_1945_1946_21 = ae1[21] + cc[21]
except:
    winter_1945_1946_21 = None
WL_28.append(winter_1945_1946_21)
station21.append(winter_1945_1946_21)

try:
    winter_1945_1946_22 = ae1[22] + cc[22]
except:
    winter_1945_1946_22 = None
WL_28.append(winter_1945_1946_22)
station22.append(winter_1945_1946_22)

try:
    winter_1945_1946_23 = ae1[23] + cc[23]
except:
    winter_1945_1946_23 = None
WL_28.append(winter_1945_1946_23)
station23.append(winter_1945_1946_23)

#last spring freeze values for #1947

cd = []

for rowOfCellObjects in mosheet['EU2':'EU25']:
    for cellObj in rowOfCellObjects:
        cd.append(cellObj.value)

#final winter length cdlculation for 1946-1947 season for all of 24 Missouri stations

WL_29 = [] #all 1946-1947 winter lengths

try:
    winter_1946_1947_0 = af1[0] + cd[0]
except:
    winter_1946_1947_0 = None
WL_29.append(winter_1946_1947_0)
station0.append(winter_1946_1947_0)

try:
    winter_1946_1947_1 = af1[1] + cd[1]
except:
    winter_1946_1947_1 = None
WL_29.append(winter_1946_1947_1)
station1.append(winter_1946_1947_1)

try:
    winter_1946_1947_2 = af1[2] + cd[2]
except:
    winter_1946_1947_2 = None
WL_29.append(winter_1946_1947_2)
station2.append(winter_1946_1947_2)

try:
    winter_1946_1947_3 = af1[3] + cd[3]
except:
    winter_1946_1947_3 = None
WL_29.append(winter_1946_1947_3)
station3.append(winter_1946_1947_3)

try:
    winter_1946_1947_4 = af1[4] + cd[4]
except:
    winter_1946_1947_4 = None
WL_29.append(winter_1946_1947_4)
station4.append(winter_1946_1947_4)

try:
    winter_1946_1947_5 = af1[5] + cd[5]
except:
    winter_1946_1947_5 = None
WL_29.append(winter_1946_1947_5)
station5.append(winter_1946_1947_5)

try:
    winter_1946_1947_6 = af1[6] + cd[6]
except:
    winter_1946_1947_6 = None
WL_29.append(winter_1946_1947_6)
station6.append(winter_1946_1947_6)

try:
    winter_1946_1947_7 = af1[7] + cd[7]
except:
    winter_1946_1947_7 = None
WL_29.append(winter_1946_1947_7)
station7.append(winter_1946_1947_7)

try:
    winter_1946_1947_8 = af1[8] + cd[8]
except:
    winter_1946_1947_8 = None
WL_29.append(winter_1946_1947_8)
station8.append(winter_1946_1947_8)

try:
    winter_1946_1947_9 = af1[9] + cd[9]
except:
    winter_1946_1947_9 = None
WL_29.append(winter_1946_1947_9)
station9.append(winter_1946_1947_9)

try:
    winter_1946_1947_10 = af1[10] + cd[10]
except:
    winter_1946_1947_10 = None
WL_29.append(winter_1946_1947_10)
station10.append(winter_1946_1947_10)

try:
    winter_1946_1947_11 = af1[11] + cd[11]
except:
    winter_1946_1947_11 = None
WL_29.append(winter_1946_1947_11)
station11.append(winter_1946_1947_11)

try:
    winter_1946_1947_12 = af1[12] + cd[12]
except:
    winter_1946_1947_12 = None
WL_29.append(winter_1946_1947_12)
station12.append(winter_1946_1947_12)

try:
    winter_1946_1947_13 = af1[13] + cd[13]
except:
    winter_1946_1947_13 = None
WL_29.append(winter_1946_1947_13)
station13.append(winter_1946_1947_13)

try:
    winter_1946_1947_14 = af1[14] + cd[14]
except:
    winter_1946_1947_14 = None
WL_29.append(winter_1946_1947_14)
station14.append(winter_1946_1947_14)

try:
    winter_1946_1947_15 = af1[15] + cd[15]
except:
    winter_1946_1947_15 = None
WL_29.append(winter_1946_1947_15)
station15.append(winter_1946_1947_15)

try:
    winter_1946_1947_16 = af1[16] + cd[16]
except:
    winter_1946_1947_16 = None
WL_29.append(winter_1946_1947_16)
station16.append(winter_1946_1947_16)

try:
    winter_1946_1947_17 = af1[17] + cd[17]
except:
    winter_1946_1947_17 = None
WL_29.append(winter_1946_1947_17)
station17.append(winter_1946_1947_17)

try:
    winter_1946_1947_18 = af1[18] + cd[18]
except:
    winter_1946_1947_18 = None
WL_29.append(winter_1946_1947_18)
station18.append(winter_1946_1947_18)

try:
    winter_1946_1947_19 = af1[19] + cd[19]
except:
    winter_1946_1947_19 = None
WL_29.append(winter_1946_1947_19)
station19.append(winter_1946_1947_19)

try:
    winter_1946_1947_20 = af1[20] + cd[20]
except:
    winter_1946_1947_20 = None
WL_29.append(winter_1946_1947_20)
station20.append(winter_1946_1947_20)

try:
    winter_1946_1947_21 = af1[21] + cd[21]
except:
    winter_1946_1947_21 = None
WL_29.append(winter_1946_1947_21)
station21.append(winter_1946_1947_21)

try:
    winter_1946_1947_22 = af1[22] + cd[22]
except:
    winter_1946_1947_22 = None
WL_29.append(winter_1946_1947_22)
station22.append(winter_1946_1947_22)

try:
    winter_1946_1947_23 = af1[23] + cd[23]
except:
    winter_1946_1947_23 = None
WL_29.append(winter_1946_1947_23)
station23.append(winter_1946_1947_23)

#last spring freeze values for #1948

ce = []

for rowOfCellObjects in mosheet['EV2':'EV25']:
    for cellObj in rowOfCellObjects:
        ce.append(cellObj.value)

#final winter length calculation for 1946-1947 season for all of 24 Missouri stations

WL_30 = [] #all 1946-1947 winter lengths

try:
    winter_1947_1948_0 = cr1[0] + ce[0]
except:
    winter_1947_1948_0 = None
WL_30.append(winter_1947_1948_0)
station0.append(winter_1947_1948_0)

try:
    winter_1947_1948_1 = cr1[1] + ce[1]
except:
    winter_1947_1948_1 = None
WL_30.append(winter_1947_1948_1)
station1.append(winter_1947_1948_1)

try:
    winter_1947_1948_2 = cr1[2] + ce[2]
except:
    winter_1947_1948_2 = None
WL_30.append(winter_1947_1948_2)
station2.append(winter_1947_1948_2)

try:
    winter_1947_1948_3 = cr1[3] + ce[3]
except:
    winter_1947_1948_3 = None
WL_30.append(winter_1947_1948_3)
station3.append(winter_1947_1948_3)

try:
    winter_1947_1948_4 = cr1[4] + ce[4]
except:
    winter_1947_1948_4 = None
WL_30.append(winter_1947_1948_4)
station4.append(winter_1947_1948_4)

try:
    winter_1947_1948_5 = cr1[5] + ce[5]
except:
    winter_1947_1948_5 = None
WL_30.append(winter_1947_1948_5)
station5.append(winter_1947_1948_5)

try:
    winter_1947_1948_6 = cr1[6] + ce[6]
except:
    winter_1947_1948_6 = None
WL_30.append(winter_1947_1948_6)
station6.append(winter_1947_1948_6)

try:
    winter_1947_1948_7 = cr1[7] + ce[7]
except:
    winter_1947_1948_7 = None
WL_30.append(winter_1947_1948_7)
station7.append(winter_1947_1948_7)

try:
    winter_1947_1948_8 = cr1[8] + ce[8]
except:
    winter_1947_1948_8 = None
WL_30.append(winter_1947_1948_8)
station8.append(winter_1947_1948_8)

try:
    winter_1947_1948_9 = cr1[9] + ce[9]
except:
    winter_1947_1948_9 = None
WL_30.append(winter_1947_1948_9)
station9.append(winter_1947_1948_9)

try:
    winter_1947_1948_10 = cr1[10] + ce[10]
except:
    winter_1947_1948_10 = None
WL_30.append(winter_1947_1948_10)
station10.append(winter_1947_1948_10)

try:
    winter_1947_1948_11 = cr1[11] + ce[11]
except:
    winter_1947_1948_11 = None
WL_30.append(winter_1947_1948_11)
station11.append(winter_1947_1948_11)

try:
    winter_1947_1948_12 = cr1[12] + ce[12]
except:
    winter_1947_1948_12 = None
WL_30.append(winter_1947_1948_12)
station12.append(winter_1947_1948_12)

try:
    winter_1947_1948_13 = cr1[13] + ce[13]
except:
    winter_1947_1948_13 = None
WL_30.append(winter_1947_1948_13)
station13.append(winter_1947_1948_13)

try:
    winter_1947_1948_14 = cr1[14] + ce[14]
except:
    winter_1947_1948_14 = None
WL_30.append(winter_1947_1948_14)
station14.append(winter_1947_1948_14)

try:
    winter_1947_1948_15 = cr1[15] + ce[15]
except:
    winter_1947_1948_15 = None
WL_30.append(winter_1947_1948_15)
station15.append(winter_1947_1948_15)

try:
    winter_1947_1948_16 = cr1[16] + ce[16]
except:
    winter_1947_1948_16 = None
WL_30.append(winter_1947_1948_16)
station16.append(winter_1947_1948_16)

try:
    winter_1947_1948_17 = cr1[17] + ce[17]
except:
    winter_1947_1948_17 = None
WL_30.append(winter_1947_1948_17)
station17.append(winter_1947_1948_17)

try:
    winter_1947_1948_18 = cr1[18] + ce[18]
except:
    winter_1947_1948_18 = None
WL_30.append(winter_1947_1948_18)
station18.append(winter_1947_1948_18)

try:
    winter_1947_1948_19 = cr1[19] + ce[19]
except:
    winter_1947_1948_19 = None
WL_30.append(winter_1947_1948_19)
station19.append(winter_1947_1948_19)

try:
    winter_1947_1948_20 = cr1[20] + ce[20]
except:
    winter_1947_1948_20 = None
WL_30.append(winter_1947_1948_20)
station20.append(winter_1947_1948_20)

try:
    winter_1947_1948_21 = cr1[21] + ce[21]
except:
    winter_1947_1948_21 = None
WL_30.append(winter_1947_1948_21)
station21.append(winter_1947_1948_21)

try:
    winter_1947_1948_22 = cr1[22] + ce[22]
except:
    winter_1947_1948_22 = None
WL_30.append(winter_1947_1948_22)
station22.append(winter_1947_1948_22)

try:
    winter_1947_1948_23 = cr1[23] + ce[23]
except:
    winter_1947_1948_23 = None
WL_30.append(winter_1947_1948_23)
station23.append(winter_1947_1948_23)

# finished with first 30 years, yay!

# now time to calculate the last 30 years in this dataset. using same methods as for first 30.

# calculating fall part of winter with first fall freeze dates

#1985

#getting cell values out of each column; each column is a year

ah = []
for rowOfCellObjects in mosheet['CB2':'CB25']:
    for cellObj in rowOfCellObjects:
        ah.append(cellObj.value)

#making list of fall part of winter lengths from each column/year for later use in final winter length calculations
ah1 = []
for i in ah:
    try:
        x = 365 - (i-1)
    except:
    	x = None
    ah1.append(x)

#1986

ai = []
for rowOfCellObjects in mosheet['CC2':'CC25']:
    for cellObj in rowOfCellObjects:
        ai.append(cellObj.value)

ai1 = []

for i in ai:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ai1.append(x)

#1987

aj = []
for rowOfCellObjects in mosheet['CD2':'CD25']:
    for cellObj in rowOfCellObjects:
        aj.append(cellObj.value)

aj1 = []

for i in aj:
    try:
        x = 365 - (i-1)
    except:
        x = None
    aj1.append(x)

#1988

ak = []
for rowOfCellObjects in mosheet['CE2':'CE25']:
    for cellObj in rowOfCellObjects:
        ak.append(cellObj.value)

ak1 = []

for i in ak:
    try:
        x = 366 - (i-1)
    except:
        x = None
    ak1.append(x)

#1989

al = []
for rowOfCellObjects in mosheet['CF2':'CF25']:
    for cellObj in rowOfCellObjects:
        al.append(cellObj.value)

al1 = []

for i in al:
    try:
        x = 365 - (i-1)
    except:
        x = None
    al1.append(x)

#1990

am = []
for rowOfCellObjects in mosheet['CG2':'CG25']:
    for cellObj in rowOfCellObjects:
        am.append(cellObj.value)

am1 = []

for i in am:
    try:
        x = 365 - (i-1)
    except:
        x = None
    am1.append(x)

#1991

an = []
for rowOfCellObjects in mosheet['CH2':'CH25']:
    for cellObj in rowOfCellObjects:
        an.append(cellObj.value)

an1 = []

for i in an:
    try:
        x = 365 - (i-1)
    except:
        x = None
    an1.append(x)

#1992

ao = []
for rowOfCellObjects in mosheet['CI2':'CI25']:
    for cellObj in rowOfCellObjects:
        ao.append(cellObj.value)

ao1 = []

for i in ao:
    try:
        x = 366 - (i-1)
    except:
        x = None
    ao1.append(x)

#1993

ap = []
for rowOfCellObjects in mosheet['CJ2':'CJ25']:
    for cellObj in rowOfCellObjects:
        ap.append(cellObj.value)

ap1 = []

for i in ap:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ap1.append(x)

#1994

aq = []
for rowOfCellObjects in mosheet['CK2':'CK25']:
    for cellObj in rowOfCellObjects:
        aq.append(cellObj.value)

aq1 = []

for i in aq:
    try:
        x = 365 - (i-1)
    except:
        x = None
    aq1.append(x)

#1995

ar = []
for rowOfCellObjects in mosheet['CL2':'CL25']:
    for cellObj in rowOfCellObjects:
        ar.append(cellObj.value)

ar1 = []

for i in ar:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ar1.append(x)

#1996
#skipping as for variable because its a keyword

at = []
for rowOfCellObjects in mosheet['CM2':'CM25']:
    for cellObj in rowOfCellObjects:
        at.append(cellObj.value)

at1 = []

for i in at:
    try:
        x = 366 - (i-1)
    except:
        x = None
    at1.append(x)

#1997

au = []
for rowOfCellObjects in mosheet['CN2':'CN25']:
    for cellObj in rowOfCellObjects:
        au.append(cellObj.value)

au1 = []

for i in au:
    try:
        x = 365 - (i-1)
    except:
        x = None
    au1.append(x)

#1998

av = []
for rowOfCellObjects in mosheet['CO2':'CO25']:
    for cellObj in rowOfCellObjects:
        av.append(cellObj.value)

av1 = []

for i in av:
    try:
        x = 365 - (i-1)
    except:
        x = None
    av1.append(x)

#1999

aw = []
for rowOfCellObjects in mosheet['CP2':'CP25']:
    for cellObj in rowOfCellObjects:
        aw.append(cellObj.value)

aw1 = []

for i in aw:
    try:
        x = 365 - (i-1)
    except:
        x = None
    aw1.append(x)

#2000

ax = []
for rowOfCellObjects in mosheet['CQ2':'CQ25']:
    for cellObj in rowOfCellObjects:
        ax.append(cellObj.value)

ax1 = []

for i in ax:
    try:
        x = 366 - (i-1)
    except:
        x = None
    ax1.append(x)

#2001

ay = []
for rowOfCellObjects in mosheet['CR2':'CR25']:
    for cellObj in rowOfCellObjects:
        ay.append(cellObj.value)

ay1 = []

for i in ay:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ay1.append(x)

#2002

az = []
for rowOfCellObjects in mosheet['CS2':'CS25']:
    for cellObj in rowOfCellObjects:
        az.append(cellObj.value)

az1 = []

for i in az:
    try:
        x = 365 - (i-1)
    except:
        x = None
    az1.append(x)

#2003

cf = []
for rowOfCellObjects in mosheet['CT2':'CT25']:
    for cellObj in rowOfCellObjects:
        cf.append(cellObj.value)

cf1 = []

for i in cf:
    try:
        x = 365 - (i-1)
    except:
        x = None
    cf1.append(x)

#2004

cg = []
for rowOfCellObjects in mosheet['CU2':'CU25']:
    for cellObj in rowOfCellObjects:
        cg.append(cellObj.value)

cg1 = []

for i in cg:
    try:
        x = 366 - (i-1)
    except:
        x = None
    cg1.append(x)

#2005

ch = []
for rowOfCellObjects in mosheet['CV2':'CV25']:
    for cellObj in rowOfCellObjects:
        ch.append(cellObj.value)

ch1 = []

for i in ch:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ch1.append(x)

#2006

ci = []
for rowOfCellObjects in mosheet['CW2':'CW25']:
    for cellObj in rowOfCellObjects:
        ci.append(cellObj.value)

ci1 = []

for i in ci:
    try:
        x = 365 - (i-1)
    except:
        x = None
    ci1.append(x)

#2007


cj = []
for rowOfCellObjects in mosheet['CX2':'CX25']:
    for cellObj in rowOfCellObjects:
        cj.append(cellObj.value)

cj1 = []

for i in cj:
    try:
        x = 365 - (i-1)
    except:
        x = None
    cj1.append(x)

#2008

ck = []
for rowOfCellObjects in mosheet['CY2':'CY25']:
    for cellObj in rowOfCellObjects:
        ck.append(cellObj.value)

ck1 = []

for i in ck:
    try:
        x = 366 - (i-1)
    except:
        x = None
    ck1.append(x)

#2009

cl = []
for rowOfCellObjects in mosheet['CZ2':'CZ25']:
    for cellObj in rowOfCellObjects:
        cl.append(cellObj.value)

cl1 = []

for i in cl:
    try:
        x = 365 - (i-1)
    except:
        x = None
    cl1.append(x)

#2010

cm = []
for rowOfCellObjects in mosheet['DA2':'DA25']:
    for cellObj in rowOfCellObjects:
        cm.append(cellObj.value)

cm1 = []

for i in cm:
    try:
        x = 365 - (i-1)
    except:
        x = None
    cm1.append(x)

#2011

cn = []
for rowOfCellObjects in mosheet['DB2':'DB25']:
    for cellObj in rowOfCellObjects:
        cn.append(cellObj.value)

cn1 = []

for i in cn:
    try:
        x = 365 - (i-1)
    except:
        x = None
    cn1.append(x)

#2012

co = []
for rowOfCellObjects in mosheet['DC2':'DC25']:
    for cellObj in rowOfCellObjects:
        co.append(cellObj.value)

co1 = []

for i in co:
    try:
        x = 366 - (i-1)
    except:
        x = None
    co1.append(x)

#2013

cp = []
for rowOfCellObjects in mosheet['DD2':'DD25']:
    for cellObj in rowOfCellObjects:
        cp.append(cellObj.value)

cp1 = []

for i in cp:
    try:
        x = 365 - (i-1)
    except:
        x = None
    cp1.append(x)

#2014

cq = []
for rowOfCellObjects in mosheet['DE2':'DE25']:
    for cellObj in rowOfCellObjects:
        cq.append(cellObj.value)

cq1 = []

for i in cq:
    try:
        x = 365 - (i-1)
    except:
        x = None
    cq1.append(x)

#2015

cr = []
for rowOfCellObjects in mosheet['DF2':'DF25']:
    for cellObj in rowOfCellObjects:
        cr.append(cellObj.value)

cr1 = []

for i in cr:
    try:
        x = 365 - (i-1)
    except:
        x = None
    cr1.append(x)

# calculating spring part of winter length values for last 30 years in dataset, then
# calculating winter length values for the last 30 years in dataset

#last spring freeze values for #1986

cs = []

for rowOfCellObjects in mosheet['GH2':'GH25']:
    for cellObj in rowOfCellObjects:
        cs.append(cellObj.value)

#final winter length calculation for 1985-1986 season for all of 24 Missouri stations

WL_31 = [] #all 1985-1986 winter lengths

try:
    winter_1985_1986_0 = ah1[0] + cs[0]
except:
    winter_1985_1986_0 = None
WL_31.append(winter_1985_1986_0)
station0.append(winter_1985_1986_0)

try:
    winter_1985_1986_1 = ah1[1] + cs[1]
except:
    winter_1985_1986_1 = None
WL_31.append(winter_1985_1986_1)
station1.append(winter_1985_1986_1)

try:
    winter_1985_1986_2 = ah1[2] + cs[2]
except:
    winter_1985_1986_2 = None
WL_31.append(winter_1985_1986_2)
station2.append(winter_1985_1986_2)

try:
    winter_1985_1986_3 = ah1[3] + cs[3]
except:
    winter_1985_1986_3 = None
WL_31.append(winter_1985_1986_3)
station3.append(winter_1985_1986_3)

try:
    winter_1985_1986_4 = ah1[4] + cs[4]
except:
    winter_1985_1986_4 = None
WL_31.append(winter_1985_1986_4)
station4.append(winter_1985_1986_4)

try:
    winter_1985_1986_5 = ah1[5] + cs[5]
except:
    winter_1985_1986_5 = None
WL_31.append(winter_1985_1986_5)
station5.append(winter_1985_1986_5)

try:
    winter_1985_1986_6 = ah1[6] + cs[6]
except:
    winter_1985_1986_6 = None
WL_31.append(winter_1985_1986_6)
station6.append(winter_1985_1986_6)

try:
    winter_1985_1986_7 = ah1[7] + cs[7]
except:
    winter_1985_1986_7 = None
WL_31.append(winter_1985_1986_7)
station7.append(winter_1985_1986_7)

try:
    winter_1985_1986_8 = ah1[8] + cs[8]
except:
    winter_1985_1986_8 = None
WL_31.append(winter_1985_1986_8)
station8.append(winter_1985_1986_8)

try:
    winter_1985_1986_9 = ah1[9] + cs[9]
except:
    winter_1985_1986_9 = None
WL_31.append(winter_1985_1986_9)
station9.append(winter_1985_1986_9)

try:
    winter_1985_1986_10 = ah1[10] + cs[10]
except:
    winter_1985_1986_10 = None
WL_31.append(winter_1985_1986_10)
station10.append(winter_1985_1986_10)

try:
    winter_1985_1986_11 = ah1[11] + cs[11]
except:
    winter_1985_1986_11 = None
WL_31.append(winter_1985_1986_11)
station11.append(winter_1985_1986_11)

try:
    winter_1985_1986_12 = ah1[12] + cs[12]
except:
    winter_1985_1986_12 = None
WL_31.append(winter_1985_1986_12)
station12.append(winter_1985_1986_12)

try:
    winter_1985_1986_13 = ah1[13] + cs[13]
except:
    winter_1985_1986_13 = None
WL_31.append(winter_1985_1986_13)
station13.append(winter_1985_1986_13)

try:
    winter_1985_1986_14 = ah1[14] + cs[14]
except:
    winter_1985_1986_14 = None
WL_31.append(winter_1985_1986_14)
station14.append(winter_1985_1986_14)

try:
    winter_1985_1986_15 = ah1[15] + cs[15]
except:
    winter_1985_1986_15 = None
WL_31.append(winter_1985_1986_15)
station15.append(winter_1985_1986_15)

try:
    winter_1985_1986_16 = ah1[16] + cs[16]
except:
    winter_1985_1986_16 = None
WL_31.append(winter_1985_1986_16)
station16.append(winter_1985_1986_16)

try:
    winter_1985_1986_17 = ah1[17] + cs[17]
except:
    winter_1985_1986_17 = None
WL_31.append(winter_1985_1986_17)
station17.append(winter_1985_1986_17)

try:
    winter_1985_1986_18 = ah1[18] + cs[18]
except:
    winter_1985_1986_18 = None
WL_31.append(winter_1985_1986_18)
station18.append(winter_1985_1986_18)

try:
    winter_1985_1986_19 = ah1[19] + cs[19]
except:
    winter_1985_1986_19 = None
WL_31.append(winter_1985_1986_19)
station19.append(winter_1985_1986_19)

try:
    winter_1985_1986_20 = ah1[20] + cs[20]
except:
    winter_1985_1986_20 = None
WL_31.append(winter_1985_1986_20)
station20.append(winter_1985_1986_20)

try:
    winter_1985_1986_21 = ah1[21] + cs[21]
except:
    winter_1985_1986_21 = None
WL_31.append(winter_1985_1986_21)
station21.append(winter_1985_1986_21)

try:
    winter_1985_1986_22 = ah1[22] + cs[22]
except:
    winter_1985_1986_22 = None
WL_31.append(winter_1985_1986_22)
station22.append(winter_1985_1986_22)

try:
    winter_1985_1986_23 = ah1[23] + cs[23]
except:
    winter_1985_1986_23 = None
WL_31.append(winter_1985_1986_23)
station23.append(winter_1985_1986_23)

#last spring freeze values for #1987

ct = []

for rowOfCellObjects in mosheet['GI2':'GI25']:
    for cellObj in rowOfCellObjects:
        ct.append(cellObj.value)

#final winter length calculation for 1986-1987 season for all of 24 Missouri stations

WL_32 = [] #all 1986-1987 winter lengths

try:
    winter_1986_1987_0 = ai1[0] + ct[0]
except:
    winter_1986_1987_0 = None
WL_32.append(winter_1986_1987_0)
station0.append(winter_1986_1987_0)

try:
    winter_1986_1987_1 = ai1[1] + ct[1]
except:
    winter_1986_1987_1 = None
WL_32.append(winter_1986_1987_1)
station1.append(winter_1986_1987_1)

try:
    winter_1986_1987_2 = ai1[2] + ct[2]
except:
    winter_1986_1987_2 = None
WL_32.append(winter_1986_1987_2)
station2.append(winter_1986_1987_2)

try:
    winter_1986_1987_3 = ai1[3] + ct[3]
except:
    winter_1986_1987_3 = None
WL_32.append(winter_1986_1987_3)
station3.append(winter_1986_1987_3)

try:
    winter_1986_1987_4 = ai1[4] + ct[4]
except:
    winter_1986_1987_4 = None
WL_32.append(winter_1986_1987_4)
station4.append(winter_1986_1987_4)

try:
    winter_1986_1987_5 = ai1[5] + ct[5]
except:
    winter_1986_1987_5 = None
WL_32.append(winter_1986_1987_5)
station5.append(winter_1986_1987_5)

try:
    winter_1986_1987_6 = ai1[6] + ct[6]
except:
    winter_1986_1987_6 = None
WL_32.append(winter_1986_1987_6)
station6.append(winter_1986_1987_6)

try:
    winter_1986_1987_7 = ai1[7] + ct[7]
except:
    winter_1986_1987_7 = None
WL_32.append(winter_1986_1987_7)
station7.append(winter_1986_1987_7)

try:
    winter_1986_1987_8 = ai1[8] + ct[8]
except:
    winter_1986_1987_8 = None
WL_32.append(winter_1986_1987_8)
station8.append(winter_1986_1987_8)

try:
    winter_1986_1987_9 = ai1[9] + ct[9]
except:
    winter_1986_1987_9 = None
WL_32.append(winter_1986_1987_9)
station9.append(winter_1986_1987_9)

try:
    winter_1986_1987_10 = ai1[10] + ct[10]
except:
    winter_1986_1987_10 = None
WL_32.append(winter_1986_1987_10)
station10.append(winter_1986_1987_10)

try:
    winter_1986_1987_11 = ai1[11] + ct[11]
except:
    winter_1986_1987_11 = None
WL_32.append(winter_1986_1987_11)
station11.append(winter_1986_1987_11)

try:
    winter_1986_1987_12 = ai1[12] + ct[12]
except:
    winter_1986_1987_12 = None
WL_32.append(winter_1986_1987_12)
station12.append(winter_1986_1987_12)

try:
    winter_1986_1987_13 = ai1[13] + ct[13]
except:
    winter_1986_1987_13 = None
WL_32.append(winter_1986_1987_13)
station13.append(winter_1986_1987_13)

try:
    winter_1986_1987_14 = ai1[14] + ct[14]
except:
    winter_1986_1987_14 = None
WL_32.append(winter_1986_1987_14)
station14.append(winter_1986_1987_14)

try:
    winter_1986_1987_15 = ai1[15] + ct[15]
except:
    winter_1986_1987_15 = None
WL_32.append(winter_1986_1987_15)
station15.append(winter_1986_1987_15)

try:
    winter_1986_1987_16 = ai1[16] + ct[16]
except:
    winter_1986_1987_16 = None
WL_32.append(winter_1986_1987_16)
station16.append(winter_1986_1987_16)

try:
    winter_1986_1987_17 = ai1[17] + ct[17]
except:
    winter_1986_1987_17 = None
WL_32.append(winter_1986_1987_17)
station17.append(winter_1986_1987_17)

try:
    winter_1986_1987_18 = ai1[18] + ct[18]
except:
    winter_1986_1987_18 = None
WL_32.append(winter_1986_1987_18)
station18.append(winter_1986_1987_18)

try:
    winter_1986_1987_19 = ai1[19] + ct[19]
except:
    winter_1986_1987_19 = None
WL_32.append(winter_1986_1987_19)
station19.append(winter_1986_1987_19)

try:
    winter_1986_1987_20 = ai1[20] + ct[20]
except:
    winter_1986_1987_20 = None
WL_32.append(winter_1986_1987_20)
station20.append(winter_1986_1987_20)

try:
    winter_1986_1987_21 = ai1[21] + ct[21]
except:
    winter_1986_1987_21 = None
WL_32.append(winter_1986_1987_21)
station21.append(winter_1986_1987_21)

try:
    winter_1986_1987_22 = ai1[22] + ct[22]
except:
    winter_1986_1987_22 = None
WL_32.append(winter_1986_1987_22)
station22.append(winter_1986_1987_22)

try:
    winter_1986_1987_23 = ai1[23] + ct[23]
except:
    winter_1986_1987_23 = None
WL_32.append(winter_1986_1987_23)
station23.append(winter_1986_1987_23)

#last spring freeze values for #1988

cu = []

for rowOfCellObjects in mosheet['GJ2':'GJ25']:
    for cellObj in rowOfCellObjects:
        cu.append(cellObj.value)

#final winter length calculation for 1987-1988 season for all of 24 Missouri stations

WL_33 = [] #all 1987-1988 winter lengths

try:
    winter_1987_1988_0 = aj1[0] + cu[0]
except:
    winter_1987_1988_0 = None
WL_33.append(winter_1987_1988_0)
station0.append(winter_1987_1988_0)

try:
    winter_1987_1988_1 = aj1[1] + cu[1]
except:
    winter_1987_1988_1 = None
WL_33.append(winter_1987_1988_1)
station1.append(winter_1987_1988_1)

try:
    winter_1987_1988_2 = aj1[2] + cu[2]
except:
    winter_1987_1988_2 = None
WL_33.append(winter_1987_1988_2)
station2.append(winter_1987_1988_2)

try:
    winter_1987_1988_3 = aj1[3] + cu[3]
except:
    winter_1987_1988_3 = None
WL_33.append(winter_1987_1988_3)
station3.append(winter_1987_1988_3)

try:
    winter_1987_1988_4 = aj1[4] + cu[4]
except:
    winter_1987_1988_4 = None
WL_33.append(winter_1987_1988_4)
station4.append(winter_1987_1988_4)

try:
    winter_1987_1988_5 = aj1[5] + cu[5]
except:
    winter_1987_1988_5 = None
WL_33.append(winter_1987_1988_5)
station5.append(winter_1987_1988_5)

try:
    winter_1987_1988_6 = aj1[6] + cu[6]
except:
    winter_1987_1988_6 = None
WL_33.append(winter_1987_1988_6)
station6.append(winter_1987_1988_6)

try:
    winter_1987_1988_7 = aj1[7] + cu[7]
except:
    winter_1987_1988_7 = None
WL_33.append(winter_1987_1988_7)
station7.append(winter_1987_1988_7)

try:
    winter_1987_1988_8 = aj1[8] + cu[8]
except:
    winter_1987_1988_8 = None
WL_33.append(winter_1987_1988_8)
station8.append(winter_1987_1988_8)

try:
    winter_1987_1988_9 = aj1[9] + cu[9]
except:
    winter_1987_1988_9 = None
WL_33.append(winter_1987_1988_9)
station9.append(winter_1987_1988_9)

try:
    winter_1987_1988_10 = aj1[10] + cu[10]
except:
    winter_1987_1988_10 = None
WL_33.append(winter_1987_1988_10)
station10.append(winter_1987_1988_10)

try:
    winter_1987_1988_11 = aj1[11] + cu[11]
except:
    winter_1987_1988_11 = None
WL_33.append(winter_1987_1988_11)
station11.append(winter_1987_1988_11)

try:
    winter_1987_1988_12 = aj1[12] + cu[12]
except:
    winter_1987_1988_12 = None
WL_33.append(winter_1987_1988_12)
station12.append(winter_1987_1988_12)

try:
    winter_1987_1988_13 = aj1[13] + cu[13]
except:
    winter_1987_1988_13 = None
WL_33.append(winter_1987_1988_13)
station13.append(winter_1987_1988_13)

try:
    winter_1987_1988_14 = aj1[14] + cu[14]
except:
    winter_1987_1988_14 = None
WL_33.append(winter_1987_1988_14)
station14.append(winter_1987_1988_14)

try:
    winter_1987_1988_15 = aj1[15] + cu[15]
except:
    winter_1987_1988_15 = None
WL_33.append(winter_1987_1988_15)
station15.append(winter_1987_1988_15)

try:
    winter_1987_1988_16 = aj1[16] + cu[16]
except:
    winter_1987_1988_16 = None
WL_33.append(winter_1987_1988_16)
station16.append(winter_1987_1988_16)

try:
    winter_1987_1988_17 = aj1[17] + cu[17]
except:
    winter_1987_1988_17 = None
WL_33.append(winter_1987_1988_17)
station17.append(winter_1987_1988_17)

try:
    winter_1987_1988_18 = aj1[18] + cu[18]
except:
    winter_1987_1988_18 = None
WL_33.append(winter_1987_1988_18)
station18.append(winter_1987_1988_18)

try:
    winter_1987_1988_19 = aj1[19] + cu[19]
except:
    winter_1987_1988_19 = None
WL_33.append(winter_1987_1988_19)
station19.append(winter_1987_1988_19)

try:
    winter_1987_1988_20 = aj1[20] + cu[20]
except:
    winter_1987_1988_20 = None
WL_33.append(winter_1987_1988_20)
station20.append(winter_1987_1988_20)

try:
    winter_1987_1988_21 = aj1[21] + cu[21]
except:
    winter_1987_1988_21 = None
WL_33.append(winter_1987_1988_21)
station21.append(winter_1987_1988_21)

try:
    winter_1987_1988_22 = aj1[22] + cu[22]
except:
    winter_1987_1988_22 = None
WL_33.append(winter_1987_1988_22)
station22.append(winter_1987_1988_22)

try:
    winter_1987_1988_23 = aj1[23] + cu[23]
except:
    winter_1987_1988_23 = None
WL_33.append(winter_1987_1988_23)
station23.append(winter_1987_1988_23)

#last spring freeze values for #1989

cv = []

for rowOfCellObjects in mosheet['GK2':'GK25']:
    for cellObj in rowOfCellObjects:
        cv.append(cellObj.value)

#final winter length calculation for 1988-1989 season for all of 24 Missouri stations

WL_34 = [] #all 1988-1989 winter lengths

try:
    winter_1988_1989_0 = ak1[0] + cv[0]
except:
    winter_1988_1989_0 = None
WL_34.append(winter_1988_1989_0)
station0.append(winter_1988_1989_0)

try:
    winter_1988_1989_1 = ak1[1] + cv[1]
except:
    winter_1988_1989_1 = None
WL_34.append(winter_1988_1989_1)
station1.append(winter_1988_1989_1)

try:
    winter_1988_1989_2 = ak1[2] + cv[2]
except:
    winter_1988_1989_2 = None
WL_34.append(winter_1988_1989_2)
station2.append(winter_1988_1989_2)

try:
    winter_1988_1989_3 = ak1[3] + cv[3]
except:
    winter_1988_1989_3 = None
WL_34.append(winter_1988_1989_3)
station3.append(winter_1988_1989_3)

try:
    winter_1988_1989_4 = ak1[4] + cv[4]
except:
    winter_1988_1989_4 = None
WL_34.append(winter_1988_1989_4)
station4.append(winter_1988_1989_4)

try:
    winter_1988_1989_5 = ak1[5] + cv[5]
except:
    winter_1988_1989_5 = None
WL_34.append(winter_1988_1989_5)
station5.append(winter_1988_1989_5)

try:
    winter_1988_1989_6 = ak1[6] + cv[6]
except:
    winter_1988_1989_6 = None
WL_34.append(winter_1988_1989_6)
station6.append(winter_1988_1989_6)

try:
    winter_1988_1989_7 = ak1[7] + cv[7]
except:
    winter_1988_1989_7 = None
WL_34.append(winter_1988_1989_7)
station7.append(winter_1988_1989_7)

try:
    winter_1988_1989_8 = ak1[8] + cv[8]
except:
    winter_1988_1989_8 = None
WL_34.append(winter_1988_1989_8)
station8.append(winter_1988_1989_8)

try:
    winter_1988_1989_9 = ak1[9] + cv[9]
except:
    winter_1988_1989_9 = None
WL_34.append(winter_1988_1989_9)
station9.append(winter_1988_1989_9)

try:
    winter_1988_1989_10 = ak1[10] + cv[10]
except:
    winter_1988_1989_10 = None
WL_34.append(winter_1988_1989_10)
station10.append(winter_1988_1989_10)

try:
    winter_1988_1989_11 = ak1[11] + cv[11]
except:
    winter_1988_1989_11 = None
WL_34.append(winter_1988_1989_11)
station11.append(winter_1988_1989_11)

try:
    winter_1988_1989_12 = ak1[12] + cv[12]
except:
    winter_1988_1989_12 = None
WL_34.append(winter_1988_1989_12)
station12.append(winter_1988_1989_12)

try:
    winter_1988_1989_13 = ak1[13] + cv[13]
except:
    winter_1988_1989_13 = None
WL_34.append(winter_1988_1989_13)
station13.append(winter_1988_1989_13)

try:
    winter_1988_1989_14 = ak1[14] + cv[14]
except:
    winter_1988_1989_14 = None
WL_34.append(winter_1988_1989_14)
station14.append(winter_1988_1989_14)

try:
    winter_1988_1989_15 = ak1[15] + cv[15]
except:
    winter_1988_1989_15 = None
WL_34.append(winter_1988_1989_15)
station15.append(winter_1988_1989_15)

try:
    winter_1988_1989_16 = ak1[16] + cv[16]
except:
    winter_1988_1989_16 = None
WL_34.append(winter_1988_1989_16)
station16.append(winter_1988_1989_16)

try:
    winter_1988_1989_17 = ak1[17] + cv[17]
except:
    winter_1988_1989_17 = None
WL_34.append(winter_1988_1989_17)
station17.append(winter_1988_1989_17)

try:
    winter_1988_1989_18 = ak1[18] + cv[18]
except:
    winter_1988_1989_18 = None
WL_34.append(winter_1988_1989_18)
station18.append(winter_1988_1989_18)

try:
    winter_1988_1989_19 = ak1[19] + cv[19]
except:
    winter_1988_1989_19 = None
WL_34.append(winter_1988_1989_19)
station19.append(winter_1988_1989_19)

try:
    winter_1988_1989_20 = ak1[20] + cv[20]
except:
    winter_1988_1989_20 = None
WL_34.append(winter_1988_1989_20)
station20.append(winter_1988_1989_20)

try:
    winter_1988_1989_21 = ak1[21] + cv[21]
except:
    winter_1988_1989_21 = None
WL_34.append(winter_1988_1989_21)
station21.append(winter_1988_1989_21)

try:
    winter_1988_1989_22 = ak1[22] + cv[22]
except:
    winter_1988_1989_22 = None
WL_34.append(winter_1988_1989_22)
station22.append(winter_1988_1989_22)

try:
    winter_1988_1989_23 = ak1[23] + cv[23]
except:
    winter_1988_1989_23 = None
WL_34.append(winter_1988_1989_23)
station23.append(winter_1988_1989_23)

#last spring freeze values for #1990

cw = []

for rowOfCellObjects in mosheet['GL2':'GL25']:
    for cellObj in rowOfCellObjects:
        cw.append(cellObj.value)

#final winter length calculation for 1989-1990 season for all of 24 Missouri stations

WL_35 = [] #all 1989-1990 winter lengths

try:
    winter_1989_1990_0 = al1[0] + cw[0]
except:
    winter_1989_1990_0 = None
WL_35.append(winter_1989_1990_0)
station0.append(winter_1989_1990_0)

try:
    winter_1989_1990_1 = al1[1] + cw[1]
except:
    winter_1989_1990_1 = None
WL_35.append(winter_1989_1990_1)
station1.append(winter_1989_1990_1)

try:
    winter_1989_1990_2 = al1[2] + cw[2]
except:
    winter_1989_1990_2 = None
WL_35.append(winter_1989_1990_2)
station2.append(winter_1989_1990_2)

try:
    winter_1989_1990_3 = al1[3] + cw[3]
except:
    winter_1989_1990_3 = None
WL_35.append(winter_1989_1990_3)
station3.append(winter_1989_1990_3)

try:
    winter_1989_1990_4 = al1[4] + cw[4]
except:
    winter_1989_1990_4 = None
WL_35.append(winter_1989_1990_4)
station4.append(winter_1989_1990_4)

try:
    winter_1989_1990_5 = al1[5] + cw[5]
except:
    winter_1989_1990_5 = None
WL_35.append(winter_1989_1990_5)
station5.append(winter_1989_1990_5)

try:
    winter_1989_1990_6 = al1[6] + cw[6]
except:
    winter_1989_1990_6 = None
WL_35.append(winter_1989_1990_6)
station6.append(winter_1989_1990_6)

try:
    winter_1989_1990_7 = al1[7] + cw[7]
except:
    winter_1989_1990_7 = None
WL_35.append(winter_1989_1990_7)
station7.append(winter_1989_1990_7)

try:
    winter_1989_1990_8 = al1[8] + cw[8]
except:
    winter_1989_1990_8 = None
WL_35.append(winter_1989_1990_8)
station8.append(winter_1989_1990_8)

try:
    winter_1989_1990_9 = al1[9] + cw[9]
except:
    winter_1989_1990_9 = None
WL_35.append(winter_1989_1990_9)
station9.append(winter_1989_1990_9)

try:
    winter_1989_1990_10 = al1[10] + cw[10]
except:
    winter_1989_1990_10 = None
WL_35.append(winter_1989_1990_10)
station10.append(winter_1989_1990_10)

try:
    winter_1989_1990_11 = al1[11] + cw[11]
except:
    winter_1989_1990_11 = None
WL_35.append(winter_1989_1990_11)
station11.append(winter_1989_1990_11)

try:
    winter_1989_1990_12 = al1[12] + cw[12]
except:
    winter_1989_1990_12 = None
WL_35.append(winter_1989_1990_12)
station12.append(winter_1989_1990_12)

try:
    winter_1989_1990_13 = al1[13] + cw[13]
except:
    winter_1989_1990_13 = None
WL_35.append(winter_1989_1990_13)
station13.append(winter_1989_1990_13)

try:
    winter_1989_1990_14 = al1[14] + cw[14]
except:
    winter_1989_1990_14 = None
WL_35.append(winter_1989_1990_14)
station14.append(winter_1989_1990_14)

try:
    winter_1989_1990_15 = al1[15] + cw[15]
except:
    winter_1989_1990_15 = None
WL_35.append(winter_1989_1990_15)
station15.append(winter_1989_1990_15)

try:
    winter_1989_1990_16 = al1[16] + cw[16]
except:
    winter_1989_1990_16 = None
WL_35.append(winter_1989_1990_16)
station16.append(winter_1989_1990_16)

try:
    winter_1989_1990_17 = al1[17] + cw[17]
except:
    winter_1989_1990_17 = None
WL_35.append(winter_1989_1990_17)
station17.append(winter_1989_1990_17)

try:
    winter_1989_1990_18 = al1[18] + cw[18]
except:
    winter_1989_1990_18 = None
WL_35.append(winter_1989_1990_18)
station18.append(winter_1989_1990_18)

try:
    winter_1989_1990_19 = al1[19] + cw[19]
except:
    winter_1989_1990_19 = None
WL_35.append(winter_1989_1990_19)
station19.append(winter_1989_1990_19)

try:
    winter_1989_1990_20 = al1[20] + cw[20]
except:
    winter_1989_1990_20 = None
WL_35.append(winter_1989_1990_20)
station20.append(winter_1989_1990_20)

try:
    winter_1989_1990_21 = al1[21] + cw[21]
except:
    winter_1989_1990_21 = None
WL_35.append(winter_1989_1990_21)
station21.append(winter_1989_1990_21)

try:
    winter_1989_1990_22 = al1[22] + cw[22]
except:
    winter_1989_1990_22 = None
WL_35.append(winter_1989_1990_22)
station22.append(winter_1989_1990_22)

try:
    winter_1989_1990_23 = al1[23] + cw[23]
except:
    winter_1989_1990_23 = None
WL_35.append(winter_1989_1990_23)
station23.append(winter_1989_1990_23)

#last spring freeze values for #1991

cx = []

for rowOfCellObjects in mosheet['GM2':'GM25']:
    for cellObj in rowOfCellObjects:
        cx.append(cellObj.value)

#final winter length calculation for 1990-1991 season for all of 24 Missouri stations

WL_36 = [] #all 1990-1991 winter lengths

try:
    winter_1990_1991_0 = al1[0] + cx[0]
except:
    winter_1990_1991_0 = None
WL_36.append(winter_1990_1991_0)
station0.append(winter_1990_1991_0)

try:
    winter_1990_1991_1 = al1[1] + cx[1]
except:
    winter_1990_1991_1 = None
WL_36.append(winter_1990_1991_1)
station1.append(winter_1990_1991_1)

try:
    winter_1990_1991_2 = al1[2] + cx[2]
except:
    winter_1990_1991_2 = None
WL_36.append(winter_1990_1991_2)
station2.append(winter_1990_1991_2)

try:
    winter_1990_1991_3 = al1[3] + cx[3]
except:
    winter_1990_1991_3 = None
WL_36.append(winter_1990_1991_3)
station3.append(winter_1990_1991_3)

try:
    winter_1990_1991_4 = al1[4] + cx[4]
except:
    winter_1990_1991_4 = None
WL_36.append(winter_1990_1991_4)
station4.append(winter_1990_1991_4)

try:
    winter_1990_1991_5 = al1[5] + cx[5]
except:
    winter_1990_1991_5 = None
WL_36.append(winter_1990_1991_5)
station5.append(winter_1990_1991_5)

try:
    winter_1990_1991_6 = al1[6] + cx[6]
except:
    winter_1990_1991_6 = None
WL_36.append(winter_1990_1991_6)
station6.append(winter_1990_1991_6)

try:
    winter_1990_1991_7 = al1[7] + cx[7]
except:
    winter_1990_1991_7 = None
WL_36.append(winter_1990_1991_7)
station7.append(winter_1990_1991_7)

try:
    winter_1990_1991_8 = al1[8] + cx[8]
except:
    winter_1990_1991_8 = None
WL_36.append(winter_1990_1991_8)
station8.append(winter_1990_1991_8)

try:
    winter_1990_1991_9 = al1[9] + cx[9]
except:
    winter_1990_1991_9 = None
WL_36.append(winter_1990_1991_9)
station9.append(winter_1990_1991_9)

try:
    winter_1990_1991_10 = al1[10] + cx[10]
except:
    winter_1990_1991_10 = None
WL_36.append(winter_1990_1991_10)
station10.append(winter_1990_1991_10)

try:
    winter_1990_1991_11 = al1[11] + cx[11]
except:
    winter_1990_1991_11 = None
WL_36.append(winter_1990_1991_11)
station11.append(winter_1990_1991_11)

try:
    winter_1990_1991_12 = al1[12] + cx[12]
except:
    winter_1990_1991_12 = None
WL_36.append(winter_1990_1991_12)
station12.append(winter_1990_1991_12)

try:
    winter_1990_1991_13 = al1[13] + cx[13]
except:
    winter_1990_1991_13 = None
WL_36.append(winter_1990_1991_13)
station13.append(winter_1990_1991_13)

try:
    winter_1990_1991_14 = al1[14] + cx[14]
except:
    winter_1990_1991_14 = None
WL_36.append(winter_1990_1991_14)
station14.append(winter_1990_1991_14)

try:
    winter_1990_1991_15 = al1[15] + cx[15]
except:
    winter_1990_1991_15 = None
WL_36.append(winter_1990_1991_15)
station15.append(winter_1990_1991_15)

try:
    winter_1990_1991_16 = al1[16] + cx[16]
except:
    winter_1990_1991_16 = None
WL_36.append(winter_1990_1991_16)
station16.append(winter_1990_1991_16)

try:
    winter_1990_1991_17 = al1[17] + cx[17]
except:
    winter_1990_1991_17 = None
WL_36.append(winter_1990_1991_17)
station17.append(winter_1990_1991_17)

try:
    winter_1990_1991_18 = al1[18] + cx[18]
except:
    winter_1990_1991_18 = None
WL_36.append(winter_1990_1991_18)
station18.append(winter_1990_1991_18)

try:
    winter_1990_1991_19 = al1[19] + cx[19]
except:
    winter_1990_1991_19 = None
WL_36.append(winter_1990_1991_19)
station19.append(winter_1990_1991_19)

try:
    winter_1990_1991_20 = al1[20] + cx[20]
except:
    winter_1990_1991_20 = None
WL_36.append(winter_1990_1991_20)
station20.append(winter_1990_1991_20)

try:
    winter_1990_1991_21 = al1[21] + cx[21]
except:
    winter_1990_1991_21 = None
WL_36.append(winter_1990_1991_21)
station21.append(winter_1990_1991_21)

try:
    winter_1990_1991_22 = al1[22] + cx[22]
except:
    winter_1990_1991_22 = None
WL_36.append(winter_1990_1991_22)
station22.append(winter_1990_1991_22)

try:
    winter_1990_1991_23 = al1[23] + cx[23]
except:
    winter_1990_1991_23 = None
WL_36.append(winter_1990_1991_23)
station23.append(winter_1990_1991_23)

#last spring freeze values for #1992

cy = []

for rowOfCellObjects in mosheet['GN2':'GN25']:
    for cellObj in rowOfCellObjects:
        cy.append(cellObj.value)

#final winter length calculation for 1991-1992 season for all of 24 Missouri stations

WL_37 = [] #all 1991-1992 winter lengths

try:
    winter_1991_1992_0 = am1[0] + cy[0]
except:
    winter_1991_1992_0 = None
WL_37.append(winter_1991_1992_0)
station0.append(winter_1991_1992_0)

try:
    winter_1991_1992_1 = am1[1] + cy[1]
except:
    winter_1991_1992_1 = None
WL_37.append(winter_1991_1992_1)
station1.append(winter_1991_1992_1)

try:
    winter_1991_1992_2 = am1[2] + cy[2]
except:
    winter_1991_1992_2 = None
WL_37.append(winter_1991_1992_2)
station2.append(winter_1991_1992_2)

try:
    winter_1991_1992_3 = am1[3] + cy[3]
except:
    winter_1991_1992_3 = None
WL_37.append(winter_1991_1992_3)
station3.append(winter_1991_1992_3)

try:
    winter_1991_1992_4 = am1[4] + cy[4]
except:
    winter_1991_1992_4 = None
WL_37.append(winter_1991_1992_4)
station4.append(winter_1991_1992_4)

try:
    winter_1991_1992_5 = am1[5] + cy[5]
except:
    winter_1991_1992_5 = None
WL_37.append(winter_1991_1992_5)
station5.append(winter_1991_1992_5)

try:
    winter_1991_1992_6 = am1[6] + cy[6]
except:
    winter_1991_1992_6 = None
WL_37.append(winter_1991_1992_6)
station6.append(winter_1991_1992_6)

try:
    winter_1991_1992_7 = am1[7] + cy[7]
except:
    winter_1991_1992_7 = None
WL_37.append(winter_1991_1992_7)
station7.append(winter_1991_1992_7)

try:
    winter_1991_1992_8 = am1[8] + cy[8]
except:
    winter_1991_1992_8 = None
WL_37.append(winter_1991_1992_8)
station8.append(winter_1991_1992_8)

try:
    winter_1991_1992_9 = am1[9] + cy[9]
except:
    winter_1991_1992_9 = None
WL_37.append(winter_1991_1992_9)
station9.append(winter_1991_1992_9)

try:
    winter_1991_1992_10 = am1[10] + cy[10]
except:
    winter_1991_1992_10 = None
WL_37.append(winter_1991_1992_10)
station10.append(winter_1991_1992_10)

try:
    winter_1991_1992_11 = am1[11] + cy[11]
except:
    winter_1991_1992_11 = None
WL_37.append(winter_1991_1992_11)
station11.append(winter_1991_1992_11)

try:
    winter_1991_1992_12 = am1[12] + cy[12]
except:
    winter_1991_1992_12 = None
WL_37.append(winter_1991_1992_12)
station12.append(winter_1991_1992_12)

try:
    winter_1991_1992_13 = am1[13] + cy[13]
except:
    winter_1991_1992_13 = None
WL_37.append(winter_1991_1992_13)
station13.append(winter_1991_1992_13)

try:
    winter_1991_1992_14 = am1[14] + cy[14]
except:
    winter_1991_1992_14 = None
WL_37.append(winter_1991_1992_14)
station14.append(winter_1991_1992_14)

try:
    winter_1991_1992_15 = am1[15] + cy[15]
except:
    winter_1991_1992_15 = None
WL_37.append(winter_1991_1992_15)
station15.append(winter_1991_1992_15)

try:
    winter_1991_1992_16 = am1[16] + cy[16]
except:
    winter_1991_1992_16 = None
WL_37.append(winter_1991_1992_16)
station16.append(winter_1991_1992_16)

try:
    winter_1991_1992_17 = am1[17] + cy[17]
except:
    winter_1991_1992_17 = None
WL_37.append(winter_1991_1992_17)
station17.append(winter_1991_1992_17)

try:
    winter_1991_1992_18 = am1[18] + cy[18]
except:
    winter_1991_1992_18 = None
WL_37.append(winter_1991_1992_18)
station18.append(winter_1991_1992_18)

try:
    winter_1991_1992_19 = am1[19] + cy[19]
except:
    winter_1991_1992_19 = None
WL_37.append(winter_1991_1992_19)
station19.append(winter_1991_1992_19)

try:
    winter_1991_1992_20 = am1[20] + cy[20]
except:
    winter_1991_1992_20 = None
WL_37.append(winter_1991_1992_20)
station20.append(winter_1991_1992_20)

try:
    winter_1991_1992_21 = am1[21] + cy[21]
except:
    winter_1991_1992_21 = None
WL_37.append(winter_1991_1992_21)
station21.append(winter_1991_1992_21)

try:
    winter_1991_1992_22 = am1[22] + cy[22]
except:
    winter_1991_1992_22 = None
WL_37.append(winter_1991_1992_22)
station22.append(winter_1991_1992_22)

try:
    winter_1991_1992_23 = am1[23] + cy[23]
except:
    winter_1991_1992_23 = None
WL_37.append(winter_1991_1992_23)
station23.append(winter_1991_1992_23)

#last spring freeze values for #1993

cz = []

for rowOfCellObjects in mosheet['GO2':'GO25']:
    for cellObj in rowOfCellObjects:
        cz.append(cellObj.value)

#final winter length calculation for 1992-1993 season for all of 24 Missouri stations

WL_38 = [] #all 1992-1993 winter lengths

try:
    winter_1992_1993_0 = an1[0] + cz[0]
except:
    winter_1992_1993_0 = None
WL_38.append(winter_1992_1993_0)
station0.append(winter_1992_1993_0)

try:
    winter_1992_1993_1 = an1[1] + cz[1]
except:
    winter_1992_1993_1 = None
WL_38.append(winter_1992_1993_1)
station1.append(winter_1992_1993_1)

try:
    winter_1992_1993_2 = an1[2] + cz[2]
except:
    winter_1992_1993_2 = None
WL_38.append(winter_1992_1993_2)
station2.append(winter_1992_1993_2)

try:
    winter_1992_1993_3 = an1[3] + cz[3]
except:
    winter_1992_1993_3 = None
WL_38.append(winter_1992_1993_3)
station3.append(winter_1992_1993_3)

try:
    winter_1992_1993_4 = an1[4] + cz[4]
except:
    winter_1992_1993_4 = None
WL_38.append(winter_1992_1993_4)
station4.append(winter_1992_1993_4)

try:
    winter_1992_1993_5 = an1[5] + cz[5]
except:
    winter_1992_1993_5 = None
WL_38.append(winter_1992_1993_5)
station5.append(winter_1992_1993_5)

try:
    winter_1992_1993_6 = an1[6] + cz[6]
except:
    winter_1992_1993_6 = None
WL_38.append(winter_1992_1993_6)
station6.append(winter_1992_1993_6)

try:
    winter_1992_1993_7 = an1[7] + cz[7]
except:
    winter_1992_1993_7 = None
WL_38.append(winter_1992_1993_7)
station7.append(winter_1992_1993_7)

try:
    winter_1992_1993_8 = an1[8] + cz[8]
except:
    winter_1992_1993_8 = None
WL_38.append(winter_1992_1993_8)
station8.append(winter_1992_1993_8)

try:
    winter_1992_1993_9 = an1[9] + cz[9]
except:
    winter_1992_1993_9 = None
WL_38.append(winter_1992_1993_9)
station9.append(winter_1992_1993_9)

try:
    winter_1992_1993_10 = an1[10] + cz[10]
except:
    winter_1992_1993_10 = None
WL_38.append(winter_1992_1993_10)
station10.append(winter_1992_1993_10)

try:
    winter_1992_1993_11 = an1[11] + cz[11]
except:
    winter_1992_1993_11 = None
WL_38.append(winter_1992_1993_11)
station11.append(winter_1992_1993_11)

try:
    winter_1992_1993_12 = an1[12] + cz[12]
except:
    winter_1992_1993_12 = None
WL_38.append(winter_1992_1993_12)
station12.append(winter_1992_1993_12)

try:
    winter_1992_1993_13 = an1[13] + cz[13]
except:
    winter_1992_1993_13 = None
WL_38.append(winter_1992_1993_13)
station13.append(winter_1992_1993_13)

try:
    winter_1992_1993_14 = an1[14] + cz[14]
except:
    winter_1992_1993_14 = None
WL_38.append(winter_1992_1993_14)
station14.append(winter_1992_1993_14)

try:
    winter_1992_1993_15 = an1[15] + cz[15]
except:
    winter_1992_1993_15 = None
WL_38.append(winter_1992_1993_15)
station15.append(winter_1992_1993_15)

try:
    winter_1992_1993_16 = an1[16] + cz[16]
except:
    winter_1992_1993_16 = None
WL_38.append(winter_1992_1993_16)
station16.append(winter_1992_1993_16)

try:
    winter_1992_1993_17 = an1[17] + cz[17]
except:
    winter_1992_1993_17 = None
WL_38.append(winter_1992_1993_17)
station17.append(winter_1992_1993_17)

try:
    winter_1992_1993_18 = an1[18] + cz[18]
except:
    winter_1992_1993_18 = None
WL_38.append(winter_1992_1993_18)
station18.append(winter_1992_1993_18)

try:
    winter_1992_1993_19 = an1[19] + cz[19]
except:
    winter_1992_1993_19 = None
WL_38.append(winter_1992_1993_19)
station19.append(winter_1992_1993_19)

try:
    winter_1992_1993_20 = an1[20] + cz[20]
except:
    winter_1992_1993_20 = None
WL_38.append(winter_1992_1993_20)
station20.append(winter_1992_1993_20)

try:
    winter_1992_1993_21 = an1[21] + cz[21]
except:
    winter_1992_1993_21 = None
WL_38.append(winter_1992_1993_21)
station21.append(winter_1992_1993_21)

try:
    winter_1992_1993_22 = an1[22] + cz[22]
except:
    winter_1992_1993_22 = None
WL_38.append(winter_1992_1993_22)
station22.append(winter_1992_1993_22)

try:
    winter_1992_1993_23 = an1[23] + cz[23]
except:
    winter_1992_1993_23 = None
WL_38.append(winter_1992_1993_23)
station23.append(winter_1992_1993_23)

#last spring freeze values for #1994

da = []

for rowOfCellObjects in mosheet['GP2':'GP25']:
    for cellObj in rowOfCellObjects:
        da.append(cellObj.value)

#final winter length calculation for 1993-1994 season for all of 24 Missouri stations

WL_39 = [] #all 1993-1994 winter lengths

try:
    winter_1993_1994_0 = ao1[0] + da[0]
except:
    winter_1993_1994_0 = None
WL_39.append(winter_1993_1994_0)
station0.append(winter_1993_1994_0)

try:
    winter_1993_1994_1 = ao1[1] + da[1]
except:
    winter_1993_1994_1 = None
WL_39.append(winter_1993_1994_1)
station1.append(winter_1993_1994_1)

try:
    winter_1993_1994_2 = ao1[2] + da[2]
except:
    winter_1993_1994_2 = None
WL_39.append(winter_1993_1994_2)
station2.append(winter_1993_1994_2)

try:
    winter_1993_1994_3 = ao1[3] + da[3]
except:
    winter_1993_1994_3 = None
WL_39.append(winter_1993_1994_3)
station3.append(winter_1993_1994_3)

try:
    winter_1993_1994_4 = ao1[4] + da[4]
except:
    winter_1993_1994_4 = None
WL_39.append(winter_1993_1994_4)
station4.append(winter_1993_1994_4)

try:
    winter_1993_1994_5 = ao1[5] + da[5]
except:
    winter_1993_1994_5 = None
WL_39.append(winter_1993_1994_5)
station5.append(winter_1993_1994_5)

try:
    winter_1993_1994_6 = ao1[6] + da[6]
except:
    winter_1993_1994_6 = None
WL_39.append(winter_1993_1994_6)
station6.append(winter_1993_1994_6)

try:
    winter_1993_1994_7 = ao1[7] + da[7]
except:
    winter_1993_1994_7 = None
WL_39.append(winter_1993_1994_7)
station7.append(winter_1993_1994_7)

try:
    winter_1993_1994_8 = ao1[8] + da[8]
except:
    winter_1993_1994_8 = None
WL_39.append(winter_1993_1994_8)
station8.append(winter_1993_1994_8)

try:
    winter_1993_1994_9 = ao1[9] + da[9]
except:
    winter_1993_1994_9 = None
WL_39.append(winter_1993_1994_9)
station9.append(winter_1993_1994_9)

try:
    winter_1993_1994_10 = ao1[10] + da[10]
except:
    winter_1993_1994_10 = None
WL_39.append(winter_1993_1994_10)
station10.append(winter_1993_1994_10)

try:
    winter_1993_1994_11 = ao1[11] + da[11]
except:
    winter_1993_1994_11 = None
WL_39.append(winter_1993_1994_11)
station11.append(winter_1993_1994_11)

try:
    winter_1993_1994_12 = ao1[12] + da[12]
except:
    winter_1993_1994_12 = None
WL_39.append(winter_1993_1994_12)
station12.append(winter_1993_1994_12)

try:
    winter_1993_1994_13 = ao1[13] + da[13]
except:
    winter_1993_1994_13 = None
WL_39.append(winter_1993_1994_13)
station13.append(winter_1993_1994_13)

try:
    winter_1993_1994_14 = ao1[14] + da[14]
except:
    winter_1993_1994_14 = None
WL_39.append(winter_1993_1994_14)
station14.append(winter_1993_1994_14)

try:
    winter_1993_1994_15 = ao1[15] + da[15]
except:
    winter_1993_1994_15 = None
WL_39.append(winter_1993_1994_15)
station15.append(winter_1993_1994_15)

try:
    winter_1993_1994_16 = ao1[16] + da[16]
except:
    winter_1993_1994_16 = None
WL_39.append(winter_1993_1994_16)
station16.append(winter_1993_1994_16)

try:
    winter_1993_1994_17 = ao1[17] + da[17]
except:
    winter_1993_1994_17 = None
WL_39.append(winter_1993_1994_17)
station17.append(winter_1993_1994_17)

try:
    winter_1993_1994_18 = ao1[18] + da[18]
except:
    winter_1993_1994_18 = None
WL_39.append(winter_1993_1994_18)
station18.append(winter_1993_1994_18)

try:
    winter_1993_1994_19 = ao1[19] + da[19]
except:
    winter_1993_1994_19 = None
WL_39.append(winter_1993_1994_19)
station19.append(winter_1993_1994_19)

try:
    winter_1993_1994_20 = ao1[20] + da[20]
except:
    winter_1993_1994_20 = None
WL_39.append(winter_1993_1994_20)
station20.append(winter_1993_1994_20)

try:
    winter_1993_1994_21 = ao1[21] + da[21]
except:
    winter_1993_1994_21 = None
WL_39.append(winter_1993_1994_21)
station21.append(winter_1993_1994_21)

try:
    winter_1993_1994_22 = ao1[22] + da[22]
except:
    winter_1993_1994_22 = None
WL_39.append(winter_1993_1994_22)
station22.append(winter_1993_1994_22)

try:
    winter_1993_1994_23 = ao1[23] + da[23]
except:
    winter_1993_1994_23 = None
WL_39.append(winter_1993_1994_23)
station23.append(winter_1993_1994_23)

