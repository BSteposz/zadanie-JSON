import json, requests
from geopy import distance



def get_json_data(url):
    response = requests.get(url)
    return response.json()

def merge_json_data(data1, data2):
    list = []
    list.append(data1)
    list.append(data2)
    return list


def post_count(list):

    for i in range(len(list[0])):
        count = 0
        posts_titles = []

        for j in range(len(list[1])):
            if list[0][i]['id'] == list[1][j]['userId']:
                count += 1
                posts_titles.append(list[1][j]['title'])

        print(f"{list[0][i]['username']} napisał(a) {count} postów")

        repetable = set([repetable for repetable in posts_titles if posts_titles.count(repetable) > 1])

        if len(repetable) == 0:
            print(f'Tytuły postów {list[0][i]["username"]} nie powtarzają się \n')
        else:
            print(f'Tytuły powtórzonych postów to \n{repetable}')

def nearby(list):

    for i in range(len(list[0])):
        Min = 0
        User = ""
        for j in range(len(list[0])):

            if list[0][i]['address']['geo'] != list[0][j]['address']['geo']:
                location_1 = (list[0][i]['address']['geo']['lat'], list[0][i]['address']['geo']['lng'])
                location_2 = (list[0][j]['address']['geo']['lat'], list[0][j]['address']['geo']['lng'])
                dist = distance.distance(location_1, location_2)
                if Min == 0 or Min > dist:
                    Min = dist
                    User = list[0][j]['name']
        print(f"Najbliżej użytkownika {list[0][i]['name']} znajduje się użytkownik {User} w odległości {Min}")









def main():
    data_post=get_json_data('https://jsonplaceholder.typicode.com/posts')
    data_users = get_json_data('https://jsonplaceholder.typicode.com/users')

    connect = merge_json_data(data_users, data_post)

    post_count(connect)
    nearby(connect)

if __name__ == '__main__':
    main()
