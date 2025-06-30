#!/bin/bash

NUM_CORES=62
TOTAL_TASKS=1000
start_time=$(date +%s)
output_file="submit_datacorrection_log.txt"

# Clear the output file at the start of the script
> "$output_file"

for (( i=0; i<TOTAL_TASKS; i++ )); do
  echo "Running task $i" | tee -a "$output_file"
  (
    python code1_negneg_datacorrection.py "$i" >> "$output_file" 2>&1
  ) &

  # Run up to NUM_CORES in parallel
  if (( $((i % NUM_CORES)) == $((NUM_CORES - 1)) )); then
    wait  # Wait for current batch of processes to finish
    end_time=$(date +%s)
    elapsed_time=$((end_time - start_time))
    echo "Elapsed time: $elapsed_time seconds" | tee -a "$output_file"
  fi
done

wait  # Ensure any remaining processes finish
echo "All tasks are done." | tee -a "$output_file"