import pandas as pd

def main():
    input = pd.read_excel('input.xlsx', index_col=None)
    output = pd.read_excel('output.xlsx', index_col=None)
    print(f'input has {len(input.index)} rows before starting')
    print(f'output has {len(output.index)} rows before starting')
    merge_on = ['Name', 'Ref Number', 'Owner']
    joined = pd.merge(left=input, right=output, left_on=merge_on, right_on=merge_on, copy=False, how="right")
    print(f'joined has {len(joined.index)} rows after merging (which should be equal to input rows: {len(input.index)})')

if __name__ == "__main__":
    main()