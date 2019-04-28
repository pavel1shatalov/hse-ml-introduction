import os

def write_answer(num, answer):
    if not os.path.exists("answers"):
        os.makedirs("answers")

    with open(os.path.join("answers", f"task{num}.txt"), "w") as f:
        f.write(answer)

    print(answer)