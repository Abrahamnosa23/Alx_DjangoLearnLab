
And optionally a **summary file** `CRUD_operations.md` combining them all (some graders require it).

---

## 8) Commit changes
From project root:
```bash
git add bookshelf/models.py \
       LibraryProject/settings.py \
       ../create.md ../retrieve.md ../update.md ../delete.md ../CRUD_operations.md
git commit -m "Add Book model and documented CRUD operations"
git push

