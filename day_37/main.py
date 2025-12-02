from pixela_client import create_user, create_graph, add_pixel

def main():
    # response = create_user() | already created https://pixe.la/@zamirhashorva

    # response = create_graph() | already created https://pixe.la/v1/users/zamirhashorva/graphs/graph001

    response = add_pixel()

    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}")

if __name__ == '__main__':
    main()
