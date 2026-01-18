# TOPSIS Implementation in Python

This project implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method using Python.  
The program is designed as a **command-line tool** to rank alternatives based on multiple criteria.

---

## About TOPSIS
TOPSIS is a multi-criteria decision-making (MCDM) technique that identifies solutions closest to the ideal best and farthest from the ideal worst solution.

---

## Features
- Command-line based execution
- Supports any number of criteria
- Validates inputs (weights, impacts, file format)
- Handles both benefit (+) and cost (−) criteria
- Generates TOPSIS score and rank
- Outputs results in CSV format

---

## Input File Format
- First column: Alternative name (e.g., Fund Name)
- Remaining columns: Numeric criteria values only
- Minimum 3 columns required

### Example:
| Fund Name | P1   | P2   | P3  | P4   | P5    |
| M1        | 0.84 | 0.71 | 6.7 | 42.1 | 12.59 |

---

##  Usage
bash
python topsis.py <InputFile.csv> <Weights> <Impacts> <OutputFile.csv>

## Example
python topsis.py data.csv "1,1,1,2,1" "+,+,-,+,+" topsis_results.csv

## Output
The output CSV file contains two additional columns:
Topsis Score, Rank
Higher TOPSIS score indicates a better alternative.

## Error Handling
The program checks for:
Incorrect number of argument
File not found errors
Non-numeric values in criteria
Mismatch in number of weights, impacts, and criteria
Invalid impact symbols (only + or - allowed)

## Technologies Used
Python
Pandas
NumPy

## Author
Saanvi Wadhwa
