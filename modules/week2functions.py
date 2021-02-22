import csv 

def print_file_content(file):
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        for element in lst:
            writer.writerow(element + "\n")
            print(element)


def write_strings_to_file(file, *strings):
    with open(file, 'w') as f:
        for string in strings:
            f.write(string + "\n")
            print(string)
            
            
def read_csv(input_file):
    with open(input_file) as f:
        new_list = []
        reader = csv.reader(f)
        for row in reader:
            new_list.append(row)
        return new_list