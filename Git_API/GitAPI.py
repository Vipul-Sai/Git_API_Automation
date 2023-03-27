import time

import pytest
import requests
import json
import unittest
from utilities.configreader import readConfig
import datetime
from utilities.customLogger import customLogger

log = customLogger()
Today = datetime.datetime.now().strftime("%H-%M-%S")
repoName = "git_flow_task" + Today
header = {
    'Authorization': 'Bearer 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',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'
}
shaCode = None
shaCodeUpdate = None

class Gitflow(unittest.TestCase):

    def user_login(self):
        end_point = "user"
        url = readConfig('url', 'web_url')+end_point
        response = requests.get(url, headers=header)
        print(response.status_code)

        if response.status_code ==  200:
            assert True
            log.info("API passed")
        else:
            log.error("API failed")
            assert False
        jsondata = response.json()
        # print(jsondata)

        response_data = jsondata["login"]
        print(response_data)

        if jsondata['login'] == 'Vipul-Sai':
            assert True
            log.info("Validation successful")
        else:
            assert False

    def create_repository(self):
        end_point = 'user/repos'
        url = readConfig('url', 'web_url')+end_point
        file = open('Data/create_repo.json', 'r')
        json_file = json.loads(file.read())
        json_file['name'] = repoName
        response = requests.post(url, headers=header, json=json_file)

        print(response.status_code)
        if response.status_code==201:
            log.info("Repository created")
            assert True
        else:
            assert False
        json_data = response.json()
        # print(json_data)

        res_data = json_data['owner']['login']
        print(res_data)
        if res_data == 'Vipul-Sai':
            assert True
        else:
            assert False
        time.sleep(5)
        print(repoName)
    print(repoName)

    def create_branch_main(self):
        print(repoName)
        end_point = "repos/Vipul-Sai/"+ str(repoName) +"/contents/main"
        print(end_point)
        url = readConfig('url', 'web_url') + end_point
        file = open('Data/create_main_branch.json','r')
        json_file = json.loads(file.read())
        response = requests.put(url, headers=header,  json=json_file)
        print(response.status_code)
        if response.status_code == 201:
            assert True
            log.info("Default branch created naming main")
        else:
            assert False
        json_data = response.json()
        # print(json_data)
        sha = json_data['commit']['sha']
        print(sha)
        global shaCode
        shaCode = sha
        print(shaCode)



    def create_branch(self):
         # Create Branch using sha

        print(str(shaCode))
        end_point = "repos/Vipul-Sai/"+repoName +"/git/refs"
        url = readConfig("url", "web_url") + end_point
        print(url)
        file = open('Data/branch.json','r')
        json_file = json.loads(file.read())
        json_file["sha"] = shaCode
        print(json_file['sha'])

        response =  requests.post(url,headers=header, json=json_file)
        print(response.status_code)
        if response.status_code == 201:
            assert True
            log.info("Branch created")
        else:
            assert False
    def create_file_in_branch(self):
        end_point = "repos/Vipul-Sai/"+repoName +"/contents/feature/git_flow_feature"
        url = readConfig("url", "web_url") + end_point
        print(url)
        file = open('Data/createFile.json','r')
        jsonFile = json.loads(file.read())

        response =  requests.put(url,headers=header, json=jsonFile)
        print(response.status_code)
        if response.status_code ==  201:
            assert True
            log.info("File created")
        else:
            assert False
        json_data = (response.json())
        print(json_data)
        shaUpdate = json_data['content']['sha']
        print(shaUpdate)
        global shaCodeUpdate
        shaCodeUpdate = shaUpdate
        print(shaCodeUpdate)


    def pull_request(self):
        end_point = "repos/Vipul-Sai/"+repoName +"/pulls"
        url = readConfig("url", "web_url") + end_point
        print(url)
        file =  open('Data/pullrequest.json','r')
        jsonfile = json.loads(file.read())

        response = requests.post(url, headers=header, json=jsonfile)

        print(response.status_code)
        if response.status_code ==  201:
            assert True
            log.info("Pull request done")
        else:
            assert False

    def update_file_in_branch(self):
        end_point = "repos/Vipul-Sai/"+repoName +"/contents/feature/git_flow_feature"
        url = readConfig("url", "web_url") + end_point
        print(url)
        file = open('Data/updateFile.json','r')
        json_file =  json.loads(file.read())
        json_file['sha'] = shaCodeUpdate

        response =  requests.put(url, headers=header, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
            log.info("File updated in branch")
        else:
            assert False

    def rename_branch(self):
        end_point = "repos/Vipul-Sai/" + str(repoName) + "/branches/feature/git_flow_feature/rename"
        url = readConfig("url", "web_url") + end_point
        file = open('Data/rename_branch.json','r')
        json_file = json.loads(file.read())
        response = requests.post(url,headers=header,json=json_file)
        if response.status_code == 201:
            assert True
        else:
            assert False

    def delete_repo(self):
        end_point = "repos/Vipul-Sai/TesterWorld"
        url = readConfig("url", "web_url") + end_point
        response =  requests.delete(url,headers=header)
        print(response.status_code)
        if response.status_code==204:
            assert True
        else:
            assert False




























