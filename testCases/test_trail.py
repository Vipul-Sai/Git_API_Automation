import json

# import pytest
# from utilities.configreader import readConfig
import requests

header = {
    'Authorization': 'Bearer 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',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'
}
# def test_createBranch_Post():
    # end_point = "repos/Vipul-Sai/Hello/git/refs"
    #
    # url =  readConfig("url", "web_url") + end_point
    # url = 'https://api.github.com/repos/Vipul-Sai/Hello/git/refs'
    # file = open('Data/branch.json','r')
    # json_file = json.loads(file.read())
    #
    # response =  requests.post(url ,json=json_file, headers=header)
    #
    # print(response.status_code)
    # if response.status_code == 201:
    #     assert True
    # else:
    #     assert False
#
# def test_createFileBranch():
#     url = "https://api.github.com/repos/Vipul-Sai/Hello/contents/intel"
#     file = open('Data/createFile.json','r')
#     jsonFile = json.loads(file.read())
#
#     response =  requests.put(url,headers=header, json=jsonFile)
#     print(response.status_code)
#     if response.status_code ==  201:
#         assert True
#     else:
#         assert False
#     json_data = (response.json())
#     print(json_data)
#
# #
# def test_pull_request():
#     url = "https://api.github.com/repos/Vipul-Sai/Hello/pulls"
#     file =  open('Data/pullrequest.json','r')
#     jsonfile = json.loads(file.read())
#
#     response = requests.post(url, headers=header, json=jsonfile)
#
#     print(response.status_code)
#     if response.status_code ==  201:
#         assert True
#     else:
#         assert False


# def test_updateFileinBranch():
#     url = "https://api.github.com/repos/Vipul-Sai/Hello/contents/intel"
#     file = open('Data/updateFile.json','r')
#     json_file =  json.loads(file.read())
#
#     response =  requests.put(url, headers=header, json=json_file)
#     print(response.status_code)
#     if response.status_code == 200:
#         assert True
#     else:
#         assert False


# def test_put_main_branch():
#     # end_point = "repos/Vipul-Sai/"+ repo_name +"contents/main"
#     url = "https://api.github.com/repos/Vipul-Sai/API_Test08-36-25/contents/main"
#     file = open('Data/create_main_branch.json','r')
#     json_file = json.loads(file.read())
#     response = requests.put(url, json=json_file, headers=header)
#     print(response.status_code)
#
#     if response.status_code == 201:
#         assert True
#     else:
#         assert False
#     json_data = response.json()
#     print(json_data)
#     sha = json_data['commit']['sha']
#     print(sha)
#     return sha

def test_getshaw():
    url = "https://api.github.com/repos/Vipul-Sai/API_Test19-00-59/contents/main"

    response = requests.get(url, headers= header)
    print(response.status_code)
    assert response.status_code == 200
    jsonData = response.json()
    print(jsonData)
    shaCode = jsonData['sha']
    print(shaCode)



