import json
import database_functions as df
import retrieve_web_data as rd

# Personal information
database = "words.db"
with open("hidden_info.json") as f:
    API_KEY = json.load(f)['API_KEY']

# create a database connection
conn = df.create_connection(database)
with conn:
    print("Welcome to Lexe")
    loop_run = True
    while loop_run:
        print("\nN: New Word | S: Search List | D: Delete Word | P: Print to File | Q: Quit")
        operation = input(":").lower()

        if operation == 'n':
            new_word = input("Enter new word or press Q to exit: ").lower()
            if new_word == 'q':
                continue
            df.add_word(conn, new_word)
        
        if operation == 's':
            search_word = input("Enter word: ").lower()
            result = df.find_word(conn, search_word)
            if result:
                print(f"Word: {result[0]}")
            else:
                print("Word not in database...")

        if operation == 'd':
            to_delete = input("Enter the word you wish to remove or press Q to exit: ").lower()
            if to_delete == 'q':
                continue
            df.delete_word(conn, to_delete)

        if operation == 'p':
            print("Here's the data:")
            print(df.return_list(conn))

        if operation == 't':
            test_word = input("Enter word: ")
            print(rd.extra_word_data(test_word, API_KEY))

        if operation == 'q':
            loop_run = False

    