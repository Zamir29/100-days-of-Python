from pixela_client import create_user, create_graph, add_pixel, update_pixel, delete_pixel

ACTIONS = {
    "create": create_user,
    "graph": create_graph,
    "add": add_pixel,
    "update": update_pixel,
    "delete": delete_pixel,
}

def main():
    while True:
        pick_action = input("What do you want to do today?\n\n"
                            "➕ Create an new user? [Create]\n"
                            "📊 Create a new graph? [Graph]\n"
                            "✅ Add a new pixel? [Add]\n"
                            "📝 Update a pixel? [Update]\n"
                            "❌ Delete a pixel? [Delete]\n"
                            "🚪 Exit [Exit]\n"
                            "\nChoose an action: ").lower().strip()

        if pick_action in ("exit", "quit"):
            print("\nOK, then, see you next time 👋")
            break
        if pick_action not in ACTIONS:
            print("😐 Dude, please spell one of the available words and don't include the brackets.\n")

        action_func = ACTIONS[pick_action]

        # --------- RETRY LOOP FOR THIS ACTION ---------
        while True:
            response = action_func()

            if response.status_code == 503:
                print("\nGuess you are on the cheap version. Do you want to retry?\n")
                retry = input("[Y] Retry | [N] Back to menu: ").lower().strip()
                if retry in ("y", "yes"):
                    # just loop again and call action_func()
                    continue
                else:
                    # break out of inner loop, go back to main menu
                    break

            if response.status_code == 200:
                print(f"\n\n{response.json()['message']} We did it 🥳")
            else:
                print(f"\n\n Shoot! 🤔 The error {response.status_code} message says {response.json()['message']}\n")

            break # done with this action, exit inner loop

        # --------- RETRY LOOP FOR THIS ACTION ---------
        do_again = input("Do you want to do some more actions?\n[Y][N]: ").lower().strip()
        if do_again not in ("y", "yes"):
            print("\nOK, then, see you next time 👋")
            break

    # print(f"Status: {response.status_code}")
    # print(f"Body: {response.text}")
    # print(f"Body: {response.json()['message']}")

if __name__ == '__main__':
    main()
