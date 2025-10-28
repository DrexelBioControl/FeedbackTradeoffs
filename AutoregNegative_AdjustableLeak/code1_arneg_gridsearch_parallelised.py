#  ---------------------------------------------------------------------
# |                                                                     |
# |                   PART 1: CREATING VALUES TO PLOT                   |
# |                                                                     |
#  ---------------------------------------------------------------------


# _________ Python preliminary _________
                                       #|
import numpy as np                     #|
from tqdm import tqdm                  #|
from paretoset import paretoset        #|
from scipy.optimize import fsolve      #|
from joblib import Parallel, delayed   #|
#______________________________________#|


# ______________ DEFINE DYNAMICAL SYSTEM ______________
#                  (CAN EDIT THIS CELL)               #|
                                                      #|
def Equ1(x, a, n):                                    #|
    return a / (1 + x**n) - x
                                                      #|
# _____________________________________________________


# ________________ FUNCTION THAT EVALUATES VECTOR FIELD AT A POINT ___________________
                                                                                     #|
# Function that takes in coordinate   P = [x value],                                 #|
#                        initial time t = time value,                                #|
#                        parameters   params = [param 1 value, param 2 value, ...]   #|
# and returns corresponding value of dx/dt in array of form [dx/dt]                  #|
def Equs(P, t, params):                                                              #|
                                                                                     #|
    x = P[0]                                                                         #|
                                                                                     #|
    a = params[0]                                                                    #|
    n = params[1]                                                                    #|
                                                                                     #|
    val0 = Equ1(x, a, n)                                                             #|
                                                                                     #|
    return np.array([val0])                                                          #|
                                                                                     #|
# ____________________________________________________________________________________


# _______________ DEFINE GRID-SEARCHED POLYHEDRON IN PARAMETER SPACE _______________
#                               CAN EDIT THIS CELL                                 #|
                                                                                   #|
# Parameter range                                                                  #|
                                                                                   #|
a_min  = 0.01                                                                      #|
a_max  = 50                                                                        #|
a_no   = 5000                                                                      #|
a_vals = np.linspace(a_min,a_max,a_no)                                             #|
                                                                                   #|
n_min  = 0.01                                                                      #|
n_max  = 10                                                                        #|
n_no   = 5000                                                                      #|
n_vals = np.linspace(n_min,n_max,n_no)                                             #|
                                                                                   #|
# __________________________________________________________________________________


# _____________ PARALLELISE TABULATING PARAMETER SPACE COORDINATES ______________
                                                                                #|
# Define the function to create a single row of the ParamPolyhedron             #|
def create_param_row(a_val, n_val, rownum):                                     #|
    return (rownum, np.array([a_val, n_val]))                                   #|
                                                                                #|
# Create the full parameter space as a list of tasks to distribute              #|
def generate_param_space():                                                     #|
    param_space = []                                                            #|
    rownum = 0                                                                  #|
    for a_val in a_vals:                                                        #|
        for n_val in n_vals:                                                    #|
            param_space.append((a_val, n_val, rownum))                          #|
            rownum += 1                                                         #|
    return param_space                                                          #|
                                                                                #|
# Parallelize the generation of ParamPolyhedron using joblib                    #|
def generate_param_polyhedron():                                                #|
    param_space = generate_param_space()                                        #|
                                                                                #|
    # Create an empty array to hold the results                                 #|
    ParamPolyhedron = np.empty((a_no * n_no, 2))                                #|
                                                                                #|
    # Use joblib's Parallel to generate the rows of ParamPolyhedron in parallel #|
    results = Parallel(n_jobs=-1)(                                              #|
        delayed(create_param_row)(a_val, n_val, rownum)                         #|
        for a_val, n_val, rownum in tqdm(param_space))                          #|
                                                                                #|
    # Collect results into ParamPolyhedron                                      #|
    for rownum, param_values in results:                                        #|
        ParamPolyhedron[rownum, :] = param_values                               #|
                                                                                #|
    # Save parameter choices                                                    #|
    np.save('ARneg_ParamPolyhedron.npy', ParamPolyhedron)                       #|
                                                                                #|
# _______________________________________________________________________________



generate_param_polyhedron()



# ____________________________________________ TABLE OF X STEADY STATES ___________________________________________
#                                                                                                                 #|
# We want to get the following array                                                                              #|
#                  ---------                                                                                      #|
#                 |   xss   |                                                                                     #|
#                 |    #    |                                                                                     #|
# xssPolyhedron = |    #    |                                                                                     #|
#                 |    #    |                                                                                     #|
#                 |    #    |                                                                                     #|
#                  ---------                                                                                      #|
                                                                                                                  #|
# Load data                                                                                                       #|
ParamPolyhedron = np.load('ARneg_ParamPolyhedron.npy', allow_pickle=True)                                         #|
                                                                                                                  #|
# Get number of rows in the ParamPolyhedron                                                                       #|
rows = ParamPolyhedron.shape[0]                                                                                   #|
                                                                                                                  #|
# Create empty arrays to store x and y steady states                                                              #|
xssPolyhedron = np.empty((rows, 1))                                                                               #|
                                                                                                                  #|
