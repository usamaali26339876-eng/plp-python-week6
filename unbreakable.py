# unbreakable.py

def main():
    print("--- Unbreakable Input App ---")
    while True:
        try:
            user_input = input("Enter a whole number (or type 'exit' to quit): ")
            if user_input.strip().lower() == 'exit':
                break
                
            number = int(user_input)
            print(f"Success! Your squared number is: {number ** 2}\n")
            
        except ValueError:
            print("Oops! That input is unwise. Please enter digits only.\n")

if __name__ == "__main__":
    main()
