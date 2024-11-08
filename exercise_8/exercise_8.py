import os

files = os.listdir("exercise_8/clutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"exercise_8/clutteredFolder/{file}",f"exercise_8/clutteredFolder/{i}.png")
        i = i + 1