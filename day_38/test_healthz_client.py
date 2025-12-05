from healthz_client import get_exercise_stats, get_details
from sheety_client import add_activity, get_table, edit_activity, delete_activity

def main():

    # get_table("all")
    # get_table("3")git

    # get_details()
    # response = get_exercise_stats()
    # response = add_activity()
    response = add_activity()
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