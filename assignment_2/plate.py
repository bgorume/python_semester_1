def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s.isalnum():
        return False
    for i, char in enumerate(s):
        if char.isdigit():
            if not s[i:].isdigit():
                return False
            if i < 2:
                return False
            if s[i] == '0':
                return False
            return True
    return True

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
