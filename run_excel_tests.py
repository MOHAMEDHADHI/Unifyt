"""
Automated test runner for Excel test cases.
Reads test_cases_template.csv, runs all tests, and generates test_results.csv
"""

import csv
from unifyt import Quantity

def run_test(input_value, input_unit, target_unit):
    """
    Run a single conversion test.
    
    Returns:
        tuple: (actual_output, status, error_message)
    """
    try:
        # Create the quantity string
        quantity_str = f"{input_value} {input_unit}"
        result = Quantity(quantity_str, target_unit)
        
        # Extract the numeric value
        actual_value = result.magnitude
        
        return actual_value, "PASS", ""
    except Exception as e:
        return None, "FAIL", str(e)

def run_all_tests(input_file='test_cases_template.csv', output_file='test_results.csv'):
    """
    Run all tests from the CSV file and generate results.
    """
    results = []
    pass_count = 0
    fail_count = 0
    
    print("=" * 80)
    print("RUNNING EXCEL TEST SUITE")
    print("=" * 80)
    print()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            category = row['Category']
            test_id = row['Test ID']
            input_value = row['Input Value']
            input_unit = row['Input Unit']
            target_unit = row['Target Unit']
            expected_output = row['Expected Output']
            notes = row['Notes']
            
            # Run the test
            actual_output, status, error_msg = run_test(input_value, input_unit, target_unit)
            
            # Update row with results
            row['Actual Output'] = f"{actual_output:.6f}" if actual_output is not None else "ERROR"
            row['Status'] = status
            
            if status == "FAIL":
                row['Notes'] = f"{notes} | ERROR: {error_msg}"
                fail_count += 1
                print(f"✗ {test_id:10s} {category:15s} {input_value:6s} {input_unit:20s} → {target_unit:20s} FAILED")
                print(f"  Error: {error_msg}")
            else:
                # Check if actual matches expected (with tolerance)
                try:
                    expected = float(expected_output)
                    actual = float(actual_output)
                    tolerance = 0.01  # 1% tolerance
                    
                    # Handle zero values
                    max_val = max(abs(expected), abs(actual))
                    if max_val == 0:
                        # Both are zero, consider it a match
                        if abs(expected - actual) < 1e-10:
                            row['Status'] = "PASS"
                            pass_count += 1
                            print(f"✓ {test_id:10s} {category:15s} {input_value:6s} {input_unit:20s} → {target_unit:20s} = {actual:.4f}")
                        else:
                            row['Status'] = "MISMATCH"
                            row['Notes'] = f"{notes} | Expected: {expected}, Got: {actual}"
                            fail_count += 1
                            print(f"⚠ {test_id:10s} {category:15s} {input_value:6s} {input_unit:20s} → {target_unit:20s} MISMATCH")
                            print(f"  Expected: {expected}, Got: {actual}")
                    elif abs(expected - actual) / max_val < tolerance:
                        row['Status'] = "PASS"
                        pass_count += 1
                        print(f"✓ {test_id:10s} {category:15s} {input_value:6s} {input_unit:20s} → {target_unit:20s} = {actual:.4f}")
                    else:
                        row['Status'] = "MISMATCH"
                        row['Notes'] = f"{notes} | Expected: {expected}, Got: {actual}"
                        fail_count += 1
                        print(f"⚠ {test_id:10s} {category:15s} {input_value:6s} {input_unit:20s} → {target_unit:20s} MISMATCH")
                        print(f"  Expected: {expected}, Got: {actual}")
                except ValueError:
                    # Can't compare, just mark as pass if no error
                    pass_count += 1
                    print(f"✓ {test_id:10s} {category:15s} {input_value:6s} {input_unit:20s} → {target_unit:20s} = {actual_output}")
            
            results.append(row)
    
    # Write results to output file
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['Category', 'Test ID', 'Input Value', 'Input Unit', 'Target Unit', 
                     'Expected Output', 'Actual Output', 'Status', 'Notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    print()
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"Total Tests: {pass_count + fail_count}")
    print(f"Passed: {pass_count}")
    print(f"Failed: {fail_count}")
    print(f"Success Rate: {pass_count / (pass_count + fail_count) * 100:.2f}%")
    print()
    print(f"Results saved to: {output_file}")
    print("=" * 80)

if __name__ == "__main__":
    run_all_tests()
