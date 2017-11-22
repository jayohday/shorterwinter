import openpyxl
import numpy as np
import csv

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
    winter_1990_1991_0 = am1[0] + cx[0]
except:
    winter_1990_1991_0 = None
WL_36.append(winter_1990_1991_0)
station0.append(winter_1990_1991_0)

try:
    winter_1990_1991_1 = am1[1] + cx[1]
except:
    winter_1990_1991_1 = None
WL_36.append(winter_1990_1991_1)
station1.append(winter_1990_1991_1)

try:
    winter_1990_1991_2 = am1[2] + cx[2]
except:
    winter_1990_1991_2 = None
WL_36.append(winter_1990_1991_2)
station2.append(winter_1990_1991_2)

try:
    winter_1990_1991_3 = am1[3] + cx[3]
except:
    winter_1990_1991_3 = None
WL_36.append(winter_1990_1991_3)
station3.append(winter_1990_1991_3)

try:
    winter_1990_1991_4 = am1[4] + cx[4]
except:
    winter_1990_1991_4 = None
WL_36.append(winter_1990_1991_4)
station4.append(winter_1990_1991_4)

try:
    winter_1990_1991_5 = am1[5] + cx[5]
except:
    winter_1990_1991_5 = None
WL_36.append(winter_1990_1991_5)
station5.append(winter_1990_1991_5)

try:
    winter_1990_1991_6 = am1[6] + cx[6]
except:
    winter_1990_1991_6 = None
WL_36.append(winter_1990_1991_6)
station6.append(winter_1990_1991_6)

try:
    winter_1990_1991_7 = am1[7] + cx[7]
except:
    winter_1990_1991_7 = None
WL_36.append(winter_1990_1991_7)
station7.append(winter_1990_1991_7)

try:
    winter_1990_1991_8 = am1[8] + cx[8]
except:
    winter_1990_1991_8 = None
WL_36.append(winter_1990_1991_8)
station8.append(winter_1990_1991_8)

try:
    winter_1990_1991_9 = am1[9] + cx[9]
except:
    winter_1990_1991_9 = None
WL_36.append(winter_1990_1991_9)
station9.append(winter_1990_1991_9)

try:
    winter_1990_1991_10 = am1[10] + cx[10]
except:
    winter_1990_1991_10 = None
WL_36.append(winter_1990_1991_10)
station10.append(winter_1990_1991_10)

try:
    winter_1990_1991_11 = am1[11] + cx[11]
except:
    winter_1990_1991_11 = None
WL_36.append(winter_1990_1991_11)
station11.append(winter_1990_1991_11)

try:
    winter_1990_1991_12 = am1[12] + cx[12]
except:
    winter_1990_1991_12 = None
WL_36.append(winter_1990_1991_12)
station12.append(winter_1990_1991_12)

try:
    winter_1990_1991_13 = am1[13] + cx[13]
except:
    winter_1990_1991_13 = None
WL_36.append(winter_1990_1991_13)
station13.append(winter_1990_1991_13)

try:
    winter_1990_1991_14 = am1[14] + cx[14]
except:
    winter_1990_1991_14 = None
WL_36.append(winter_1990_1991_14)
station14.append(winter_1990_1991_14)

try:
    winter_1990_1991_15 = am1[15] + cx[15]
except:
    winter_1990_1991_15 = None
WL_36.append(winter_1990_1991_15)
station15.append(winter_1990_1991_15)

try:
    winter_1990_1991_16 = am1[16] + cx[16]
except:
    winter_1990_1991_16 = None
WL_36.append(winter_1990_1991_16)
station16.append(winter_1990_1991_16)

try:
    winter_1990_1991_17 = am1[17] + cx[17]
except:
    winter_1990_1991_17 = None
WL_36.append(winter_1990_1991_17)
station17.append(winter_1990_1991_17)

try:
    winter_1990_1991_18 = am1[18] + cx[18]
except:
    winter_1990_1991_18 = None
WL_36.append(winter_1990_1991_18)
station18.append(winter_1990_1991_18)

try:
    winter_1990_1991_19 = am1[19] + cx[19]
except:
    winter_1990_1991_19 = None
WL_36.append(winter_1990_1991_19)
station19.append(winter_1990_1991_19)

try:
    winter_1990_1991_20 = am1[20] + cx[20]
except:
    winter_1990_1991_20 = None
WL_36.append(winter_1990_1991_20)
station20.append(winter_1990_1991_20)

try:
    winter_1990_1991_21 = am1[21] + cx[21]
except:
    winter_1990_1991_21 = None
WL_36.append(winter_1990_1991_21)
station21.append(winter_1990_1991_21)

try:
    winter_1990_1991_22 = am1[22] + cx[22]
except:
    winter_1990_1991_22 = None
WL_36.append(winter_1990_1991_22)
station22.append(winter_1990_1991_22)

try:
    winter_1990_1991_23 = am1[23] + cx[23]
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
    winter_1991_1992_0 = an1[0] + cy[0]
except:
    winter_1991_1992_0 = None
WL_37.append(winter_1991_1992_0)
station0.append(winter_1991_1992_0)

try:
    winter_1991_1992_1 = an1[1] + cy[1]
except:
    winter_1991_1992_1 = None
WL_37.append(winter_1991_1992_1)
station1.append(winter_1991_1992_1)

try:
    winter_1991_1992_2 = an1[2] + cy[2]
except:
    winter_1991_1992_2 = None
WL_37.append(winter_1991_1992_2)
station2.append(winter_1991_1992_2)

try:
    winter_1991_1992_3 = an1[3] + cy[3]
except:
    winter_1991_1992_3 = None
WL_37.append(winter_1991_1992_3)
station3.append(winter_1991_1992_3)

try:
    winter_1991_1992_4 = an1[4] + cy[4]
except:
    winter_1991_1992_4 = None
WL_37.append(winter_1991_1992_4)
station4.append(winter_1991_1992_4)

try:
    winter_1991_1992_5 = an1[5] + cy[5]
except:
    winter_1991_1992_5 = None
WL_37.append(winter_1991_1992_5)
station5.append(winter_1991_1992_5)

try:
    winter_1991_1992_6 = an1[6] + cy[6]
except:
    winter_1991_1992_6 = None
WL_37.append(winter_1991_1992_6)
station6.append(winter_1991_1992_6)

try:
    winter_1991_1992_7 = an1[7] + cy[7]
except:
    winter_1991_1992_7 = None
WL_37.append(winter_1991_1992_7)
station7.append(winter_1991_1992_7)

try:
    winter_1991_1992_8 = an1[8] + cy[8]
except:
    winter_1991_1992_8 = None
WL_37.append(winter_1991_1992_8)
station8.append(winter_1991_1992_8)

try:
    winter_1991_1992_9 = an1[9] + cy[9]
except:
    winter_1991_1992_9 = None
WL_37.append(winter_1991_1992_9)
station9.append(winter_1991_1992_9)

try:
    winter_1991_1992_10 = an1[10] + cy[10]
except:
    winter_1991_1992_10 = None
WL_37.append(winter_1991_1992_10)
station10.append(winter_1991_1992_10)

try:
    winter_1991_1992_11 = an1[11] + cy[11]
except:
    winter_1991_1992_11 = None
WL_37.append(winter_1991_1992_11)
station11.append(winter_1991_1992_11)

try:
    winter_1991_1992_12 = an1[12] + cy[12]
except:
    winter_1991_1992_12 = None
WL_37.append(winter_1991_1992_12)
station12.append(winter_1991_1992_12)

try:
    winter_1991_1992_13 = an1[13] + cy[13]
except:
    winter_1991_1992_13 = None
WL_37.append(winter_1991_1992_13)
station13.append(winter_1991_1992_13)

try:
    winter_1991_1992_14 = an1[14] + cy[14]
except:
    winter_1991_1992_14 = None
WL_37.append(winter_1991_1992_14)
station14.append(winter_1991_1992_14)

try:
    winter_1991_1992_15 = an1[15] + cy[15]
except:
    winter_1991_1992_15 = None
WL_37.append(winter_1991_1992_15)
station15.append(winter_1991_1992_15)

try:
    winter_1991_1992_16 = an1[16] + cy[16]
except:
    winter_1991_1992_16 = None
WL_37.append(winter_1991_1992_16)
station16.append(winter_1991_1992_16)

try:
    winter_1991_1992_17 = an1[17] + cy[17]
except:
    winter_1991_1992_17 = None
WL_37.append(winter_1991_1992_17)
station17.append(winter_1991_1992_17)

try:
    winter_1991_1992_18 = an1[18] + cy[18]
except:
    winter_1991_1992_18 = None
WL_37.append(winter_1991_1992_18)
station18.append(winter_1991_1992_18)

try:
    winter_1991_1992_19 = an1[19] + cy[19]
except:
    winter_1991_1992_19 = None
WL_37.append(winter_1991_1992_19)
station19.append(winter_1991_1992_19)

try:
    winter_1991_1992_20 = an1[20] + cy[20]
except:
    winter_1991_1992_20 = None
WL_37.append(winter_1991_1992_20)
station20.append(winter_1991_1992_20)

try:
    winter_1991_1992_21 = an1[21] + cy[21]
except:
    winter_1991_1992_21 = None
WL_37.append(winter_1991_1992_21)
station21.append(winter_1991_1992_21)

try:
    winter_1991_1992_22 = an1[22] + cy[22]
except:
    winter_1991_1992_22 = None
WL_37.append(winter_1991_1992_22)
station22.append(winter_1991_1992_22)

try:
    winter_1991_1992_23 = an1[23] + cy[23]
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
    winter_1992_1993_0 = ao1[0] + cz[0]
except:
    winter_1992_1993_0 = None
WL_38.append(winter_1992_1993_0)
station0.append(winter_1992_1993_0)

try:
    winter_1992_1993_1 = ao1[1] + cz[1]
except:
    winter_1992_1993_1 = None
WL_38.append(winter_1992_1993_1)
station1.append(winter_1992_1993_1)

try:
    winter_1992_1993_2 = ao1[2] + cz[2]
except:
    winter_1992_1993_2 = None
WL_38.append(winter_1992_1993_2)
station2.append(winter_1992_1993_2)

try:
    winter_1992_1993_3 = ao1[3] + cz[3]
except:
    winter_1992_1993_3 = None
WL_38.append(winter_1992_1993_3)
station3.append(winter_1992_1993_3)

try:
    winter_1992_1993_4 = ao1[4] + cz[4]
except:
    winter_1992_1993_4 = None
WL_38.append(winter_1992_1993_4)
station4.append(winter_1992_1993_4)

try:
    winter_1992_1993_5 = ao1[5] + cz[5]
except:
    winter_1992_1993_5 = None
WL_38.append(winter_1992_1993_5)
station5.append(winter_1992_1993_5)

try:
    winter_1992_1993_6 = ao1[6] + cz[6]
except:
    winter_1992_1993_6 = None
WL_38.append(winter_1992_1993_6)
station6.append(winter_1992_1993_6)

try:
    winter_1992_1993_7 = ao1[7] + cz[7]
except:
    winter_1992_1993_7 = None
WL_38.append(winter_1992_1993_7)
station7.append(winter_1992_1993_7)

try:
    winter_1992_1993_8 = ao1[8] + cz[8]
except:
    winter_1992_1993_8 = None
WL_38.append(winter_1992_1993_8)
station8.append(winter_1992_1993_8)

try:
    winter_1992_1993_9 = ao1[9] + cz[9]
except:
    winter_1992_1993_9 = None
WL_38.append(winter_1992_1993_9)
station9.append(winter_1992_1993_9)

try:
    winter_1992_1993_10 = ao1[10] + cz[10]
except:
    winter_1992_1993_10 = None
WL_38.append(winter_1992_1993_10)
station10.append(winter_1992_1993_10)

try:
    winter_1992_1993_11 = ao1[11] + cz[11]
except:
    winter_1992_1993_11 = None
WL_38.append(winter_1992_1993_11)
station11.append(winter_1992_1993_11)

try:
    winter_1992_1993_12 = ao1[12] + cz[12]
except:
    winter_1992_1993_12 = None
WL_38.append(winter_1992_1993_12)
station12.append(winter_1992_1993_12)

try:
    winter_1992_1993_13 = ao1[13] + cz[13]
except:
    winter_1992_1993_13 = None
WL_38.append(winter_1992_1993_13)
station13.append(winter_1992_1993_13)

try:
    winter_1992_1993_14 = ao1[14] + cz[14]
except:
    winter_1992_1993_14 = None
WL_38.append(winter_1992_1993_14)
station14.append(winter_1992_1993_14)

try:
    winter_1992_1993_15 = ao1[15] + cz[15]
except:
    winter_1992_1993_15 = None
WL_38.append(winter_1992_1993_15)
station15.append(winter_1992_1993_15)

try:
    winter_1992_1993_16 = ao1[16] + cz[16]
except:
    winter_1992_1993_16 = None
WL_38.append(winter_1992_1993_16)
station16.append(winter_1992_1993_16)

try:
    winter_1992_1993_17 = ao1[17] + cz[17]
except:
    winter_1992_1993_17 = None
WL_38.append(winter_1992_1993_17)
station17.append(winter_1992_1993_17)

try:
    winter_1992_1993_18 = ao1[18] + cz[18]
except:
    winter_1992_1993_18 = None
WL_38.append(winter_1992_1993_18)
station18.append(winter_1992_1993_18)

try:
    winter_1992_1993_19 = ao1[19] + cz[19]
except:
    winter_1992_1993_19 = None
WL_38.append(winter_1992_1993_19)
station19.append(winter_1992_1993_19)

try:
    winter_1992_1993_20 = ao1[20] + cz[20]
except:
    winter_1992_1993_20 = None
WL_38.append(winter_1992_1993_20)
station20.append(winter_1992_1993_20)

try:
    winter_1992_1993_21 = ao1[21] + cz[21]
except:
    winter_1992_1993_21 = None
WL_38.append(winter_1992_1993_21)
station21.append(winter_1992_1993_21)

try:
    winter_1992_1993_22 = ao1[22] + cz[22]
except:
    winter_1992_1993_22 = None
WL_38.append(winter_1992_1993_22)
station22.append(winter_1992_1993_22)

try:
    winter_1992_1993_23 = ao1[23] + cz[23]
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
    winter_1993_1994_0 = ap1[0] + da[0]
except:
    winter_1993_1994_0 = None
WL_39.append(winter_1993_1994_0)
station0.append(winter_1993_1994_0)

try:
    winter_1993_1994_1 = ap1[1] + da[1]
except:
    winter_1993_1994_1 = None
WL_39.append(winter_1993_1994_1)
station1.append(winter_1993_1994_1)

try:
    winter_1993_1994_2 = ap1[2] + da[2]
except:
    winter_1993_1994_2 = None
WL_39.append(winter_1993_1994_2)
station2.append(winter_1993_1994_2)

try:
    winter_1993_1994_3 = ap1[3] + da[3]
except:
    winter_1993_1994_3 = None
WL_39.append(winter_1993_1994_3)
station3.append(winter_1993_1994_3)

try:
    winter_1993_1994_4 = ap1[4] + da[4]
except:
    winter_1993_1994_4 = None
WL_39.append(winter_1993_1994_4)
station4.append(winter_1993_1994_4)

try:
    winter_1993_1994_5 = ap1[5] + da[5]
except:
    winter_1993_1994_5 = None
WL_39.append(winter_1993_1994_5)
station5.append(winter_1993_1994_5)

try:
    winter_1993_1994_6 = ap1[6] + da[6]
except:
    winter_1993_1994_6 = None
WL_39.append(winter_1993_1994_6)
station6.append(winter_1993_1994_6)

try:
    winter_1993_1994_7 = ap1[7] + da[7]
except:
    winter_1993_1994_7 = None
WL_39.append(winter_1993_1994_7)
station7.append(winter_1993_1994_7)

try:
    winter_1993_1994_8 = ap1[8] + da[8]
except:
    winter_1993_1994_8 = None
WL_39.append(winter_1993_1994_8)
station8.append(winter_1993_1994_8)

try:
    winter_1993_1994_9 = ap1[9] + da[9]
except:
    winter_1993_1994_9 = None
WL_39.append(winter_1993_1994_9)
station9.append(winter_1993_1994_9)

try:
    winter_1993_1994_10 = ap1[10] + da[10]
except:
    winter_1993_1994_10 = None
WL_39.append(winter_1993_1994_10)
station10.append(winter_1993_1994_10)

try:
    winter_1993_1994_11 = ap1[11] + da[11]
except:
    winter_1993_1994_11 = None
WL_39.append(winter_1993_1994_11)
station11.append(winter_1993_1994_11)

try:
    winter_1993_1994_12 = ap1[12] + da[12]
except:
    winter_1993_1994_12 = None
WL_39.append(winter_1993_1994_12)
station12.append(winter_1993_1994_12)

try:
    winter_1993_1994_13 = ap1[13] + da[13]
