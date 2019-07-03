import json
import sys
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
json_str = '\n'.join(lines)
json_data = json.loads(json_str)


print(json_data['Records'][0]['s3']['bucket']['arn'])

