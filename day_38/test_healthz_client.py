from healthz_client import get_exercise_stats

def main():

    get_query = input("Tell me which exercise you did: ")

    response = get_exercise_stats(get_query)

    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    main()