except:
    winter_1993_1994_13 = None
WL_39.append(winter_1993_1994_13)
station13.append(winter_1993_1994_13)

try:
    winter_1993_1994_14 = ap1[14] + da[14]
except:
    winter_1993_1994_14 = None
WL_39.append(winter_1993_1994_14)
station14.append(winter_1993_1994_14)

try:
    winter_1993_1994_15 = ap1[15] + da[15]
except:
    winter_1993_1994_15 = None
WL_39.append(winter_1993_1994_15)
station15.append(winter_1993_1994_15)

try:
    winter_1993_1994_16 = ap1[16] + da[16]
except:
    winter_1993_1994_16 = None
WL_39.append(winter_1993_1994_16)
station16.append(winter_1993_1994_16)

try:
    winter_1993_1994_17 = ap1[17] + da[17]
except:
    winter_1993_1994_17 = None
WL_39.append(winter_1993_1994_17)
station17.append(winter_1993_1994_17)

try:
    winter_1993_1994_18 = ap1[18] + da[18]
except:
    winter_1993_1994_18 = None
WL_39.append(winter_1993_1994_18)
station18.append(winter_1993_1994_18)

try:
    winter_1993_1994_19 = ap1[19] + da[19]
except:
    winter_1993_1994_19 = None
WL_39.append(winter_1993_1994_19)
station19.append(winter_1993_1994_19)

try:
    winter_1993_1994_20 = ap1[20] + da[20]
except:
    winter_1993_1994_20 = None
WL_39.append(winter_1993_1994_20)
station20.append(winter_1993_1994_20)

try:
    winter_1993_1994_21 = ap1[21] + da[21]
except:
    winter_1993_1994_21 = None
WL_39.append(winter_1993_1994_21)
station21.append(winter_1993_1994_21)

try:
    winter_1993_1994_22 = ap1[22] + da[22]
except:
    winter_1993_1994_22 = None
WL_39.append(winter_1993_1994_22)
station22.append(winter_1993_1994_22)

try:
    winter_1993_1994_23 = ap1[23] + da[23]
except:
    winter_1993_1994_23 = None
WL_39.append(winter_1993_1994_23)
station23.append(winter_1993_1994_23)

#last spring freeze values for #1995

db = []

for rowOfCellObjects in mosheet['GQ2':'GQ25']:
    for cellObj in rowOfCellObjects:
        db.append(cellObj.value)

#final winter length calculation for 1994-1995 season for all of 24 Missouri stations

WL_40 = [] #all 1994-1995 winter lengths

try:
    winter_1994_1995_0 = ap1[0] + db[0]
except:
    winter_1994_1995_0 = None
WL_40.append(winter_1994_1995_0)
station0.append(winter_1994_1995_0)

try:
    winter_1994_1995_1 = aq1[1] + db[1]
except:
    winter_1994_1995_1 = None
WL_40.append(winter_1994_1995_1)
station1.append(winter_1994_1995_1)

try:
    winter_1994_1995_2 = aq1[2] + db[2]
except:
    winter_1994_1995_2 = None
WL_40.append(winter_1994_1995_2)
station2.append(winter_1994_1995_2)

try:
    winter_1994_1995_3 = aq1[3] + db[3]
except:
    winter_1994_1995_3 = None
WL_40.append(winter_1994_1995_3)
station3.append(winter_1994_1995_3)

try:
    winter_1994_1995_4 = aq1[4] + db[4]
except:
    winter_1994_1995_4 = None
WL_40.append(winter_1994_1995_4)
station4.append(winter_1994_1995_4)

try:
    winter_1994_1995_5 = aq1[5] + db[5]
except:
    winter_1994_1995_5 = None
WL_40.append(winter_1994_1995_5)
station5.append(winter_1994_1995_5)

try:
    winter_1994_1995_6 = aq1[6] + db[6]
except:
    winter_1994_1995_6 = None
WL_40.append(winter_1994_1995_6)
station6.append(winter_1994_1995_6)

try:
    winter_1994_1995_7 = aq1[7] + db[7]
except:
    winter_1994_1995_7 = None
WL_40.append(winter_1994_1995_7)
station7.append(winter_1994_1995_7)

try:
    winter_1994_1995_8 = aq1[8] + db[8]
except:
    winter_1994_1995_8 = None
WL_40.append(winter_1994_1995_8)
station8.append(winter_1994_1995_8)

try:
    winter_1994_1995_9 = aq1[9] + db[9]
except:
    winter_1994_1995_9 = None
WL_40.append(winter_1994_1995_9)
station9.append(winter_1994_1995_9)

try:
    winter_1994_1995_10 = aq1[10] + db[10]
except:
    winter_1994_1995_10 = None
WL_40.append(winter_1994_1995_10)
station10.append(winter_1994_1995_10)

try:
    winter_1994_1995_11 = aq1[11] + db[11]
except:
    winter_1994_1995_11 = None
WL_40.append(winter_1994_1995_11)
station11.append(winter_1994_1995_11)

try:
    winter_1994_1995_12 = aq1[12] + db[12]
except:
    winter_1994_1995_12 = None
WL_40.append(winter_1994_1995_12)
station12.append(winter_1994_1995_12)

try:
    winter_1994_1995_13 = aq1[13] + db[13]
except:
    winter_1994_1995_13 = None
WL_40.append(winter_1994_1995_13)
station13.append(winter_1994_1995_13)

try:
    winter_1994_1995_14 = aq1[14] + db[14]
except:
    winter_1994_1995_14 = None
WL_40.append(winter_1994_1995_14)
station14.append(winter_1994_1995_14)

try:
    winter_1994_1995_15 = aq1[15] + db[15]
except:
    winter_1994_1995_15 = None
WL_40.append(winter_1994_1995_15)
station15.append(winter_1994_1995_15)

try:
    winter_1994_1995_16 = aq1[16] + db[16]
except:
    winter_1994_1995_16 = None
WL_40.append(winter_1994_1995_16)
station16.append(winter_1994_1995_16)

try:
    winter_1994_1995_17 = aq1[17] + db[17]
except:
    winter_1994_1995_17 = None
WL_40.append(winter_1994_1995_17)
station17.append(winter_1994_1995_17)

try:
    winter_1994_1995_18 = aq1[18] + db[18]
except:
    winter_1994_1995_18 = None
WL_40.append(winter_1994_1995_18)
station18.append(winter_1994_1995_18)

try:
    winter_1994_1995_19 = aq1[19] + db[19]
except:
    winter_1994_1995_19 = None
WL_40.append(winter_1994_1995_19)
station19.append(winter_1994_1995_19)

try:
    winter_1994_1995_20 = aq1[20] + db[20]
except:
    winter_1994_1995_20 = None
WL_40.append(winter_1994_1995_20)
station20.append(winter_1994_1995_20)

try:
    winter_1994_1995_21 = aq1[21] + db[21]
except:
    winter_1994_1995_21 = None
WL_40.append(winter_1994_1995_21)
station21.append(winter_1994_1995_21)

try:
    winter_1994_1995_22 = aq1[22] + db[22]
except:
    winter_1994_1995_22 = None
WL_40.append(winter_1994_1995_22)
station22.append(winter_1994_1995_22)

try:
    winter_1994_1995_23 = aq1[23] + db[23]
except:
    winter_1994_1995_23 = None
WL_40.append(winter_1994_1995_23)
station23.append(winter_1994_1995_23)

#last spring freeze values for #1996

dc = []

for rowOfCellObjects in mosheet['GR2':'GR25']:
    for cellObj in rowOfCellObjects:
        dc.append(cellObj.value)

#final winter length calculation for 1995-1996 season for all of 24 Missouri stations

WL_41 = [] #all 1995-1996 winter lengths

try:
    winter_1995_1996_0 = ar1[0] + dc[0]
except:
    winter_1995_1996_0 = None
WL_41.append(winter_1995_1996_0)
station0.append(winter_1995_1996_0)

try:
    winter_1995_1996_1 = ar1[1] + dc[1]
except:
    winter_1995_1996_1 = None
WL_41.append(winter_1995_1996_1)
station1.append(winter_1995_1996_1)

try:
    winter_1995_1996_2 = ar1[2] + dc[2]
except:
    winter_1995_1996_2 = None
WL_41.append(winter_1995_1996_2)
station2.append(winter_1995_1996_2)

try:
    winter_1995_1996_3 = ar1[3] + dc[3]
except:
    winter_1995_1996_3 = None
WL_41.append(winter_1995_1996_3)
station3.append(winter_1995_1996_3)

try:
    winter_1995_1996_4 = ar1[4] + dc[4]
except:
    winter_1995_1996_4 = None
WL_41.append(winter_1995_1996_4)
station4.append(winter_1995_1996_4)

try:
    winter_1995_1996_5 = ar1[5] + dc[5]
except:
    winter_1995_1996_5 = None
WL_41.append(winter_1995_1996_5)
station5.append(winter_1995_1996_5)

try:
    winter_1995_1996_6 = ar1[6] + dc[6]
except:
    winter_1995_1996_6 = None
WL_41.append(winter_1995_1996_6)
station6.append(winter_1995_1996_6)

try:
    winter_1995_1996_7 = ar1[7] + dc[7]
except:
    winter_1995_1996_7 = None
WL_41.append(winter_1995_1996_7)
station7.append(winter_1995_1996_7)

try:
    winter_1995_1996_8 = ar1[8] + dc[8]
except:
    winter_1995_1996_8 = None
WL_41.append(winter_1995_1996_8)
station8.append(winter_1995_1996_8)

try:
    winter_1995_1996_9 = ar1[9] + dc[9]
except:
    winter_1995_1996_9 = None
WL_41.append(winter_1995_1996_9)
station9.append(winter_1995_1996_9)

try:
    winter_1995_1996_10 = ar1[10] + dc[10]
except:
    winter_1995_1996_10 = None
WL_41.append(winter_1995_1996_10)
station10.append(winter_1995_1996_10)

try:
    winter_1995_1996_11 = ar1[11] + dc[11]
except:
    winter_1995_1996_11 = None
WL_41.append(winter_1995_1996_11)
station11.append(winter_1995_1996_11)

try:
    winter_1995_1996_12 = ar1[12] + dc[12]
except:
    winter_1995_1996_12 = None
WL_41.append(winter_1995_1996_12)
station12.append(winter_1995_1996_12)

try:
    winter_1995_1996_13 = ar1[13] + dc[13]
except:
    winter_1995_1996_13 = None
WL_41.append(winter_1995_1996_13)
station13.append(winter_1995_1996_13)

try:
    winter_1995_1996_14 = ar1[14] + dc[14]
except:
    winter_1995_1996_14 = None
WL_41.append(winter_1995_1996_14)
station14.append(winter_1995_1996_14)

try:
    winter_1995_1996_15 = ar1[15] + dc[15]
except:
    winter_1995_1996_15 = None
WL_41.append(winter_1995_1996_15)
station15.append(winter_1995_1996_15)

try:
    winter_1995_1996_16 = ar1[16] + dc[16]
except:
    winter_1995_1996_16 = None
WL_41.append(winter_1995_1996_16)
station16.append(winter_1995_1996_16)

try:
    winter_1995_1996_17 = ar1[17] + dc[17]
except:
    winter_1995_1996_17 = None
WL_41.append(winter_1995_1996_17)
station17.append(winter_1995_1996_17)

try:
    winter_1995_1996_18 = ar1[18] + dc[18]
except:
    winter_1995_1996_18 = None
WL_41.append(winter_1995_1996_18)
station18.append(winter_1995_1996_18)

try:
    winter_1995_1996_19 = ar1[19] + dc[19]
except:
    winter_1995_1996_19 = None
WL_41.append(winter_1995_1996_19)
station19.append(winter_1995_1996_19)

try:
    winter_1995_1996_20 = ar1[20] + dc[20]
except:
    winter_1995_1996_20 = None
WL_41.append(winter_1995_1996_20)
station20.append(winter_1995_1996_20)

try:
    winter_1995_1996_21 = ar1[21] + dc[21]
except:
    winter_1995_1996_21 = None
WL_41.append(winter_1995_1996_21)
station21.append(winter_1995_1996_21)

try:
    winter_1995_1996_22 = ar1[22] + dc[22]
except:
    winter_1995_1996_22 = None
WL_41.append(winter_1995_1996_22)
station22.append(winter_1995_1996_22)

try:
    winter_1995_1996_23 = ar1[23] + dc[23]
except:
    winter_1995_1996_23 = None
WL_41.append(winter_1995_1996_23)
station23.append(winter_1995_1996_23)

#last spring freeze values for #1997

dd = []

for rowOfCellObjects in mosheet['GS2':'GS25']:
    for cellObj in rowOfCellObjects:
        dd.append(cellObj.value)

#final winter length calculation for 1996-1997 season for all of 24 Missouri stations

WL_42 = [] #all 1996-1997 winter lengths

try:
    winter_1996_1997_0 = at1[0] + dd[0]
except:
    winter_1996_1997_0 = None
WL_42.append(winter_1996_1997_0)
station0.append(winter_1996_1997_0)

try:
    winter_1996_1997_1 = at1[1] + dd[1]
except:
    winter_1996_1997_1 = None
WL_42.append(winter_1996_1997_1)
station1.append(winter_1996_1997_1)

try:
    winter_1996_1997_2 = at1[2] + dd[2]
except:
    winter_1996_1997_2 = None
WL_42.append(winter_1996_1997_2)
station2.append(winter_1996_1997_2)

try:
    winter_1996_1997_3 = at1[3] + dd[3]
except:
    winter_1996_1997_3 = None
WL_42.append(winter_1996_1997_3)
station3.append(winter_1996_1997_3)

try:
    winter_1996_1997_4 = at1[4] + dd[4]
except:
    winter_1996_1997_4 = None
WL_42.append(winter_1996_1997_4)
station4.append(winter_1996_1997_4)

try:
    winter_1996_1997_5 = at1[5] + dd[5]
except:
    winter_1996_1997_5 = None
WL_42.append(winter_1996_1997_5)
station5.append(winter_1996_1997_5)

try:
    winter_1996_1997_6 = at1[6] + dd[6]
except:
    winter_1996_1997_6 = None
WL_42.append(winter_1996_1997_6)
station6.append(winter_1996_1997_6)

try:
    winter_1996_1997_7 = at1[7] + dd[7]
except:
    winter_1996_1997_7 = None
WL_42.append(winter_1996_1997_7)
station7.append(winter_1996_1997_7)

try:
    winter_1996_1997_8 = at1[8] + dd[8]
except:
    winter_1996_1997_8 = None
WL_42.append(winter_1996_1997_8)
station8.append(winter_1996_1997_8)

try:
    winter_1996_1997_9 = at1[9] + dd[9]
except:
    winter_1996_1997_9 = None
WL_42.append(winter_1996_1997_9)
station9.append(winter_1996_1997_9)

try:
    winter_1996_1997_10 = at1[10] + dd[10]
except:
    winter_1996_1997_10 = None
WL_42.append(winter_1996_1997_10)
station10.append(winter_1996_1997_10)

try:
    winter_1996_1997_11 = at1[11] + dd[11]
except:
    winter_1996_1997_11 = None
WL_42.append(winter_1996_1997_11)
station11.append(winter_1996_1997_11)

try:
    winter_1996_1997_12 = at1[12] + dd[12]
except:
    winter_1996_1997_12 = None
WL_42.append(winter_1996_1997_12)
station12.append(winter_1996_1997_12)

try:
    winter_1996_1997_13 = at1[13] + dd[13]
except:
    winter_1996_1997_13 = None
WL_42.append(winter_1996_1997_13)
station13.append(winter_1996_1997_13)

try:
    winter_1996_1997_14 = at1[14] + dd[14]
except:
    winter_1996_1997_14 = None
WL_42.append(winter_1996_1997_14)
station14.append(winter_1996_1997_14)

try:
    winter_1996_1997_15 = at1[15] + dd[15]
except:
    winter_1996_1997_15 = None
WL_42.append(winter_1996_1997_15)
station15.append(winter_1996_1997_15)

try:
    winter_1996_1997_16 = at1[16] + dd[16]
except:
    winter_1996_1997_16 = None
WL_42.append(winter_1996_1997_16)
station16.append(winter_1996_1997_16)

try:
    winter_1996_1997_17 = at1[17] + dd[17]
except:
    winter_1996_1997_17 = None
WL_42.append(winter_1996_1997_17)
station17.append(winter_1996_1997_17)

try:
    winter_1996_1997_18 = at1[18] + dd[18]
except:
    winter_1996_1997_18 = None
WL_42.append(winter_1996_1997_18)
station18.append(winter_1996_1997_18)

try:
    winter_1996_1997_19 = at1[19] + dd[19]
except:
    winter_1996_1997_19 = None
WL_42.append(winter_1996_1997_19)
station19.append(winter_1996_1997_19)