# Define function to solve for steady states                                                                      #|
def solve_steady_state(rownum, ParamPolyhedron):                                                                  #|
    params = ParamPolyhedron[rownum]                                                                              #|
    InitGuesses = [np.array([2]),np.array([0.5]),np.array([4.627])]                                               #|
    t = 0.0                                                                                                       #|
                                                                                                                  #|
    for InitGuess in InitGuesses:                                                                                 #|
        output, infodict, intflag, _ = fsolve(Equs, InitGuess, args=(t, params), xtol=1e-12, full_output=True)    #|
        xss = output                                                                                              #|
        fvec = infodict['fvec']                                                                                   #|
                                                                                                                  #|
        # Check for valid solution                                                                                #|
        if xss > 0.04 and np.linalg.norm(fvec) < 1e-10 and intflag == 1:                                          #|
            return xss, rownum                                                                                    #|
                                                                                                                  #|
    return float('nan'), rownum                                                                                   #|
                                                                                                                  #|
                                                                                                                  #|
# Parallel processing to solve steady states                                                                      #|
results = Parallel(n_jobs=-1)(                                                                                    #|
    delayed(solve_steady_state)(rownum, ParamPolyhedron)                                                          #|
    for rownum in range(rows))                                                                                    #|
                                                                                                                  #|
# Process results and store them in the polyhedron arrays                                                         #|
for xss, rownum in results:                                                                                       #|
    xssPolyhedron[rownum] = xss                                                                                   #|
                                                                                                                  #|
# Save arrays                                                                                                     #|
np.savez('ARneg_EquilibriumPolyhedrons.npz', xssPolyhedron=xssPolyhedron)                                         #|
                                                                                                                  #|
#__________________________________________________________________________________________________________________



# ___________________________________ DEFINE SENSITIVITY FUNCTIONS ___________________________________
#                                          CAN EDIT THIS CELL                                        #|
                                                                                                     #|
# Setting up progress printing of loop                                                               #|
pbar = tqdm(total=2, desc="Defining sensitivity functions")                                          #|
                                                                                                     #|
# Define analytical expression for s_a(xss)                                                          #|
def S_a_xss_analytic(xss, a, n):                                                                     #|
    numer = a * (1 + xss**n)                                                                         #|
    denom = xss + a * n * xss**n + 2 * xss**(1+n) + xss**(1+2*n)                                     #|
    sensitivity = numer/denom                                                                        #|
    return abs(sensitivity)                                                                          #|
# Update progress bar                                                                                #|
pbar.update(1)                                                                                       #|
                                                                                                     #|
# Define analytical expression for s_n(xss)                                                          #|
def S_n_xss_analytic(xss, a, n):                                                                     #|
    numer = a * n * np.log(xss) * xss**(n-1)                                                         #|
    denom = 1 + a * n * xss**(n-1) + 2 * xss**(n) + xss**(2*n)                                       #|
    sensitivity = - numer/denom                                                                      #|
    return abs(sensitivity)                                                                          #|
# Update progress bar                                                                                #|
pbar.update(1)                                                                                       #|
                                                                                                     #|
# Close the progress bar                                                                             #|
pbar.close()                                                                                         #|
                                                                                                     #|
#_____________________________________________________________________________________________________



# __________________________ OBTAIN TABLE OF SENSITIVITIES ___________________________
#                                                                                    #|
# We want to get the following array                                                 #|
#  -------------------------                                                         #|
# | S_{a}(xss) | S_{n}(xss) |                                                        #|
# |      #     |      #     |                                                        #|
# |      #     |      #     |                                                        #|
# |      #     |      #     |                                                        #|
# |      #     |      #     |                                                        #|
#  -------------------------                                                         #|
                                                                                     #|
                                                                                     #|
def compute_sensitivities(rownum, ParamPolyhedron, xssPolyhedron):                   #|
    a_val = ParamPolyhedron[rownum, 0]                                               #|
    n_val = ParamPolyhedron[rownum, 1]                                               #|
                                                                                     #|
    xss_val = xssPolyhedron[rownum]                                                  #|
                                                                                     #|
    return np.array([                                                                #|
        S_a_xss_analytic(xss_val, a_val, n_val),                                     #|
        S_n_xss_analytic(xss_val, a_val, n_val)])                                    #|
                                                                                     #|
                                                                                     #|
# Parallel processing for sensitivity calculations                                   #|
sensitivity_results = Parallel(n_jobs=-1)(                                           #|
    delayed(compute_sensitivities)(rownum, ParamPolyhedron, xssPolyhedron)           #|
    for rownum in range(rows))                                                       #|
                                                                                     #|
# Collect results                                                                    #|
SenPolyhedrons = np.array(sensitivity_results).squeeze()                             #|
                                                                                     #|
# Save table                                                                         #|
np.save('ARneg_SensitivityPolyhedrons.npy', SenPolyhedrons)                          #|
                                                                                     #|
#_____________________________________________________________________________________



# Pareto minimisation will think NaNs are minimum. Replace NaNs with infinities.
SenPolyhedrons = np.where(np.isnan(SenPolyhedrons), np.inf, SenPolyhedrons)


# Obtaining Pareto mask
#print("Obtaining and saving Pareto mask... in progress")
mask = paretoset(SenPolyhedrons, sense=["min", "min"])
np.save('ARneg_ParetoMask.npy', mask)
print("Obtaining and saving Pareto mask... complete")


# Obtaining Pareto front in sensitivity space
print("Obtaining and saving Pareto points in sensitivity space... in progress")
pareto_Sens = SenPolyhedrons[mask]
np.save('ARneg_SensitivityPareto.npy', pareto_Sens)
print("Obtaining and saving Pareto points in sensitivity space... complete")


# Obtaining coordinates in parameter space corresponding to Pareto front in sensitivity space
#print("Obtaining and saving Pareto points in parameter space... in progress")
pareto_Params = ParamPolyhedron[mask]
np.save('ARneg_ParamPareto.npy', pareto_Params)
print("Obtaining and saving Pareto points in parameter space... complete")
