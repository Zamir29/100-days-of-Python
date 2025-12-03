from pixela_client import create_user, create_graph, add_pixel, update_pixel, delete_pixel

def main():
    pick_action = input("What do you want to do today?\n"
                        "➕ Create an new user? [Create]\n"
                        "📊 Create a new graph? [Graph]\n"
                        "✅ Add a new pixel? [Add]\n"
                        "📝 Update a pixel? [Update]\n"
                        "❌ Delete a pixel? [Delete]\n"
                        "Choose an action: ").lower()
    response = ""

    if pick_action == "create":
        response = create_user() #| already created https://pixe.la/@zamirhashorva
    elif pick_action == "graph":
        response = create_graph() #| already created https://pixe.la/v1/users/zamirhashorva/graphs/graph001
    elif pick_action == "add":
        response = add_pixel()
    elif pick_action == "update":
        response = update_pixel()
    elif pick_action == "delete":
        response = delete_pixel()
    else:
        print("😐Dude, please spell the word correctly towards the available ones and don't include the brackets ")
        main()

    if response.status_code == 200:
        print(f"\n\n{response.json()['message']} We did it 🥳\n\n")
        while True:
            do_again = input("Do you want to do some more actions?\n[Y][N]: ")
            if do_again.lower() == "y" or do_again.lower() == "yes":
                main()
            elif do_again.lower() == "n" or do_again.lower() == "no":
                print("\nOK, then, see you next time 👋")
            else:
                return False
    elif response.status_code == 503:
        print("\n\nGuess we are on cheap version. Let's retry\n\n")
        main()
    else:
        print(f"\n\nShoot! 🤔 The error {response.status_code} message says {response.json()['message']}")


    # print(f"Status: {response.status_code}")
    # print(f"Body: {response.text}")
    # print(f"Body: {response.json()['message']}")

if __name__ == '__main__':
    main()