try:
    winter_1996_1997_20 = at1[20] + dd[20]
except:
    winter_1996_1997_20 = None
WL_42.append(winter_1996_1997_20)
station20.append(winter_1996_1997_20)

try:
    winter_1996_1997_21 = at1[21] + dd[21]
except:
    winter_1996_1997_21 = None
WL_42.append(winter_1996_1997_21)
station21.append(winter_1996_1997_21)

try:
    winter_1996_1997_22 = at1[22] + dd[22]
except:
    winter_1996_1997_22 = None
WL_42.append(winter_1996_1997_22)
station22.append(winter_1996_1997_22)

try:
    winter_1996_1997_23 = at1[23] + dd[23]
except:
    winter_1996_1997_23 = None
WL_42.append(winter_1996_1997_23)
station23.append(winter_1996_1997_23)

#last spring freeze values for #1998

de = []

for rowOfCellObjects in mosheet['GT2':'GT25']:
    for cellObj in rowOfCellObjects:
        de.append(cellObj.value)

#final winter length calculation for 1997-1998 season for all of 24 Missouri stations

WL_43 = [] #all 1997-1998 winter lengths

try:
    winter_1997_1998_0 = au1[0] + de[0]
except:
    winter_1997_1998_0 = None
WL_43.append(winter_1997_1998_0)
station0.append(winter_1997_1998_0)

try:
    winter_1997_1998_1 = au1[1] + de[1]
except:
    winter_1997_1998_1 = None
WL_43.append(winter_1997_1998_1)
station1.append(winter_1997_1998_1)

try:
    winter_1997_1998_2 = au1[2] + de[2]
except:
    winter_1997_1998_2 = None
WL_43.append(winter_1997_1998_2)
station2.append(winter_1997_1998_2)

try:
    winter_1997_1998_3 = au1[3] + de[3]
except:
    winter_1997_1998_3 = None
WL_43.append(winter_1997_1998_3)
station3.append(winter_1997_1998_3)

try:
    winter_1997_1998_4 = au1[4] + de[4]
except:
    winter_1997_1998_4 = None
WL_43.append(winter_1997_1998_4)
station4.append(winter_1997_1998_4)

try:
    winter_1997_1998_5 = au1[5] + de[5]
except:
    winter_1997_1998_5 = None
WL_43.append(winter_1997_1998_5)
station5.append(winter_1997_1998_5)

try:
    winter_1997_1998_6 = au1[6] + de[6]
except:
    winter_1997_1998_6 = None
WL_43.append(winter_1997_1998_6)
station6.append(winter_1997_1998_6)

try:
    winter_1997_1998_7 = au1[7] + de[7]
except:
    winter_1997_1998_7 = None
WL_43.append(winter_1997_1998_7)
station7.append(winter_1997_1998_7)

try:
    winter_1997_1998_8 = au1[8] + de[8]
except:
    winter_1997_1998_8 = None
WL_43.append(winter_1997_1998_8)
station8.append(winter_1997_1998_8)

try:
    winter_1997_1998_9 = au1[9] + de[9]
except:
    winter_1997_1998_9 = None
WL_43.append(winter_1997_1998_9)
station9.append(winter_1997_1998_9)

try:
    winter_1997_1998_10 = au1[10] + de[10]
except:
    winter_1997_1998_10 = None
WL_43.append(winter_1997_1998_10)
station10.append(winter_1997_1998_10)

try:
    winter_1997_1998_11 = au1[11] + de[11]
except:
    winter_1997_1998_11 = None
WL_43.append(winter_1997_1998_11)
station11.append(winter_1997_1998_11)

try:
    winter_1997_1998_12 = au1[12] + de[12]
except:
    winter_1997_1998_12 = None
WL_43.append(winter_1997_1998_12)
station12.append(winter_1997_1998_12)

try:
    winter_1997_1998_13 = au1[13] + de[13]
except:
    winter_1997_1998_13 = None
WL_43.append(winter_1997_1998_13)
station13.append(winter_1997_1998_13)

try:
    winter_1997_1998_14 = au1[14] + de[14]
except:
    winter_1997_1998_14 = None
WL_43.append(winter_1997_1998_14)
station14.append(winter_1997_1998_14)

try:
    winter_1997_1998_15 = au1[15] + de[15]
except:
    winter_1997_1998_15 = None
WL_43.append(winter_1997_1998_15)
station15.append(winter_1997_1998_15)

try:
    winter_1997_1998_16 = au1[16] + de[16]
except:
    winter_1997_1998_16 = None
WL_43.append(winter_1997_1998_16)
station16.append(winter_1997_1998_16)

try:
    winter_1997_1998_17 = au1[17] + de[17]
except:
    winter_1997_1998_17 = None
WL_43.append(winter_1997_1998_17)
station17.append(winter_1997_1998_17)

try:
    winter_1997_1998_18 = au1[18] + de[18]
except:
    winter_1997_1998_18 = None
WL_43.append(winter_1997_1998_18)
station18.append(winter_1997_1998_18)

try:
    winter_1997_1998_19 = au1[19] + de[19]
except:
    winter_1997_1998_19 = None
WL_43.append(winter_1997_1998_19)
station19.append(winter_1997_1998_19)

try:
    winter_1997_1998_20 = au1[20] + de[20]
except:
    winter_1997_1998_20 = None
WL_43.append(winter_1997_1998_20)
station20.append(winter_1997_1998_20)

try:
    winter_1997_1998_21 = au1[21] + de[21]
except:
    winter_1997_1998_21 = None
WL_43.append(winter_1997_1998_21)
station21.append(winter_1997_1998_21)

try:
    winter_1997_1998_22 = au1[22] + de[22]
except:
    winter_1997_1998_22 = None
WL_43.append(winter_1997_1998_22)
station22.append(winter_1997_1998_22)

try:
    winter_1997_1998_23 = au1[23] + de[23]
except:
    winter_1997_1998_23 = None
WL_43.append(winter_1997_1998_23)
station23.append(winter_1997_1998_23)

#last spring freeze values for #1999

df = []

for rowOfCellObjects in mosheet['GU2':'GU25']:
    for cellObj in rowOfCellObjects:
        df.append(cellObj.value)

#final winter length calculation for 1998-1999 season for all of 24 Missouri stations

WL_44 = [] #all 1998-1999 winter lengths

try:
    winter_1998_1999_0 = av1[0] + df[0]
except:
    winter_1998_1999_0 = None
WL_44.append(winter_1998_1999_0)
station0.append(winter_1998_1999_0)

try:
    winter_1998_1999_1 = av1[1] + df[1]
except:
    winter_1998_1999_1 = None
WL_44.append(winter_1998_1999_1)
station1.append(winter_1998_1999_1)

try:
    winter_1998_1999_2 = av1[2] + df[2]
except:
    winter_1998_1999_2 = None
WL_44.append(winter_1998_1999_2)
station2.append(winter_1998_1999_2)

try:
    winter_1998_1999_3 = av1[3] + df[3]
except:
    winter_1998_1999_3 = None
WL_44.append(winter_1998_1999_3)
station3.append(winter_1998_1999_3)

try:
    winter_1998_1999_4 = av1[4] + df[4]
except:
    winter_1998_1999_4 = None
WL_44.append(winter_1998_1999_4)
station4.append(winter_1998_1999_4)

try:
    winter_1998_1999_5 = av1[5] + df[5]
except:
    winter_1998_1999_5 = None
WL_44.append(winter_1998_1999_5)
station5.append(winter_1998_1999_5)

try:
    winter_1998_1999_6 = av1[6] + df[6]
except:
    winter_1998_1999_6 = None
WL_44.append(winter_1998_1999_6)
station6.append(winter_1998_1999_6)

try:
    winter_1998_1999_7 = av1[7] + df[7]
except:
    winter_1998_1999_7 = None
WL_44.append(winter_1998_1999_7)
station7.append(winter_1998_1999_7)

try:
    winter_1998_1999_8 = av1[8] + df[8]
except:
    winter_1998_1999_8 = None
WL_44.append(winter_1998_1999_8)
station8.append(winter_1998_1999_8)

try:
    winter_1998_1999_9 = av1[9] + df[9]
except:
    winter_1998_1999_9 = None
WL_44.append(winter_1998_1999_9)
station9.append(winter_1998_1999_9)

try:
    winter_1998_1999_10 = av1[10] + df[10]
except:
    winter_1998_1999_10 = None
WL_44.append(winter_1998_1999_10)
station10.append(winter_1998_1999_10)

try:
    winter_1998_1999_11 = av1[11] + df[11]
except:
    winter_1998_1999_11 = None
WL_44.append(winter_1998_1999_11)
station11.append(winter_1998_1999_11)

try:
    winter_1998_1999_12 = av1[12] + df[12]
except:
    winter_1998_1999_12 = None
WL_44.append(winter_1998_1999_12)
station12.append(winter_1998_1999_12)

try:
    winter_1998_1999_13 = av1[13] + df[13]
except:
    winter_1998_1999_13 = None
WL_44.append(winter_1998_1999_13)
station13.append(winter_1998_1999_13)

try:
    winter_1998_1999_14 = av1[14] + df[14]
except:
    winter_1998_1999_14 = None
WL_44.append(winter_1998_1999_14)
station14.append(winter_1998_1999_14)

try:
    winter_1998_1999_15 = av1[15] + df[15]
except:
    winter_1998_1999_15 = None
WL_44.append(winter_1998_1999_15)
station15.append(winter_1998_1999_15)

try:
    winter_1998_1999_16 = av1[16] + df[16]
except:
    winter_1998_1999_16 = None
WL_44.append(winter_1998_1999_16)
station16.append(winter_1998_1999_16)

try:
    winter_1998_1999_17 = av1[17] + df[17]
except:
    winter_1998_1999_17 = None
WL_44.append(winter_1998_1999_17)
station17.append(winter_1998_1999_17)

try:
    winter_1998_1999_18 = av1[18] + df[18]
except:
    winter_1998_1999_18 = None
WL_44.append(winter_1998_1999_18)
station18.append(winter_1998_1999_18)

try:
    winter_1998_1999_19 = av1[19] + df[19]
except:
    winter_1998_1999_19 = None
WL_44.append(winter_1998_1999_19)
station19.append(winter_1998_1999_19)

try:
    winter_1998_1999_20 = av1[20] + df[20]
except:
    winter_1998_1999_20 = None
WL_44.append(winter_1998_1999_20)
station20.append(winter_1998_1999_20)

try:
    winter_1998_1999_21 = av1[21] + df[21]
except:
    winter_1998_1999_21 = None
WL_44.append(winter_1998_1999_21)
station21.append(winter_1998_1999_21)

try:
    winter_1998_1999_22 = av1[22] + df[22]
except:
    winter_1998_1999_22 = None
WL_44.append(winter_1998_1999_22)
station22.append(winter_1998_1999_22)

try:
    winter_1998_1999_23 = av1[23] + df[23]
except:
    winter_1998_1999_23 = None
WL_44.append(winter_1998_1999_23)
station23.append(winter_1998_1999_23)

#last spring freeze values for #2000

dg = []

for rowOfCellObjects in mosheet['GV2':'GV25']:
    for cellObj in rowOfCellObjects:
        dg.append(cellObj.value)

#final winter length calculation for 1999-2000 season for all of 24 Missouri stations

WL_45 = [] #all 1999-2000 winter lengths

try:
    winter_1999_2000_0 = aw1[0] + dg[0]
except:
    winter_1999_2000_0 = None
WL_45.append(winter_1999_2000_0)
station0.append(winter_1999_2000_0)

try:
    winter_1999_2000_1 = aw1[1] + dg[1]
except:
    winter_1999_2000_1 = None
WL_45.append(winter_1999_2000_1)
station1.append(winter_1999_2000_1)

try:
    winter_1999_2000_2 = aw1[2] + dg[2]
except:
    winter_1999_2000_2 = None
WL_45.append(winter_1999_2000_2)
station2.append(winter_1999_2000_2)

try:
    winter_1999_2000_3 = aw1[3] + dg[3]
except:
    winter_1999_2000_3 = None
WL_45.append(winter_1999_2000_3)
station3.append(winter_1999_2000_3)

try:
    winter_1999_2000_4 = aw1[4] + dg[4]
except:
    winter_1999_2000_4 = None
WL_45.append(winter_1999_2000_4)
station4.append(winter_1999_2000_4)

try:
    winter_1999_2000_5 = aw1[5] + dg[5]
except:
    winter_1999_2000_5 = None
WL_45.append(winter_1999_2000_5)
station5.append(winter_1999_2000_5)

try:
    winter_1999_2000_6 = aw1[6] + dg[6]
except:
    winter_1999_2000_6 = None
WL_45.append(winter_1999_2000_6)
station6.append(winter_1999_2000_6)

try:
    winter_1999_2000_7 = aw1[7] + dg[7]
except:
    winter_1999_2000_7 = None
WL_45.append(winter_1999_2000_7)
station7.append(winter_1999_2000_7)

try:
    winter_1999_2000_8 = aw1[8] + dg[8]
except:
    winter_1999_2000_8 = None
WL_45.append(winter_1999_2000_8)
station8.append(winter_1999_2000_8)

try:
    winter_1999_2000_9 = aw1[9] + dg[9]
except:
    winter_1999_2000_9 = None
WL_45.append(winter_1999_2000_9)
station9.append(winter_1999_2000_9)

try:
    winter_1999_2000_10 = aw1[10] + dg[10]
except:
    winter_1999_2000_10 = None
WL_45.append(winter_1999_2000_10)
station10.append(winter_1999_2000_10)

try:
    winter_1999_2000_11 = aw1[11] + dg[11]
except:
    winter_1999_2000_11 = None
WL_45.append(winter_1999_2000_11)
station11.append(winter_1999_2000_11)

try:
    winter_1999_2000_12 = aw1[12] + dg[12]
except:
    winter_1999_2000_12 = None
WL_45.append(winter_1999_2000_12)
station12.append(winter_1999_2000_12)

try:
    winter_1999_2000_13 = aw1[13] + dg[13]
except:
    winter_1999_2000_13 = None
WL_45.append(winter_1999_2000_13)
station13.append(winter_1999_2000_13)

try:
    winter_1999_2000_14 = aw1[14] + dg[14]
except:
    winter_1999_2000_14 = None
WL_45.append(winter_1999_2000_14)
station14.append(winter_1999_2000_14)

try:
    winter_1999_2000_15 = aw1[15] + dg[15]
except:
    winter_1999_2000_15 = None
WL_45.append(winter_1999_2000_15)
station15.append(winter_1999_2000_15)

try:
    winter_1999_2000_16 = aw1[16] + dg[16]
except:
    winter_1999_2000_16 = None
WL_45.append(winter_1999_2000_16)
station16.append(winter_1999_2000_16)

try:
    winter_1999_2000_17 = aw1[17] + dg[17]
except:
    winter_1999_2000_17 = None
WL_45.append(winter_1999_2000_17)
station17.append(winter_1999_2000_17)

try:
    winter_1999_2000_18 = aw1[18] + dg[18]
except:
    winter_1999_2000_18 = None
WL_45.append(winter_1999_2000_18)
station18.append(winter_1999_2000_18)

try:
    winter_1999_2000_19 = aw1[19] + dg[19]
except:
    winter_1999_2000_19 = None
WL_45.append(winter_1999_2000_19)
station19.append(winter_1999_2000_19)

try:
    winter_1999_2000_20 = aw1[20] + dg[20]
except:
    winter_1999_2000_20 = None
WL_45.append(winter_1999_2000_20)
station20.append(winter_1999_2000_20)

try:
    winter_1999_2000_21 = aw1[21] + dg[21]
except:
    winter_1999_2000_21 = None
WL_45.append(winter_1999_2000_21)
station21.append(winter_1999_2000_21)

try:
    winter_1999_2000_22 = aw1[22] + dg[22]
except:
    winter_1999_2000_22 = None
WL_45.append(winter_1999_2000_22)
station22.append(winter_1999_2000_22)

try:
    winter_1999_2000_23 = aw1[23] + dg[23]
except:
    winter_1999_2000_23 = None
WL_45.append(winter_1999_2000_23)
station23.append(winter_1999_2000_23)

#last spring freeze values for #2001

dh = []

for rowOfCellObjects in mosheet['GW2':'GW25']:
    for cellObj in rowOfCellObjects:
        dh.append(cellObj.value)

#final winter length calculation for 2000-2001 season for all of 24 Missouri stations

WL_46 = [] #all 2000-2001 winter lengths

try:
    winter_2000_2001_0 = ax1[0] + dh[0]
except:
    winter_2000_2001_0 = None
WL_46.append(winter_2000_2001_0)
station0.append(winter_2000_2001_0)

try:
    winter_2000_2001_1 = ax1[1] + dh[1]
except:
    winter_2000_2001_1 = None
WL_46.append(winter_2000_2001_1)
station1.append(winter_2000_2001_1)

