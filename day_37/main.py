from pixela_client import create_user, create_graph, add_pixel, update_pixel, delete_pixel

def main():
    pick_action = input("What do you want to do today?\n"
                        "➕ Create an new user? [Create]\n"
                        "📊 Create a new graph? [Graph]\n"
                        "✅ Add a new pixel? [Add]\n"
                        "📝 Update a pixel? [Update]\n"
                        "❌ Delete a pixel? [Delete]\n"
                        "Choose an action: ").lower()
    # response = create_user() | already created https://pixe.la/@zamirhashorva

    # response = create_graph() | already created https://pixe.la/v1/users/zamirhashorva/graphs/graph001
    response = ""
    if pick_action == "add":
        response = add_pixel()
    elif pick_action == "update":
        response = update_pixel()
    elif pick_action == "delete":
        response = delete_pixel()

    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}")

if __name__ == '__main__':
    main()
