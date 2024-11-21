def count_words(text):
    """
    Counts the number of words in the given text.

    Args:
        text (str): The input text to process.

    Returns:
        int: The count of words in the input text.
    """
    words = text.split()
    return len(words)

def display_banner():
    """
    Displays a user-friendly banner for the program.
    """
    print("=" * 50)
    print(" " * 15 + "Word Counter Program")
    print("=" * 50)

def main():
    """
    Main function to run the Word Counter program.
    """
    display_banner()
    
    while True:
        print("\nEnter your sentence or paragraph below (type 'exit' to quit):")
        user_input = input(">> ").strip()
        
        if user_input.lower() == "exit":
            print("\nThank you for using the Word Counter. Goodbye!")
            break
        
        if not user_input:
            print("\n⚠️  Error: No input detected. Please enter a valid sentence or paragraph.")
            continue
        
        word_count = count_words(user_input)
        print("\n📄 Input:")
        print(f'"{user_input}"')
        print(f"\n🧮 Word Count: {word_count}")
        print("-" * 50)

if __name__ == "__main__":
    main()
