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

# Define leakiness value
L = 0.1

print('checkpoint2')

# __________________________ PAMATER RANGES OF INTEREST ____________________________
#                               CAN EDIT THIS CELL                                 #|
                                                                                   #|
beta_x_min  = 0.01                                                                 #|
beta_x_max  = 50                                                                   #|
beta_x_no   = 1000                                                                 #|
beta_x_vals = np.linspace(beta_x_min,beta_x_max,beta_x_no)                         #|
                                                                                   #|
#We are only taking 1 betax at a time                                              #|
betaindex = int(sys.argv[1])                                                       #|
beta_x_vals = np.array([beta_x_vals[betaindex]])                                   #|
beta_x_no = 1                                                                      #|
                                                                                   #|
beta_y_min  = 0.01                                                                 #|
beta_y_max  = 50                                                                   #|
beta_y_no   = 1000                                                                 #|
beta_y_vals = np.linspace(beta_y_min,beta_y_max,beta_y_no)                         #|
                                                                                   #|
n_min  = 0.01                                                                      #|
n_max  = 10                                                                        #|
n_no   = 1000                                                                      #|
n_vals = np.linspace(n_min,n_max,n_no)                                             #|
                                                                                   #|
# __________________________________________________________________________________

print('checkpoint3')

# ________________ TABULATE OUTER CUBE WHILE FILTERING OUT REGIONS OF CUBE WE DO NOT WANT _________________
#                        IE. CREATING PARAMTER POLYHEDRON SUBSPACE OF INTEREST                            #|
                                                                                                          #|
#  ---------------------------------------                                                                #|
# | beta_x value | beta_y value | n value |                                                               #|
# |       #      |       #      |    #    | <--- row 0                                                    #|
# |       #      |       #      |    #    |                                                               #|
# |       #      |       #      |    #    |                                                               #|
# |       #      |       #      |    #    | <--- row (beta_x_no)*(beta_y_no)*(n_no)                       #|
#  ---------------------------------------                                                                #|
                                                                                                          #|
# Initialise memory corresponding to largest case scenario                                                #|
ParamCombinations = np.full( (beta_x_no*beta_y_no*n_no , 3) , None)                                       #|
                                                                                                          #|
# Dummy counter to track current row in table                                                             #|
currentrow = 0                                                                                            #|
                                                                                                          #|
# For each position in parameter space cube                                                               #|
for beta_x_val in beta_x_vals:                                                                            #|
  for beta_y_val in beta_y_vals:                                                                          #|
    for n_val in n_vals:                                                                                  #|
        ParamCombinations[currentrow,:] = np.array([beta_x_val, beta_y_val, n_val])                       #|
        # Update current row                                                                              #|
        currentrow += 1                                                                                   #|
                                                                                                          #|
# _________________________________________________________________________________________________________

print('checkpoint4')

# Replacment code
rows = ParamCombinations.shape[0] 

print('checkpoint5')

# Replacement code
data = np.load('Toggle_steadystates' + str(betaindex) + '.npz', allow_pickle=True)
xss1 = data['xss1']
xss2 = data['xss2']
yss1 = data['yss1']
yss2 = data['yss2']

print('checkpoint6')

# ___________________________________ DEFINE SENSITIVITY FUNCTIONS ___________________________________
#                                          CAN EDIT THIS CELL                                        #|
                                                                                                     #|
def expr(xss, yss, beta_x, beta_y, n):
    return xss * yss * beta_x * beta_y - n**2 * (L - xss) * (L - yss) * (L - xss + beta_x) * (L - yss + beta_y)

# Define analytical expression for s_betax(xss)                                                      #|
def S_betax_xss_analytic(xss, yss, beta_x, beta_y, n):                                               #|
    numer = (L - xss)**2 * yss * beta_x * beta_y
    denom = (-L + xss) * expr(xss, yss, beta_x, beta_y, n)
    sensitivity = numer/denom
    return abs(sensitivity)                                                                          #|
                                                                                                     #|
