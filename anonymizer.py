import csv, random, os
class Group:
    def __init__(self, val):
        self.vals = [val]
        self.n = 1

    def add_val(self, vals):
        for val in vals:
            self.vals.append(val)
    
    def __str__(self):
        to_return = "[" + str(self.vals[0])
        for i in range(1, len(self.vals)):
            to_return += ", " + str(self.vals[i])
        to_return += "]"
        return to_return


class Column:
    def __init__(self):
        self.group_list = []

    def add_group(self, to_add):
        if not self.in_group(to_add):
            new_group = Group(to_add)
            self.group_list.append(new_group)

    def in_group(self, to_add):
        for group in self.group_list:
            for val in group.vals:
                if val == to_add:
                    group.n += 1
                    return True
        return False

    def allAtLeastN(self, n):
        for g in self.group_list:
            if g.n < n:
                return False
        return True

    def anonymize(self, k):
        while not self.allAtLeastN(k):
            self.merge(k)

    def merge(self, k):
        i = 0
        while i < len(self.group_list)-1:
            merge_group = self.group_list.pop(i+1)
            group_to_be_merged = self.group_list[i]
            group_to_be_merged.add_val(merge_group.vals)
            group_to_be_merged.n += merge_group.n
            i += 1
        last_group = self.group_list[self.group_list.__len__()-1]
        if(last_group.n < k):
            last_group = self.group_list.pop(self.group_list.__len__()-1)
            self.group_list[self.group_list.__len__()-1].add_val(last_group.vals)
            self.group_list[self.group_list.__len__()-1].n + last_group.n
    
    def get_group(self, value):
        for group in self.group_list:
            if value in group.vals:
                return group
        return None

def load_csv():
    with open('pokemon.csv', mode='r', encoding='utf8') as file:
        read_file = csv.reader(file, delimiter=',')
        table = []
        for row in read_file:
            if row[0] == 'abilities':
                headers = row
            else:
                table.append(row)
        return table, headers

def write_csv(table, headers):
    with open('pokeanon.csv', mode='w', encoding='utf8') as file:
        write_file = csv.writer(file, delimiter=',')
        write_file.writerow(headers)
        write_file.writerows(table)

def anonymity(table, k, column_dict):
    for row in table:
        column_dict['attack'].add_group(int(row[19]))
        column_dict['defense'].add_group(int(row[24]))
        column_dict['sp_attack'].add_group(int(row[29]))
        column_dict['sp_defense'].add_group(int(row[30]))
        column_dict['hp'].add_group(int(row[27]))
        column_dict['speed'].add_group(int(row[31]))
    for column in column_dict.items():
        column[1].anonymize(k)
    for row in table:
        group = column_dict['attack'].get_group(int(row[19]))
        row[19] = group.__str__()
        group = column_dict['defense'].get_group(int(row[24]))
        row[24] = group.__str__()
        group = column_dict['hp'].get_group(int(row[27]))
        row[27] = group.__str__()
        group = column_dict['sp_attack'].get_group(int(row[29]))
        row[29] = group.__str__()
        group = column_dict['sp_defense'].get_group(int(row[30]))
        row[30] = group.__str__()
        group = column_dict['speed'].get_group(int(row[31]))
        row[31] = group.__str__()

def main():
    print("Welcome to the anonymizer! We will begin to anonymize the pokemon file now!")
    print("First we must load the CSV file")
    table, headers = load_csv()
    print("We will be implementing k-Anonymity on this file ")
    k = input("Enter your preferred value of k please: ") 
    print("The following have been identified as quasi-identifiers")
    print("Attack, Defense, Special Attack, Special Defense, Speed")
    print("Here we go!")
    column_dict = {}
    column_dict['hp'] = Column()
    column_dict['attack'] = Column()
    column_dict['defense'] = Column()
    column_dict['sp_attack'] = Column()
    column_dict['sp_defense'] = Column()
    column_dict['speed'] = Column()
    anonymity(table, int(k), column_dict)
    print("Done!")
    print("Time to write to the file! This will be outputted as pokeanon.csv")
    write_csv(table, headers)
    print("All done! Goodbye!")
    exit(0)

if __name__ == "__main__":
    main()