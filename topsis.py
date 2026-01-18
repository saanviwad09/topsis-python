import sys
import pandas as pd
import numpy as np
import os

def error(msg):
    print("Error:", msg)
    sys.exit(1)

def main():
    if len(sys.argv) != 5:
        error("Incorrect number of parameters.\nUsage:\npython topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>")

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.exists(input_file):
        error("Input file not found.")

    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        error("Input file must contain three or more columns.")

    matrix = data.iloc[:, 1:].values

    if not np.issubdtype(matrix.dtype, np.number):
        error("Columns from 2nd to last must contain numeric values only.")

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != matrix.shape[1]:
        error("Number of weights must match number of criteria.")

    if len(impacts) != matrix.shape[1]:
        error("Number of impacts must match number of criteria.")

    for i in impacts:
        if i not in ['+', '-']:
            error("Impacts must be either '+' or '-'.")

    norm = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    weighted = norm * weights

    ideal_best = []
    ideal_worst = []

    for j in range(matrix.shape[1]):
        if impacts[j] == '+':
            ideal_best.append(weighted[:, j].max())
            ideal_worst.append(weighted[:, j].min())
        else:
            ideal_best.append(weighted[:, j].min())
            ideal_worst.append(weighted[:, j].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    s_pos = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    s_neg = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = s_neg / (s_pos + s_neg)
    rank = score.argsort()[::-1].argsort() + 1

    data['Topsis Score'] = score
    data['Rank'] = rank

    data.to_csv(output_file, index=False)
    print("TOPSIS analysis completed successfully.")

if __name__ == "__main__":
    main()