# ____________________________                                                                       #|
                                                                                                     #|
# Define analytical expression for s_betay(xss)                                                      #|
def S_betay_xss_analytic(xss, yss, beta_x, beta_y, n):                                               #|
    
    frac1 = beta_x / (-L + xss)
    
    numer = n * (L - xss)**2 * (-L + yss) * (-1 + frac1) * (beta_y)
    denom = expr(xss, yss, beta_x, beta_y, n)
    sensitivity = - numer/denom                                                                      #|
    return abs(sensitivity)                                                                          #|
                                                                                                     #|
# ____________________________                                                                       #|
                                                                                                     #|
# Define analytical expression for s_n(xss)                                                          #|
def S_n_xss_analytic(xss, yss, n, beta_x, beta_y):                                                   #|
    
    frac1 = beta_x / (-L + xss)
    frac2 = xss * yss * beta_x * beta_y / (L - xss)**2
    
    numer = n * (-1 + frac1) * (n * (L - yss)**2 * np.log(xss) + (n * (L - yss) * np.log(xss) + yss * np.log(yss)) * beta_y)
    denom = frac2 + n**2 * (L - yss) * (-1 + frac1) * (L - yss + beta_y)
    sensitivity = - numer/denom                                                                      #|
    return abs(sensitivity)                                                                          #|
                                                                                                     #|
# ____________________________                                                                       #|
                                                                                                     #|
# Define analytical expression for s_betax(yss)                                                      #|
def S_betax_yss_analytic(xss, yss, n, beta_x, beta_y):                                               #|
    
    frac3 = beta_y / (-L + yss)
    
    numer = n * (L - yss)**2 * (-L + xss) * (-1 + frac3) * (beta_x)
    denom = expr(xss, yss, beta_x, beta_y, n)
    sensitivity = - numer/denom                                                                      #|
    return abs(sensitivity)                                                                          #|
                                                                                                     #|
# ____________________________                                                                       #|
                                                                                                     #|
# Define analytical expression for s_betay(yss)                                                      #|
def S_betay_yss_analytic(xss, yss, n, beta_x, beta_y):                                               #|
    numer = (L - yss)**2 * xss * beta_x * beta_y
    denom = (-L + yss) * expr(xss, yss, beta_x, beta_y, n)
    sensitivity = - numer/denom                                                                      #|
    return abs(sensitivity)                                                                          #|
                                                                                                     #|
# ____________________________                                                                       #|
                                                                                                     #|
# Define analytical expression for s_n(yss)                                                          #|
def S_n_yss_analytic(xss, yss, n, beta_x, beta_y):                                                   #|
    
    frac3 = beta_y / (-L + yss)
    frac4 = xss * yss * beta_x * beta_y / (L - yss)**2
    
    numer = n * (n * (L - xss)**2 * np.log(yss) + (xss * np.log(xss) + n * (L - xss) * np.log(yss)) * beta_x) * (-1 + frac3)
    denom = n**2 * (L - xss)**2 * (-1 + frac3) + frac4 + beta_x * n**2 * (L - xss) * (-1 + frac3)
    sensitivity = - numer/denom                                                                      #|
    return abs(sensitivity)                                                                          #|
                                                                                                     #|
#_____________________________________________________________________________________________________

print('checkpoint7')

# _______________________ TABLE OF SENSITIVITIES FOR STEADY STATES 1 AND 2 ____________________________
#                                                                                                     #|
#                                                                                                     #|
# Create two empty sensitivity space numpy array of shape                                             #|
#  -------------------------------------------------------------------------------------------------  #|
# | S_{beta_x}(xss) | S_{beta_x}(yss) | S_{beta_y}(xss) | S_{beta_y}(yss) | S_{n}(xss) | S_{n}(yss) | #|
# |         #       |         #       |         #       |         #       |      #     |      #     | #|
# |         #       |         #       |         #       |         #       |      #     |      #     | #|
# |         #       |         #       |         #       |         #       |      #     |      #     | #|
# |         #       |         #       |         #       |         #       |      #     |      #     | #|
#  -------------------------------------------------------------------------------------------------  #|
Sens1 = np.empty([rows, 6])                                                                           #|
Sens2 = np.empty([rows, 6])                                                                           #|
                                                                                                      #|
