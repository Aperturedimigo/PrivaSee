import requests

def Detect():
    data = open('face.jpg', 'rb')
    FaceListId = "aperture_test"
    urlArray = []
    key = open("./key.txt").readline()
    check = "<bound method Response.json of <Response [200]>>"
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key
    }
    param = True
    r = requests.post("https://api.projectoxford.ai/face/v1.0/detect?{}".format(param), data=data, headers=headers)
    a = r.json
    b = str(a)
    if ((r.json() == list()) | (b != check)):
        return False
    NumberOfFace = len(r.json())
    maxValue = 0
    offset = 0
    i = 0
    while i < NumberOfFace:
        height = r.json()[i]['faceRectangle']['height']
        width = r.json()[i]['faceRectangle']['width']
        if maxValue < height * width:
            maxValue = height * width
            offset = i
        i += 1
    FaceIdValue = r.json()[offset]['faceId']
    return FaceIdValue

def Create_FaceList():
    data = open('face.jpg', 'rb')
    FaceListId = "aperture_test"
    urlArray = []
    key = open("./key.txt").readline()
    check = "<bound method Response.json of <Response [200]>>"
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key
    }
    body = {
        "name": userName,
    }
    r = requests.put("https://api.projectoxford.ai/face/v1.0/facelists/{}".format(FaceListId), json=body,
                     headers=headers)
    a = r.json
    b = str(a)
    if b != check:
        return False

def Add_Face():
    data = open('face.jpg', 'rb')
    FaceListId = "aperture_test"
    urlArray = []
    key = open("./key.txt").readline()
    check = "<bound method Response.json of <Response [200]>>"
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key
    }
    r = requests.post("https://api.projectoxford.ai/face/v1.0/facelists/{}/persistedFaces?".format(FaceListId),
                        data=data, headers=headers)
    a = r.json
    b = str(a)
    if b != check:
        return False

def Find_Similar(FaceId):
    data = open('face.jpg', 'rb')
    FaceListId = "aperture_test"
    urlArray = []
    key = open("./key.txt").readline()
    check = "<bound method Response.json of <Response [200]>>"
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key
    }
    body = {
        "faceId": FaceId,
        "faceListId": FaceListId,
        "maxNumOfCandidatesReturned": 1000,
        "mode": "matchFace"
    }
    r = requests.post("https://api.projectoxford.ai/face/v1.0/findsimilars", json=body, headers=headers)
    length = len(r.json())
    Sum = 0
    i = 0
    while i < length:
        Sum = Sum + float(r.json()[i]['confidence'])
        Confidence = Sum / length
        i += 1
    a = r.json
    b = str(a)
    if b != check:
        return False
    return Confidence