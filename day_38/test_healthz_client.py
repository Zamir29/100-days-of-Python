from healthz_client import get_exercise_stats, add_activity, get_table, edit_activity

def main():

    # get_table("all")
    # get_table("3")

    # get_details()
    # response = get_exercise_stats()
    # response = add_activity()
    response = edit_activity()
    print(response.status_code)
    print(response.json())


    # get_query = input("Tell me which exercise you did: ")
    #
    # stats_response = get_exercise_stats(get_query)
    #
    #
    # print(stats_response.status_code)
    # print(stats_response.json())
    #
    # get_data = stats_response.json()
    #
    # activity_response = add_activity(get_data)
    #
    # print(activity_response.status_code)

if __name__ == "__main__":
    main()