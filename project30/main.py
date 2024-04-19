# try: Something that might cause an Exception
# except: Do this if there was an Exception
# else: Do this if there were no exceptions
# finally: Do this no matter what happens
# raise     - is used for your own errors that you need to catch

height = float(input("Height(in meters): "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters")
bmi = weight / height**2
print(bmi)
