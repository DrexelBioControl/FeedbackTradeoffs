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
import sys                             #|
#______________________________________#|


# ____________________________ DEFINE DYNAMICAL SYSTEM _______________________________
#                               (CAN EDIT THIS CELL)                                 #|                             
                                                                                     #|
# x-nullcline                                                                        #|
def Equ1(x, a, n):
    return ((a * x**(n-1)) / (1 + x**n)) - 1
                                                                                     #|
# ____________________________________________________________________________________

print('checkpoint1')

# ________________ FUNCTION THAT EVALUATES VECTOR FIELD AT A POINT ___________________
                                                                                     #|
# Function that takes in coordinate   P = [x value],                                 #|
#                        initial time t = time value,                                #|
#                        parameters   params = [param 1 value, param 2 value, ...]   #|
# and returns corresponding value of dx/dt and dy/dt in array of form [dx/dt, dy/dt] #|
def Equs(P, t, params):                                                              #|
                                                                                     #|
    x = P[0]

    a = params[0]
    n = params[1]

    val0 = Equ1(x, a, n)

    return np.array([val0])
                                                                                     #|
# ____________________________________________________________________________________

print('checkpoint2')

# __________________________ PAMATER RANGES OF INTEREST ____________________________
#                               CAN EDIT THIS CELL                                 #|
                                                                                   #|
# Parameter ranges
a_min      = 0.01
a_max      = 50
a_no       = 1000
a_vals = np.linspace(a_min,a_max,a_no)

# We are only taking 1 a value at a time
aindex = int(sys.argv[1])
a_vals = np.array([a_vals[aindex]])
a_no = 1

n_min      = 0.01
n_max      = 10
n_no       = 1000
n_vals = np.linspace(n_min,n_max,n_no)
                                                                                   #|
# __________________________________________________________________________________

print('checkpoint3')

# ________________ TABULATE OUTER CUBE WHILE FILTERING OUT REGIONS OF CUBE WE DO NOT WANT _________________
#                        IE. CREATING PARAMTER POLYHEDRON SUBSPACE OF INTEREST                            #|
                                                                                                          #|
#  -----------------------------                                                                          #|
# |    a value   |    n value   |                                                                         #|
# |       #      |       #      | <--- row 0                                                              #|
# |       #      |       #      |                                                                         #|
# |       #      |       #      |                                                                         #|
# |       #      |       #      | <--- row (a_no)*(n_no)                                                  #|
#  -----------------------------                                                                          #|
                                                                                                          #|
# Initialise memory corresponding to largest case scenario                                                #|
ParamCombinations = np.full( (a_no*n_no , 2) , None )
                                                                                                          #|
# Dummy counter to track current row in table                                                             #|
currentrow = 0                                                                                            #|
                                                                                                          #|
# For each position in parameter space cube                                                               #|
for a_val in a_vals:
  for n_val in n_vals:
    ParamCombinations[currentrow,:] = np.array([a_val, n_val])
    # Update current row
    currentrow += 1
                                                                                                          #|
# _________________________________________________________________________________________________________

print('checkpoint4a')
np.savez('arpos_ParamCombinations' + str(aindex) + '.npz', ParamCombinations = ParamCombinations) #new
print('checkpoint4b')

# _____________________________________________ TABLE OF X STEADY STATES ____________________________________________
#                                        CAN EDIT INITGUESSES ARRAY IN THIS CELL                                    #|
#                                                                                                                   #|
#             ---------                               ---------                                                     #|
#            |   xss   |                             |   yss   |                                                    #|
#            |    #    |                             |    #    |                                                    #|
# xss1   =   |    #    |        and       xss2   =   |    #    |                                                    #|
#            |    #    |                             |    #    |                                                    #|
#            |    #    |                             |    #    |                                                    #|
#             ---------                               ---------                                                     #|
#                                                                                                                   #|
                                                                                                                    #|
# Get number of rows in table                                                                                       #|
rows = ParamCombinations.shape[0]                                                                                   #|
                                                                                                                    #|
# Initialize empty arrays to store steady-state values (xss) for the two distinct solutions
xss1 = np.empty((rows, 1))  # To store the first x steady state for each row                                        #|
xss2 = np.empty((rows, 1))  # To store the second x steady state for each row                                       #|
                                                                                                                    #|
# Define a threshold for what you consider "far enough apart"                                                       #|
DISTANCE_THRESHOLD = 0.2
                                                                                                                    #|
# Function to calculate the Euclidean distance between two points                                                   #|
def euclidean_distance(x1, x2):
    return abs(x1 - x2)
                                                                                                                    #|
