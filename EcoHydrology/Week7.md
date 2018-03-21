Cynthia Chan

16 March 2018

Week 7 Assignment


## Purpose

This model chains together various models to best simulate hydrologic processes. When models are aggregated, they each carry in their own assumptions concerning inputs and methodology. It is therefore important that an aggregated model considers the various parameter sensitivites and acknowledges how one internal model can affect the others.

## Methodology
Two EcoHydRology functions are utilized: SnowMelt and Lumped_VSA_model.

The SnowMelt model calculates snow pack accumulation and snow melt. The relevant input arguments for this model are:
- Date
- Precipitation (mm)
- Maximum temperature (°C)
- Minimum temperature (°C)
- Degrees latitude
- Slope of the area of interest
- Ground Albedo, 0-1
- Surface Emissivity, 0-1
- Wind speed - either a vector of measured values or a single value of average wind speed for the site (m/s)
- Forest cover (shade) - use this only when determining snowmelt under a canopy, 0-1
- The depth of the snow pack initially (m)
- The density of snow on the ground on the first day (kg/m3)

The Lumped_VSA_model calculates streamflow and saturated area contributing to overland flow. The model was developed in watersheds dominated by excesses in saturation, so it is only applicable for the US Northeast. It is based on the Thornthwaite-Mather water budget which assumes a linearity in the Available Water Content to Evapotranspiration relationship in the soil vadose zone. The Soil Conservation Service Curve Number approach is used to model overland runoff. The relevant inputs arguments for this model are:
- Date
- Precipitation as both rain and snow (mm)
- Maximum temperature (°C)
- Minimum temperature (°C)
- Average watershed and soil depth (mm)
- Porosity of the soil (volumetric fraction, 0-1)
- Available water capacity, Field capacity - wilting point (volumetric fraction, 0-1)
- Percent of the watershed that is impervious (percentage, 0-100)
- Number of wetness classes to distribute runoff over
- Time to peak of hydrograph (hours)
- latitude (degrees)
- Average surface albedo
- Minimal daily CN S value. (mm)
- Coefficient relating daily Curve Number S to soil water
- Initial abstraction coefficient for CN-equation. (range ~ 0.05 - 0.2)

The metric I test the model against is annual peak streamflow, or flooding. Parameters which are in both the SnowMelt model and Lumped_VSA_model are chosen to test for sensitivity, because the individual parameters in one model are not independent of impacts on a subsequent model. Initial abstraction (Ia), forest cover (Fc), storage (Se), percent impervious (PI), and wind speed (u) are chosen as parameters to test for sensitivity in the model with. A Monte Carlo sensitivity analysis with 1000 runs is performed. All parameters except for wind speed are hypothesized to be sensitive. The modeled annual peak flow is compared to the actual peak flow by USGS gage data to estimate how well the model performs. The objective function is the Nash Sutcliffe Model Efficiency equation:
$$NSE = 1 -  \frac{\sum_{t=2}^{n}[(sim_t-obs_t)^2]}{\sum_{t=2}^{n}[(obs_t-\overline{obs_t})^2]}$$

## Results
In Figure 1 below, the relationship between 5 different model inputs is shown as a function of time in Fall Creek. Snow water equivalent is largest in the winter and early spring, and looks to impact discharge. Soil water and ground water storage are highly inversely related.


![FlowvTime](/Users/cynthia/github/spring18/FlowvTime.png)
<p align="center">
Figure 1a: Effective Precipitation vs. Time in Fall Creek, NY, 1950 - 1954
</br>
Figure 1b: Snow Water Equivalent vs. Time in Fall Creek, NY, 1950 - 1954
</br>
Figure 1c: Soil Water vs. Time in Fall Creek, NY, 1950 - 1954
</br>
Figure 1d: Groundwater Storage vs. Time in Fall Creek, NY, 1950 - 1954
</br>
Figure 1e: Discharge vs. Time in Fall Creek, NY, 1950 - 1954
</p>

