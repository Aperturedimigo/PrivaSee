from Minsung.util import *

def verify(face_id, another_face_id=None, person_group_id=None,person_id=None):
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