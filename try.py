def runTimeError():

    try:
        x = int(input("Enter a number: "))
        y = 10 / x
        print("Result:", y)

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

    finally:
        print("This block will always execute, regardless of whether an exception occurred or not.")


runTimeError()