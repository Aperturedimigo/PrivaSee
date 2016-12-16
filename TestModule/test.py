import requests

def Detect():
    data = open('face.jpg', 'rb')
    key = open("key.txt").readline()
    check = "<bound method Response.json of <Response [200]>>"
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': key
    }
    faceIdreturn = True
    r = requests.post("https://api.projectoxford.ai/face/v1.0/detect?{}".format(faceIdreturn), data=data, headers=headers)
    a = r.json
    b = str(a)
    if ((r.json() == list()) or (b != check)):
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
    FaceListId = "aperture_test"
    key = open("../key.txt").readline()
    check = "<bound method Response.json of <Response [200]>>"
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key
    }
    body = {
        "name": "aperture_jyk",
    }
    r = requests.put("https://api.projectoxford.ai/face/v1.0/facelists/{}".format(FaceListId), json=body,
                     headers=headers)
    a = r.json
    b = str(a)
    if b != check:
        return False

def Add_Face():
    data = open('TestImage.jpg', 'rb')
    fAceListId = "aperture_test"
    key = open("../key.txt").readline()
    check = "<bound method Response.json of <Response [200]>>"
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': key,
        'Content-Length' : 0
    }
    r = requests.post("https://api.projectoxford.ai/face/v1.0/facelists/{}/persistedFaces".format(fAceListId),data=data, headers=headers)
    a = r.json
    b = str(a)
    print(a)
    if b != check:
        return False
    else:
        return a

def Find_Similar(FaceId):
    data = open('TestImage.jpg', 'rb')
    FaceListId = "aperture_test"
    key = open("../key.txt").readline()
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
        i += 1
    Confidence = Sum / length
    a = r.json
    b = str(a)
    if b != check:
        return False
    return Confidence

b = Add_Face()
print(b)