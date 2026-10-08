# Homework — Week 8, Day 1

Due: _______________ · **GitHub PR**

## Already done in lab (must stay green)

- Nil-pointer crash understood and fixed  
- `StudentRepository` owns the map  
- Handler calls repo for create / list / get  
- Health still 200  

## Required homework

1. **PR** with handler → repository for all student routes you have (include update/delete if present).  
2. **Memory diagram** in the PR description — notebook photo or ASCII showing `&x` / nil dereference.  
3. `gofmt` clean; no secrets; no Postgres/JWT.  
4. README one paragraph: why handlers no longer hold the map.

## Stretch

- Repo returns `error`; map missing → a sentinel `ErrNotFound`; handler maps to 404  
- `go test` on repository Create + GetByID  

## Marking

| Check | Pass |
| --- | --- |
| Routes still work |  |
| Map not on handler |  |
| Repo package has no `gin` |  |
| Memory diagram in PR |  |
| Evidence / screenshots |  |
