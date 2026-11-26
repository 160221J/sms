# Refactor lab — consistent errors

Goal: one JSON error shape and structured logs. Apply the same idea in *your* handlers.

## Before

```go
if err != nil {
    c.String(http.StatusInternalServerError, err.Error()) // leaks internals; not JSON
    return
}
```

## After

```go
if err != nil {
    slog.Error("list students", "err", err)
    c.JSON(http.StatusInternalServerError, gin.H{"error": "internal error"})
    return
}
```

## Also look for

- Dead commented blocks and unused imports  
- Vague names (`data`, `tmp`, `HandleStuff`)  
- Mixed `log.Println` vs `slog` — prefer `slog`  
- Returning password hashes (must stay `json:"-"`)

Commit message idea: `refactor: consistent JSON errors and slog on student list`.
