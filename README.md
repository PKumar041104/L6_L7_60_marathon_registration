# PES University
## Department of Computer Science and Engineering

### Software Engineering Laboratory

# Lab 6 & Lab 7: Software Testing and Quality Assurance

**Project:** Marathon Registration  
**Course Code:** UE24CS341A – Software Engineering

---

## Student Details

| Field | Details |
|---|---|
| Student Name | Pratham Kumar |
| SRN | PES2UG24CS368 |
| PRN | PES2202400086 |
| University | PES University |
| Campus | Electronic City, Bengaluru |
| Department | Computer Science and Engineering |
| Semester | 5th Semester |
| Academic Year | 2026–27 |
| Programming Language | Python |

---

## Repository Overview

This repository contains the implementations, automated test suites, screenshots, and consolidated laboratory reports for two Software Engineering laboratory assignments conducted using the Marathon Registration application.

The assignments focus on two important aspects of software quality assurance:

1. **Lab 6 – Code and Branch Coverage Analysis:** Evaluating test-suite completeness through statement and branch coverage.
2. **Lab 7 – Fuzzing for Input Validation Bugs:** Identifying and fixing input-validation defects using property-based testing with Hypothesis.

Each laboratory assignment is maintained independently in its respective directory.

---

# Lab 6: Code and Branch Coverage Analysis

## 1. Objective

The objective of Lab 6 is to evaluate software test completeness using code coverage and branch coverage techniques.

The experiment involves extending the provided test suite, testing normal and boundary conditions, measuring coverage using automated tools, and maintaining the implementation and evidence in GitHub.

The target was to achieve **greater than 90% code and branch coverage**, as required by the laboratory evaluation criteria.

## 2. Project Overview

The Marathon Registration application implements three primary functions:

- **Entry Fee Calculation:** Calculates registration fees according to race distance, participant age, early-bird discounts, and T-shirt requirements.
- **Start-Wave Assignment:** Assigns runners to start waves based on their recorded best time and race category.
- **Finisher Status Determination:** Determines whether a runner finishes, does not finish (DNF), or is disqualified (DSQ), based on elapsed time and missed checkpoints.

The application is tested using `pytest`, while `coverage.py` measures statement and branch coverage.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.14.0 | Application development and execution |
| pytest 9.2.0 | Automated test execution |
| coverage.py 7.17.0 | Code and branch coverage measurement |
| Git | Version control |
| GitHub | Repository hosting and submission |

## 4. Test Coverage Results

| Metric | Achieved Result |
|---|---:|
| Code-coverage test cases passed | 35 |
| Line coverage | 100% |
| Branch-coverage test cases passed | 28 |
| Branch coverage | 100% |
| Missing statements | 0 |
| Missing branches | 0 |
| Partially covered branches | 0 |

Both test suites passed successfully. The measured line and branch coverage exceeded the minimum 90% target.

## 5. Deliverables

The `LAB6` directory contains:

- Original Marathon Registration application.
- Original starter test file.
- Additional code-coverage test suite.
- Additional branch-coverage test suite.
- Screenshots demonstrating coverage results.
- Consolidated Lab 6 report.

---

# Lab 7: Fuzzing for Input Validation Bugs

## 1. Objective

The objective of Lab 7 is to explore fuzz testing as a security and quality assurance technique by identifying and fixing input-validation bugs in the provided Python application using the Hypothesis property-based testing library.

The experiment focuses on automatically generating unexpected, malformed, and invalid inputs to identify runtime exceptions and improve application robustness through defensive programming.

## 2. Project Overview

The Marathon Registration Parser application consists of three primary functions:

- **`format_bib_name()`:** Converts a runner's name into uppercase and limits it to 12 characters for the race bib.
- **`parse_finish_time()`:** Converts a marathon finish time in `H:MM:SS` format into its equivalent value in seconds.
- **`average_split()`:** Calculates the average of space-separated split times provided in minutes.

Initially, the application assumed that all supplied inputs were valid and correctly formatted. Hypothesis-based fuzz testing was used to identify input-validation weaknesses in these functions.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.14.0 | Application development and execution |
| Hypothesis 6.170.15 | Property-based fuzz testing |
| pytest 9.2.0 | Automated test execution |
| Git | Version control |
| GitHub | Repository hosting and submission |

## 4. Implementation and Testing Workflow

The experiment followed the six procedural steps specified in the laboratory instructions.

### Step 1: Installing Dependencies

Installed the required Python libraries:

```powershell
python -m pip install hypothesis
python -m pip install pytest
```

Verified the installation and availability of both dependencies.

### Step 2: Running the Original Buggy Application

Executed the original application:

```powershell
python marathon_registration_parser.py
```

Verified the normal behaviour of all three application functions using valid sample inputs.

### Step 3: Completing the Hypothesis Test File

Completed the faculty-provided test template, `test_marathon_registration_parser.py`.

