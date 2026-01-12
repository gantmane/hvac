---
title: "Optimization Techniques"
weight: 3
---

Optimization techniques apply mathematical algorithms to identify optimal HVAC system configurations, operating parameters, and control strategies. These methods balance competing objectives including energy consumption, thermal comfort, indoor air quality, equipment life, and operating costs.

## Optimization Problem Formulation

HVAC optimization problems consist of objective functions, decision variables, and constraints. Typical formulations include:

**Objective Function**:
- Minimize total energy cost: f(x) = Σ(E_i × C_i)
- Minimize peak demand charges
- Minimize CO2 emissions
- Maximize thermal comfort indices (PMV, PPD)
- Maximize system efficiency

**Decision Variables**:
- Supply air temperature (12-18°C typical range)
- Supply air flow rates (variable volume systems)
- Chilled water temperature (4-10°C)
- Condenser water temperature (18-32°C)
- Equipment staging sequences
- Zone setpoints (20-26°C occupied, setback ranges)

**Constraints**:
- Thermal comfort limits: -0.5 ≤ PMV ≤ 0.5 (Category A per ISO 7730)
- Equipment capacity limits: 0 ≤ Q ≤ Q_max
- Supply air humidity: 30% ≤ RH ≤ 60%
- Minimum outdoor air requirements per ASHRAE 62.1
- Pressure differential requirements for critical zones

## Genetic Algorithms for HVAC

Genetic algorithms (GA) mimic natural selection to evolve optimal solutions through generations of candidate designs.

**Algorithm Structure**:

1. **Initialize Population**: Generate N random solutions (chromosomes)
2. **Fitness Evaluation**: Calculate objective function for each solution
3. **Selection**: Choose parents based on fitness (tournament, roulette wheel)
4. **Crossover**: Combine parent genes to create offspring (single-point, uniform)
5. **Mutation**: Randomly alter genes (typically 1-5% probability)
6. **Replace Population**: Insert offspring into next generation
7. **Terminate**: Stop after convergence or maximum generations (100-1000 typical)

**HVAC Applications**:
- Chiller plant optimization: sequence multiple chillers, pumps, cooling towers
- Duct and pipe sizing: minimize material cost while meeting pressure drop constraints
- Equipment selection: balance capital cost versus operating efficiency
- Control schedule optimization: develop optimal start/stop times for equipment

**Example Chromosome Encoding**:
```
[T_supply, CFM_zone1, CFM_zone2, ..., Chiller_stages, Pump_speed]
```

**Performance Parameters**:
- Population size: 50-200 individuals
- Crossover rate: 0.6-0.9
- Mutation rate: 0.01-0.05
- Convergence criterion: < 0.1% improvement over 20 generations

## Gradient-Based Optimization

Gradient methods use derivative information to iteratively move toward optimal solutions. These deterministic approaches work well for continuous, differentiable problems.

**Gradient Descent Algorithm**:

x_{k+1} = x_k - α ∇f(x_k)

Where:
- x_k = current solution vector
- α = step size (learning rate): 0.001-0.1 typical
- ∇f(x_k) = gradient of objective function

**Newton's Method**:

x_{k+1} = x_k - [H(x_k)]^(-1) ∇f(x_k)

Where H(x_k) is the Hessian matrix (second derivatives). Converges faster than gradient descent but requires more computation.

**HVAC Applications**:
- Optimal supply temperature reset based on load conditions
- Economizer control optimization (mixing damper position)
- Chilled water differential pressure setpoint optimization
- VAV box damper position control for zone temperature

**Advantages**:
- Fast convergence for convex problems
- Low computational cost per iteration
- Guaranteed convergence for well-behaved functions

**Limitations**:
- Can converge to local minima in non-convex problems
- Requires differentiable objective functions
- Sensitive to initial conditions

## Sequential Quadratic Programming (SQP)

SQP solves nonlinear constrained optimization by approximating the problem as a sequence of quadratic programs.

**Formulation**:
Minimize f(x) subject to:
- g_i(x) ≤ 0 (inequality constraints)
- h_j(x) = 0 (equality constraints)

**HVAC Applications**:
- Central plant optimization with equipment capacity constraints
- Optimal load distribution among parallel chillers
- Pump speed optimization with pressure constraints
- Temperature and humidity control with comfort bounds

