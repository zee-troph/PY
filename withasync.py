import asyncio

async def task1():
    print("Task 1 start")
    await asyncio.sleep(100)  # task1 is suspended
    print("Task 1 end")
    
async def task2():
    print("Task 2 runs immediately")
    
async def main():
    await asyncio.gather(task1(), task2())  # task1 and task2 run concurrently
    
asyncio.run(main())            