# For each row in parameter table                                                                     #|
for row in range(rows):                                                                               #|
                                                                                                      #|
      # get the corresponding parameter values                                                        #|
      beta_x_val = ParamCombinations[row,0]                                                           #|
      beta_y_val = ParamCombinations[row,1]                                                           #|
      n_val      = ParamCombinations[row,2]                                                           #|
                                                                                                      #|
      # get the corresponding steady state 1 values                                                   #|
      xss1_val = xss1[row]                                                                            #|
      yss1_val = yss1[row]                                                                            #|
      # get the corresponding steady state 2 values                                                   #|
      xss2_val = xss2[row]                                                                            #|
      yss2_val = yss2[row]                                                                            #|
                                                                                                      #|
      # compute sensitivity values of steady state 1                                                  #|
      S_beta_x_xss_val1 = S_betax_xss_analytic(xss1_val, yss1_val, n_val, beta_x_val, beta_y_val)     #|
      S_beta_x_yss_val1 = S_betax_yss_analytic(xss1_val, yss1_val, n_val, beta_x_val, beta_y_val)     #|
      S_beta_y_xss_val1 = S_betay_xss_analytic(xss1_val, yss1_val, n_val, beta_x_val, beta_y_val)     #|
      S_beta_y_yss_val1 = S_betay_yss_analytic(xss1_val, yss1_val, n_val, beta_x_val, beta_y_val)     #|
      S_n_xss_val1      =     S_n_xss_analytic(xss1_val, yss1_val, n_val, beta_x_val, beta_y_val)     #|
      S_n_yss_val1      =     S_n_yss_analytic(xss1_val, yss1_val, n_val, beta_x_val, beta_y_val)     #|
      # compute sensitivity values of steady state 2                                                  #|
      S_beta_x_xss_val2 = S_betax_xss_analytic(xss2_val, yss2_val, n_val, beta_x_val, beta_y_val)     #|
      S_beta_x_yss_val2 = S_betax_yss_analytic(xss2_val, yss2_val, n_val, beta_x_val, beta_y_val)     #|
      S_beta_y_xss_val2 = S_betay_xss_analytic(xss2_val, yss2_val, n_val, beta_x_val, beta_y_val)     #|
      S_beta_y_yss_val2 = S_betay_yss_analytic(xss2_val, yss2_val, n_val, beta_x_val, beta_y_val)     #|
      S_n_xss_val2      =     S_n_xss_analytic(xss2_val, yss2_val, n_val, beta_x_val, beta_y_val)     #|
      S_n_yss_val2      =     S_n_yss_analytic(xss2_val, yss2_val, n_val, beta_x_val, beta_y_val)     #|
                                                                                                      #|
      # Add sensitivity values to sensitivity table 1                                                 #|
      Sens1[row,:] = np.array([S_beta_x_xss_val1,                                                     #|
                               S_beta_x_yss_val1,                                                     #|
                               S_beta_y_xss_val1,                                                     #|
                               S_beta_y_yss_val1,                                                     #|
                               S_n_xss_val1     ,                                                     #|
                               S_n_yss_val1    ]).flatten()                                           #|
      # Add sensitivity values to sensitivity table 2                                                 #|
      Sens2[row,:] = np.array([S_beta_x_xss_val2,                                                     #|
                               S_beta_x_yss_val2,                                                     #|
                               S_beta_y_xss_val2,                                                     #|
                               S_beta_y_yss_val2,                                                     #|
                               S_n_xss_val2     ,                                                     #|
                               S_n_yss_val2    ]).flatten()                                           #|
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
Sens1Pair1  = Sens1[:, [0, 1]]      #Columns: 'S_beta_x_xss', 'S_beta_x_yss'                             #|
Sens1Pair2  = Sens1[:, [0, 2]]      #Columns: 'S_beta_x_xss', 'S_beta_y_xss'                             #|
Sens1Pair3  = Sens1[:, [0, 3]]      #Columns: 'S_beta_x_xss', 'S_beta_y_yss'                             #|
Sens1Pair4  = Sens1[:, [0, 4]]      #Columns: 'S_beta_x_xss', 'S_n_xss'                                  #|
Sens1Pair5  = Sens1[:, [0, 5]]      #Columns: 'S_beta_x_xss', 'S_n_yss'                                  #|
Sens1Pair6  = Sens1[:, [1, 2]]      #Columns: 'S_beta_x_yss', 'S_beta_y_xss'                             #|
Sens1Pair7  = Sens1[:, [1, 3]]      #Columns: 'S_beta_x_yss', 'S_beta_y_yss'                             #|
Sens1Pair8  = Sens1[:, [1, 4]]      #Columns: 'S_beta_x_yss', 'S_n_xss'                                  #|
Sens1Pair9  = Sens1[:, [1, 5]]      #Columns: 'S_beta_x_yss', 'S_n_yss'                                  #|
Sens1Pair10 = Sens1[:, [2, 3]]      #Columns: 'S_beta_y_xss', 'S_beta_y_yss'                             #|
Sens1Pair11 = Sens1[:, [2, 4]]      #Columns: 'S_beta_y_xss', 'S_n_xss'                                  #|
Sens1Pair12 = Sens1[:, [2, 5]]      #Columns: 'S_beta_y_xss', 'S_n_yss'                                  #|
Sens1Pair13 = Sens1[:, [3, 4]]      #Columns: 'S_beta_y_yss', 'S_n_xss'                                  #|
Sens1Pair14 = Sens1[:, [3, 5]]      #Columns: 'S_beta_y_yss', 'S_n_yss'                                  #|
Sens1Pair15 = Sens1[:, [4, 5]]      #Columns: 'S_n_xss', 'S_n_yss'                                       #|
                                                                                                         #|
