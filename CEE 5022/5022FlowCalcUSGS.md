The following caluclations are stream flow from the USGS for Virginia's urban basins. The report is titled: "Methods and Equations for Estimating Peak Streamflow per Square Mile in Virginia's Urban Basins" and was updated 2014.


```python

from aide_design.play import*


def USGS_flow_1yr(URBAN, DA):
  '''The following is the 1 year recurrence interval - USGS empirically derived equation for stream flow. The equation is not dimensionally consistent so drainage area must be entered in square miles. Urban area is denoted as a percentage value from 0 to 100.'''
  logflow =  1.673 + (URBAN - 43.179) * ((np.log10(DA)-1.412) * -0.00637) + 0.00372 * URBAN - 0.512 * np.log10(DA)
  flow = 10**(logflow)
  return (flow * (u.ft**3 / u.s))

def USGS_flow_2yr(URBAN, DA):
    '''The following is the 2 year recurrence interval - USGS empirically derived equation for stream flow. The equation is not dimensionally consistent so drainage area must be entered in square miles. Urban area is denoted as a percentage value from 0% to 100%.'''
    logflow =  1.713 + (URBAN - 43.538) * ((np.log10(DA)-1.400) * -0.00626) + 0.00359 * URBAN - 0.505 * np.log10(DA)
    flow = 10**(logflow)
    return (flow * (u.ft**3 / u.s))

```

```python

URBAN = 34
DA = np.array([0.441, .416]) # square miles

print(USGS_flow_1yr(URBAN, DA).magnitude, USGS_flow_1yr(URBAN, DA).units)

print(USGS_flow_2yr(URBAN, DA).magnitude, USGS_flow_2yr(URBAN, DA).units)

```

| 1 Year Flow (cfs) | Urban Percentage | Drainage Area (sq. miles) |
| ----------------- | ---------------- | ------------------------- |
| 59.4              | 27               | .44                       |
| 60.8              | 27               | .416                      |


| 2 Year Flow (cfs) | Urban Percentage | Drainage Area (sq. miles) |
| ----------------- | ---------------- | ------------------------- |
| 64.3              | 27               | .44                       |
| 65.8              | 27               | .416                      |
