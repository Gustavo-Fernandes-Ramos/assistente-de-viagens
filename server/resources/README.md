# API do Servidor

## Endpoints

http://localhost:8000/criar_auth
```
GET /palavras_chave HTTP/1.1
```
```
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhc3Npc3RlbnRlX3ZpYWdlbnMiLCJhdWQiOiJjbGllbnQiLCJzdWIiOjExLCJqdGkiOiJhZGJkNzc3NS03ZGU4LTQxNDAtOWU3Yy1kNmZmODIyMGE2YzMiLCJpYXQiOjE2OTY2NTk2MTEsIm5iZiI6MTY5NjY1OTYxMSwiZXhwIjoxODU0MzM5NjExfQ.ePyGfCl59_zkD1CAZqqkR9C19ihN7X4_gYySughU5C1UxTtLars0ckpruSTTMCFAUVfOmnH1pTVaF_IFfQgw8-Tg6AGE2rbnd_Nze2fbwv6DvvH9iJzZZEwg2lrOmpAGVp31pKUQrFTnUET_vZYaqzxlD814Pw2zERVNb7eye9kV2d2Y2s4OJiV_I02RsSJThiLqxoX9NnFaFX4otCCI61T_CkxnfTgX2OxbBWts7Bsx84W_VVxG_t5nCRrm26cLqv6QwcITKI15lDbqWHbkFaUNBdM-VQ8kE-CbmsSgjsRFxy1NUGpzQJCRDCaaDaIUzzDBO14qtTOZU1GQnh16vw",
  "token_type": "Bearer",
  "expires_in": 1854339611,
  "scope": "client"
}
```

```
Authorization: Bearer "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhc3Npc3RlbnRlX3ZpYWdlbnMiLCJhdWQiOiJjbGllbnQiLCJzdWIiOjExLCJqdGkiOiJhZGJkNzc3NS03ZGU4LTQxNDAtOWU3Yy1kNmZmODIyMGE2YzMiLCJpYXQiOjE2OTY2NTk2MTEsIm5iZiI6MTY5NjY1OTYxMSwiZXhwIjoxODU0MzM5NjExfQ.ePyGfCl59_zkD1CAZqqkR9C19ihN7X4_gYySughU5C1UxTtLars0ckpruSTTMCFAUVfOmnH1pTVaF_IFfQgw8-Tg6AGE2rbnd_Nze2fbwv6DvvH9iJzZZEwg2lrOmpAGVp31pKUQrFTnUET_vZYaqzxlD814Pw2zERVNb7eye9kV2d2Y2s4OJiV_I02RsSJThiLqxoX9NnFaFX4otCCI61T_CkxnfTgX2OxbBWts7Bsx84W_VVxG_t5nCRrm26cLqv6QwcITKI15lDbqWHbkFaUNBdM-VQ8kE-CbmsSgjsRFxy1NUGpzQJCRDCaaDaIUzzDBO14qtTOZU1GQnh16vw"
```

http://localhost:8000/palavras_chave
```
GET /palavras_chave HTTP/1.1
```
```
Authorization: Bearer dXNlcm5hbWU6cGFzc3dvcmQ
```
```
{
  destinos: ["São Paulo, SP"]
  palavras_chave: ["passeio a pé", "outdoor", "natureza"]
}
```

http://localhost:8000/palavras_chave
```
POST /palavras_chave HTTP/1.1
```
```
Authorization: Bearer dXNlcm5hbWU6cGFzc3dvcmQ
```
```
{
  "destino": "São Paulo, SP",
  "data_inicio": 1854339220,
  "data_fim": 1854339220,
  "palavras_chave": ["passeio a pé", "outdoor", "natureza"]
}
```

http://localhost:8000/roteiros
```
GET /roteiros HTTP/1.1
```
```
Authorization: Bearer dXNlcm5hbWU6cGFzc3dvcmQ
```
```
{
  "roteiros": ["roteiro1":{}, "roteiro2":{}, "roteiro3":{}]
}
```

http://localhost:8000/roteiros/{id}
```
GET /roteiros HTTP/1.1
```
```
Authorization: Bearer dXNlcm5hbWU6cGFzc3dvcmQ
```
```
{
  "roteiro": [{}, {}, {}]
}
```

#### 200 OK
```
HTTP/1.0 200 OK
```
#### 201 Created
```
HTTP/1.0 201 Created
```
#### 401 Unauthorized
```
HTTP/1.0 401 Unauthorized
```
#### 404 Not Found
```
HTTP/1.0 404 Not Found
```

### links

**icones:** https://fonts.google.com/icons

**design das páginas:** https://www.figma.com/file/zeEImDKJikqiyY6i4Q1RRT/travel_assistant_html_prototype?type=design&node-id=0%3A1&mode=design&t=UYFGVd1Iklj40qmM-1

**kanban do projeto(notion):** https://www.notion.so/Assistente-de-Viagens-f7e79a889e3a4f9697b20c338a100ba8
