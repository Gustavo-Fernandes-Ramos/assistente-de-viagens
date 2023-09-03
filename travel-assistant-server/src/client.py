import http.client

conn = http.client.HTTPConnection("localhost", 8080)

conn.request("GET", "/index.html")

response = conn.getresponse()

print(response.status, response.reason)

# data = response.read()
# print(data)

while chunk := response.read(200):
    print(repr(chunk))

