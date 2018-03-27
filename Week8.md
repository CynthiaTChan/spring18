Cynthia Chan

21 March 2018

Week 8 Assignment


## Purpose

This week's assignment investigates model evaluation techniques. The Dynamically Dimensioned Search (DDS) algorithm is a global optimization algorithm designed to calibrate a model with many parameters. DDS needs to start with an initial parameter value and searches within the feasible parameter space for globally
optimal solutions to a complex problem.

## Methods
USGS Gage observed flow data will be used to compare to modeled data. USGS Gage 01644000, by Goose Creek near Leesburg, VA, is used to
obtain observed flow data. Daily precipitation and temperature data from
2000 - 2009 are obtained from the NCDC for Sterling, VA. The NCDC temperature and precipitation data is used as forcing data to feed into the SnowMelt and Lumped_VSA_model functions in the R EcoHydRology package to obtain modeled flow.

The Dynamically Dimensioned Search (DDS) algorithm is a global optimization
algorithm designed to calibrate a model with many parameters. For our purposes,
DDS is deployed to calibrate the best parameter values for our seven parameters:
1. Forest cover (0 - 1)
2. Time to peak of hyrograph (hours)
3. Cutoff for maximal PET allowed per day (mm)
4. Baseflow recession coefficient
5. Minimal daily CN S value. (mm)
6. Coefficient relating daily Curve Number S to soil water
7. Initial abstraction coefficient for CN-equation. (range ~ 0.05 - 0.2)

The DDS algorithm starts by scaling each parameter. It uses an initial value for each parameter (usually a minimum or maximum bound) and jumps around the feasible parameter space by a perturbation size of 0.2. It evaluates the initial function with the initial parameter and the perturbation moves around the feasible space and attempts to find the best solution, replacing itself if a better evaluation is found. While this is happening, the various decision variables are chosen at random to be held constant or changed by the standard deviation of the normalized decision variable. The algorithm stops when the index finishes running through function evaluations.

I had to remove some data from the NCDC precipitation and temperature set due to missing/ NA values.


## Results and Discussion

| Parameter                                     | Min  | Max | Best |
| --------------------------------------------- | ---- | --- | ---- |
| Forest                                        | 0.1  | 0.9 | 0.14 |
| Time to Peak                                  | 1    | 10  | 8.07 |
| PET cutoff                                    | 4    | 6   | 5.89 |
| Baseflow Recession Coefficient                | 0.01 | 0.2 | 0.01 |
| Minimal Daily CN S                            | 50   | 150 | 77.4 |
| Coefficient relating daily CN S to soil water | 1    | 5   | 4.59 |
| Initial Abstraction                           | 0.05 | 0.2 | 0.61 |

The Nash Sutcliffe Equation is used as a metric of model accuracy compared to actual gage data. The NSE value for the flow model is 0.3667, which means that the model does not perform well. The observed data has lows that are lower than what the model predicts. This could be due to the effect from the Beaverdam Resevoir in nearby Dulles. It could be that altered water use is having an impact on the water quantity outside of what is expected.

![ModelParam](/Users/cynthia/github/spring18/EcoHydrology/Week 8/ModelParam.png)


pandoc Week8.md -o Cynthia_Chan_Week8.pdf