In Figure 2 below, the five specific model parameters are chosen for a Monte Carlo Sensitivity analysis against peak annual modeled flow as a proxy for flooding. Of the 5 subfigures, Figure 2b shows the largest correlation. It makes sense that the model parameter of percent impervious is very sensitive to flow. With increasing impervious cover over an area, surface water is unable to be infiltrated and runoff and subsequently streamflow will increase. Initial abstraction does not seem to have any imact on modeled flow despite being hypothesized as sensitive. Figures 2c and 2e seem to have a weakly negative relationship with modeled flow. This makes sense since if forest cover increases, pervious cover should also be increasing to allow for water infiltration. Additionally, if storage increases, then the hydrologic cycle should slow down, and streamflow should decrease. In Figure 2d, wind speed surprisingly has a weak positive correlation with modeled flow. This may be due to increased wind speed being a proxy for lack of land cover and turbulence from forest, trees, and so on.

![Sensitivity](/Users/cynthia/github/spring18/Sensitivity.png)
<p align="center">
Figure 2a: Initial Abstraction vs. Modeled Flow in Fall Creek, NY
</br>
Figure 2b: Percent Impervious vs. Modeled Flow in Fall Creek, NY
</br>
Figure 2a: Forest Cover vs. Modeled Flow in Fall Creek, NY
</br>
Figure 2a: Wind Speed vs. Modeled Flow in Fall Creek, NY
</br>
Figure 2a: Storage vs. Modeled Flow in Fall Creek, NY
</p>

In Figure 3 below, the final modeled flow and observed flow are plotted together. The modeled flow is an output of the Lumped_VSA_model and the SnowMelt model is internal model of this analysis. The observed flow values come from the USGS Fall Creek gage. The model follows the trend of observed data well but does not estimate winter snowmelt peaks well. Some points are overestimated and some are underestimated. It also seems to underestimate summer flows. Perhaps it is overestimating groundwater storage in the summer or underestimating soil water. A drawback of this  model is that it does not take into account the dynamic plant uptake of water and its seasonality.

![ModelvObs](/Users/cynthia/github/spring18/ModelvObs.png)
<p align="center">
Figure 3: Modeled Flow and Observed Flow in Fall Creek, 1950 - 1954
</p>

The Nash Sutcliffe Equilibrium for this model is calculated and found to be 0.523. This model is decent at estimating flow based off of forcing data and the constant inputs.

## Discussion
1. We are chaining together different models with different assumptions and therefore error, do water balance errors tend to grow without bounds? Why or why not?


Although we chain together several models, the hydrologic cycle self corrects for factors like increasing ET. Decreased ET will decrease precipitation which keeps ET in check. The highly dependent nature of the individual hydrologic cycle processes prevent our model from growing without bounds.


2. We started off with a poor assumption about the catchment water storage, why doesn't this seem to matter?


The initial assumption about catchment water storage does not matter because our model predicts flow for a longer period than what the initial catchment water storage would effect. That is, the initial conditions matter less for long term analyses.

3. ET is a function of soil water and PET, but PETc (week 5) was a function of plant growth stage, which should also be a function of soil moisture.


  a. We're missing an obvious feedback between soil water and plant growth, but we're not modeling this. How does this limit our predictions?

  Seasonal plant growth will effect present soil water. In the summer and spring, there should be less soil water because this will be taken up by plant root systems. Therefore, it is possible that our model will overestimate summer flows. This does not happen however; another parameter that is underestimating seems to balance this other metric out.

  b. What else does our simple model neglect about plant growth?

  Our simple model neglects that plants will uptake water in the spring and summer and will die in the fall and winter and stop taking in water through root systems. Additionally, presence of plants and growth will change rougnhness in the system and slow down runoff.

pandoc Week7.md -o Cynthia_Chan_Week7.pdf
