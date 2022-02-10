import sys

out_input = sys.argv[1]

with open(out_input, 'r') as f:
    next(f)
    next(f)
    next(f)
    for line in f:
        line = line.rstrip('\n').split('\t')
        if line[8] == 'C':
            line[8] = '-'
        output = line[4] + '\t' + 'RepeatMasker' + '\t' + 'similarity' + '\t' + line[5] + '\t' + line[6] + '\t' + line[1] + '\t' + line[8] + '\t' + '.' + '\t' + 'ID=' + line[10] + ':' + line[9]
        print(output)