**Typical Convergence**: 10-50 iterations for moderate complexity problems

## Multi-Objective Optimization (MOO)

HVAC systems inherently involve conflicting objectives. MOO identifies the Pareto front: solutions where improving one objective worsens another.

**Common HVAC Objective Pairs**:
- Energy cost versus thermal comfort
- Capital cost versus lifecycle cost
- Energy efficiency versus peak demand
- Indoor air quality versus energy consumption

**Pareto Optimality**:
A solution x* is Pareto optimal if no other solution y exists where:
- f_i(y) ≤ f_i(x*) for all objectives i
- f_j(y) < f_j(x*) for at least one objective j

**Weighted Sum Method**:
F(x) = w_1·f_1(x) + w_2·f_2(x) + ... + w_n·f_n(x)

Where Σw_i = 1, w_i ≥ 0. By varying weights, different Pareto points are discovered.

## NSGA-II Algorithm

Non-dominated Sorting Genetic Algorithm II is the standard method for multi-objective HVAC optimization.

**Algorithm Steps**:
1. **Non-dominated Sorting**: Rank solutions by dominance level
2. **Crowding Distance**: Calculate density of solutions in objective space
3. **Selection**: Prefer lower rank, higher crowding distance
4. **Generate Offspring**: Apply crossover and mutation
5. **Combine Populations**: Merge parent and offspring
6. **Truncate**: Select best N solutions for next generation

**HVAC Case Study Results**:
For a VAV system optimization (energy vs. comfort):
- Pareto front contains 50-100 non-dominated solutions
- Energy savings: 15-30% at acceptable comfort penalty
- Optimal supply temperature varies: 12.5-15.5°C
- Fan speed modulation: 40-85% of maximum

## Particle Swarm Optimization (PSO)

PSO mimics social behavior of bird flocking or fish schooling to search solution space.

**Velocity Update**:
v_{i,k+1} = w·v_{i,k} + c_1·r_1·(p_i - x_{i,k}) + c_2·r_2·(p_g - x_{i,k})

**Position Update**:
x_{i,k+1} = x_{i,k} + v_{i,k+1}

Where:
- w = inertia weight (0.4-0.9)
- c_1, c_2 = cognitive and social coefficients (typically 2.0)
- r_1, r_2 = random numbers [0,1]
- p_i = particle's best position
- p_g = global best position

**HVAC Applications**:
- Chiller sequencing and load allocation
- Thermal energy storage charging/discharging schedules
- Zone temperature setpoint optimization
- HVAC scheduling for demand response

**Parameters**:
- Swarm size: 20-50 particles
- Maximum iterations: 100-500
- Convergence: Velocity magnitude < 0.01

## Simulated Annealing

Simulated annealing mimics the metallurgical annealing process, accepting worse solutions probabilistically to escape local minima.

**Acceptance Probability**:
P(accept) = exp(-ΔE / T)

Where:
- ΔE = change in objective function (positive for worse solutions)
- T = temperature parameter (decreases over time)

**Cooling Schedule**:
T_k = T_0 × α^k

Where α = 0.85-0.95 (cooling rate)

**HVAC Applications**:
- Equipment layout optimization (minimize piping/ductwork)
- Retrofit planning (sequence of equipment replacements)
- Maintenance scheduling optimization
- Control parameter tuning

## Design of Experiments (DOE)

DOE systematically varies input parameters to understand their effects on system performance.

**Factorial Design**:
Full factorial: N = L^k (L levels, k factors)
For 3 factors at 2 levels: 2^3 = 8 experiments

**Example HVAC Factors**:
- Supply air temperature: [12°C, 16°C]
- Chilled water setpoint: [5°C, 8°C]
- Outdoor air fraction: [15%, 30%]

**Analysis of Variance (ANOVA)**:
Quantifies contribution of each factor to total variance.

Main effect: E_i = Σ(y_high - y_low) / n

Interaction effect: I_ij measures non-additive effects between factors i and j

## Response Surface Methodology (RSM)

RSM creates polynomial approximations of complex HVAC performance relationships.

**Second-Order Model**:
y = β_0 + Σβ_i·x_i + Σβ_{ii}·x_i^2 + Σβ_{ij}·x_i·x_j + ε

**HVAC Example**: Chiller power consumption model
P_chiller = β_0 + β_1·Q_load + β_2·T_chw + β_3·T_cw + β_{11}·Q_load^2 + β_{12}·Q_load·T_chw + ...

