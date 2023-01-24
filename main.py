from database import models
from database.database import engine
import time
from pose_detection import pose_detection
from database.functions import add_data


print(
    "__ Welcome to the Knee Bend Commputer Vision Task __ \nConnecting to the database ..."
)
models.Base.metadata.create_all(engine)
print("Database Connected")

print("__ Session started __")
while True:
    name = input("Enter the name of the examiner: ")

    print("Starting the computer vision model ...")
    time.sleep(1)
    print("\nPress q to exit the model...")
    reps_count = pose_detection()
    print(f"\nUser {name} have done {reps_count} reps !")

    print("\nSaving the details to the database ...")
    add_data(name=f"{name}", reps=reps_count)
    print(f"\nData of user {name} saved successfully\n")

    command = input("Do you want to continue the session [Y/N]")
    if command == "Y" or command == "y":
        continue
    else:
        break