# ______________                                                                                         #|
                                                                                                         #|
# Create a new table for each unique pair of sensitivites                                                #|
Sens2Pair1  = Sens2[:, [0, 1]]      #Columns: 'S_beta_x_xss', 'S_beta_x_yss'                             #|
Sens2Pair2  = Sens2[:, [0, 2]]      #Columns: 'S_beta_x_xss', 'S_beta_y_xss'                             #|
Sens2Pair3  = Sens2[:, [0, 3]]      #Columns: 'S_beta_x_xss', 'S_beta_y_yss'                             #|
Sens2Pair4  = Sens2[:, [0, 4]]      #Columns: 'S_beta_x_xss', 'S_n_xss'                                  #|
Sens2Pair5  = Sens2[:, [0, 5]]      #Columns: 'S_beta_x_xss', 'S_n_yss'                                  #|
Sens2Pair6  = Sens2[:, [1, 2]]      #Columns: 'S_beta_x_yss', 'S_beta_y_xss'                             #|
Sens2Pair7  = Sens2[:, [1, 3]]      #Columns: 'S_beta_x_yss', 'S_beta_y_yss'                             #|
Sens2Pair8  = Sens2[:, [1, 4]]      #Columns: 'S_beta_x_yss', 'S_n_xss'                                  #|
Sens2Pair9  = Sens2[:, [1, 5]]      #Columns: 'S_beta_x_yss', 'S_n_yss'                                  #|
Sens2Pair10 = Sens2[:, [2, 3]]      #Columns: 'S_beta_y_xss', 'S_beta_y_yss'                             #|
Sens2Pair11 = Sens2[:, [2, 4]]      #Columns: 'S_beta_y_xss', 'S_n_xss'                                  #|
Sens2Pair12 = Sens2[:, [2, 5]]      #Columns: 'S_beta_y_xss', 'S_n_yss'                                  #|
Sens2Pair13 = Sens2[:, [3, 4]]      #Columns: 'S_beta_y_yss', 'S_n_xss'                                  #|
Sens2Pair14 = Sens2[:, [3, 5]]      #Columns: 'S_beta_y_yss', 'S_n_yss'                                  #|
Sens2Pair15 = Sens2[:, [4, 5]]      #Columns: 'S_n_xss', 'S_n_yss'                                       #|
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
Sens1mask2 = paretoset(Sens1Pair2, sense=["min", "min"])                                                 #|
paretoset_Sens1Pair2 = Sens1Pair2[Sens1mask2]                                                            #|
                                                                                                         #|
