from sheety_client import add_activity, edit_activity, delete_activity, get_table

logo = """
  _    _            _ _   _       _______             _    
 | |  | |          | | | | |     |__   __|           | |   
 | |__| | ___  __ _| | |_| |__      | |_ __ __ _  ___| | __
 |  __  |/ _ \/ _` | | __| '_ \     | | '__/ _` |/ __| |/ /
 | |  | |  __/ (_| | | |_| | | |    | | | | (_| | (__|   < 
 |_|  |_|\___|\__,_|_|\__|_| |_|    |_|_|  \__,_|\___|_|\_\
                                                           
"""
def main():
    print(logo)
    print("Welcome! Do you want to add an activity?\n")
    while True:
        user_input = input(
              "Press [ENTER] to add a new one!\n"
              "Type the commands below to:\n"
              "  └── [Edit]: to edit an existing activity\n"
              "  └── [Delete]: to delete an existing activity\n"
              "  └── [Table]: to see the activities tracked\n"
              "  └── [Exit]: leave the tracker\n").lower().strip()
        if user_input == "":
            add_activity()
        elif user_input == "edit":
            edit_activity()
        elif user_input == "delete":
            delete_activity()
        elif user_input == "table":
            all_table, _, _ = get_table("all")
            print(all_table)
        elif user_input in ["exit", "q"]:
            break
        else:
            print("Invalid input. Please hit [Enter] or type [Edit], [Delete], [Table] without brackets.")

        while True:
            user_input = input("\nDo you want to do something else?\n Type [Y]/[N]: ").lower().strip()

            if user_input in ["y", "yes"]:
                break
            elif user_input in ["n", "no"]:
                return
            else:
                print("Please type [Y] or [N] without brackets")

    print("See you next time 👋")
if __name__ == '__main__':
    main()
