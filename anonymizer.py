import csv, random, os

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
        # for row in table:
        #     write_file.writerow(row)

def anonymize(table):
    one_ability_list = []
    two_ability_list = []
    three_ability_list = []
    four_ability_list = []
    five_ability_list = []
    six_ability_list = []
    for row in table:
        abilities = row[0]
        num_commas = abilities.count(',')
        if num_commas == 0:
            one_ability_list.append(abilities)
        elif num_commas == 1:
            two_ability_list.append(abilities)
        elif num_commas == 2:
            three_ability_list.append(abilities)
        elif num_commas == 3:
            four_ability_list.append(abilities)
        elif num_commas == 4:
            five_ability_list.append(abilities)
        elif num_commas == 5:
            six_ability_list.append(abilities)
    for row in table:
        # Attack stat
        row[19] = anonymize_stat(row[19])
        # Stat total
        row[22] = anonymize_stat(row[22])
        #Defense stat
        row[24] = anonymize_stat(row[24])
        # HP stat
        row[27] = anonymize_stat(row[27])
        # Special Attack Stat
        row[29] = anonymize_stat(row[29])
        # Special Defense Stat
        row[30] = anonymize_stat(row[30])
        # Speed stat
        row[31] = anonymize_stat(row[31])
        # Pokemon Type
        full_type = row[32] + "/" + row[33]
        new_types = anonymize_type(full_type)
        type_array = new_types.split(":")
        row[32] = type_array[0]
        row[33] = type_array[1]
        # Pokemon Ability
        row[0] = anonymize_abilities(row[0], one_ability_list, two_ability_list, three_ability_list, four_ability_list, five_ability_list, six_ability_list)


def anonymize_abilities(abilities, one_ability_list, two_ability_list, three_ability_list, four_ability_list, five_ability_list, six_ability_list):
    num_commas = abilities.count(",")
    rand_ability = ""
    if num_commas == 0:
        rand_ability = ability_helper(abilities, one_ability_list)
    elif num_commas == 1:
        rand_ability = ability_helper(abilities, two_ability_list)
    elif num_commas == 2:
        rand_ability = ability_helper(abilities, three_ability_list)
    elif num_commas == 3:
        rand_ability = ability_helper(abilities, four_ability_list)
    elif num_commas == 4:
        rand_ability = ability_helper(abilities, five_ability_list)
    elif num_commas == 5:
        rand_ability = ability_helper(abilities, six_ability_list)
    return rand_ability

def ability_helper(abilities, ability_list):
    rand_int = random.randint(0, (ability_list.__len__()-1))
    rand_ability = ability_list[rand_int]
    while rand_ability == abilities:
        rand_int = random.randint(0, (ability_list.__len__()-1))
        rand_ability = ability_list[rand_int]
    anon_ability = ""
    return_format = random.randint(0, 1)
    if return_format == 0:
        anon_ability = "[" + abilities + ", " + rand_ability + "]"
    else:
        anon_ability = "[" + rand_ability + ", " + abilities + "]"
    return anon_ability

def anonymize_type(full_type):
    types = ("","bug", "dark", "dragon", 
    "normal" ,"ice", "fighting", 
    "fire", "ghost", "ground", 
    "grass", "psychic", "poison", 
    "steel", "rock", "bug",
    "electric", "fairy", "water")
    type_array = full_type.split("/")
    rand_type_int1 = random.randint(1, 18)
    rand_type_int2 = random.randint(0, 18)
    while rand_type_int2 == rand_type_int1:
        rand_type_int2 = random.randint(0, 18)
    rand_type1 = types[rand_type_int1]
    rand_type2 = types[rand_type_int2]
    if not rand_type2:
        rand_type2 = "none"
    if not type_array[1]:
        type_array[1] = "none"
    return_format = random.randint(0, 1)
    anon_type1 = ""
    if return_format == 0:
        anon_type1 = "[" + type_array[0] + ", " + rand_type1 + "]"
    else:
        anon_type1 = "[" + rand_type1 + ", " + type_array[0] + "]"
    return_format = random.randint(0, 1)
    anon_type2 = ""
    if return_format == 0:
        anon_type2 = "[" + type_array[1] + ", " + rand_type2 + "]"
    else:
        anon_type2 = "[" + rand_type2 + ", " + type_array[1] + "]" 
    new_types = anon_type1 + ":" + anon_type2
    return new_types



def anonymize_stat(stat):
    stat_num = int(stat)
    anon_val = random.randint(stat_num, int(stat_num*1.5))
    return_format = random.randint(0, 1)
    new_val = ""
    if return_format == 0:
        new_val = "[" + stat + ", " + str(anon_val) + "]"
    else:
        new_val = "[" + str(anon_val) + ", " + stat + "]"
    return new_val


def main():
    print("Welcome to the anonymizer! We will begin to anonymize the pokemon file now!")
    table, headers = load_csv()
    print("We will be implementing 8-Anonymity on this file ")
    print("The following have been identified as quasi-identifiers")
    print("Attack, Defense, Special Attack, Special Defense, Speed, Type, Base total, Ability")
    print("Here we go!")
    anonymize(table)
    print("Done!")
    print("Time to write to the file! This will be outputted as pokeanon.csv")
    write_csv(table, headers)
    print("All done! Goodbye!")
    exit(0)

if __name__ == "__main__":
    main()