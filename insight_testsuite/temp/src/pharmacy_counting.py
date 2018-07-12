#!/bin/bash

from argparse import ArgumentParser


def main(args):
    input_fname = args.input
    output_fname = args.output

    drug_cost = {}
    drug_pres = {}
    drug_names = []


    #read file
    with open(input_fname) as f:
        data = f.readlines()

    #sort data
    for l in data:
        line = l.strip('\n').split(',')
        i, lname, fname, dname, cost = line
        if i != 'id':
            if dname not in drug_names:
                drug_cost[dname] = float(cost)
                drug_pres[dname] = 1
                drug_names.append(dname)
            else:
                drug_cost[dname] += float(cost)
                drug_pres[dname] += 1
    #sort drugs by the total cost
    sorted_by_value = sorted(drug_cost.items(), key=lambda kv: kv[1], reverse=True)
    #make output list
    output = [['drug_name','num_prescriber','total_cost']]
    for d, cost in sorted_by_value:
        output.append([d, str(drug_pres[d]), str(int(cost))])
    #save file
    output_text = [','.join(l) for l in output]
    with open(output_fname, 'w') as outfile:
        outfile.write('\n'.join(output_text))

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('input', help='input file, ./input/itcont.txt')
    parser.add_argument('output', help='output file ./output/top_cost_drug.txt')

    args = parser.parse_args()
    main(args)