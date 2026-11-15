# Homework — Week 12, Day 1

Due: _______________ · **GitHub PR**

## Already done in lab

- Race lab: red → mutex → green  
- Understood Mutex vs WaitGroup  

## Required

1. Document in README:

   ```bash
   go test -race ./...
   ```

2. SMS (or your fork): shared maps locked; repository methods take `context.Context` (may ignore body until week 14); handlers pass `c.Request.Context()`.

3. PR description: what `-race` reported, what you changed.

## Marking

| Check | Pass |
| --- | --- |
| README has `-race` |  |
| Shared state locked |  |
| Context on repo + handlers |  |
| PR explanation |  |
