import database_functions as df

database = "words.db"

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
            df.add_word(conn, new_word, 'defintion')
        
        if operation == 's':
            search_pref = input("Search for word or definition? (w/d): ").lower()
            if search_pref == 'w':
                search_word = input("Enter word: ").lower()
                result = df.find_word(conn, search_word)
                print(f"Word: {result[0]}\nDefintion: {result[1]}")
            if search_pref == 'd':
                print("Feature still to be added :(")
            if search_pref not in ['w', 'd']:
                print("Incorrect input, there should be a loop, but should check design first")
            

        if operation == 'd':
            to_delete = input("Enter the word you wish to remove or press Q to exit: ").lower()
            if to_delete == 'q':
                continue
            df.delete_word(conn, to_delete)

        if operation == 'p':
            print("Here's the data:")
            print(df.return_list(conn))

        if operation == 'q':
            loop_run = False

    