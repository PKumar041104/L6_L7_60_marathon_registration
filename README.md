# PES University
## Department of Computer Science and Engineering

### Software Engineering Laboratory

# Lab 6: Code and Branch Coverage Analysis

**Project:** Marathon Registration

---

## Student Details

| Field | Details |
|---|---|
| Student Name | Pratham Kumar |
| SRN | PES2UG24CS368 |
| University | PES University |
| Campus | Electronic City, Bengaluru |
| Course | Software Engineering |
| Lab Assignment | Lab 6 — Code and Branch Coverage |
| Programming Language | Python |

---

## 1. Objective

The objective of this laboratory assignment is to evaluate software test completeness using code coverage and branch coverage techniques. The experiment involves extending the provided test suite, testing normal and boundary conditions, measuring coverage using automated tools, and maintaining the implementation and evidence in GitHub.

The target is to achieve **greater than 90% code and branch coverage**, as required by the laboratory evaluation criteria.

## 2. Project Overview

The Marathon Registration application is a Python module that implements three primary functions:

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

## 4. Repository Structure

```text
L6_L7_60_marathon_registration/
├── .gitignore
├── README.md
└── LAB6/
    ├── README.md
    ├── marathon_registration.py
    ├── test_marathon_registration.py
    ├── CodeCoverageTest_PES2UG24CS368_marathon_registration.py
    ├── BranchCoverageTest_PES2UG24CS368_marathon_registration.py
    └── screenshots/
        ├── Figure_3_Code_Coverage_100_Percent.png
        └── Figure_4_Branch_Coverage_100_Percent.png
```

The consolidated laboratory report is also available in the `LAB6` directory.

## 5. Test Coverage Results

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

## 6. Version Control and Submission

The work was maintained in a fork of the faculty-provided repository. Separate commits were created for the code-coverage and branch-coverage test suites, including their respective evidence screenshots.

**GitHub Repository:**  
[PKumar041104/L6_L7_60_marathon_registration](https://github.com/PKumar041104/L6_L7_60_marathon_registration)

The `LAB6` directory contains the application, original starter tests, additional coverage test suites, screenshot evidence, and consolidated laboratory report.

## 7. Conclusion

This experiment demonstrates the use of automated testing and coverage analysis to evaluate the completeness of a software test suite. Additional test cases were developed to exercise the application's validation rules, fee calculations, start-wave decisions, and finishing-status conditions.

The final test suites achieved 100% line coverage and 100% branch coverage according to the recorded coverage reports. The source code, test files, and evidence were maintained in GitHub using separate commits to support version control and evaluation.

---

*Software Engineering Laboratory — PES University, Electronic City Campus*
