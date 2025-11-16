import sys

 True:while
    try:

        name = input("Give me a filename: ").strip().lower()


        if name.endswith((".gif", ".png", ".jpeg", ".jpg")):
            print(f"image/{name.split('.')[-1]}")
            break
        elif name.endswith(".pdf"):
            print("application/pdf")
            break
        elif name.endswith(".zip"):
            print("application/zip")
            break
        elif name.endswith(".txt"):
            print("text/plain")
            break
        else:

            print(f"File extension for '{name}' could not be determined.")
            attempt = input("Do you want to try another file? (yes/no): ").strip().lower()

            if attempt in ["yes", "yea", "si", "neh"]:
                continue
            else:
                sys.exit(1)



