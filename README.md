# Student Management System (SMS)

Demo / capstone project for the Epic Learn **Go Programming Master Course**.

- **Curriculum (16 weeks):** [COURSE.md](COURSE.md)
- **Project spec:** [docs/sms-project-spec.md](docs/sms-project-spec.md)

## Run (week 15+)

PostgreSQL database `sms`, then:

```bash
psql -U postgres -d sms -f backend/migrations/001_init.sql
cp backend/.env.example backend/.env   # edit secrets locally; never commit .env
cd backend && go run ./cmd/server
```

```bash
cd frontend && npm install && npm run dev
```

API: `http://localhost:8080` · UI: `http://localhost:5173`
