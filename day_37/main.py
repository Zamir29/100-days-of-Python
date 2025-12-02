from pixela_client import create_user


def main():
    response = create_user()

    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}")

if __name__ == '__main__':
    main()