Sens1mask3 = paretoset(Sens1Pair3, sense=["min", "min"])                                                 #|
paretoset_Sens1Pair3 = Sens1Pair3[Sens1mask3]                                                            #|
                                                                                                         #|
Sens1mask4 = paretoset(Sens1Pair4, sense=["min", "min"])                                                 #|
paretoset_Sens1Pair4 = Sens1Pair4[Sens1mask4]                                                            #|
                                                                                                         #|
Sens1mask5 = paretoset(Sens1Pair5, sense=["min", "min"])                                                 #|
paretoset_Sens1Pair5 = Sens1Pair5[Sens1mask5]                                                            #|
                                                                                                         #|
Sens1mask6 = paretoset(Sens1Pair6, sense=["min", "min"])                                                 #|
paretoset_Sens1Pair6 = Sens1Pair6[Sens1mask6]                                                            #|
                                                                                                         #|
Sens1mask7 = paretoset(Sens1Pair7, sense=["min", "min"])                                                 #|
paretoset_Sens1Pair7 = Sens1Pair7[Sens1mask7]                                                            #|
                                                                                                         #|
Sens1mask8 = paretoset(Sens1Pair8, sense=["min", "min"])                                                 #|
paretoset_Sens1Pair8 = Sens1Pair8[Sens1mask8]                                                            #|
                                                                                                         #|
Sens1mask9 = paretoset(Sens1Pair9, sense=["min", "min"])                                                 #|
paretoset_Sens1Pair9 = Sens1Pair9[Sens1mask9]                                                            #|
                                                                                                         #|
Sens1mask10 = paretoset(Sens1Pair10, sense=["min", "min"])                                               #|
paretoset_Sens1Pair10 = Sens1Pair10[Sens1mask10]                                                         #|
                                                                                                         #|
Sens1mask11 = paretoset(Sens1Pair11, sense=["min", "min"])                                               #|
paretoset_Sens1Pair11 = Sens1Pair11[Sens1mask11]                                                         #|
                                                                                                         #|
Sens1mask12 = paretoset(Sens1Pair12, sense=["min", "min"])                                               #|
paretoset_Sens1Pair12 = Sens1Pair12[Sens1mask12]                                                         #|
                                                                                                         #|
Sens1mask13 = paretoset(Sens1Pair13, sense=["min", "min"])                                               #|
paretoset_Sens1Pair13 = Sens1Pair13[Sens1mask13]                                                         #|
                                                                                                         #|
Sens1mask14 = paretoset(Sens1Pair14, sense=["min", "min"])                                               #|
paretoset_Sens1Pair14 = Sens1Pair14[Sens1mask14]                                                         #|
                                                                                                         #|
Sens1mask15 = paretoset(Sens1Pair15, sense=["min", "min"])                                               #|
paretoset_Sens1Pair15 = Sens1Pair15[Sens1mask15]                                                         #|
                                                                                                         #|
