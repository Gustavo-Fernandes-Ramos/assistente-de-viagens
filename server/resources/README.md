### links

**icones:** https://fonts.google.com/icons

**design das páginas:** https://www.figma.com/file/zeEImDKJikqiyY6i4Q1RRT/travel_assistant_html_prototype?type=design&node-id=0%3A1&mode=design&t=UYFGVd1Iklj40qmM-1

**kanban do projeto(notion):** https://www.notion.so/Assistente-de-Viagens-f7e79a889e3a4f9697b20c338a100ba8

# Aplicação front-end

## Tarefa

Obter tela inicial

### URI

http://localhost:8080/resources/index.html

### Request

GET /resources/index.html HTTP/1.0

User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)

Host: www.tutorialspoint.com

Accept-Language: pt-br

Accept-Encoding: gzip, deflate

Connection: Keep-Alive

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

### Responses

#### OK

HTTP/1.0 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 88
Content-Type: text/html
Connection: Closed

(arquivo html da tela inicial)

#### Not Found

HTTP/1.0 404 Not Found
Date: Sun, 18 Oct 2012 10:36:20 GMT
Server: Apache/2.2.14 (Win32)
Content-Length: 230
Connection: Closed
Content-Type: text/html; charset=iso-8859-1

### Request

POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: length

licenseID=string&content=string&/paramsXML=string

### Response
