# Instructor checklist — Week 12, Day 1

## Before class

- [ ] Slides `docs/slides/week-12-day-01.html`  
- [ ] `gcc` available; `cd starter/race-lab && CGO_ENABLED=1 go test -race ./...`  
- [ ] Confirm Unsafe counter still fails before students patch  

## During

- [ ] Show DATA RACE on projector once  
- [ ] Fix with Mutex live  
- [ ] Context + `c.Request.Context()`  
- [ ] Cut shutdown demo if lab needs time  

## After

- [ ] Collect PRs with `-race` in README  
- [ ] Reject “WaitGroup only” race “fixes”  
