# Combines files from code 1



import numpy as np
from paretoset import paretoset



nfiles = 1000

xss1_final = np.empty((0,1))
xss2_final = np.empty((0,1))

paretoset_Sens1Pair1_combined  = np.empty((0, 2))
paretoset_Sens2Pair1_combined  = np.empty((0, 2))

paretoset_Sens1mask1_Param_combined  = np.empty((0, 2))
paretoset_Sens2mask1_Param_combined  = np.empty((0, 2))

ParamCombinations_final = np.empty((0, 2)) #new



for ifile in range(nfiles):

  print('File ' + str(ifile))
  
  filename0 = 'arpos_steadystates' + str(ifile) + '.npz'
  
  filename1 = 'arpos_Paretos_Sens1' + str(ifile) + '.npz'
  filename2 = 'arpos_Paretos_Sens2' + str(ifile) + '.npz'
  
  filename3 = 'arpos_Paretos_Params1' + str(ifile) + '.npz'
  filename4 = 'arpos_Paretos_Params2' + str(ifile) + '.npz'
  
  filename5 = 'arpos_ParamCombinations' + str(ifile) + '.npz' #new
  
  fsteadystate = np.load(filename0, allow_pickle=True)
  
  fsenspair1 = np.load(filename1, allow_pickle=True)
  fsenspair2 = np.load(filename2, allow_pickle=True)
  
  fparams1 = np.load(filename3, allow_pickle=True)
  fparams2 = np.load(filename4, allow_pickle=True)
  
  fparamcombs = np.load(filename5, allow_pickle=True) #new
 
  xss1_final = np.vstack((xss1_final , fsteadystate['xss1']))
  xss2_final = np.vstack((xss2_final , fsteadystate['xss2']))
  
  paretoset_Sens1Pair1_combined       = np.vstack((paretoset_Sens1Pair1_combined      , fsenspair1['paretoset_Sens1Pair1']))
  paretoset_Sens1mask1_Param_combined = np.vstack((paretoset_Sens1mask1_Param_combined, fparams1['paretoset_Sens1mask1_Param']))

  paretoset_Sens2Pair1_combined       = np.vstack((paretoset_Sens2Pair1_combined      , fsenspair2['paretoset_Sens2Pair1']))
  paretoset_Sens2mask1_Param_combined = np.vstack((paretoset_Sens2mask1_Param_combined, fparams2['paretoset_Sens2mask1_Param']))

  ParamCombinations_final = np.vstack((ParamCombinations_final, fparamcombs['ParamCombinations'])) #new


# Run Pareto tool with minimisation setting to get a mask

Sens1mask1_final = paretoset(paretoset_Sens1Pair1_combined, sense=["min", "min"])
paretoset_Sens1Pair1_final = paretoset_Sens1Pair1_combined[Sens1mask1_final]

Sens2mask1_final = paretoset(paretoset_Sens2Pair1_combined, sense=["min", "min"])
paretoset_Sens2Pair1_final = paretoset_Sens2Pair1_combined[Sens2mask1_final]



# Save collection of steady states
print("Saving steady state sets... in progress")

np.savez('arpos_SteadyStates_final.npz',
xss1_final = xss1_final,
xss2_final = xss2_final)

print("Saving steady state sets... complete")



# Save tables of Pareto points for each sensitivity pair
print("Saving Pareto points in sensitivity space... in progress")

np.savez('arpos_Paretos_Sens1_final.npz',
paretoset_Sens1Pair1_final  = paretoset_Sens1Pair1_final)

np.savez('arpos_Paretos_Sens2_final.npz',
paretoset_Sens2Pair1_final  = paretoset_Sens2Pair1_final)

print("Saving Pareto points in sensitivity space...complete")



# __________________ CORRESPONDING PARETO FRONTS IN PARAMETER SPACE ____________________

# Get the corresponding pareto fronts in parameter space

print("Obtaining Pareto points in parameter space... in progress")

paretoset_Sens1mask1_Param_final  = paretoset_Sens1mask1_Param_combined[Sens1mask1_final]
paretoset_Sens2mask1_Param_final  = paretoset_Sens2mask1_Param_combined[Sens2mask1_final]

print("Obtaining Pareto points in parameter space... complete")

# Save the arrays

print("Saving Pareto points in parameter space... in progress")

np.savez('arpos_Paretos_Param1_final.npz', 
paretoset_Sens1mask1_Param_final  = paretoset_Sens1mask1_Param_final)

np.savez('arpos_Paretos_Param2_final.npz', 
paretoset_Sens2mask1_Param_final  = paretoset_Sens2mask1_Param_final)

print("Saving Pareto points in parameter space... complete")

#_______________________ NEW: save collection of all parameter combinations _______________________

print("Saving table of all paramter combinations... in progress")

np.savez('arpos_ParamCombinations_final.npz', ParamCombinations_final = ParamCombinations_final)

print("Saving table of all paramter combinations... complete")

