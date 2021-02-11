import base64
import json
import urllib

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

class TestTrack:
    def test_get_no_data(self, client):
        resp = client.get('/track?verbose=1')
        assert resp.json['status'] == 0

    def test_get(self, client):
        resp = client.get('/track?verbose=1&ip=1&data=%s' % event_encoded)
        assert resp.json['status'] == 1

    def test_post(self, client):
        resp = client.post('/track', data={'verbose': 1, 'ip': 1, 'data': json.dumps(event_data)})
        assert resp.json['status'] == 1
