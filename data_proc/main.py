from scheduler import Scheduler


if __name__ == '__main__':
    scheduler = Scheduler()
    print("Press Ctrl+C to exit...")
    scheduler.run()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Application closing...")
        scheduler.stop()
        print("Application exited")

