# Pre-class — Week 14, Day 1

Bring week 13: green tests, `StudentStore` interface + fake.

**Install before class (pick one):**

```bash
# Ubuntu packages
sudo apt-get install -y postgresql postgresql-contrib

# or Docker
docker run --name sms-pg -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16
```

Have a DB user/password ready for `.env` (`DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME=sms`).
