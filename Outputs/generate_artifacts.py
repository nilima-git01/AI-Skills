import pandas as pd
import os

outputs_dir = r"c:\Nilima-Automation\AILLM_Test_Case_generation\Project02_Real_Project_prompt_template\Outputs"

test_cases = [
    {'Test Case ID': 'TC_VWO_001', 'Description': 'Verify successful login with valid credentials', 'Steps': '1. Navigate to VWO login page\n2. Enter valid email\n3. Enter valid password\n4. Click Sign In', 'Expected Result': 'User is redirected to the dashboard', 'Actual Result': 'Pass', 'Status': 'Passed'},
    {'Test Case ID': 'TC_VWO_002', 'Description': 'Verify login with invalid credentials', 'Steps': '1. Navigate to VWO login page\n2. Enter invalid email or password\n3. Click Sign In', 'Expected Result': 'Error message \'Your email, password, IP address or location did not match\' is displayed', 'Actual Result': 'Error message displayed', 'Status': 'Passed'},
    {'Test Case ID': 'TC_VWO_003', 'Description': 'Verify login with empty fields', 'Steps': '1. Navigate to VWO login page\n2. Leave email and password empty\n3. Click Sign In', 'Expected Result': 'Validation error prompts for required fields', 'Actual Result': 'Validation error displayed', 'Status': 'Passed'},
    {'Test Case ID': 'TC_VWO_004', 'Description': 'Verify \'Remember Me\' functionality', 'Steps': '1. Navigate to VWO login page\n2. Enter valid credentials\n3. Check \'Remember Me\'\n4. Click Sign In\n5. Close and reopen browser', 'Expected Result': 'User is automatically logged in or email is pre-filled', 'Actual Result': 'Functionality not fully working', 'Status': 'Failed'},
    {'Test Case ID': 'TC_API_001', 'Description': 'Verify RESTful Booker API POST request', 'Steps': '1. Send POST request to /booking endpoint with valid payload', 'Expected Result': '201 Created and booking details returned', 'Actual Result': '201 Created', 'Status': 'Passed'},
    {'Test Case ID': 'TC_API_002', 'Description': 'Verify RESTful Booker API POST request with missing payload', 'Steps': '1. Send POST request to /booking endpoint with missing payload', 'Expected Result': '400 Bad Request with accurate error message', 'Actual Result': '500 Internal Server Error returned instead of 400', 'Status': 'Failed'}
]

# Generate XLSX
df = pd.DataFrame(test_cases)
df.to_excel(os.path.join(outputs_dir, 'Test_Cases.xlsx'), index=False)

# Generate HTML Traceability Matrix
html_content = '''
<!DOCTYPE html>
<html>
<head>
<style>
table { font-family: Arial, sans-serif; border-collapse: collapse; width: 100%; }
td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; }
tr:nth-child(even) { background-color: #f2f2f2; }
.passed { color: green; font-weight: bold; }
.failed { color: red; font-weight: bold; }
</style>
</head>
<body>
<h2>Requirements Traceability Matrix (Pass/Fail Mapping)</h2>
<table>
  <tr>
    <th>Requirement ID</th>
    <th>Feature</th>
    <th>Test Case ID</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>REQ-01</td>
    <td>VWO Login Authentication</td>
    <td>TC_VWO_001, TC_VWO_002, TC_VWO_003</td>
    <td class=\"passed\">Passed</td>
  </tr>
  <tr>
    <td>REQ-02</td>
    <td>VWO Remember Me</td>
    <td>TC_VWO_004</td>
    <td class=\"failed\">Failed</td>
  </tr>
  <tr>
    <td>REQ-03</td>
    <td>API POST Booking Valid Payload</td>
    <td>TC_API_001</td>
    <td class=\"passed\">Passed</td>
  </tr>
  <tr>
    <td>REQ-04</td>
    <td>API POST Booking Invalid Payload</td>
    <td>TC_API_002</td>
    <td class=\"failed\">Failed</td>
  </tr>
</table>
</body>
</html>
'''

with open(os.path.join(outputs_dir, 'Test_Matrix.html'), 'w') as f:
    f.write(html_content)

print('Files generated successfully.')