# Save tables of Pareto points for each sensitivity pair                                                 #|
np.savez('Toggle_Paretos_Sens1' + str(betaindex) + '.npz',                                               #|
							paretoset_Sens1Pair1  = paretoset_Sens1Pair1,    #|
                                                        paretoset_Sens1Pair2  = paretoset_Sens1Pair2,    #|
                                                        paretoset_Sens1Pair3  = paretoset_Sens1Pair3,    #|
                                                        paretoset_Sens1Pair4  = paretoset_Sens1Pair4,    #|
                                                        paretoset_Sens1Pair5  = paretoset_Sens1Pair5,    #|
                                                        paretoset_Sens1Pair6  = paretoset_Sens1Pair6,    #|
                                                        paretoset_Sens1Pair7  = paretoset_Sens1Pair7,    #|
                                                        paretoset_Sens1Pair8  = paretoset_Sens1Pair8,    #|
                                                        paretoset_Sens1Pair9  = paretoset_Sens1Pair9,    #|
                                                        paretoset_Sens1Pair10 = paretoset_Sens1Pair10,   #|
                                                        paretoset_Sens1Pair11 = paretoset_Sens1Pair11,   #|
                                                        paretoset_Sens1Pair12 = paretoset_Sens1Pair12,   #|
                                                        paretoset_Sens1Pair13 = paretoset_Sens1Pair13,   #|
                                                        paretoset_Sens1Pair14 = paretoset_Sens1Pair14,   #|
                                                        paretoset_Sens1Pair15 = paretoset_Sens1Pair15)   #|
                                                                                                         #|
# ______________                                                                                         #|
                                                                                                         #|
