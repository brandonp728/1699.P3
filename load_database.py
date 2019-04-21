import csv, sqlite3, numpy as np

db = sqlite3.connect('pokemon.db')
cursor = db.cursor()

def load_csv():
    with open('pokeanon.csv', 'r', encoding='utf8') as file:
        print_status("Reading file")
        readFile = csv.reader(file, delimiter=',')
        print_status("Reading Complete!")
        with db:
            print_status("Creating Database!")
            create_table = """CREATE TABLE pokemon (
                abilities text, 
                against_bug real,
                against_dark real, 
                against_dragon real,
                against_electric real,
                against_fairy real,
                against_fighting real,
                against_fire real,
                against_flying real,
                against_ghost real,
                against_grass real,
                against_ground real,
                against_ice real,
                against_normal real,
                against_poison real,
                against_pyschic real,
                against_rock real,
                against_steel real,
                against_water real,
                attack text,
                base_egg_steps integer,
                base_happiness integer,
                base_total text,
                capture_rate integer,
                defense text,
                experience integer, 
                height_m real,
                hp text,
                percentage_male real,
                sp_attack text,
                sp_defense text,
                speed text, 
                type1 text,
                type2 text,
                weight_kg real,
                generation integer, 
                is_legendary integer
                )"""
            cursor.execute(create_table)
            print_status("Created!")
            print_status("Adding entries!")
            for row in readFile:
                if(row and row[0] != 'abilities'):
                    row_data = []
                    # Need to clear empty cells out of row to be 0
                    fix_row_list(row)
                    row_data.append(row[0])
                    row_data.append(float(row[1]))
                    row_data.append(float(row[2]))
                    row_data.append(float(row[3]))
                    row_data.append(float(row[4]))
                    row_data.append(float(row[5]))
                    row_data.append(float(row[6]))
                    row_data.append(float(row[7]))
                    row_data.append(float(row[8]))
                    row_data.append(float(row[9]))
                    row_data.append(float(row[10]))
                    row_data.append(float(row[11]))
                    row_data.append(float(row[12]))
                    row_data.append(float(row[13]))
                    row_data.append(float(row[14]))
                    row_data.append(float(row[15]))
                    row_data.append(float(row[16]))
                    row_data.append(float(row[17]))
                    row_data.append(float(row[18]))
                    row_data.append(row[19])
                    row_data.append(int(row[20]))
                    row_data.append(int(row[21]))
                    row_data.append(row[22])
                    row_data.append(int(row[23]))
                    row_data.append(row[24])
                    row_data.append(int(row[25]))
                    row_data.append(float(row[26]))
                    row_data.append(row[27])
                    row_data.append(float(row[28]))
                    row_data.append(row[29])
                    row_data.append(row[30])
                    row_data.append(row[31])
                    row_data.append(row[32])
                    row_data.append(row[33])
                    row_data.append(float(row[34]))
                    row_data.append(int(row[35]))
                    row_data.append(int(row[36]))
                    cursor.execute("INSERT INTO pokemon VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row_data)
            print_status("Done with the database!!")    

def print_status(msg):
    print("\n" + ("*"*10) + msg + ("*"*10) + "\n")

def fix_row_list(row):
    for i in range(0,len(row)):
        if row[i] == '' and i != 33:
            row[i] = 0


def taskC4():
    query = """SELECT count(*) from Pokemon
               WHERE type1 = 'fire' 
               and type2 = 'fighting'
               and base_total > 300"""
    print("For task C4 we will be getting all fire/fighting type pokemon\nwhere their base stat total is greater than 300")
    cursor.execute(query)
    count = cursor.fetchone()[0]
    print("Count: " + str(count))

def taskC6():
    query = """SELECT count(*) from Pokemon
               WHERE type1 = 'water' 
               and is_legendary = 1"""
    print("For task C4 we will be getting the count of all legendary water type pokemon")
    cursor.execute(query) 
    result = cursor.fetchone()[0]
    scale = 1.0
    noise = np.random.laplace(scale)
    print("Query result: " + str(result) + " Laplacian noise: " + str(noise))
    print("Noise + Query: " + str(noise+result))

def main():
    try:
        cursor.execute("DROP TABLE pokemon")
    except:
        print()
    print('Getting ready to load the database!')
    print_status("Hang in there!")
    load_csv()
    task = input("Which task are you trying to perform?\n1) Task C4\n2) Task C6\n")
    if task == '1':
        taskC4()
    elif task == '2':
        taskC6()
    print("Goodbye!")
    db.close()

if __name__ == "__main__":
    main()


