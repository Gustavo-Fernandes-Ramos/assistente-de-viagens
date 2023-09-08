### links

**icones:** https://fonts.google.com/icons

**design das páginas:** https://www.figma.com/file/zeEImDKJikqiyY6i4Q1RRT/travel_assistant_html_prototype?type=design&node-id=0%3A1&mode=design&t=UYFGVd1Iklj40qmM-1

**kanban do projeto(notion):** https://www.notion.so/Assistente-de-Viagens-f7e79a889e3a4f9697b20c338a100ba8

# Aplicação front-end

## Tarefa

Obter tela inicial

### URI

```
http://localhost:5000/home
```

### Request

```
GET /home HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: localhost:5000
Accept: text/html
Accept-Charset: utf-8
Accept-Language: pt-br
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
```

### Responses

#### 200 OK
```
HTTP/1.0 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 988
Content-Type: text/html; charset=utf-8
Connection: Closed

[arquivo html da tela inicial]
```
#### 404 Not Found
```
HTTP/1.0 404 Not Found
Date: Sun, 18 Oct 2012 10:36:20 GMT
Server: Apache/2.2.14 (Win32)
Content-Length: 0
Content-Type: text/html; charset=utf-8
Connection: Closed
```

## Tarefa
Autenticar viajante

### URI
```
http://localhost:5000/auth?credentials=true
```

### Request
```
GET /auth?credentials=true HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: localhost:5000
Connection: Keep-Alive
Authorization: Bearer dXNlcm5hbWU6cGFzc3dvcmQ=
```

### Responses

#### 200 OK
```
HTTP/1.0 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 0
Content-Type: text/html; charset=utf-8
Connection: Closed
```
#### 401 Unauthorized
```
HTTP/1.0 401 Unauthorized
Date: Sun, 18 Oct 2012 10:36:20 GMT
Server: Apache/2.2.14 (Win32)
Content-Length: 0
Content-Type: text/html; charset=utf-8
Connection: Closed
```
#### 201 Created
```
HTTP/1.0 201 Created
Date: Sun, 18 Oct 2012 10:36:20 GMT
Server: Apache/2.2.14 (Win32)
Content-Length: 0
Content-Type: text/html; charset=utf-8
Connection: Closed
Set-Cookie: token=dXNlcm5hbWU6cGFzc3dvcmQ=; expires=Fri, 31 Dec 2024 23:59:59 GMT; path=/; Domain=localhost:5000
```
## Tarefa

obter atrações para avaliação

### URI
```
http://localhost:5000/avaliation?credentials=true
```
### Request

### Responses

###

### Request
```
POST /cgi-bin/process.cgi HTTP/1.0
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: localhost:5000
Accept: application/json
Accept-Charset: utf-8
Accept-Language: pt-br
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
Content-Type: application/json
Content-Length: 98

{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
### Responses
