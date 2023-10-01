from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models import Task
from database import tasks
from utils import task_exist_check, task_not_exist_check

router = APIRouter()

@router.get("/", response_model=dict)
async def task_list():
    return {'tasks': tasks}

@router.get("/{task_id}", response_model=Task)
async def task_detail(task_id: int):
    task_exist_check(tasks, task_id)
    return tasks[task_id]

@router.post("/", response_model=Task)
async def task_add(task: Task):
    task_not_exist_check(tasks, task.id)
    new_task = task.dict()
    tasks.append(new_task)
    return new_task

@router.put("/{task_id}", response_model=Task)
async def edit_task(task_id: int, new_task: Task):
    task_exist_check(tasks, task_id)
    index_to_update = next((i for i, task in enumerate(tasks) if task['id'] == task_id), None)
    if index_to_update is not None:
        new_task.id = task_id
        tasks[index_to_update] = new_task
        return new_task
    raise HTTPException(status_code=404, detail=f'Task {task_id} not found')

@router.delete("/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    task_exist_check(tasks, task_id)
    task_to_remove = next((task for task in tasks if task['id'] == task_id), None)
    if task_to_remove:
        tasks.remove(task_to_remove)
        return task_to_remove
    raise HTTPException(status_code=404, detail=f'Task {task_id} not found')