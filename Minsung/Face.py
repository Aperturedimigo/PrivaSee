from Minsung.util import *

def detect(image):
    url = 'detect'
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': KEY,
               'Content-Length': 0,
               }
    data = open(image, "rb")
    return request('POST', url,data,headers)


def find_similars(face_id, face_list_id=None, face_ids=None,
                  max_candidates_return=20, mode='matchPerson'):

    url = 'findsimilars'
    json = {
        'faceId': face_id,
        'faceListId': face_list_id,
        'faceIds': face_ids,
        'maxNumOfCandidatesReturned': max_candidates_return,
        'mode': mode,
    }

    return request('POST', url, json=json)


def group(face_ids):

    url = 'group'
    json = {
        'faceIds': face_ids,
    }

    return request('POST', url, json=json)


def identify(face_ids, person_group_id, max_candidates_return=1,
             threshold=None):

    url = 'identify'
    json = {
        'personGroupId': person_group_id,
        'faceIds': face_ids,
        'maxNumOfCandidatesReturned': max_candidates_return,
        'confidenceThreshold': threshold,
    }

    return request('POST', url, json=json)


def verify(face_id, another_face_id=None, person_group_id=None,
           person_id=None):

    url = 'verify'
    json = {}
    if another_face_id:
        json.update({
            'faceId1': face_id,
            'faceId2': another_face_id,
        })
    else:
        json.update({
            'faceId': face_id,
            'personGroupId': person_group_id,
            'personId': person_id,
        })

    return request('POST', url, json=json)