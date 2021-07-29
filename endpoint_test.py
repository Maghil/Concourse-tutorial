import json
from endpoint import free_api

def test_status_code():
    code = free_api().status_code
    assert code == 200

def test_content():
    data = json.loads(free_api().content)
    assert data["meta"]["pagination"]["links"]["previous"] == None