try:
    winter_2000_2001_2 = ax1[2] + dh[2]
except:
    winter_2000_2001_2 = None
WL_46.append(winter_2000_2001_2)
station2.append(winter_2000_2001_2)

try:
    winter_2000_2001_3 = ax1[3] + dh[3]
except:
    winter_2000_2001_3 = None
WL_46.append(winter_2000_2001_3)
station3.append(winter_2000_2001_3)

try:
    winter_2000_2001_4 = ax1[4] + dh[4]
except:
    winter_2000_2001_4 = None
WL_46.append(winter_2000_2001_4)
station4.append(winter_2000_2001_4)

try:
    winter_2000_2001_5 = ax1[5] + dh[5]
except:
    winter_2000_2001_5 = None
WL_46.append(winter_2000_2001_5)
station5.append(winter_2000_2001_5)

try:
    winter_2000_2001_6 = ax1[6] + dh[6]
except:
    winter_2000_2001_6 = None
WL_46.append(winter_2000_2001_6)
station6.append(winter_2000_2001_6)

try:
    winter_2000_2001_7 = ax1[7] + dh[7]
except:
    winter_2000_2001_7 = None
WL_46.append(winter_2000_2001_7)
station7.append(winter_2000_2001_7)

try:
    winter_2000_2001_8 = ax1[8] + dh[8]
except:
    winter_2000_2001_8 = None
WL_46.append(winter_2000_2001_8)
station8.append(winter_2000_2001_8)

try:
    winter_2000_2001_9 = ax1[9] + dh[9]
except:
    winter_2000_2001_9 = None
WL_46.append(winter_2000_2001_9)
station9.append(winter_2000_2001_9)

try:
    winter_2000_2001_10 = ax1[10] + dh[10]
except:
    winter_2000_2001_10 = None
WL_46.append(winter_2000_2001_10)
station10.append(winter_2000_2001_10)

try:
    winter_2000_2001_11 = ax1[11] + dh[11]
except:
    winter_2000_2001_11 = None
WL_46.append(winter_2000_2001_11)
station11.append(winter_2000_2001_11)

try:
    winter_2000_2001_12 = ax1[12] + dh[12]
except:
    winter_2000_2001_12 = None
WL_46.append(winter_2000_2001_12)
station12.append(winter_2000_2001_12)

try:
    winter_2000_2001_13 = ax1[13] + dh[13]
except:
    winter_2000_2001_13 = None
WL_46.append(winter_2000_2001_13)
station13.append(winter_2000_2001_13)

try:
    winter_2000_2001_14 = ax1[14] + dh[14]
except:
    winter_2000_2001_14 = None
WL_46.append(winter_2000_2001_14)
station14.append(winter_2000_2001_14)

try:
    winter_2000_2001_15 = ax1[15] + dh[15]
except:
    winter_2000_2001_15 = None
WL_46.append(winter_2000_2001_15)
station15.append(winter_2000_2001_15)

try:
    winter_2000_2001_16 = ax1[16] + dh[16]
except:
    winter_2000_2001_16 = None
WL_46.append(winter_2000_2001_16)
station16.append(winter_2000_2001_16)

try:
    winter_2000_2001_17 = ax1[17] + dh[17]
except:
    winter_2000_2001_17 = None
WL_46.append(winter_2000_2001_17)
station17.append(winter_2000_2001_17)

try:
    winter_2000_2001_18 = ax1[18] + dh[18]
except:
    winter_2000_2001_18 = None
WL_46.append(winter_2000_2001_18)
station18.append(winter_2000_2001_18)

try:
    winter_2000_2001_19 = ax1[19] + dh[19]
except:
    winter_2000_2001_19 = None
WL_46.append(winter_2000_2001_19)
station19.append(winter_2000_2001_19)

try:
    winter_2000_2001_20 = ax1[20] + dh[20]
except:
    winter_2000_2001_20 = None
WL_46.append(winter_2000_2001_20)
station20.append(winter_2000_2001_20)

try:
    winter_2000_2001_21 = ax1[21] + dh[21]
except:
    winter_2000_2001_21 = None
WL_46.append(winter_2000_2001_21)
station21.append(winter_2000_2001_21)

try:
    winter_2000_2001_22 = ax1[22] + dh[22]
except:
    winter_2000_2001_22 = None
WL_46.append(winter_2000_2001_22)
station22.append(winter_2000_2001_22)

try:
    winter_2000_2001_23 = ax1[23] + dh[23]
except:
    winter_2000_2001_23 = None
WL_46.append(winter_2000_2001_23)
station23.append(winter_2000_2001_23)

#last spring freeze values for #2002

di = []

for rowOfCellObjects in mosheet['GX2':'GX25']:
    for cellObj in rowOfCellObjects:
        di.append(cellObj.value)

#final winter length calculation for 2001-2002 season for all of 24 Missouri stations

WL_47 = [] #all 2001-2002 winter lengths

try:
    winter_2001_2002_0 = ay1[0] + di[0]
except:
    winter_2001_2002_0 = None
WL_47.append(winter_2001_2002_0)
station0.append(winter_2001_2002_0)

try:
    winter_2001_2002_1 = ay1[1] + di[1]
except:
    winter_2001_2002_1 = None
WL_47.append(winter_2001_2002_1)
station1.append(winter_2001_2002_1)

try:
    winter_2001_2002_2 = ay1[2] + di[2]
except:
    winter_2001_2002_2 = None
WL_47.append(winter_2001_2002_2)
station2.append(winter_2001_2002_2)

try:
    winter_2001_2002_3 = ay1[3] + di[3]
except:
    winter_2001_2002_3 = None
WL_47.append(winter_2001_2002_3)
station3.append(winter_2001_2002_3)

try:
    winter_2001_2002_4 = ay1[4] + di[4]
except:
    winter_2001_2002_4 = None
WL_47.append(winter_2001_2002_4)
station4.append(winter_2001_2002_4)

try:
    winter_2001_2002_5 = ay1[5] + di[5]
except:
    winter_2001_2002_5 = None
WL_47.append(winter_2001_2002_5)
station5.append(winter_2001_2002_5)

try:
    winter_2001_2002_6 = ay1[6] + di[6]
except:
    winter_2001_2002_6 = None
WL_47.append(winter_2001_2002_6)
station6.append(winter_2001_2002_6)

try:
    winter_2001_2002_7 = ay1[7] + di[7]
except:
    winter_2001_2002_7 = None
WL_47.append(winter_2001_2002_7)
station7.append(winter_2001_2002_7)

try:
    winter_2001_2002_8 = ay1[8] + di[8]
except:
    winter_2001_2002_8 = None
WL_47.append(winter_2001_2002_8)
station8.append(winter_2001_2002_8)

try:
    winter_2001_2002_9 = ay1[9] + di[9]
except:
    winter_2001_2002_9 = None
WL_47.append(winter_2001_2002_9)
station9.append(winter_2001_2002_9)

try:
    winter_2001_2002_10 = ay1[10] + di[10]
except:
    winter_2001_2002_10 = None
WL_47.append(winter_2001_2002_10)
station10.append(winter_2001_2002_10)

try:
    winter_2001_2002_11 = ay1[11] + di[11]
except:
    winter_2001_2002_11 = None
WL_47.append(winter_2001_2002_11)
station11.append(winter_2001_2002_11)

try:
    winter_2001_2002_12 = ay1[12] + di[12]
except:
    winter_2001_2002_12 = None
WL_47.append(winter_2001_2002_12)
station12.append(winter_2001_2002_12)

try:
    winter_2001_2002_13 = ay1[13] + di[13]
except:
    winter_2001_2002_13 = None
WL_47.append(winter_2001_2002_13)
station13.append(winter_2001_2002_13)

try:
    winter_2001_2002_14 = ay1[14] + di[14]
except:
    winter_2001_2002_14 = None
WL_47.append(winter_2001_2002_14)
station14.append(winter_2001_2002_14)

try:
    winter_2001_2002_15 = ay1[15] + di[15]
except:
    winter_2001_2002_15 = None
WL_47.append(winter_2001_2002_15)
station15.append(winter_2001_2002_15)

try:
    winter_2001_2002_16 = ay1[16] + di[16]
except:
    winter_2001_2002_16 = None
WL_47.append(winter_2001_2002_16)
station16.append(winter_2001_2002_16)

try:
    winter_2001_2002_17 = ay1[17] + di[17]
except:
    winter_2001_2002_17 = None
WL_47.append(winter_2001_2002_17)
station17.append(winter_2001_2002_17)

try:
    winter_2001_2002_18 = ay1[18] + di[18]
except:
    winter_2001_2002_18 = None
WL_47.append(winter_2001_2002_18)
station18.append(winter_2001_2002_18)

try:
    winter_2001_2002_19 = ay1[19] + di[19]
except:
    winter_2001_2002_19 = None
WL_47.append(winter_2001_2002_19)
station19.append(winter_2001_2002_19)

try:
    winter_2001_2002_20 = ay1[20] + di[20]
except:
    winter_2001_2002_20 = None
WL_47.append(winter_2001_2002_20)
station20.append(winter_2001_2002_20)

try:
    winter_2001_2002_21 = ay1[21] + di[21]
except:
    winter_2001_2002_21 = None
WL_47.append(winter_2001_2002_21)
station21.append(winter_2001_2002_21)

try:
    winter_2001_2002_22 = ay1[22] + di[22]
except:
    winter_2001_2002_22 = None
WL_47.append(winter_2001_2002_22)
station22.append(winter_2001_2002_22)

try:
    winter_2001_2002_23 = ay1[23] + di[23]
except:
    winter_2001_2002_23 = None
WL_47.append(winter_2001_2002_23)
station23.append(winter_2001_2002_23)

#last spring freeze values for #2003

dj = []

for rowOfCellObjects in mosheet['GY2':'GY25']:
    for cellObj in rowOfCellObjects:
        dj.append(cellObj.value)

#final winter length calculation for 2002-2003 season for all of 24 Missouri stations

WL_48 = [] #all 2002-2003 winter lengths

try:
    winter_2002_2003_0 = az1[0] + dj[0]
except:
    winter_2002_2003_0 = None
WL_48.append(winter_2002_2003_0)
station0.append(winter_2002_2003_0)

try:
    winter_2002_2003_1 = az1[1] + dj[1]
except:
    winter_2002_2003_1 = None
WL_48.append(winter_2002_2003_1)
station1.append(winter_2002_2003_1)

try:
    winter_2002_2003_2 = az1[2] + dj[2]
except:
    winter_2002_2003_2 = None
WL_48.append(winter_2002_2003_2)
station2.append(winter_2002_2003_2)

try:
    winter_2002_2003_3 = az1[3] + dj[3]
except:
    winter_2002_2003_3 = None
WL_48.append(winter_2002_2003_3)
station3.append(winter_2002_2003_3)

try:
    winter_2002_2003_4 = az1[4] + dj[4]
except:
    winter_2002_2003_4 = None
WL_48.append(winter_2002_2003_4)
station4.append(winter_2002_2003_4)

try:
    winter_2002_2003_5 = az1[5] + dj[5]
except:
    winter_2002_2003_5 = None
WL_48.append(winter_2002_2003_5)
station5.append(winter_2002_2003_5)

try:
    winter_2002_2003_6 = az1[6] + dj[6]
except:
    winter_2002_2003_6 = None
WL_48.append(winter_2002_2003_6)
station6.append(winter_2002_2003_6)

try:
    winter_2002_2003_7 = az1[7] + dj[7]
except:
    winter_2002_2003_7 = None
WL_48.append(winter_2002_2003_7)
station7.append(winter_2002_2003_7)

try:
    winter_2002_2003_8 = az1[8] + dj[8]
except:
    winter_2002_2003_8 = None
WL_48.append(winter_2002_2003_8)
station8.append(winter_2002_2003_8)

try:
    winter_2002_2003_9 = az1[9] + dj[9]
except:
    winter_2002_2003_9 = None
WL_48.append(winter_2002_2003_9)
station9.append(winter_2002_2003_9)

try:
    winter_2002_2003_10 = az1[10] + dj[10]
except:
    winter_2002_2003_10 = None
WL_48.append(winter_2002_2003_10)
station10.append(winter_2002_2003_10)

try:
    winter_2002_2003_11 = az1[11] + dj[11]
except:
    winter_2002_2003_11 = None
WL_48.append(winter_2002_2003_11)
station11.append(winter_2002_2003_11)

try:
    winter_2002_2003_12 = az1[12] + dj[12]
except:
    winter_2002_2003_12 = None
WL_48.append(winter_2002_2003_12)
station12.append(winter_2002_2003_12)

try:
    winter_2002_2003_13 = az1[13] + dj[13]
except:
    winter_2002_2003_13 = None
WL_48.append(winter_2002_2003_13)
station13.append(winter_2002_2003_13)

try:
    winter_2002_2003_14 = az1[14] + dj[14]
except:
    winter_2002_2003_14 = None
WL_48.append(winter_2002_2003_14)
station14.append(winter_2002_2003_14)

try:
    winter_2002_2003_15 = az1[15] + dj[15]
except:
    winter_2002_2003_15 = None
WL_48.append(winter_2002_2003_15)
station15.append(winter_2002_2003_15)

try:
    winter_2002_2003_16 = az1[16] + dj[16]
except:
    winter_2002_2003_16 = None
WL_48.append(winter_2002_2003_16)
station16.append(winter_2002_2003_16)

try:
    winter_2002_2003_17 = az1[17] + dj[17]
except:
    winter_2002_2003_17 = None
WL_48.append(winter_2002_2003_17)
station17.append(winter_2002_2003_17)

try:
    winter_2002_2003_18 = az1[18] + dj[18]
except:
    winter_2002_2003_18 = None
WL_48.append(winter_2002_2003_18)
station18.append(winter_2002_2003_18)

try:
    winter_2002_2003_19 = az1[19] + dj[19]
except:
    winter_2002_2003_19 = None
WL_48.append(winter_2002_2003_19)
station19.append(winter_2002_2003_19)

try:
    winter_2002_2003_20 = az1[20] + dj[20]
except:
    winter_2002_2003_20 = None
WL_48.append(winter_2002_2003_20)
station20.append(winter_2002_2003_20)

try:
    winter_2002_2003_21 = az1[21] + dj[21]
except:
    winter_2002_2003_21 = None
WL_48.append(winter_2002_2003_21)
station21.append(winter_2002_2003_21)

try:
    winter_2002_2003_22 = az1[22] + dj[22]
except:
    winter_2002_2003_22 = None
WL_48.append(winter_2002_2003_22)
station22.append(winter_2002_2003_22)

try:
    winter_2002_2003_23 = az1[23] + dj[23]
except:
    winter_2002_2003_23 = None
WL_48.append(winter_2002_2003_23)
station23.append(winter_2002_2003_23)

#last spring freeze values for #2004

dk = []

for rowOfCellObjects in mosheet['GZ2':'GZ25']:
    for cellObj in rowOfCellObjects:
        dk.append(cellObj.value)

#final winter length calculation for 2003-2004 season for all of 24 Missouri stations

WL_49 = [] #all 2003-2004 winter lengths

try:
    winter_2003_2004_0 = cf1[0] + dk[0]
except:
    winter_2003_2004_0 = None
WL_49.append(winter_2003_2004_0)
station0.append(winter_2003_2004_0)

try:
    winter_2003_2004_1 = cf1[1] + dk[1]
except:
    winter_2003_2004_1 = None
WL_49.append(winter_2003_2004_1)
station1.append(winter_2003_2004_1)

try:
    winter_2003_2004_2 = cf1[2] + dk[2]
except:
    winter_2003_2004_2 = None
WL_49.append(winter_2003_2004_2)
station2.append(winter_2003_2004_2)

try:
    winter_2003_2004_3 = cf1[3] + dk[3]
except:
    winter_2003_2004_3 = None
WL_49.append(winter_2003_2004_3)
station3.append(winter_2003_2004_3)

try:
    winter_2003_2004_4 = cf1[4] + dk[4]
except:
    winter_2003_2004_4 = None
WL_49.append(winter_2003_2004_4)
station4.append(winter_2003_2004_4)

try:
    winter_2003_2004_5 = cf1[5] + dk[5]
except:
    winter_2003_2004_5 = None
WL_49.append(winter_2003_2004_5)
station5.append(winter_2003_2004_5)

try:
    winter_2003_2004_6 = cf1[6] + dk[6]
except:
    winter_2003_2004_6 = None
WL_49.append(winter_2003_2004_6)
station6.append(winter_2003_2004_6)

try:
    winter_2003_2004_7 = cf1[7] + dk[7]
except:
    winter_2003_2004_7 = None
WL_49.append(winter_2003_2004_7)
station7.append(winter_2003_2004_7)

try:
    winter_2003_2004_8 = cf1[8] + dk[8]
except:
    winter_2003_2004_8 = None
WL_49.append(winter_2003_2004_8)
station8.append(winter_2003_2004_8)