# For each position in parameter polyhedron                                                                         #|
for row in range(rows):                                                                                             #|
                                                                                                                    #|
    # Extract the parameter values (a_val and n_val) from the current row
    a_val = ParamCombinations[row, 0]
    n_val = ParamCombinations[row, 1]
                                                                                                                    #|
    # Store the parameter values in an array for passing to the equation solver                                     #|
    params = np.array([a_val, n_val])
                                                                                                                    #|
    # Initial guesses for solving the steady-state equations                                                        #|
    InitGuesses = [
        np.array([0.5]),
        np.array([1]),
        np.array([1.5]),
        np.array([10])]
                                                                                                                    #|
    # To store valid solutions                                                                                      #|
    solutions = []                                                                                                  #|
                                                                                                                    #|
    # Iterate over the initial guesses and solve the equations                                                      #|
    for InitGuess in InitGuesses:                                                                                   #|
        # Solve the steady-state equations using fsolve                                                             #|
        t = 0.0                                                                                                     #|
        output, infodict, intflag, mesg = fsolve(Equs, InitGuess, args=(t, params), xtol=1e-12, full_output=True)   #|
        # Extract x steady states
        xss = output
        # Residuals from fsolve (how well the solution satisfies the equations)                                     #|
        fvec = infodict['fvec']                                                                                     #|
                                                                                                                    #|
        # Check stability of steady state                                                                           #|
        delta = 1e-8                                                                                                #|
        dEqudx = (Equs([xss+delta], t, params)-Equs([xss], t, params))/delta
        jac = np.array([[dEqudx]])
        eig = jac
        instablility = np.real(eig) >= 0
                                                                                                                    #|
        # Check conditions for valid steady states                                                                  #|
        # i.e. xss is nonzero, residuals small, and successful convergence
        if xss > 0.01 and np.linalg.norm(fvec) < 1e-10 and intflag == 1 and instablility==False:
            # If this is the first valid solution, just store it                                                    #|
            if len(solutions) == 0:                                                                                 #|
                solutions.append(xss)
            else:                                                                                                   #|
                # Compare the new solution with the previous one                                                    #|
                x1 = solutions[0]
                if euclidean_distance(xss, x1) > DISTANCE_THRESHOLD:
                    solutions.append(xss)
                    break  # Stop as we now have two distinct solutions                                             #|
                                                                                                                    #|
    # After looping through the guesses, store the solutions or NaN if no distinct solutions were found             #|
    if len(solutions) == 2:                                                                                         #|
        # Two distinct solutions found, sort and store them                                                         #|
        solutions.sort()
        xss1[row, 0] = solutions[0]
        xss2[row, 0] = solutions[1]
    elif len(solutions) == 1:                                                                                       #|
        # Only one distinct solution found, store it twice                                                          #|
        xss1[row, 0] = solutions[0]
        xss2[row, 0] = solutions[0]
    else:                                                                                                           #|
        # No valid solutions found, store NaN                                                                       #|
        xss1[row, 0] = float('nan')                                                                                 #|
        xss2[row, 0] = float('nan')                                                                                 #|
                                                                                                                    #|
#____________________________________________________________________________________________________________________

print('checkpoint5')

np.savez('arpos_steadystates' + str(aindex) + '.npz', xss1=xss1, xss2=xss2)

print('checkpoint6')

# ___________________________________ DEFINE SENSITIVITY FUNCTIONS ___________________________________
#                                          CAN EDIT THIS CELL                                        #|
                                                                                                     #|
# Define analytical expression for s_a(xss)
def S_a_xss_analytic(xss, a, n):
    numer = 1 + xss**n
    denom = 1 - n + xss**n
    sensitivity = numer/denom
    return abs(sensitivity)
                                                                                                     #|
# ____________________________                                                                       #|
                                                                                                     #|
# Define analytical expression for s_n(xss)
def S_n_xss_analytic(xss, a, n):
    numer = n * np.log(xss)
    denom = 1 - n + xss**n
    sensitivity = numer/denom
    return abs(sensitivity)
                                                                                                     #|
#_____________________________________________________________________________________________________

print('checkpoint7')

# _______________________ TABLE OF SENSITIVITIES FOR STEADY STATES 1 AND 2 ____________________________
#                                                                                                     #|
#                                                                                                     #|
# Create two empty sensitivity space numpy array of shape                                             #|
#  -----------------------------------                                                                #|
# |    S_{a}(xss)   |    S_{n}(yss)   |                                                               #|
# |         #       |         #       |                                                               #|
# |         #       |         #       |                                                               #|
# |         #       |         #       |                                                               #|
# |         #       |         #       |                                                               #|
#  -----------------------------------                                                                #|
Sens1 = np.empty([rows, 2])                                                                           #|
Sens2 = np.empty([rows, 2])                                                                           #|
                                                                                                      #|
