import base64
import json

event_data = {
    'event': 'test event',
    'properties': {
        'token': '6888bfdec29d84ab2d36ae18c57b8535',
        'str': 'string',
        'int': 1,
        'float': 1.235,
        'object': {'one': 1, 'two': 2},
        'list': ['one', 'two'],
    }
}
event_encoded = base64.b64encode(str.encode(json.dumps(event_data))).decode('utf-8')

profile_update = {
    '$token': '6888bfdec29d84ab2d36ae18c57b8535',
    '$distinct_id': '13793',
    '$ip': '123.123.123.123',
    '$set': {
        'Address': '1313 Mockingbird Lane',
        'Birthday': '1948-01-01'
    }
}
profile_update_encoded = base64.b64encode(str.encode(json.dumps(profile_update))).decode('utf-8')

group_update = {
    '$token': '6888bfdec29d84ab2d36ae18c57b8535',
    '$group_key': 'Company',
    '$group_id': 'company_a',
    '$set': {
        '$name': 'Company A',
        'Address': '1313 Mockingbird Lane'
    }
}
group_update_encoded = base64.b64encode(str.encode(json.dumps(group_update))).decode('utf-8')

class TestTrack:
    def test_get_no_data(self, client):
        resp = client.get('/track?verbose=1')
        assert resp.json['status'] == 0

    def test_get(self, client):
        resp = client.get('/track?verbose=1&data=%s' % event_encoded)
        assert resp.json['status'] == 1

    def test_post(self, client):
        resp = client.post('/track', data={'verbose': 1, 'data': json.dumps(event_data)})
        assert resp.json['status'] == 1

class TestEngage:
    def test_get_no_data(self, client):
        resp = client.get('/engage?verbose=1')
        assert resp.json['status'] == 0

    def test_get(self, client):
        resp = client.get('/engage?verbose=1&data=%s' % profile_update_encoded)
        assert resp.json['status'] == 1

    def test_post(self, client):
        resp = client.post('/engage', data={'verbose': 1, 'data': json.dumps(profile_update)})
        assert resp.json['status'] == 1

class TestGroups:
    def test_get_no_data(self, client):
        resp = client.get('/groups?verbose=1')
        assert resp.json['status'] == 0

    def test_get(self, client):
        resp = client.get('/groups?verbose=1&data=%s' % group_update_encoded)
        print(resp.data)
        assert resp.json['status'] == 1

    def test_post(self, client):
        resp = client.post('/groups', data={'verbose': 1, 'data': json.dumps(group_update)})
        assert resp.json['status'] == 1
