```markdown
# Task Tracker CLI

Простой консольный трекер задач (CLI), написанный на Python без использования сторонних библиотек. Позволяет добавлять, обновлять, удалять задачи и управлять их статусом.

## Требования
- Python 3.x

## Как запустить проект

1. Добавить новую задачу:
   ```bash
   python task_tracker.py add "Изучить Python"
   ```

2. Посмотреть все задачи:
   ```bash
   python task_tracker.py list
   ```

3. Посмотреть задачи по статусу (`todo`, `in-progress`, `done`):
   ```bash
   python task_tracker.py list done
   ```

4. Обновить описание задачи:
   ```bash
   python task_tracker.py update 1 "Изучить Python и Git"
   ```

5. Изменить статус задачи:
   ```bash
   python task_tracker.py mark-in-progress 1
   python task_tracker.py mark-done 1
   ```

6. Удалить задачу:
   ```bash
   python task_tracker.py delete 1
   ```

## Project URL
- GitHub Repository: [https://github.com/cursider808/task-tracker-cli](https://github.com/cursider808/task-tracker-cli)
```

### Что делать после сохранения файла:
Сохраните изменения в файле и выполните три команды в терминале, чтобы отправить обновление на GitHub:

```bash
git add README.md
git commit -m "Add project URL to README"
git push
```
