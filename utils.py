from typing import List
from fastapi import HTTPException

def task_exist_check(tasks: List[dict], task_id: int):
    if not any(task['id'] == task_id for task in tasks):
        raise HTTPException(status_code=404, detail=f'Task with id={task_id} Not Found')

def task_not_exist_check(tasks: List[dict], task_id: int):
    if any(task['id'] == task_id for task in tasks):
        raise HTTPException(status_code=404, detail=f'Task with id={task_id} Already Exists')