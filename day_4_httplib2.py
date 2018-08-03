import httplib2
import os
import json

# jsonData = '{"connection":{"online":false,"on-net":false}}'

# create a python dictionary object from the json data
# jsonToPython = json.loads(jsonData)

def getCurrentStatus():
    print("Query the current-status api, see d4 p8")



def getJsonFromResponseBody():
    return '{"connection":{"online":false,"on-net":false}}'


def main():
    python_dict_oblect = json.loads(getJsonFromResponseBody())
    print(python_dict_oblect)
    print(python_dict_oblect['connection'])
    # print(python_dict_oblect['online'])
    # print(python_dict_oblect['connection.online'])
    # print(python_dict_oblect['$connection.online'])

    dict_to_json_object = json.dumps(python_dict_oblect)
    print(dict_to_json_object)


if __name__ == "__main__":
    main()