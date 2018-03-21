The following calculations are streamflow from the FEMA Region III Hydrologic Analysis Loudoun County in Virginia.

Loudoun County's analysis estimates flood discharge for the 50, 20, 10, 4, 2, 1, and 0.2 % (2, 5, 10, 25, 50, 100, 500 year recurrence interval) chance flood at each of the test stations.

The equations take in 4 parameters:
- Drainage Area (A) in square miles
- Channel Slope (SL) in ft per mile
- Impervious Area (IA), in percentage of the drainage area
- Dsoils (Dsoil), hydrologic soil group D in percent of the drainage area

```python

from aide_design.play import*

def Loudoun_flow_2yr(A, SL, IA, Dsoil):
  '''Loudon County's empirically derived formula for peak flows.'''
  flow = 32.5 * A**0.672 * (IA + 1)**0.245 * SL**0.248 * (Dsoil + 1)**0.204
  return flow * (u.ft**3/u.s)




```
We are primarily subwatershed 41, so I use these values for D soil group as opposed to weighting the contribution by subwatershed 40 and 41. I do not make distinctions for D soil groups if impervious areas have been laid atop them.

```python

A = 0.44 #square miles
SL = 0.01625 * 5280 #ft/mile
print(SL)
IA = 26.6
#Dsoil = (.15 + 3.65 + 2.93 + 0.57 + 0.37)/281.6  #2.7 %
Dsoil = 3.52


A1 = 3.91
SL1 = 30.68
IA1 = 5.67
DS1 = 50.54

print(Loudoun_flow_2yr(A1, SL1, IA1, DS1))
print(Loudoun_flow_2yr(A, SL, IA, Dsoil))

```

| 2 Year Flow (cfs) | Drainage Area (sq. miles) | Slope (ft/mile) | Impervious Area (%) | Dsoils (%) |
| ----------------- | ------------------------- | --------------- | ------------------- | ---------- |
| 256.2             | .44                       | 488.4           | 26.6                | 2.7        |
