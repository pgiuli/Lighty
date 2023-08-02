import multiprocessing
import color_api
import telegram_bot



if __name__ == '__main__':
    # Create a FastAPI process
    
    #fastapi_process = multiprocessing.Process(target=lambda: uvicorn.run("color_api:app", host="0.0.0.0", port=8000, reload=True))    
    fastapi_process = multiprocessing.Process(target=color_api.start_api)
    telegram_process = multiprocessing.Process(target=telegram_bot.start_bot)


    # Start both processes
    fastapi_process.start()
    telegram_process.start()


    # Wait for both processes to finish
    fastapi_process.join()
    telegram_process.join()
 