try:
    winter_2003_2004_9 = cf1[9] + dk[9]
except:
    winter_2003_2004_9 = None
WL_49.append(winter_2003_2004_9)
station9.append(winter_2003_2004_9)

try:
    winter_2003_2004_10 = cf1[10] + dk[10]
except:
    winter_2003_2004_10 = None
WL_49.append(winter_2003_2004_10)
station10.append(winter_2003_2004_10)

try:
    winter_2003_2004_11 = cf1[11] + dk[11]
except:
    winter_2003_2004_11 = None
WL_49.append(winter_2003_2004_11)
station11.append(winter_2003_2004_11)

try:
    winter_2003_2004_12 = cf1[12] + dk[12]
except:
    winter_2003_2004_12 = None
WL_49.append(winter_2003_2004_12)
station12.append(winter_2003_2004_12)

try:
    winter_2003_2004_13 = cf1[13] + dk[13]
except:
    winter_2003_2004_13 = None
WL_49.append(winter_2003_2004_13)
station13.append(winter_2003_2004_13)

try:
    winter_2003_2004_14 = cf1[14] + dk[14]
except:
    winter_2003_2004_14 = None
WL_49.append(winter_2003_2004_14)
station14.append(winter_2003_2004_14)

try:
    winter_2003_2004_15 = cf1[15] + dk[15]
except:
    winter_2003_2004_15 = None
WL_49.append(winter_2003_2004_15)
station15.append(winter_2003_2004_15)

try:
    winter_2003_2004_16 = cf1[16] + dk[16]
except:
    winter_2003_2004_16 = None
WL_49.append(winter_2003_2004_16)
station16.append(winter_2003_2004_16)

try:
    winter_2003_2004_17 = cf1[17] + dk[17]
except:
    winter_2003_2004_17 = None
WL_49.append(winter_2003_2004_17)
station17.append(winter_2003_2004_17)

try:
    winter_2003_2004_18 = cf1[18] + dk[18]
except:
    winter_2003_2004_18 = None
WL_49.append(winter_2003_2004_18)
station18.append(winter_2003_2004_18)

try:
    winter_2003_2004_19 = cf1[19] + dk[19]
except:
    winter_2003_2004_19 = None
WL_49.append(winter_2003_2004_19)
station19.append(winter_2003_2004_19)

try:
    winter_2003_2004_20 = cf1[20] + dk[20]
except:
    winter_2003_2004_20 = None
WL_49.append(winter_2003_2004_20)
station20.append(winter_2003_2004_20)

try:
    winter_2003_2004_21 = cf1[21] + dk[21]
except:
    winter_2003_2004_21 = None
WL_49.append(winter_2003_2004_21)
station21.append(winter_2003_2004_21)

try:
    winter_2003_2004_22 = cf1[22] + dk[22]
except:
    winter_2003_2004_22 = None
WL_49.append(winter_2003_2004_22)
station22.append(winter_2003_2004_22)

try:
    winter_2003_2004_23 = cf1[23] + dk[23]
except:
    winter_2003_2004_23 = None
WL_49.append(winter_2003_2004_23)
station23.append(winter_2003_2004_23)

#last spring freeze values for #2005

dl = []

for rowOfCellObjects in mosheet['HA2':'HA25']:
    for cellObj in rowOfCellObjects:
        dl.append(cellObj.value)

#final winter length calculation for 2004-2005 season for all of 24 Missouri stations

WL_50 = [] #all 2004-2005 winter lengths

try:
    winter_2004_2005_0 = cg1[0] + dl[0]
except:
    winter_2004_2005_0 = None
WL_50.append(winter_2004_2005_0)
station0.append(winter_2004_2005_0)

try:
    winter_2004_2005_1 = cg1[1] + dl[1]
except:
    winter_2004_2005_1 = None
WL_50.append(winter_2004_2005_1)
station1.append(winter_2004_2005_1)

try:
    winter_2004_2005_2 = cg1[2] + dl[2]
except:
    winter_2004_2005_2 = None
WL_50.append(winter_2004_2005_2)
station2.append(winter_2004_2005_2)

try:
    winter_2004_2005_3 = cg1[3] + dl[3]
except:
    winter_2004_2005_3 = None
WL_50.append(winter_2004_2005_3)
station3.append(winter_2004_2005_3)

try:
    winter_2004_2005_4 = cg1[4] + dl[4]
except:
    winter_2004_2005_4 = None
WL_50.append(winter_2004_2005_4)
station4.append(winter_2004_2005_4)

try:
    winter_2004_2005_5 = cg1[5] + dl[5]
except:
    winter_2004_2005_5 = None
WL_50.append(winter_2004_2005_5)
station5.append(winter_2004_2005_5)

try:
    winter_2004_2005_6 = cg1[6] + dl[6]
except:
    winter_2004_2005_6 = None
WL_50.append(winter_2004_2005_6)
station6.append(winter_2004_2005_6)

try:
    winter_2004_2005_7 = cg1[7] + dl[7]
except:
    winter_2004_2005_7 = None
WL_50.append(winter_2004_2005_7)
station7.append(winter_2004_2005_7)

try:
    winter_2004_2005_8 = cg1[8] + dl[8]
except:
    winter_2004_2005_8 = None
WL_50.append(winter_2004_2005_8)
station8.append(winter_2004_2005_8)

try:
    winter_2004_2005_9 = cg1[9] + dl[9]
except:
    winter_2004_2005_9 = None
WL_50.append(winter_2004_2005_9)
station9.append(winter_2004_2005_9)

try:
    winter_2004_2005_10 = cg1[10] + dl[10]
except:
    winter_2004_2005_10 = None
WL_50.append(winter_2004_2005_10)
station10.append(winter_2004_2005_10)

try:
    winter_2004_2005_11 = cg1[11] + dl[11]
except:
    winter_2004_2005_11 = None
WL_50.append(winter_2004_2005_11)
station11.append(winter_2004_2005_11)

try:
    winter_2004_2005_12 = cg1[12] + dl[12]
except:
    winter_2004_2005_12 = None
WL_50.append(winter_2004_2005_12)
station12.append(winter_2004_2005_12)

try:
    winter_2004_2005_13 = cg1[13] + dl[13]
except:
    winter_2004_2005_13 = None
WL_50.append(winter_2004_2005_13)
station13.append(winter_2004_2005_13)

try:
    winter_2004_2005_14 = cg1[14] + dl[14]
except:
    winter_2004_2005_14 = None
WL_50.append(winter_2004_2005_14)
station14.append(winter_2004_2005_14)

try:
    winter_2004_2005_15 = cg1[15] + dl[15]
except:
    winter_2004_2005_15 = None
WL_50.append(winter_2004_2005_15)
station15.append(winter_2004_2005_15)

try:
    winter_2004_2005_16 = cg1[16] + dl[16]
except:
    winter_2004_2005_16 = None
WL_50.append(winter_2004_2005_16)
station16.append(winter_2004_2005_16)

try:
    winter_2004_2005_17 = cg1[17] + dl[17]
except:
    winter_2004_2005_17 = None
WL_50.append(winter_2004_2005_17)
station17.append(winter_2004_2005_17)

try:
    winter_2004_2005_18 = cg1[18] + dl[18]
except:
    winter_2004_2005_18 = None
WL_50.append(winter_2004_2005_18)
station18.append(winter_2004_2005_18)

try:
    winter_2004_2005_19 = cg1[19] + dl[19]
except:
    winter_2004_2005_19 = None
WL_50.append(winter_2004_2005_19)
station19.append(winter_2004_2005_19)

try:
    winter_2004_2005_20 = cg1[20] + dl[20]
except:
    winter_2004_2005_20 = None
WL_50.append(winter_2004_2005_20)
station20.append(winter_2004_2005_20)

try:
    winter_2004_2005_21 = cg1[21] + dl[21]
except:
    winter_2004_2005_21 = None
WL_50.append(winter_2004_2005_21)
station21.append(winter_2004_2005_21)

try:
    winter_2004_2005_22 = cg1[22] + dl[22]
except:
    winter_2004_2005_22 = None
WL_50.append(winter_2004_2005_22)
station22.append(winter_2004_2005_22)

try:
    winter_2004_2005_23 = cg1[23] + dl[23]
except:
    winter_2004_2005_23 = None
WL_50.append(winter_2004_2005_23)
station23.append(winter_2004_2005_23)

#last spring freeze values for #2006

dm = []

for rowOfCellObjects in mosheet['HB2':'HB25']:
    for cellObj in rowOfCellObjects:
        dm.append(cellObj.value)

#final winter length calculation for 2005-2006 season for all of 24 Missouri stations

WL_51 = [] #all 2005-2006 winter lengths

try:
    winter_2005_2006_0 = ch1[0] + dm[0]
except:
    winter_2005_2006_0 = None
WL_51.append(winter_2005_2006_0)
station0.append(winter_2005_2006_0)

try:
    winter_2005_2006_1 = ch1[1] + dm[1]
except:
    winter_2005_2006_1 = None
WL_51.append(winter_2005_2006_1)
station1.append(winter_2005_2006_1)

try:
    winter_2005_2006_2 = ch1[2] + dm[2]
except:
    winter_2005_2006_2 = None
WL_51.append(winter_2005_2006_2)
station2.append(winter_2005_2006_2)

try:
    winter_2005_2006_3 = ch1[3] + dm[3]
except:
    winter_2005_2006_3 = None
WL_51.append(winter_2005_2006_3)
station3.append(winter_2005_2006_3)

try:
    winter_2005_2006_4 = ch1[4] + dm[4]
except:
    winter_2005_2006_4 = None
WL_51.append(winter_2005_2006_4)
station4.append(winter_2005_2006_4)

try:
    winter_2005_2006_5 = ch1[5] + dm[5]
except:
    winter_2005_2006_5 = None
WL_51.append(winter_2005_2006_5)
station5.append(winter_2005_2006_5)

try:
    winter_2005_2006_6 = ch1[6] + dm[6]
except:
    winter_2005_2006_6 = None
WL_51.append(winter_2005_2006_6)
station6.append(winter_2005_2006_6)

try:
    winter_2005_2006_7 = ch1[7] + dm[7]
except:
    winter_2005_2006_7 = None
WL_51.append(winter_2005_2006_7)
station7.append(winter_2005_2006_7)

try:
    winter_2005_2006_8 = ch1[8] + dm[8]
except:
    winter_2005_2006_8 = None
WL_51.append(winter_2005_2006_8)
station8.append(winter_2005_2006_8)

try:
    winter_2005_2006_9 = ch1[9] + dm[9]
except:
    winter_2005_2006_9 = None
WL_51.append(winter_2005_2006_9)
station9.append(winter_2005_2006_9)

try:
    winter_2005_2006_10 = ch1[10] + dm[10]
except:
    winter_2005_2006_10 = None
WL_51.append(winter_2005_2006_10)
station10.append(winter_2005_2006_10)

try:
    winter_2005_2006_11 = ch1[11] + dm[11]
except:
    winter_2005_2006_11 = None
WL_51.append(winter_2005_2006_11)
station11.append(winter_2005_2006_11)

try:
    winter_2005_2006_12 = ch1[12] + dm[12]
except:
    winter_2005_2006_12 = None
WL_51.append(winter_2005_2006_12)
station12.append(winter_2005_2006_12)

try:
    winter_2005_2006_13 = ch1[13] + dm[13]
except:
    winter_2005_2006_13 = None
WL_51.append(winter_2005_2006_13)
station13.append(winter_2005_2006_13)

try:
    winter_2005_2006_14 = ch1[14] + dm[14]
except:
    winter_2005_2006_14 = None
WL_51.append(winter_2005_2006_14)
station14.append(winter_2005_2006_14)

try:
    winter_2005_2006_15 = ch1[15] + dm[15]
except:
    winter_2005_2006_15 = None
WL_51.append(winter_2005_2006_15)
station15.append(winter_2005_2006_15)

try:
    winter_2005_2006_16 = ch1[16] + dm[16]
except:
    winter_2005_2006_16 = None
WL_51.append(winter_2005_2006_16)
station16.append(winter_2005_2006_16)

try:
    winter_2005_2006_17 = ch1[17] + dm[17]
except:
    winter_2005_2006_17 = None
WL_51.append(winter_2005_2006_17)
station17.append(winter_2005_2006_17)

try:
    winter_2005_2006_18 = ch1[18] + dm[18]
except:
    winter_2005_2006_18 = None
WL_51.append(winter_2005_2006_18)
station18.append(winter_2005_2006_18)

try:
    winter_2005_2006_19 = ch1[19] + dm[19]
except:
    winter_2005_2006_19 = None
WL_51.append(winter_2005_2006_19)
station19.append(winter_2005_2006_19)

try:
    winter_2005_2006_20 = ch1[20] + dm[20]
except:
    winter_2005_2006_20 = None
WL_51.append(winter_2005_2006_20)
station20.append(winter_2005_2006_20)

try:
    winter_2005_2006_21 = ch1[21] + dm[21]
except:
    winter_2005_2006_21 = None
WL_51.append(winter_2005_2006_21)
station21.append(winter_2005_2006_21)

try:
    winter_2005_2006_22 = ch1[22] + dm[22]
except:
    winter_2005_2006_22 = None
WL_51.append(winter_2005_2006_22)
station22.append(winter_2005_2006_22)

try:
    winter_2005_2006_23 = ch1[23] + dm[23]
except:
    winter_2005_2006_23 = None
WL_51.append(winter_2005_2006_23)
station23.append(winter_2005_2006_23)

#last spring freeze values for #2007

dn = []

for rowOfCellObjects in mosheet['HC2':'HC25']:
    for cellObj in rowOfCellObjects:
        dn.append(cellObj.value)

#final winter length calculation for 2006-2007 season for all of 24 Missouri stations

WL_52 = [] #all 2006-2007 winter lengths

try:
    winter_2006_2007_0 = ci1[0] + dn[0]
except:
    winter_2006_2007_0 = None
WL_52.append(winter_2006_2007_0)
station0.append(winter_2006_2007_0)

try:
    winter_2006_2007_1 = ci1[1] + dn[1]
except:
    winter_2006_2007_1 = None
WL_52.append(winter_2006_2007_1)
station1.append(winter_2006_2007_1)

try:
    winter_2006_2007_2 = ci1[2] + dn[2]
except:
    winter_2006_2007_2 = None
WL_52.append(winter_2006_2007_2)
station2.append(winter_2006_2007_2)

try:
    winter_2006_2007_3 = ci1[3] + dn[3]
except:
    winter_2006_2007_3 = None
WL_52.append(winter_2006_2007_3)
station3.append(winter_2006_2007_3)

try:
    winter_2006_2007_4 = ci1[4] + dn[4]
except:
    winter_2006_2007_4 = None
WL_52.append(winter_2006_2007_4)
station4.append(winter_2006_2007_4)

try:
    winter_2006_2007_5 = ci1[5] + dn[5]
except:
    winter_2006_2007_5 = None
WL_52.append(winter_2006_2007_5)
station5.append(winter_2006_2007_5)

try:
    winter_2006_2007_6 = ci1[6] + dn[6]
except:
    winter_2006_2007_6 = None
WL_52.append(winter_2006_2007_6)
station6.append(winter_2006_2007_6)

try:
    winter_2006_2007_7 = ci1[7] + dn[7]
except:
    winter_2006_2007_7 = None
WL_52.append(winter_2006_2007_7)
station7.append(winter_2006_2007_7)

try:
    winter_2006_2007_8 = ci1[8] + dn[8]
except:
    winter_2006_2007_8 = None
WL_52.append(winter_2006_2007_8)
station8.append(winter_2006_2007_8)

try:
    winter_2006_2007_9 = ci1[9] + dn[9]
except:
    winter_2006_2007_9 = None
WL_52.append(winter_2006_2007_9)
station9.append(winter_2006_2007_9)

try:
    winter_2006_2007_10 = ci1[10] + dn[10]
except:
    winter_2006_2007_10 = None
WL_52.append(winter_2006_2007_10)
station10.append(winter_2006_2007_10)

try:
    winter_2006_2007_11 = ci1[11] + dn[11]
except:
    winter_2006_2007_11 = None
WL_52.append(winter_2006_2007_11)
station11.append(winter_2006_2007_11)

try:
    winter_2006_2007_12 = ci1[12] + dn[12]
except:
    winter_2006_2007_12 = None
WL_52.append(winter_2006_2007_12)
station12.append(winter_2006_2007_12)

try:
    winter_2006_2007_13 = ci1[13] + dn[13]
except:
    winter_2006_2007_13 = None
WL_52.append(winter_2006_2007_13)
station13.append(winter_2006_2007_13)

try:
    winter_2006_2007_14 = ci1[14] + dn[14]
except:
    winter_2006_2007_14 = None
WL_52.append(winter_2006_2007_14)
station14.append(winter_2006_2007_14)