Sens2mask1 = paretoset(Sens2Pair1, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair1 = Sens2Pair1[Sens2mask1]                                                            #|
                                                                                                         #|
Sens2mask2 = paretoset(Sens2Pair2, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair2 = Sens2Pair2[Sens2mask2]                                                            #|
                                                                                                         #|
Sens2mask3 = paretoset(Sens2Pair3, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair3 = Sens2Pair3[Sens2mask3]                                                            #|
                                                                                                         #|
Sens2mask4 = paretoset(Sens2Pair4, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair4 = Sens2Pair4[Sens2mask4]                                                            #|
                                                                                                         #|
Sens2mask5 = paretoset(Sens2Pair5, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair5 = Sens2Pair5[Sens2mask5]                                                            #|
                                                                                                         #|
Sens2mask6 = paretoset(Sens2Pair6, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair6 = Sens2Pair6[Sens2mask6]                                                            #|
                                                                                                         #|
Sens2mask7 = paretoset(Sens2Pair7, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair7 = Sens2Pair7[Sens2mask7]                                                            #|
                                                                                                         #|
Sens2mask8 = paretoset(Sens2Pair8, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair8 = Sens2Pair8[Sens2mask8]                                                            #|
                                                                                                         #|
Sens2mask9 = paretoset(Sens2Pair9, sense=["min", "min"])                                                 #|
paretoset_Sens2Pair9 = Sens2Pair9[Sens2mask9]                                                            #|
                                                                                                         #|
Sens2mask10 = paretoset(Sens2Pair10, sense=["min", "min"])                                               #|
paretoset_Sens2Pair10 = Sens2Pair10[Sens2mask10]                                                         #|
                                                                                                         #|
Sens2mask11 = paretoset(Sens2Pair11, sense=["min", "min"])                                               #|
paretoset_Sens2Pair11 = Sens2Pair11[Sens2mask11]                                                         #|
                                                                                                         #|
Sens2mask12 = paretoset(Sens2Pair12, sense=["min", "min"])                                               #|
paretoset_Sens2Pair12 = Sens2Pair12[Sens2mask12]                                                         #|
                                                                                                         #|
Sens2mask13 = paretoset(Sens2Pair13, sense=["min", "min"])                                               #|
paretoset_Sens2Pair13 = Sens2Pair13[Sens2mask13]                                                         #|
                                                                                                         #|
Sens2mask14 = paretoset(Sens2Pair14, sense=["min", "min"])                                               #|
paretoset_Sens2Pair14 = Sens2Pair14[Sens2mask14]                                                         #|
                                                                                                         #|
Sens2mask15 = paretoset(Sens2Pair15, sense=["min", "min"])                                               #|
paretoset_Sens2Pair15 = Sens2Pair15[Sens2mask15]                                                         #|
                                                                                                         #|
# Save tables of Pareto points for each sensitivity pair                                                 #|
np.savez('Toggle_Paretos_Sens2' + str(betaindex) + '.npz',                                               #|
							paretoset_Sens2Pair1  = paretoset_Sens2Pair1,    #|
                                                        paretoset_Sens2Pair2  = paretoset_Sens2Pair2,    #|
                                                        paretoset_Sens2Pair3  = paretoset_Sens2Pair3,    #|
                                                        paretoset_Sens2Pair4  = paretoset_Sens2Pair4,    #|
                                                        paretoset_Sens2Pair5  = paretoset_Sens2Pair5,    #|
                                                        paretoset_Sens2Pair6  = paretoset_Sens2Pair6,    #|
                                                        paretoset_Sens2Pair7  = paretoset_Sens2Pair7,    #|
                                                        paretoset_Sens2Pair8  = paretoset_Sens2Pair8,    #|
                                                        paretoset_Sens2Pair9  = paretoset_Sens2Pair9,    #|
                                                        paretoset_Sens2Pair10 = paretoset_Sens2Pair10,   #|
                                                        paretoset_Sens2Pair11 = paretoset_Sens2Pair11,   #|
                                                        paretoset_Sens2Pair12 = paretoset_Sens2Pair12,   #|
                                                        paretoset_Sens2Pair13 = paretoset_Sens2Pair13,   #|
                                                        paretoset_Sens2Pair14 = paretoset_Sens2Pair14,   #|
                                                        paretoset_Sens2Pair15 = paretoset_Sens2Pair15)   #|
                                                                                                         #|
#_________________________________________________________________________________________________________

print('checkpoint9')

# ___________________ CORRESPONDING PARETO FRONTS IN PARAMETER SPACE _____________________
                                                                                         #|
# Get the corresponding pareto fronts in parameter space                                 #|
                                                                                         #|
paretoset_Sens1mask1_Param  = ParamCombinations[Sens1mask1]                              #|
paretoset_Sens1mask2_Param  = ParamCombinations[Sens1mask2]                              #|
paretoset_Sens1mask3_Param  = ParamCombinations[Sens1mask3]                              #|
paretoset_Sens1mask4_Param  = ParamCombinations[Sens1mask4]                              #|
paretoset_Sens1mask5_Param  = ParamCombinations[Sens1mask5]                              #|
paretoset_Sens1mask6_Param  = ParamCombinations[Sens1mask6]                              #|
paretoset_Sens1mask7_Param  = ParamCombinations[Sens1mask7]                              #|
paretoset_Sens1mask8_Param  = ParamCombinations[Sens1mask8]                              #|
paretoset_Sens1mask9_Param  = ParamCombinations[Sens1mask9]                              #|
paretoset_Sens1mask10_Param = ParamCombinations[Sens1mask10]                             #|
paretoset_Sens1mask11_Param = ParamCombinations[Sens1mask11]                             #|
paretoset_Sens1mask12_Param = ParamCombinations[Sens1mask12]                             #|
paretoset_Sens1mask13_Param = ParamCombinations[Sens1mask13]                             #|
paretoset_Sens1mask14_Param = ParamCombinations[Sens1mask14]                             #|
paretoset_Sens1mask15_Param = ParamCombinations[Sens1mask15]                             #|
                                                                                         #|
paretoset_Sens2mask1_Param  = ParamCombinations[Sens2mask1]                              #|
paretoset_Sens2mask2_Param  = ParamCombinations[Sens2mask2]                              #|
paretoset_Sens2mask3_Param  = ParamCombinations[Sens2mask3]                              #|
paretoset_Sens2mask4_Param  = ParamCombinations[Sens2mask4]                              #|
paretoset_Sens2mask5_Param  = ParamCombinations[Sens2mask5]                              #|
paretoset_Sens2mask6_Param  = ParamCombinations[Sens2mask6]                              #|
paretoset_Sens2mask7_Param  = ParamCombinations[Sens2mask7]                              #|
paretoset_Sens2mask8_Param  = ParamCombinations[Sens2mask8]                              #|
paretoset_Sens2mask9_Param  = ParamCombinations[Sens2mask9]                              #|
paretoset_Sens2mask10_Param = ParamCombinations[Sens2mask10]                             #|
paretoset_Sens2mask11_Param = ParamCombinations[Sens2mask11]                             #|
paretoset_Sens2mask12_Param = ParamCombinations[Sens2mask12]                             #|
paretoset_Sens2mask13_Param = ParamCombinations[Sens2mask13]                             #|
paretoset_Sens2mask14_Param = ParamCombinations[Sens2mask14]                             #|
paretoset_Sens2mask15_Param = ParamCombinations[Sens2mask15]                             #|
                                                                                         #|
# ______________                                                                         #|
                                                                                         #|
# Save the arrays                                                                        #|
                                                                                         #|
np.savez('Toggle_Paretos_Params1' + str(betaindex) + '.npz',                             #|
			paretoset_Sens1mask1_Param  = paretoset_Sens1mask1_Param,        #|
			paretoset_Sens1mask2_Param  = paretoset_Sens1mask2_Param,        #|
			paretoset_Sens1mask3_Param  = paretoset_Sens1mask3_Param,        #|
			paretoset_Sens1mask4_Param  = paretoset_Sens1mask4_Param,        #|
			paretoset_Sens1mask5_Param  = paretoset_Sens1mask5_Param,        #|
			paretoset_Sens1mask6_Param  = paretoset_Sens1mask6_Param,        #|
			paretoset_Sens1mask7_Param  = paretoset_Sens1mask7_Param,        #|
			paretoset_Sens1mask8_Param  = paretoset_Sens1mask8_Param,        #|
			paretoset_Sens1mask9_Param  = paretoset_Sens1mask9_Param,        #|
			paretoset_Sens1mask10_Param = paretoset_Sens1mask10_Param,       #|
			paretoset_Sens1mask11_Param = paretoset_Sens1mask11_Param,       #|
			paretoset_Sens1mask12_Param = paretoset_Sens1mask12_Param,       #|
			paretoset_Sens1mask13_Param = paretoset_Sens1mask13_Param,       #|
			paretoset_Sens1mask14_Param = paretoset_Sens1mask14_Param,       #|
			paretoset_Sens1mask15_Param = paretoset_Sens1mask15_Param)       #|
                                                                                         #|
np.savez('Toggle_Paretos_Params2' + str(betaindex) + '.npz',                             #|
			paretoset_Sens2mask1_Param  = paretoset_Sens2mask1_Param,        #|
			paretoset_Sens2mask2_Param  = paretoset_Sens2mask2_Param,        #|
			paretoset_Sens2mask3_Param  = paretoset_Sens2mask3_Param,        #|
			paretoset_Sens2mask4_Param  = paretoset_Sens2mask4_Param,        #|
			paretoset_Sens2mask5_Param  = paretoset_Sens2mask5_Param,        #|
			paretoset_Sens2mask6_Param  = paretoset_Sens2mask6_Param,        #|
			paretoset_Sens2mask7_Param  = paretoset_Sens2mask7_Param,        #|
			paretoset_Sens2mask8_Param  = paretoset_Sens2mask8_Param,        #|
			paretoset_Sens2mask9_Param  = paretoset_Sens2mask9_Param,        #|
			paretoset_Sens2mask10_Param = paretoset_Sens2mask10_Param,       #|
			paretoset_Sens2mask11_Param = paretoset_Sens2mask11_Param,       #|
			paretoset_Sens2mask12_Param = paretoset_Sens2mask12_Param,       #|
			paretoset_Sens2mask13_Param = paretoset_Sens2mask13_Param,       #|
			paretoset_Sens2mask14_Param = paretoset_Sens2mask14_Param,       #|
			paretoset_Sens2mask15_Param = paretoset_Sens2mask15_Param)       #|
                                                                                         #|
#_________________________________________________________________________________________

' + str(betaindex) + '
' + str(betaindex) + '

print('checkpoint10')
