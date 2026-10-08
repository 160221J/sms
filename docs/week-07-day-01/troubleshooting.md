# Week 7 troubleshooting

| What they see | Cause | Fix |
| --- | --- | --- |
| JSON shows `FirstName` | missing tags | add `` `json:"first_name"` `` |
| 400 always on POST | trailing comma / wrong content-type | raw JSON; Content-Type application/json |
| empty list after create | wrote different map / restarted | same process; print len after create |
| 404 for valid id | string vs int key | `strconv.Atoi(c.Param("id"))` |
| panic on bind | forgot `&req` | `ShouldBindJSON(&req)` |
| import models fail | wrong path | `student-management-system/internal/models` |
| order of GET list changes | map range | expected; sort by id if needed |

## Minimal create body

```json
{
  "first_name": "Ada",
  "last_name": "Lovelace",
  "email": "ada@example.com",
  "phone": "0770000000",
  "course": "SE"
}
```