try:
    winter_2006_2007_15 = ci1[15] + dn[15]
except:
    winter_2006_2007_15 = None
WL_52.append(winter_2006_2007_15)
station15.append(winter_2006_2007_15)

try:
    winter_2006_2007_16 = ci1[16] + dn[16]
except:
    winter_2006_2007_16 = None
WL_52.append(winter_2006_2007_16)
station16.append(winter_2006_2007_16)

try:
    winter_2006_2007_17 = ci1[17] + dn[17]
except:
    winter_2006_2007_17 = None
WL_52.append(winter_2006_2007_17)
station17.append(winter_2006_2007_17)

try:
    winter_2006_2007_18 = ci1[18] + dn[18]
except:
    winter_2006_2007_18 = None
WL_52.append(winter_2006_2007_18)
station18.append(winter_2006_2007_18)

try:
    winter_2006_2007_19 = ci1[19] + dn[19]
except:
    winter_2006_2007_19 = None
WL_52.append(winter_2006_2007_19)
station19.append(winter_2006_2007_19)

try:
    winter_2006_2007_20 = ci1[20] + dn[20]
except:
    winter_2006_2007_20 = None
WL_52.append(winter_2006_2007_20)
station20.append(winter_2006_2007_20)

try:
    winter_2006_2007_21 = ci1[21] + dn[21]
except:
    winter_2006_2007_21 = None
WL_52.append(winter_2006_2007_21)
station21.append(winter_2006_2007_21)

try:
    winter_2006_2007_22 = ci1[22] + dn[22]
except:
    winter_2006_2007_22 = None
WL_52.append(winter_2006_2007_22)
station22.append(winter_2006_2007_22)

try:
    winter_2006_2007_23 = ci1[23] + dn[23]
except:
    winter_2006_2007_23 = None
WL_52.append(winter_2006_2007_23)
station23.append(winter_2006_2007_23)

#last spring freeze values for #2008

do = []

for rowOfCellObjects in mosheet['HD2':'HD25']:
    for cellObj in rowOfCellObjects:
        do.append(cellObj.value)

#final winter length calculation for 2007-2008 season for all of 24 Missouri stations

WL_53 = [] #all 2007-2008 winter lengths

try:
    winter_2007_2008_0 = cj1[0] + do[0]
except:
    winter_2007_2008_0 = None
WL_53.append(winter_2007_2008_0)
station0.append(winter_2007_2008_0)

try:
    winter_2007_2008_1 = cj1[1] + do[1]
except:
    winter_2007_2008_1 = None
WL_53.append(winter_2007_2008_1)
station1.append(winter_2007_2008_1)

try:
    winter_2007_2008_2 = cj1[2] + do[2]
except:
    winter_2007_2008_2 = None
WL_53.append(winter_2007_2008_2)
station2.append(winter_2007_2008_2)

try:
    winter_2007_2008_3 = cj1[3] + do[3]
except:
    winter_2007_2008_3 = None
WL_53.append(winter_2007_2008_3)
station3.append(winter_2007_2008_3)

try:
    winter_2007_2008_4 = cj1[4] + do[4]
except:
    winter_2007_2008_4 = None
WL_53.append(winter_2007_2008_4)
station4.append(winter_2007_2008_4)

try:
    winter_2007_2008_5 = cj1[5] + do[5]
except:
    winter_2007_2008_5 = None
WL_53.append(winter_2007_2008_5)
station5.append(winter_2007_2008_5)

try:
    winter_2007_2008_6 = cj1[6] + do[6]
except:
    winter_2007_2008_6 = None
WL_53.append(winter_2007_2008_6)
station6.append(winter_2007_2008_6)

try:
    winter_2007_2008_7 = cj1[7] + do[7]
except:
    winter_2007_2008_7 = None
WL_53.append(winter_2007_2008_7)
station7.append(winter_2007_2008_7)

try:
    winter_2007_2008_8 = cj1[8] + do[8]
except:
    winter_2007_2008_8 = None
WL_53.append(winter_2007_2008_8)
station8.append(winter_2007_2008_8)

try:
    winter_2007_2008_9 = cj1[9] + do[9]
except:
    winter_2007_2008_9 = None
WL_53.append(winter_2007_2008_9)
station9.append(winter_2007_2008_9)

try:
    winter_2007_2008_10 = cj1[10] + do[10]
except:
    winter_2007_2008_10 = None
WL_53.append(winter_2007_2008_10)
station10.append(winter_2007_2008_10)

try:
    winter_2007_2008_11 = cj1[11] + do[11]
except:
    winter_2007_2008_11 = None
WL_53.append(winter_2007_2008_11)
station11.append(winter_2007_2008_11)

try:
    winter_2007_2008_12 = cj1[12] + do[12]
except:
    winter_2007_2008_12 = None
WL_53.append(winter_2007_2008_12)
station12.append(winter_2007_2008_12)

try:
    winter_2007_2008_13 = cj1[13] + do[13]
except:
    winter_2007_2008_13 = None
WL_53.append(winter_2007_2008_13)
station13.append(winter_2007_2008_13)

try:
    winter_2007_2008_14 = cj1[14] + do[14]
except:
    winter_2007_2008_14 = None
WL_53.append(winter_2007_2008_14)
station14.append(winter_2007_2008_14)

try:
    winter_2007_2008_15 = cj1[15] + do[15]
except:
    winter_2007_2008_15 = None
WL_53.append(winter_2007_2008_15)
station15.append(winter_2007_2008_15)

try:
    winter_2007_2008_16 = cj1[16] + do[16]
except:
    winter_2007_2008_16 = None
WL_53.append(winter_2007_2008_16)
station16.append(winter_2007_2008_16)

try:
    winter_2007_2008_17 = cj1[17] + do[17]
except:
    winter_2007_2008_17 = None
WL_53.append(winter_2007_2008_17)
station17.append(winter_2007_2008_17)

try:
    winter_2007_2008_18 = cj1[18] + do[18]
except:
    winter_2007_2008_18 = None
WL_53.append(winter_2007_2008_18)
station18.append(winter_2007_2008_18)

try:
    winter_2007_2008_19 = cj1[19] + do[19]
except:
    winter_2007_2008_19 = None
WL_53.append(winter_2007_2008_19)
station19.append(winter_2007_2008_19)

try:
    winter_2007_2008_20 = cj1[20] + do[20]
except:
    winter_2007_2008_20 = None
WL_53.append(winter_2007_2008_20)
station20.append(winter_2007_2008_20)

try:
    winter_2007_2008_21 = cj1[21] + do[21]
except:
    winter_2007_2008_21 = None
WL_53.append(winter_2007_2008_21)
station21.append(winter_2007_2008_21)

try:
    winter_2007_2008_22 = cj1[22] + do[22]
except:
    winter_2007_2008_22 = None
WL_53.append(winter_2007_2008_22)
station22.append(winter_2007_2008_22)

try:
    winter_2007_2008_23 = cj1[23] + do[23]
except:
    winter_2007_2008_23 = None
WL_53.append(winter_2007_2008_23)
station23.append(winter_2007_2008_23)

#last spring freeze values for #2009

dp = []

for rowOfCellObjects in mosheet['HE2':'HE25']:
    for cellObj in rowOfCellObjects:
        dp.append(cellObj.value)

#final winter length calculation for 2008-2009 season for all of 24 Missouri stations

WL_54 = [] #all 2008-2009 winter lengths

try:
    winter_2008_2009_0 = ck1[0] + dp[0]
except:
    winter_2008_2009_0 = None
WL_54.append(winter_2008_2009_0)
station0.append(winter_2008_2009_0)

try:
    winter_2008_2009_1 = ck1[1] + dp[1]
except:
    winter_2008_2009_1 = None
WL_54.append(winter_2008_2009_1)
station1.append(winter_2008_2009_1)

try:
    winter_2008_2009_2 = ck1[2] + dp[2]
except:
    winter_2008_2009_2 = None
WL_54.append(winter_2008_2009_2)
station2.append(winter_2008_2009_2)

try:
    winter_2008_2009_3 = ck1[3] + dp[3]
except:
    winter_2008_2009_3 = None
WL_54.append(winter_2008_2009_3)
station3.append(winter_2008_2009_3)

try:
    winter_2008_2009_4 = ck1[4] + dp[4]
except:
    winter_2008_2009_4 = None
WL_54.append(winter_2008_2009_4)
station4.append(winter_2008_2009_4)

try:
    winter_2008_2009_5 = ck1[5] + dp[5]
except:
    winter_2008_2009_5 = None
WL_54.append(winter_2008_2009_5)
station5.append(winter_2008_2009_5)

try:
    winter_2008_2009_6 = ck1[6] + dp[6]
except:
    winter_2008_2009_6 = None
WL_54.append(winter_2008_2009_6)
station6.append(winter_2008_2009_6)

try:
    winter_2008_2009_7 = ck1[7] + dp[7]
except:
    winter_2008_2009_7 = None
WL_54.append(winter_2008_2009_7)
station7.append(winter_2008_2009_7)

try:
    winter_2008_2009_8 = ck1[8] + dp[8]
except:
    winter_2008_2009_8 = None
WL_54.append(winter_2008_2009_8)
station8.append(winter_2008_2009_8)

try:
    winter_2008_2009_9 = ck1[9] + dp[9]
except:
    winter_2008_2009_9 = None
WL_54.append(winter_2008_2009_9)
station9.append(winter_2008_2009_9)

try:
    winter_2008_2009_10 = ck1[10] + dp[10]
except:
    winter_2008_2009_10 = None
WL_54.append(winter_2008_2009_10)
station10.append(winter_2008_2009_10)

try:
    winter_2008_2009_11 = ck1[11] + dp[11]
except:
    winter_2008_2009_11 = None
WL_54.append(winter_2008_2009_11)
station11.append(winter_2008_2009_11)

try:
    winter_2008_2009_12 = ck1[12] + dp[12]
except:
    winter_2008_2009_12 = None
WL_54.append(winter_2008_2009_12)
station12.append(winter_2008_2009_12)

try:
    winter_2008_2009_13 = ck1[13] + dp[13]
except:
    winter_2008_2009_13 = None
WL_54.append(winter_2008_2009_13)
station13.append(winter_2008_2009_13)

try:
    winter_2008_2009_14 = ck1[14] + dp[14]
except:
    winter_2008_2009_14 = None
WL_54.append(winter_2008_2009_14)
station14.append(winter_2008_2009_14)

try:
    winter_2008_2009_15 = ck1[15] + dp[15]
except:
    winter_2008_2009_15 = None
WL_54.append(winter_2008_2009_15)
station15.append(winter_2008_2009_15)

try:
    winter_2008_2009_16 = ck1[16] + dp[16]
except:
    winter_2008_2009_16 = None
WL_54.append(winter_2008_2009_16)
station16.append(winter_2008_2009_16)

try:
    winter_2008_2009_17 = ck1[17] + dp[17]
except:
    winter_2008_2009_17 = None
WL_54.append(winter_2008_2009_17)
station17.append(winter_2008_2009_17)

try:
    winter_2008_2009_18 = ck1[18] + dp[18]
except:
    winter_2008_2009_18 = None
WL_54.append(winter_2008_2009_18)
station18.append(winter_2008_2009_18)

try:
    winter_2008_2009_19 = ck1[19] + dp[19]
except:
    winter_2008_2009_19 = None
WL_54.append(winter_2008_2009_19)
station19.append(winter_2008_2009_19)

try:
    winter_2008_2009_20 = ck1[20] + dp[20]
except:
    winter_2008_2009_20 = None
WL_54.append(winter_2008_2009_20)
station20.append(winter_2008_2009_20)

try:
    winter_2008_2009_21 = ck1[21] + dp[21]
except:
    winter_2008_2009_21 = None
WL_54.append(winter_2008_2009_21)
station21.append(winter_2008_2009_21)

try:
    winter_2008_2009_22 = ck1[22] + dp[22]
except:
    winter_2008_2009_22 = None
WL_54.append(winter_2008_2009_22)
station22.append(winter_2008_2009_22)

try:
    winter_2008_2009_23 = ck1[23] + dp[23]
except:
    winter_2008_2009_23 = None
WL_54.append(winter_2008_2009_23)
station23.append(winter_2008_2009_23)

#last spring freeze values for #2010

dq = []

for rowOfCellObjects in mosheet['HF2':'HF25']:
    for cellObj in rowOfCellObjects:
        dq.append(cellObj.value)

#final winter length calculation for 2009-2010 season for all of 24 Missouri stations

WL_55 = [] #all 2009-2010 winter lengths

try:
    winter_2009_2010_0 = cl1[0] + dq[0]
except:
    winter_2009_2010_0 = None
WL_55.append(winter_2009_2010_0)
station0.append(winter_2009_2010_0)

try:
    winter_2009_2010_1 = cl1[1] + dq[1]
except:
    winter_2009_2010_1 = None
WL_55.append(winter_2009_2010_1)
station1.append(winter_2009_2010_1)

try:
    winter_2009_2010_2 = cl1[2] + dq[2]
except:
    winter_2009_2010_2 = None
WL_55.append(winter_2009_2010_2)
station2.append(winter_2009_2010_2)

try:
    winter_2009_2010_3 = cl1[3] + dq[3]
except:
    winter_2009_2010_3 = None
WL_55.append(winter_2009_2010_3)
station3.append(winter_2009_2010_3)

try:
    winter_2009_2010_4 = cl1[4] + dq[4]
except:
    winter_2009_2010_4 = None
WL_55.append(winter_2009_2010_4)
station4.append(winter_2009_2010_4)

try:
    winter_2009_2010_5 = cl1[5] + dq[5]
except:
    winter_2009_2010_5 = None
WL_55.append(winter_2009_2010_5)
station5.append(winter_2009_2010_5)

try:
    winter_2009_2010_6 = cl1[6] + dq[6]
except:
    winter_2009_2010_6 = None
WL_55.append(winter_2009_2010_6)
station6.append(winter_2009_2010_6)

try:
    winter_2009_2010_7 = cl1[7] + dq[7]
except:
    winter_2009_2010_7 = None
WL_55.append(winter_2009_2010_7)
station7.append(winter_2009_2010_7)

try:
    winter_2009_2010_8 = cl1[8] + dq[8]
except:
    winter_2009_2010_8 = None
WL_55.append(winter_2009_2010_8)
station8.append(winter_2009_2010_8)

try:
    winter_2009_2010_9 = cl1[9] + dq[9]
except:
    winter_2009_2010_9 = None
WL_55.append(winter_2009_2010_9)
station9.append(winter_2009_2010_9)

try:
    winter_2009_2010_10 = cl1[10] + dq[10]
except:
    winter_2009_2010_10 = None
WL_55.append(winter_2009_2010_10)
station10.append(winter_2009_2010_10)

try:
    winter_2009_2010_11 = cl1[11] + dq[11]
except:
    winter_2009_2010_11 = None
WL_55.append(winter_2009_2010_11)
station11.append(winter_2009_2010_11)

try:
    winter_2009_2010_12 = cl1[12] + dq[12]
except:
    winter_2009_2010_12 = None
WL_55.append(winter_2009_2010_12)
station12.append(winter_2009_2010_12)

try:
    winter_2009_2010_13 = cl1[13] + dq[13]
except:
    winter_2009_2010_13 = None
WL_55.append(winter_2009_2010_13)
station13.append(winter_2009_2010_13)

try:
    winter_2009_2010_14 = cl1[14] + dq[14]
except:
    winter_2009_2010_14 = None
WL_55.append(winter_2009_2010_14)
station14.append(winter_2009_2010_14)

try:
    winter_2009_2010_15 = cl1[15] + dq[15]
except:
    winter_2009_2010_15 = None
WL_55.append(winter_2009_2010_15)
station15.append(winter_2009_2010_15)

try:
    winter_2009_2010_16 = cl1[16] + dq[16]
except:
    winter_2009_2010_16 = None
WL_55.append(winter_2009_2010_16)
station16.append(winter_2009_2010_16)

try:
    winter_2009_2010_17 = cl1[17] + dq[17]
except:
    winter_2009_2010_17 = None
WL_55.append(winter_2009_2010_17)
station17.append(winter_2009_2010_17)

try:
    winter_2009_2010_18 = cl1[18] + dq[18]
except:
    winter_2009_2010_18 = None
WL_55.append(winter_2009_2010_18)
station18.append(winter_2009_2010_18)

try:
    winter_2009_2010_19 = cl1[19] + dq[19]
except:
    winter_2009_2010_19 = None
WL_55.append(winter_2009_2010_19)
station19.append(winter_2009_2010_19)

try:
    winter_2009_2010_20 = cl1[20] + dq[20]
except:
    winter_2009_2010_20 = None
WL_55.append(winter_2009_2010_20)
station20.append(winter_2009_2010_20)

try:
    winter_2009_2010_21 = cl1[21] + dq[21]
except:
    winter_2009_2010_21 = None