**Optimization on Response Surface**:
Once fitted, standard optimization algorithms rapidly find optimal operating points without running full simulations.

**Accuracy Metrics**:
- R² > 0.95 for good fit
- Root mean square error (RMSE) < 5% of mean response

## Latin Hypercube Sampling (LHS)

LHS efficiently samples multi-dimensional parameter spaces for uncertainty analysis and optimization.

**Procedure**:
1. Divide range of each variable into N intervals of equal probability
2. Sample once from each interval
3. Randomly pair samples across variables

**Advantage over Random Sampling**:
Achieves better space coverage with fewer samples (typically 1.5k to 2k samples, where k = number of variables).

**HVAC Applications**:
- Uncertainty quantification in energy models
- Calibration of building simulation models
- Sensitivity analysis of design parameters

## Bayesian Optimization

Bayesian optimization builds probabilistic models (Gaussian processes) of expensive objective functions.

**Acquisition Function**:
Expected Improvement (EI):
EI(x) = E[max(f(x*) - f(x), 0)]

Where x* is current best solution.

**Algorithm**:
1. Build Gaussian process model from existing evaluations
2. Maximize acquisition function to select next evaluation point
3. Evaluate objective function at selected point
4. Update model
5. Repeat until convergence

**HVAC Applications**:
- Optimization when simulations are computationally expensive (CFD, whole-building energy)
- Control parameter tuning requiring physical experiments
- Model predictive control optimization

**Typical Performance**:
Converges in 50-200 evaluations versus thousands for traditional methods.

## Surrogate Modeling

Surrogate models replace computationally expensive simulations with fast approximations.

**Model Types**:
- Polynomial regression: fast, limited accuracy for complex relationships
- Radial basis functions (RBF): good for scattered data
- Kriging: provides uncertainty estimates
- Artificial neural networks: excellent for highly nonlinear systems

**HVAC Applications**:
- Replace EnergyPlus simulations (30-60 min) with neural network predictions (< 1 sec)
- Enable real-time optimization of complex systems
- Support model predictive control implementations

**Validation Requirements**:
- Training set: 70-80% of data
- Testing set: 20-30% of data
- Cross-validation R² > 0.90

## Control Optimization

Control optimization tunes parameters and strategies for real-time HVAC operation.

**PID Tuning Optimization**:
Objective: Minimize integral of absolute error (IAE)
IAE = ∫|SP(t) - PV(t)|dt

Decision variables: K_p, K_i, K_d

Constraints:
- Avoid oscillation: damping ratio ζ > 0.7
- Limit overshoot: < 10% of setpoint
- Settling time: < 15 minutes typical

**Model Predictive Control (MPC)**:
Solves optimization at each time step over prediction horizon.

min J = Σ[Q·(T_zone - T_setpoint)² + R·u²]

Where:
- Q = comfort penalty weight
- R = energy cost weight
- u = control action (damper position, valve position, etc.)

**Prediction Horizon**: 1-24 hours
**Control Horizon**: 15 minutes to 2 hours

## Practical Implementation Considerations

**Computational Requirements**:
- Genetic algorithms: 10³-10⁵ function evaluations
- Gradient methods: 10¹-10³ function evaluations
- Bayesian optimization: 10²-10³ function evaluations

**Solution Time**:
- Real-time control: < 1 minute
- Daily optimization: 10-60 minutes acceptable
- Design optimization: hours to days

**Robustness Testing**:
Verify optimized solutions across:
- Weather conditions (TMY3 annual data)
- Occupancy variations (±30%)
- Equipment degradation (10-20% capacity loss)

**Validation Methods**:
- Compare optimized versus baseline operation
- Field testing over multiple seasons
- Continuous monitoring of key performance indicators

## Components

- Genetic Algorithms Hvac
- Particle Swarm Optimization Pso
- Simulated Annealing
- Gradient Based Optimization
- Sequential Quadratic Programming
- Multi Objective Optimization Moo
- Pareto Front Identification
- Nsga Ii Algorithm
- Design Of Experiments Doe
- Response Surface Methodology
- Latin Hypercube Sampling
- Monte Carlo Simulation
- Bayesian Optimization
- Surrogate Modeling
- Artificial Neural Networks Optimization
- Fuzzy Optimization
