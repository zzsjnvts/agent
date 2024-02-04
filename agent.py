import json
import requests
from valclient.client import Client
import time
import configparser
import os

def run_app_again():
    answer = input("Enter y if you want to lock an agent again.").lower()
    return answer == 'y'

while True:
    config = configparser.ConfigParser()
    config_file_path = 'C:/region.ini'

    try:
        config.read(config_file_path)
    except Exception as e:
        print(f"Error reading {config_file_path}: {e}")
        time.sleep(3)
        exit(0)

    agents_response = requests.get("https://valorant-api.com/v1/agents")
    print("Agent 1nstal0cker Modified by @.tyeso99 on discord")
    print("")

    if agents_response.status_code != 200:
        print("Error reaching valorant-api.com")
        time.sleep(3)
        exit(0)

    agents_json = agents_response.json()['data']

    agent_dict = {}
    if 'SelectedRegion' in config and 'Region' in config['SelectedRegion']:
        regfinal = config['SelectedRegion']['Region']
    else:
        print("1. ap")
        print("2. latam")
        print("3. br")
        print("4. eu")
        print("5. na")

        myregion = input("Enter the number of your region: ")
        regfinal = "test"

        try:
            myregion = int(myregion)
            if myregion == 1:
                regfinal = "ap"
            elif myregion == 2:
                regfinal = "latam"
            elif myregion == 3:
                regfinal = "br"
            elif myregion == 4:
                regfinal = "eu"
            elif myregion == 5:
                regfinal = "na"
            else:
                print("Invalid region number")
                time.sleep(3)
                exit(0)
        except ValueError:
            print("Invalid input. Please enter a number.")
            time.sleep(3)
            exit(0)

        config['SelectedRegion'] = {'Region': regfinal}
        try:
            with open(config_file_path, 'w') as configfile:
                config.write(configfile)
        except PermissionError:
            print("Error writing to", config_file_path)
            print("Please run the app as an administrator.")
            time.sleep(3)
            exit(0)

    print("Selected region is " + regfinal + ".")
    print("To edit your region, delete the region.ini file in C:/.")
    print("And close the app and run again.")
    print("")
    print("")

    def get_time_input(prompt):
        while True:
            try:
                user_input = float(input(prompt))
                return user_input
            except ValueError:
                print("")
                print("Error: Please enter a valid time.")

    agent_names = [agent['displayName'] for agent in agents_json if agent['isPlayableCharacter']]

    for name in agent_names:
        print(name)

    client = 0

    try:
        client = Client(region=regfinal)
        client.activate()
    except:
        print("Valorant is not running")
        time.sleep(3)
        exit(0)

    agent = input("Enter name of agent to lock: ").lower()
    print("")
    print("")

    uuid = ''
    for agent_data in agents_json:
        if agent_data['displayName'].lower() == agent.lower():
            uuid = agent_data['uuid']

    if uuid == '':
        print("Invalid agent name")
        time.sleep(3)
        exit(0)
    time_input = get_time_input("Enter time to lock " + agent + " ( in sec): ")
    while client.session_fetch()['loopState'] != "PREGAME":
        time.sleep(0.01)
        print("Locking " + agent + " in " + str(time_input) + " seconds")

    client.pregame_select_character(uuid)
    client.pregame_lock_character(uuid)
    print("Locked " + agent)

    if not run_app_again():
        break