WL_55.append(winter_2009_2010_21)
station21.append(winter_2009_2010_21)

try:
    winter_2009_2010_22 = cl1[22] + dq[22]
except:
    winter_2009_2010_22 = None
WL_55.append(winter_2009_2010_22)
station22.append(winter_2009_2010_22)

try:
    winter_2009_2010_23 = cl1[23] + dq[23]
except:
    winter_2009_2010_23 = None
WL_55.append(winter_2009_2010_23)
station23.append(winter_2009_2010_23)

#last spring freeze values for #2011

dr = []

for rowOfCellObjects in mosheet['HG2':'HG25']:
    for cellObj in rowOfCellObjects:
        dr.append(cellObj.value)

#final winter length calculation for 2010-2011 season for all of 24 Missouri stations

WL_56 = [] #all 2010-2011 winter lengths

try:
    winter_2010_2011_0 = cm1[0] + dr[0]
except:
    winter_2010_2011_0 = None
WL_56.append(winter_2010_2011_0)
station0.append(winter_2010_2011_0)

try:
    winter_2010_2011_1 = cm1[1] + dr[1]
except:
    winter_2010_2011_1 = None
WL_56.append(winter_2010_2011_1)
station1.append(winter_2010_2011_1)

try:
    winter_2010_2011_2 = cm1[2] + dr[2]
except:
    winter_2010_2011_2 = None
WL_56.append(winter_2010_2011_2)
station2.append(winter_2010_2011_2)

try:
    winter_2010_2011_3 = cm1[3] + dr[3]
except:
    winter_2010_2011_3 = None
WL_56.append(winter_2010_2011_3)
station3.append(winter_2010_2011_3)

try:
    winter_2010_2011_4 = cm1[4] + dr[4]
except:
    winter_2010_2011_4 = None
WL_56.append(winter_2010_2011_4)
station4.append(winter_2010_2011_4)

try:
    winter_2010_2011_5 = cm1[5] + dr[5]
except:
    winter_2010_2011_5 = None
WL_56.append(winter_2010_2011_5)
station5.append(winter_2010_2011_5)

try:
    winter_2010_2011_6 = cm1[6] + dr[6]
except:
    winter_2010_2011_6 = None
WL_56.append(winter_2010_2011_6)
station6.append(winter_2010_2011_6)

try:
    winter_2010_2011_7 = cm1[7] + dr[7]
except:
    winter_2010_2011_7 = None
WL_56.append(winter_2010_2011_7)
station7.append(winter_2010_2011_7)

try:
    winter_2010_2011_8 = cm1[8] + dr[8]
except:
    winter_2010_2011_8 = None
WL_56.append(winter_2010_2011_8)
station8.append(winter_2010_2011_8)

try:
    winter_2010_2011_9 = cm1[9] + dr[9]
except:
    winter_2010_2011_9 = None
WL_56.append(winter_2010_2011_9)
station9.append(winter_2010_2011_9)

try:
    winter_2010_2011_10 = cm1[10] + dr[10]
except:
    winter_2010_2011_10 = None
WL_56.append(winter_2010_2011_10)
station10.append(winter_2010_2011_10)

try:
    winter_2010_2011_11 = cm1[11] + dr[11]
except:
    winter_2010_2011_11 = None
WL_56.append(winter_2010_2011_11)
station11.append(winter_2010_2011_11)

try:
    winter_2010_2011_12 = cm1[12] + dr[12]
except:
    winter_2010_2011_12 = None
WL_56.append(winter_2010_2011_12)
station12.append(winter_2010_2011_12)

try:
    winter_2010_2011_13 = cm1[13] + dr[13]
except:
    winter_2010_2011_13 = None
WL_56.append(winter_2010_2011_13)
station13.append(winter_2010_2011_13)

try:
    winter_2010_2011_14 = cm1[14] + dr[14]
except:
    winter_2010_2011_14 = None
WL_56.append(winter_2010_2011_14)
station14.append(winter_2010_2011_14)

try:
    winter_2010_2011_15 = cm1[15] + dr[15]
except:
    winter_2010_2011_15 = None
WL_56.append(winter_2010_2011_15)
station15.append(winter_2010_2011_15)

try:
    winter_2010_2011_16 = cm1[16] + dr[16]
except:
    winter_2010_2011_16 = None
WL_56.append(winter_2010_2011_16)
station16.append(winter_2010_2011_16)

try:
    winter_2010_2011_17 = cm1[17] + dr[17]
except:
    winter_2010_2011_17 = None
WL_56.append(winter_2010_2011_17)
station17.append(winter_2010_2011_17)

try:
    winter_2010_2011_18 = cm1[18] + dr[18]
except:
    winter_2010_2011_18 = None
WL_56.append(winter_2010_2011_18)
station18.append(winter_2010_2011_18)

try:
    winter_2010_2011_19 = cm1[19] + dr[19]
except:
    winter_2010_2011_19 = None
WL_56.append(winter_2010_2011_19)
station19.append(winter_2010_2011_19)

try:
    winter_2010_2011_20 = cm1[20] + dr[20]
except:
    winter_2010_2011_20 = None
WL_56.append(winter_2010_2011_20)
station20.append(winter_2010_2011_20)

try:
    winter_2010_2011_21 = cm1[21] + dr[21]
except:
    winter_2010_2011_21 = None
WL_56.append(winter_2010_2011_21)
station21.append(winter_2010_2011_21)

try:
    winter_2010_2011_22 = cm1[22] + dr[22]
except:
    winter_2010_2011_22 = None
WL_56.append(winter_2010_2011_22)
station22.append(winter_2010_2011_22)

try:
    winter_2010_2011_23 = cm1[23] + dr[23]
except:
    winter_2010_2011_23 = None
WL_56.append(winter_2010_2011_23)
station23.append(winter_2010_2011_23)

#last spring freeze values for #2012

ds = []

for rowOfCellObjects in mosheet['HH2':'HH25']:
    for cellObj in rowOfCellObjects:
        ds.append(cellObj.value)

#final winter length calculation for 2011-2012 season for all of 24 Missouri stations

WL_57 = [] #all 2011-2012 winter lengths

try:
    winter_2011_2012_0 = cn1[0] + ds[0]
except:
    winter_2011_2012_0 = None
WL_57.append(winter_2011_2012_0)
station0.append(winter_2011_2012_0)

try:
    winter_2011_2012_1 = cn1[1] + ds[1]
except:
    winter_2011_2012_1 = None
WL_57.append(winter_2011_2012_1)
station1.append(winter_2011_2012_1)

try:
    winter_2011_2012_2 = cn1[2] + ds[2]
except:
    winter_2011_2012_2 = None
WL_57.append(winter_2011_2012_2)
station2.append(winter_2011_2012_2)

try:
    winter_2011_2012_3 = cn1[3] + ds[3]
except:
    winter_2011_2012_3 = None
WL_57.append(winter_2011_2012_3)
station3.append(winter_2011_2012_3)

try:
    winter_2011_2012_4 = cn1[4] + ds[4]
except:
    winter_2011_2012_4 = None
WL_57.append(winter_2011_2012_4)
station4.append(winter_2011_2012_4)

try:
    winter_2011_2012_5 = cn1[5] + ds[5]
except:
    winter_2011_2012_5 = None
WL_57.append(winter_2011_2012_5)
station5.append(winter_2011_2012_5)

try:
    winter_2011_2012_6 = cn1[6] + ds[6]
except:
    winter_2011_2012_6 = None
WL_57.append(winter_2011_2012_6)
station6.append(winter_2011_2012_6)

try:
    winter_2011_2012_7 = cn1[7] + ds[7]
except:
    winter_2011_2012_7 = None
WL_57.append(winter_2011_2012_7)
station7.append(winter_2011_2012_7)

try:
    winter_2011_2012_8 = cn1[8] + ds[8]
except:
    winter_2011_2012_8 = None
WL_57.append(winter_2011_2012_8)
station8.append(winter_2011_2012_8)

try:
    winter_2011_2012_9 = cn1[9] + ds[9]
except:
    winter_2011_2012_9 = None
WL_57.append(winter_2011_2012_9)
station9.append(winter_2011_2012_9)

try:
    winter_2011_2012_10 = cn1[10] + ds[10]
except:
    winter_2011_2012_10 = None
WL_57.append(winter_2011_2012_10)
station10.append(winter_2011_2012_10)

try:
    winter_2011_2012_11 = cn1[11] + ds[11]
except:
    winter_2011_2012_11 = None
WL_57.append(winter_2011_2012_11)
station11.append(winter_2011_2012_11)

try:
    winter_2011_2012_12 = cn1[12] + ds[12]
except:
    winter_2011_2012_12 = None
WL_57.append(winter_2011_2012_12)
station12.append(winter_2011_2012_12)

try:
    winter_2011_2012_13 = cn1[13] + ds[13]
except:
    winter_2011_2012_13 = None
WL_57.append(winter_2011_2012_13)
station13.append(winter_2011_2012_13)

try:
    winter_2011_2012_14 = cn1[14] + ds[14]
except:
    winter_2011_2012_14 = None
WL_57.append(winter_2011_2012_14)
station14.append(winter_2011_2012_14)

try:
    winter_2011_2012_15 = cn1[15] + ds[15]
except:
    winter_2011_2012_15 = None
WL_57.append(winter_2011_2012_15)
station15.append(winter_2011_2012_15)

try:
    winter_2011_2012_16 = cn1[16] + ds[16]
except:
    winter_2011_2012_16 = None
WL_57.append(winter_2011_2012_16)
station16.append(winter_2011_2012_16)

try:
    winter_2011_2012_17 = cn1[17] + ds[17]
except:
    winter_2011_2012_17 = None
WL_57.append(winter_2011_2012_17)
station17.append(winter_2011_2012_17)

try:
    winter_2011_2012_18 = cn1[18] + ds[18]
except:
    winter_2011_2012_18 = None
WL_57.append(winter_2011_2012_18)
station18.append(winter_2011_2012_18)

try:
    winter_2011_2012_19 = cn1[19] + ds[19]
except:
    winter_2011_2012_19 = None
WL_57.append(winter_2011_2012_19)
station19.append(winter_2011_2012_19)

try:
    winter_2011_2012_20 = cn1[20] + ds[20]
except:
    winter_2011_2012_20 = None
WL_57.append(winter_2011_2012_20)
station20.append(winter_2011_2012_20)

try:
    winter_2011_2012_21 = cn1[21] + ds[21]
except:
    winter_2011_2012_21 = None
WL_57.append(winter_2011_2012_21)
station21.append(winter_2011_2012_21)

try:
    winter_2011_2012_22 = cn1[22] + ds[22]
except:
    winter_2011_2012_22 = None
WL_57.append(winter_2011_2012_22)
station22.append(winter_2011_2012_22)

try:
    winter_2011_2012_23 = cn1[23] + ds[23]
except:
    winter_2011_2012_23 = None
WL_57.append(winter_2011_2012_23)
station23.append(winter_2011_2012_23)

#last spring freeze values for #2013

dt = []

for rowOfCellObjects in mosheet['HI2':'HI25']:
    for cellObj in rowOfCellObjects:
        dt.append(cellObj.value)

#final winter length calculation for 2012-2013 season for all of 24 Missouri stations

WL_58 = [] #all 2012-2013 winter lengths

try:
    winter_2012_2013_0 = co1[0] + dt[0]
except:
    winter_2012_2013_0 = None
WL_58.append(winter_2012_2013_0)
station0.append(winter_2012_2013_0)

try:
    winter_2012_2013_1 = co1[1] + dt[1]
except:
    winter_2012_2013_1 = None
WL_58.append(winter_2012_2013_1)
station1.append(winter_2012_2013_1)

try:
    winter_2012_2013_2 = co1[2] + dt[2]
except:
    winter_2012_2013_2 = None
WL_58.append(winter_2012_2013_2)
station2.append(winter_2012_2013_2)

try:
    winter_2012_2013_3 = co1[3] + dt[3]
except:
    winter_2012_2013_3 = None
WL_58.append(winter_2012_2013_3)
station3.append(winter_2012_2013_3)

try:
    winter_2012_2013_4 = co1[4] + dt[4]
except:
    winter_2012_2013_4 = None
WL_58.append(winter_2012_2013_4)
station4.append(winter_2012_2013_4)

try:
    winter_2012_2013_5 = co1[5] + dt[5]
except:
    winter_2012_2013_5 = None
WL_58.append(winter_2012_2013_5)
station5.append(winter_2012_2013_5)

try:
    winter_2012_2013_6 = co1[6] + dt[6]
except:
    winter_2012_2013_6 = None
WL_58.append(winter_2012_2013_6)
station6.append(winter_2012_2013_6)

try:
    winter_2012_2013_7 = co1[7] + dt[7]
except:
    winter_2012_2013_7 = None
WL_58.append(winter_2012_2013_7)
station7.append(winter_2012_2013_7)

try:
    winter_2012_2013_8 = co1[8] + dt[8]
except:
    winter_2012_2013_8 = None
WL_58.append(winter_2012_2013_8)
station8.append(winter_2012_2013_8)

try:
    winter_2012_2013_9 = co1[9] + dt[9]
except:
    winter_2012_2013_9 = None
WL_58.append(winter_2012_2013_9)
station9.append(winter_2012_2013_9)

try:
    winter_2012_2013_10 = co1[10] + dt[10]
except:
    winter_2012_2013_10 = None
WL_58.append(winter_2012_2013_10)
station10.append(winter_2012_2013_10)

try:
    winter_2012_2013_11 = co1[11] + dt[11]
except:
    winter_2012_2013_11 = None
WL_58.append(winter_2012_2013_11)
station11.append(winter_2012_2013_11)

try:
    winter_2012_2013_12 = co1[12] + dt[12]
except:
    winter_2012_2013_12 = None
WL_58.append(winter_2012_2013_12)
station12.append(winter_2012_2013_12)

try:
    winter_2012_2013_13 = co1[13] + dt[13]
except:
    winter_2012_2013_13 = None
WL_58.append(winter_2012_2013_13)
station13.append(winter_2012_2013_13)

try:
    winter_2012_2013_14 = co1[14] + dt[14]
except:
    winter_2012_2013_14 = None
WL_58.append(winter_2012_2013_14)
station14.append(winter_2012_2013_14)

try:
    winter_2012_2013_15 = co1[15] + dt[15]
except:
    winter_2012_2013_15 = None
WL_58.append(winter_2012_2013_15)
station15.append(winter_2012_2013_15)

try:
    winter_2012_2013_16 = co1[16] + dt[16]
except:
    winter_2012_2013_16 = None
WL_58.append(winter_2012_2013_16)
station16.append(winter_2012_2013_16)

try:
    winter_2012_2013_17 = co1[17] + dt[17]
except:
    winter_2012_2013_17 = None
WL_58.append(winter_2012_2013_17)
station17.append(winter_2012_2013_17)

try:
    winter_2012_2013_18 = co1[18] + dt[18]
except:
    winter_2012_2013_18 = None
WL_58.append(winter_2012_2013_18)
station18.append(winter_2012_2013_18)

try:
    winter_2012_2013_19 = co1[19] + dt[19]
except:
    winter_2012_2013_19 = None
WL_58.append(winter_2012_2013_19)
station19.append(winter_2012_2013_19)

try:
    winter_2012_2013_20 = co1[20] + dt[20]
except:
    winter_2012_2013_20 = None
WL_58.append(winter_2012_2013_20)
station20.append(winter_2012_2013_20)

try:
    winter_2012_2013_21 = co1[21] + dt[21]
except:
    winter_2012_2013_21 = None
WL_58.append(winter_2012_2013_21)
station21.append(winter_2012_2013_21)

try:
    winter_2012_2013_22 = co1[22] + dt[22]
except:
    winter_2012_2013_22 = None
WL_58.append(winter_2012_2013_22)
station22.append(winter_2012_2013_22)

try:
    winter_2012_2013_23 = co1[23] + dt[23]
except:
    winter_2012_2013_23 = None
WL_58.append(winter_2012_2013_23)
station23.append(winter_2012_2013_23)

#last spring freeze values for #2014

du = []

for rowOfCellObjects in mosheet['HJ2':'HJ25']:
    for cellObj in rowOfCellObjects:
        du.append(cellObj.value)

#final winter length calculation for 2013-2014 season for all of 24 Missouri stations

WL_59 = [] #all 2013-2014 winter lengths

try:
    winter_2013_2014_0 = cp1[0] + du[0]
except:
    winter_2013_2014_0 = None
WL_59.append(winter_2013_2014_0)
station0.append(winter_2013_2014_0)

try:
    winter_2013_2014_1 = cp1[1] + du[1]
except:
    winter_2013_2014_1 = None
WL_59.append(winter_2013_2014_1)
station1.append(winter_2013_2014_1)

try:
    winter_2013_2014_2 = cp1[2] + du[2]
except:
    winter_2013_2014_2 = None
