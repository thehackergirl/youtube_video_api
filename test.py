import requests

BASE = "http://127.0.0.1:5000/"     #location on api
# print("starteeeeeeeeeeed")
# data = [{"likes": 78, "name": "Java tutorial", "views": 120},
#         {"likes": 1000, "name": "How to make rest api", "views": 80000},
#         {"likes": 1220, "name": "Van Conversion", "views": 4200},
#         {"likes": 132420, "name": "Python tutorial", "views": 4320}]
#
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i) , data[i])
#     print(response.json())

response = requests.patch(BASE + "video/2", {"views": 9999999})
print(response.json())




# response = requests.delete(BASE + "video/0")
# print(response.json)

# response = requests.put(BASE + "video/3", {"likes": 10, "name": "Pocahontas", "views": 120})    # im sanding get request to BASE(URL) and slash/ helloworld
# print(response.json()) #json so it doesn't look like an object but some information
# input()
# response = requests.get(BASE + "video/6")    # im sanding get request to BASE(URL) and slash/ helloworld
# print(response.json()) #json so it doesn't look like an object but some information
