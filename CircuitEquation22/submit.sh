#!/bin/bash
# Usage: ./farm_out.sh <num_cores> <total_tasks>
#cd /Users/nt625/Documents/GitHub/ACSPaperSep2024/PAPERREVIEWS/NEWCODE/DoublePositive

NUM_CORES=62
TOTAL_TASKS=500
start_time=$(date +%s)

for (( i=0; i<TOTAL_TASKS; i++ )); do
  echo "Running task $i"
  (
    python code1_circuit1_optimisedsolve.py "$i" > /dev/null 2>&1
  ) &

  # Run up to NUM_CORES in parallel
  if (( $((i % NUM_CORES)) == $((NUM_CORES - 1)) )); then
    wait  # Wait for current batch of processes to finish
    end_time=$(date +%s)
    elapsed_time=$((end_time - start_time))
    echo "Elapsed time: $elapsed_time seconds"
  fi
done

wait  # Ensure any remaining processes finish
echo "All tasks are done."

