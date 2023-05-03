cd /Users/bradleywoodcock/Documents/GitHub/NP-Longest-Path/exact_solution

# Run test cases
python3 longest_path_exact.py <test_cases/inputs/test_2.txt> test_cases/actual_outputs/test_2.txt
python3 longest_path_exact.py <test_cases/inputs/test_3.txt> test_cases/actual_outputs/test_3.txt
python3 longest_path_exact.py <test_cases/inputs/test_4.txt> test_cases/actual_outputs/test_4.txt
python3 longest_path_exact.py <test_cases/inputs/test_5.txt> test_cases/actual_outputs/test_5.txt
python3 longest_path_exact.py <test_cases/inputs/test_6.txt> test_cases/actual_outputs/test_6.txt
python3 longest_path_exact.py <test_cases/inputs/test_7.txt> test_cases/actual_outputs/test_7.txt
python3 longest_path_exact.py <test_cases/inputs/test_8.txt> test_cases/actual_outputs/test_8.txt
python3 longest_path_exact.py <test_cases/inputs/test_9.txt> test_cases/actual_outputs/test_9.txt
python3 longest_path_exact.py <test_cases/inputs/test_10.txt> test_cases/actual_outputs/test_10.txt
file1="test_cases/outputs/test_10.txt"
file2="test_cases/actual_outputs/test_10.txt"
if cmp -s "$file1" "$file2"; then
    printf 'Test 10: Passed\n'
else
    printf 'Test 10: Failed\n'
fi
python3 longest_path_exact.py <test_cases/inputs/test_11.txt> test_cases/actual_outputs/test_11.txt
#python3 longest_path_exact.py <test_cases/inputs/test_12.txt> test_cases/actual_outputs/test_12.txt
#python3 longest_path_exact.py <test_cases/inputs/test_13.txt> test_cases/actual_outputs/test_13.txt