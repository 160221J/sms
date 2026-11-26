# Week 15 auth-lab — E2E checklist

No separate Go module — exercise the week-15 backend + repo `frontend/`.

## Postman / curl

```bash
# 1) Register
curl -s -X POST localhost:8080/api/register \
  -H 'Content-Type: application/json' \
  -d '{"first_name":"Ada","last_name":"Lovelace","username":"ada","email":"ada@example.com","password":"secret123"}'

# 2) Login — copy token
curl -s -X POST localhost:8080/api/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"ada","password":"secret123"}'

# 3) Without token → 401
curl -si localhost:8080/api/students | head -5

# 4) With token → 200
TOKEN='paste-here'
curl -s -H "Authorization: Bearer $TOKEN" localhost:8080/api/students
```

## React

```bash
cd frontend
echo 'VITE_API_URL=http://localhost:8080' > .env
npm install
npm run dev
```

Register → Login → confirm `localStorage.token` and Network shows `Authorization: Bearer …`.