# For each row in parameter table                                                                     #|
for row in range(rows):                                                                               #|
                                                                                                      #|
      # get the corresponding parameter values                                                        #|
      a_val = ParamCombinations[row,0]
      n_val = ParamCombinations[row,1]
                                                                                                      #|
      # get the corresponding steady state 1 values                                                   #|
      xss1_val = xss1[row]                                                                            #|
      # get the corresponding steady state 2 values                                                   #|
      xss2_val = xss2[row]                                                                            #|
                                                                                                      #|
      # compute sensitivity values of steady state 1                                                  #|
      S_a_xss_val1 = S_a_xss_analytic(xss1_val, a_val, n_val)
      S_n_xss_val1 = S_n_xss_analytic(xss1_val, a_val, n_val)
      # compute sensitivity values of steady state 2                                                  #|
      S_a_xss_val2 = S_a_xss_analytic(xss1_val, a_val, n_val)
      S_n_xss_val2 = S_n_xss_analytic(xss1_val, a_val, n_val)
                                                                                                      #|
      # Add sensitivity values to sensitivity table 1                                                 #|
      Sens1[row,:] = np.array([S_a_xss_val1,
                               S_n_xss_val1]).flatten()
      # Add sensitivity values to sensitivity table 2                                                 #|
      Sens2[row,:] = np.array([S_a_xss_val2,
                               S_n_xss_val2]).flatten()
                                                                                                      #|
#______________________________________________________________________________________________________

print('checkpoint8')

# _______________________ PARETO FRONTS FOR EACH PAIR OF SENSITIVITY POLYHEDRONS _________________________
                                                                                                         #|
# There may be NaNs in the array. Pareto minimisation will think NaNs                                    #|
# are minimum. We don't want this. Let's replace NaNs with infinities.                                   #|
Sens1 = np.where(np.isnan(Sens1), np.inf, Sens1)                                                         #|
Sens2 = np.where(np.isnan(Sens2), np.inf, Sens2)                                                         #|
                                                                                                         #|
# _____________________________________________________________________                                  #|
                                                                                                         #|
# Create a new table for each unique pair of sensitivites                                                #|
Sens1Pair1  = Sens1[:, [0, 1]]      #Columns: 'S_a_xss', 'S_n_yss'
                                                                                                         #|
# ______________                                                                                         #|
                                                                                                         #|
# Create a new table for each unique pair of sensitivites                                                #|
Sens2Pair1  = Sens2[:, [0, 1]]      #Columns: 'S_a_xss', 'S_n_yss'
                                                                                                         #|
# _____________________________________________________________________                                  #|
                                                                                                         #|
# Run Pareto tool with minimisation setting to get a mask.                                               #|
# Each mask is an array of the form [True, False, True, ...].                                            #|
# Indexing another array with this mask will remove rows corresponding to Falses.                        #|
# Eg:  dummy       = [1   , 2   , 3    ]                                                                 #|
#      mask        = [True, True, False]                                                                 #|
#      dummy[mask] = [1   , 2          ]                                                                 #|
                                                                                                         #|
Sens1mask1 = paretoset(Sens1Pair1, sense=["min", "min"])                                                 #|
paretoset_Sens1Pair1 = Sens1Pair1[Sens1mask1]                                                            #|
                                                                                                         #|
# Save tables of Pareto points for each sensitivity pair                                                 #|
np.savez('arpos_Paretos_Sens1' + str(aindex) + '.npz', paretoset_Sens1Pair1  = paretoset_Sens1Pair1)
                                                                                                         #|
# ______________                                                                                         #|
                                                                                                         #|
Sens2mask1 = paretoset(Sens2Pair1, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair1 = Sens2Pair1[Sens2mask1]                                                            #|
                                                                                                         #|
# Save tables of Pareto points for each sensitivity pair                                                 #|
np.savez('arpos_Paretos_Sens2' + str(aindex) + '.npz', paretoset_Sens2Pair1  = paretoset_Sens2Pair1)
                                                                                                         #|
#_________________________________________________________________________________________________________

print('checkpoint9')

# ___________________ CORRESPONDING PARETO FRONTS IN PARAMETER SPACE _____________________
                                                                                         #|
# Get the corresponding pareto fronts in parameter space                                 #|
                                                                                         #|
paretoset_Sens1mask1_Param  = ParamCombinations[Sens1mask1]                              #|
                                                                                         #|
paretoset_Sens2mask1_Param  = ParamCombinations[Sens2mask1]                              #|
                                                                                         #|
# ______________                                                                         #|
                                                                                         #|
# Save the arrays                                                                        #|
                                                                                         #|
np.savez('arpos_Paretos_Params1' + str(aindex) + '.npz',
			paretoset_Sens1mask1_Param  = paretoset_Sens1mask1_Param)
                                                                                         #|
np.savez('arpos_Paretos_Params2' + str(aindex) + '.npz',
			paretoset_Sens2mask1_Param  = paretoset_Sens2mask1_Param)
                                                                                         #|
#_________________________________________________________________________________________

' + str(aindex) + '
' + str(aindex) + '

print('checkpoint10')