Implemented three property-based no-crash tests using:

```python
@given(st.text() | st.none())
```

The tests automatically generate arbitrary text inputs and `None` values to examine whether the corresponding application functions raise runtime exceptions.

### Step 4: Executing Tests on the Original Application

Executed the test suite against the original implementation:

```powershell
python -m pytest test_marathon_registration_parser.py
```

All three test functions failed, exposing input-validation defects, including:

- `AttributeError` caused by operations on `None`.
- `ValueError` caused by malformed inputs and invalid numeric conversions.
- `ZeroDivisionError` caused by attempting to calculate an average from empty input.

**Initial result:** 3 failed.

### Step 5: Fixing the Buggy Application

Modified `marathon_registration_parser.py` using defensive programming techniques.

The corrections included:

- Input type validation.
- Empty-input validation.
- Input-format verification.
- ASCII digit validation.
- Exception handling for numeric conversions.
- Validation of minute and second ranges.
- Graceful handling of invalid results in the main function.

Invalid inputs are handled safely by returning `None`, while the application displays meaningful error messages.

The corrected application was executed again using valid sample inputs to verify its normal behaviour.

### Step 6: Re-executing Hypothesis Tests

Re-executed the same test suite against the corrected implementation:

```powershell
python -m pytest test_marathon_registration_parser.py
```

All three test functions passed successfully.

**Final result:** 3 passed.

This demonstrates that the identified runtime exceptions were addressed for the inputs generated by the Hypothesis test suite.

## 5. Final Test Results

| Test Function | Original Application | Corrected Application |
|---|---|---|
| `test_format_bib_name_no_crash()` | Failed | Passed |
| `test_parse_finish_time_no_crash()` | Failed | Passed |
| `test_average_split_no_crash()` | Failed | Passed |
| **Total** | **3 Failed** | **3 Passed** |

The same Hypothesis test suite was used before and after modifying the application, allowing the effectiveness of the corrections to be evaluated consistently.

## 6. Deliverables

The `LAB7` directory contains:

- Corrected Marathon Registration Parser application.
- Completed Hypothesis-based test file.
- Screenshots of dependency installation and verification.
- Screenshot of the original application execution.
- Screenshot of the completed Hypothesis test implementation.
- Screenshot of failing tests on the original application.
- Screenshot of the corrected application execution.
- Screenshot of passing tests on the corrected application.
- Consolidated Lab 7 report.

---

# Repository Structure

```text
L6_L7_60_marathon_registration/
│
├── README.md
│
├── LAB6/
│   ├── README.md
│   ├── marathon_registration.py
│   ├── test_marathon_registration.py
│   ├── CodeCoverageTest_PES2UG24CS368_marathon_registration.py
│   ├── BranchCoverageTest_PES2UG24CS368_marathon_registration.py
│   ├── screenshots/
│   │   ├── Figure_3_Code_Coverage_100_Percent.png
│   │   └── Figure_4_Branch_Coverage_100_Percent.png
│   └── [Consolidated Lab 6 Report]
│
└── LAB7/
    ├── marathon_registration_parser.py
    ├── test_marathon_registration_parser.py
    ├── screenshots/
    │   ├── SS1_Original_Application.png
    │   ├── SS2_Dependency_Installation.png
    │   ├── SS2_Hypothesis_Failing_Tests.png
    │   ├── SS3_Fixed_Application.png
    │   ├── SS3_Hypothesis_Test_Code.png
    │   └── SS4_Hypothesis_Passing_Tests.png
    └── PES2UG24CS368-LAB7.pdf
```

---

# Version Control and Submission

The work for both laboratory assignments was maintained in the GitHub repository using version control.

- Lab 6 contains the code-coverage and branch-coverage implementations and their supporting evidence.
- Lab 7 contains the corrected application, completed Hypothesis test suite, screenshots, and consolidated report.
- Both assignments are maintained separately to preserve their individual implementations and deliverables.

**GitHub Repository:**

[PKumar041104/L6_L7_60_marathon_registration](https://github.com/PKumar041104/L6_L7_60_marathon_registration)

---

# Overall Conclusion

The two laboratory assignments demonstrate different but complementary approaches to software testing and quality assurance.

**Lab 6** demonstrates the use of automated testing and coverage analysis to evaluate test-suite completeness. The final test suites achieved 100% line coverage and 100% branch coverage, exceeding the required coverage target.

**Lab 7** demonstrates the use of property-based fuzz testing to identify unexpected input-validation defects. The original application initially failed all three Hypothesis test functions. Following the implementation of input validation and defensive programming techniques, all three tests passed successfully.

Together, these experiments demonstrate the importance of comprehensive test coverage, automated testing, edge-case identification, and defensive programming in developing reliable software applications.

---

*Software Engineering Laboratory — PES University, Electronic City Campus*  
*Academic Year 2026–27*
