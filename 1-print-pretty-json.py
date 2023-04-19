import json

res = request.post(Url, data)

print(json.dumps(res, indent=2))