WL_59.append(winter_2013_2014_2)
station2.append(winter_2013_2014_2)

try:
    winter_2013_2014_3 = cp1[3] + du[3]
except:
    winter_2013_2014_3 = None
WL_59.append(winter_2013_2014_3)
station3.append(winter_2013_2014_3)

try:
    winter_2013_2014_4 = cp1[4] + du[4]
except:
    winter_2013_2014_4 = None
WL_59.append(winter_2013_2014_4)
station4.append(winter_2013_2014_4)

try:
    winter_2013_2014_5 = cp1[5] + du[5]
except:
    winter_2013_2014_5 = None
WL_59.append(winter_2013_2014_5)
station5.append(winter_2013_2014_5)

try:
    winter_2013_2014_6 = cp1[6] + du[6]
except:
    winter_2013_2014_6 = None
WL_59.append(winter_2013_2014_6)
station6.append(winter_2013_2014_6)

try:
    winter_2013_2014_7 = cp1[7] + du[7]
except:
    winter_2013_2014_7 = None
WL_59.append(winter_2013_2014_7)
station7.append(winter_2013_2014_7)

try:
    winter_2013_2014_8 = cp1[8] + du[8]
except:
    winter_2013_2014_8 = None
WL_59.append(winter_2013_2014_8)
station8.append(winter_2013_2014_8)

try:
    winter_2013_2014_9 = cp1[9] + du[9]
except:
    winter_2013_2014_9 = None
WL_59.append(winter_2013_2014_9)
station9.append(winter_2013_2014_9)

try:
    winter_2013_2014_10 = cp1[10] + du[10]
except:
    winter_2013_2014_10 = None
WL_59.append(winter_2013_2014_10)
station10.append(winter_2013_2014_10)

try:
    winter_2013_2014_11 = cp1[11] + du[11]
except:
    winter_2013_2014_11 = None
WL_59.append(winter_2013_2014_11)
station11.append(winter_2013_2014_11)

try:
    winter_2013_2014_12 = cp1[12] + du[12]
except:
    winter_2013_2014_12 = None
WL_59.append(winter_2013_2014_12)
station12.append(winter_2013_2014_12)

try:
    winter_2013_2014_13 = cp1[13] + du[13]
except:
    winter_2013_2014_13 = None
WL_59.append(winter_2013_2014_13)
station13.append(winter_2013_2014_13)

try:
    winter_2013_2014_14 = cp1[14] + du[14]
except:
    winter_2013_2014_14 = None
WL_59.append(winter_2013_2014_14)
station14.append(winter_2013_2014_14)

try:
    winter_2013_2014_15 = cp1[15] + du[15]
except:
    winter_2013_2014_15 = None
WL_59.append(winter_2013_2014_15)
station15.append(winter_2013_2014_15)

try:
    winter_2013_2014_16 = cp1[16] + du[16]
except:
    winter_2013_2014_16 = None
WL_59.append(winter_2013_2014_16)
station16.append(winter_2013_2014_16)

try:
    winter_2013_2014_17 = cp1[17] + du[17]
except:
    winter_2013_2014_17 = None
WL_59.append(winter_2013_2014_17)
station17.append(winter_2013_2014_17)

try:
    winter_2013_2014_18 = cp1[18] + du[18]
except:
    winter_2013_2014_18 = None
WL_59.append(winter_2013_2014_18)
station18.append(winter_2013_2014_18)

try:
    winter_2013_2014_19 = cp1[19] + du[19]
except:
    winter_2013_2014_19 = None
WL_59.append(winter_2013_2014_19)
station19.append(winter_2013_2014_19)

try:
    winter_2013_2014_20 = cp1[20] + du[20]
except:
    winter_2013_2014_20 = None
WL_59.append(winter_2013_2014_20)
station20.append(winter_2013_2014_20)

try:
    winter_2013_2014_21 = cp1[21] + du[21]
except:
    winter_2013_2014_21 = None
WL_59.append(winter_2013_2014_21)
station21.append(winter_2013_2014_21)

try:
    winter_2013_2014_22 = cp1[22] + du[22]
except:
    winter_2013_2014_22 = None
WL_59.append(winter_2013_2014_22)
station22.append(winter_2013_2014_22)

try:
    winter_2013_2014_23 = cp1[23] + du[23]
except:
    winter_2013_2014_23 = None
WL_59.append(winter_2013_2014_23)
station23.append(winter_2013_2014_23)

#last spring freeze values for #2015

dv = []

for rowOfCellObjects in mosheet['HK2':'HK25']:
    for cellObj in rowOfCellObjects:
        dv.append(cellObj.value)

#final winter length calculation for 2014-2015 season for all of 24 Missouri stations

WL_60 = [] #all 2014-2015 winter lengths

try:
    winter_2014_2015_0 = cq1[0] + dv[0]
except:
    winter_2014_2015_0 = None
WL_60.append(winter_2014_2015_0)
station0.append(winter_2014_2015_0)

try:
    winter_2014_2015_1 = cq1[1] + dv[1]
except:
    winter_2014_2015_1 = None
WL_60.append(winter_2014_2015_1)
station1.append(winter_2014_2015_1)

try:
    winter_2014_2015_2 = cq1[2] + dv[2]
except:
    winter_2014_2015_2 = None
WL_60.append(winter_2014_2015_2)
station2.append(winter_2014_2015_2)

try:
    winter_2014_2015_3 = cq1[3] + dv[3]
except:
    winter_2014_2015_3 = None
WL_60.append(winter_2014_2015_3)
station3.append(winter_2014_2015_3)

try:
    winter_2014_2015_4 = cq1[4] + dv[4]
except:
    winter_2014_2015_4 = None
WL_60.append(winter_2014_2015_4)
station4.append(winter_2014_2015_4)

try:
    winter_2014_2015_5 = cq1[5] + dv[5]
except:
    winter_2014_2015_5 = None
WL_60.append(winter_2014_2015_5)
station5.append(winter_2014_2015_5)

try:
    winter_2014_2015_6 = cq1[6] + dv[6]
except:
    winter_2014_2015_6 = None
WL_60.append(winter_2014_2015_6)
station6.append(winter_2014_2015_6)

try:
    winter_2014_2015_7 = cq1[7] + dv[7]
except:
    winter_2014_2015_7 = None
WL_60.append(winter_2014_2015_7)
station7.append(winter_2014_2015_7)

try:
    winter_2014_2015_8 = cq1[8] + dv[8]
except:
    winter_2014_2015_8 = None
WL_60.append(winter_2014_2015_8)
station8.append(winter_2014_2015_8)

try:
    winter_2014_2015_9 = cq1[9] + dv[9]
except:
    winter_2014_2015_9 = None
WL_60.append(winter_2014_2015_9)
station9.append(winter_2014_2015_9)

try:
    winter_2014_2015_10 = cq1[10] + dv[10]
except:
    winter_2014_2015_10 = None
WL_60.append(winter_2014_2015_10)
station10.append(winter_2014_2015_10)

try:
    winter_2014_2015_11 = cq1[11] + dv[11]
except:
    winter_2014_2015_11 = None
WL_60.append(winter_2014_2015_11)
station11.append(winter_2014_2015_11)

try:
    winter_2014_2015_12 = cq1[12] + dv[12]
except:
    winter_2014_2015_12 = None
WL_60.append(winter_2014_2015_12)
station12.append(winter_2014_2015_12)

try:
    winter_2014_2015_13 = cq1[13] + dv[13]
except:
    winter_2014_2015_13 = None
WL_60.append(winter_2014_2015_13)
station13.append(winter_2014_2015_13)

try:
    winter_2014_2015_14 = cq1[14] + dv[14]
except:
    winter_2014_2015_14 = None
WL_60.append(winter_2014_2015_14)
station14.append(winter_2014_2015_14)

try:
    winter_2014_2015_15 = cq1[15] + dv[15]
except:
    winter_2014_2015_15 = None
WL_60.append(winter_2014_2015_15)
station15.append(winter_2014_2015_15)

try:
    winter_2014_2015_16 = cq1[16] + dv[16]
except:
    winter_2014_2015_16 = None
WL_60.append(winter_2014_2015_16)
station16.append(winter_2014_2015_16)

try:
    winter_2014_2015_17 = cq1[17] + dv[17]
except:
    winter_2014_2015_17 = None
WL_60.append(winter_2014_2015_17)
station17.append(winter_2014_2015_17)

try:
    winter_2014_2015_18 = cq1[18] + dv[18]
except:
    winter_2014_2015_18 = None
WL_60.append(winter_2014_2015_18)
station18.append(winter_2014_2015_18)

try:
    winter_2014_2015_19 = cq1[19] + dv[19]
except:
    winter_2014_2015_19 = None
WL_60.append(winter_2014_2015_19)
station19.append(winter_2014_2015_19)

try:
    winter_2014_2015_20 = cq1[20] + dv[20]
except:
    winter_2014_2015_20 = None
WL_60.append(winter_2014_2015_20)
station20.append(winter_2014_2015_20)

try:
    winter_2014_2015_21 = cq1[21] + dv[21]
except:
    winter_2014_2015_21 = None
WL_60.append(winter_2014_2015_21)
station21.append(winter_2014_2015_21)

try:
    winter_2014_2015_22 = cq1[22] + dv[22]
except:
    winter_2014_2015_22 = None
WL_60.append(winter_2014_2015_22)
station22.append(winter_2014_2015_22)

try:
    winter_2014_2015_23 = cq1[23] + dv[23]
except:
    winter_2014_2015_23 = None
WL_60.append(winter_2014_2015_23)
station23.append(winter_2014_2015_23)

#last spring freeze values for #2016

dw = []

for rowOfCellObjects in mosheet['HL2':'HL25']:
    for cellObj in rowOfCellObjects:
        dw.append(cellObj.value)

#final winter length calculation for 2015-2016 season for all of 24 Missouri stations

WL_61 = [] #all 2015-2016 winter lengths

try:
    winter_2015_2016_0 = cr1[0] + dw[0]
except:
    winter_2015_2016_0 = None
WL_61.append(winter_2015_2016_0)
station0.append(winter_2015_2016_0)

try:
    winter_2015_2016_1 = cr1[1] + dw[1]
except:
    winter_2015_2016_1 = None
WL_61.append(winter_2015_2016_1)
station1.append(winter_2015_2016_1)

try:
    winter_2015_2016_2 = cr1[2] + dw[2]
except:
    winter_2015_2016_2 = None
WL_61.append(winter_2015_2016_2)
station2.append(winter_2015_2016_2)

try:
    winter_2015_2016_3 = cr1[3] + dw[3]
except:
    winter_2015_2016_3 = None
WL_61.append(winter_2015_2016_3)
station3.append(winter_2015_2016_3)

try:
    winter_2015_2016_4 = cr1[4] + dw[4]
except:
    winter_2015_2016_4 = None
WL_61.append(winter_2015_2016_4)
station4.append(winter_2015_2016_4)

try:
    winter_2015_2016_5 = cr1[5] + dw[5]
except:
    winter_2015_2016_5 = None
WL_61.append(winter_2015_2016_5)
station5.append(winter_2015_2016_5)

try:
    winter_2015_2016_6 = cr1[6] + dw[6]
except:
    winter_2015_2016_6 = None
WL_61.append(winter_2015_2016_6)
station6.append(winter_2015_2016_6)

try:
    winter_2015_2016_7 = cr1[7] + dw[7]
except:
    winter_2015_2016_7 = None
WL_61.append(winter_2015_2016_7)
station7.append(winter_2015_2016_7)

try:
    winter_2015_2016_8 = cr1[8] + dw[8]
except:
    winter_2015_2016_8 = None
WL_61.append(winter_2015_2016_8)
station8.append(winter_2015_2016_8)

try:
    winter_2015_2016_9 = cr1[9] + dw[9]
except:
    winter_2015_2016_9 = None
WL_61.append(winter_2015_2016_9)
station9.append(winter_2015_2016_9)

try:
    winter_2015_2016_10 = cr1[10] + dw[10]
except:
    winter_2015_2016_10 = None
WL_61.append(winter_2015_2016_10)
station10.append(winter_2015_2016_10)

try:
    winter_2015_2016_11 = cr1[11] + dw[11]
except:
    winter_2015_2016_11 = None
WL_61.append(winter_2015_2016_11)
station11.append(winter_2015_2016_11)

try:
    winter_2015_2016_12 = cr1[12] + dw[12]
except:
    winter_2015_2016_12 = None
WL_61.append(winter_2015_2016_12)
station12.append(winter_2015_2016_12)

try:
    winter_2015_2016_13 = cr1[13] + dw[13]
except:
    winter_2015_2016_13 = None
WL_61.append(winter_2015_2016_13)
station13.append(winter_2015_2016_13)

try:
    winter_2015_2016_14 = cr1[14] + dw[14]
except:
    winter_2015_2016_14 = None
WL_61.append(winter_2015_2016_14)
station14.append(winter_2015_2016_14)

try:
    winter_2015_2016_15 = cr1[15] + dw[15]
except:
    winter_2015_2016_15 = None
WL_61.append(winter_2015_2016_15)
station15.append(winter_2015_2016_15)

try:
    winter_2015_2016_16 = cr1[16] + dw[16]
except:
    winter_2015_2016_16 = None
WL_61.append(winter_2015_2016_16)
station16.append(winter_2015_2016_16)

try:
    winter_2015_2016_17 = cr1[17] + dw[17]
except:
    winter_2015_2016_17 = None
WL_61.append(winter_2015_2016_17)
station17.append(winter_2015_2016_17)

try:
    winter_2015_2016_18 = cr1[18] + dw[18]
except:
    winter_2015_2016_18 = None
WL_61.append(winter_2015_2016_18)
station18.append(winter_2015_2016_18)

try:
    winter_2015_2016_19 = cr1[19] + dw[19]
except:
    winter_2015_2016_19 = None
WL_61.append(winter_2015_2016_19)
station19.append(winter_2015_2016_19)

try:
    winter_2015_2016_20 = cr1[20] + dw[20]
except:
    winter_2015_2016_20 = None
WL_61.append(winter_2015_2016_20)
station20.append(winter_2015_2016_20)

try:
    winter_2015_2016_21 = cr1[21] + dw[21]
except:
    winter_2015_2016_21 = None
WL_61.append(winter_2015_2016_21)
station21.append(winter_2015_2016_21)

try:
    winter_2015_2016_22 = cr1[22] + dw[22]
except:
    winter_2015_2016_22 = None
WL_61.append(winter_2015_2016_22)
station22.append(winter_2015_2016_22)

try:
    winter_2015_2016_23 = cr1[23] + dw[23]
except:
    winter_2015_2016_23 = None
WL_61.append(winter_2015_2016_23)
station23.append(winter_2015_2016_23)

# now let's write all that work to a csv 

with open('winter_compare.txt', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(WL_0)
    wr.writerow(WL_1)
    wr.writerow(WL_2)
    wr.writerow(WL_3)
    wr.writerow(WL_4)
    wr.writerow(WL_5)
    wr.writerow(WL_6)
    wr.writerow(WL_7)
    wr.writerow(WL_8)
    wr.writerow(WL_9)
    wr.writerow(WL_10)
    wr.writerow(WL_11)
    wr.writerow(WL_12)
    wr.writerow(WL_13)
    wr.writerow(WL_14)
    wr.writerow(WL_15)
    wr.writerow(WL_16)
    wr.writerow(WL_17)
    wr.writerow(WL_18)
    wr.writerow(WL_19)
    wr.writerow(WL_20)
    wr.writerow(WL_21)
    wr.writerow(WL_22)
    wr.writerow(WL_23)
    wr.writerow(WL_24)
    wr.writerow(WL_25)
    wr.writerow(WL_26)
    wr.writerow(WL_27)
    wr.writerow(WL_28)
    wr.writerow(WL_29)
    wr.writerow(WL_30)
    wr.writerow(WL_31)
    wr.writerow(WL_32)
    wr.writerow(WL_33)
    wr.writerow(WL_34)
    wr.writerow(WL_35)
    wr.writerow(WL_36)
    wr.writerow(WL_37)
    wr.writerow(WL_38)
    wr.writerow(WL_39)
    wr.writerow(WL_40)
    wr.writerow(WL_41)
    wr.writerow(WL_42)
    wr.writerow(WL_43)
    wr.writerow(WL_44) 
    wr.writerow(WL_45)
    wr.writerow(WL_46)
    wr.writerow(WL_47)
    wr.writerow(WL_48)
    wr.writerow(WL_49)
    wr.writerow(WL_50)
    wr.writerow(WL_51)
    wr.writerow(WL_52)
    wr.writerow(WL_53)
    wr.writerow(WL_54)
    wr.writerow(WL_55)
    wr.writerow(WL_56)
    wr.writerow(WL_57)
    wr.writerow(WL_58)
    wr.writerow(WL_59)
    wr.writerow(WL_60)
    wr.writerow(WL_61)
