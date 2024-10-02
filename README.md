# Student Performance Analysis

This Python script analyzes student performance data from a CSV file. It provides insights such as:

- Students who failed in any subject.
- Average scores for each subject per semester.
- The student with the highest overall average score.
- The subject with the lowest average score.
- Visualization of average scores per subject and per semester.
- Saving the average scores per semester to an Excel file.

## Features

1. **Failed Students Detection**: Lists all students who scored less than 50 in any subject.
2. **Average Scores Calculation**: Calculates the average score for each subject per semester.
3. **Highest Scoring Student**: Identifies the student with the highest average score.
4. **Lowest Average Subject**: Finds the subject with the lowest average score across all semesters.
5. **Excel Export**: Saves the average scores per semester to an Excel file.
6. **Data Visualization**:
   - Bar chart showing average scores across all subjects.
   - Line chart showing average scores per semester.

## Prerequisites

You need the following Python libraries to run this script:

- `pandas`
- `matplotlib`

You can install these dependencies via pip:

```bash
pip install pandas matplotlib
