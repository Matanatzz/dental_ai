from dental_ai import backend_api, backend_local

def choose_backend():
    choice = input("Choose backend:\n1) OpenAI API\n2) Local LLaMA model\nEnter 1 or 2: ").strip()
    if choice == "1":
        api_key = input("Enter your OpenAI API key (or press enter to use default): ").strip()
        return backend_api.APIBackend(api_key=api_key if api_key else None)
    elif choice == "2":
        return backend_local.LocalBackend()
    else:
        print("Invalid choice.")
        exit(1)

def get_multiline_input(prompt):
    print(prompt)
    print("(Press Enter twice to finish)\n")
    lines = []
    while True:
        line = input()
        if line.strip() == "" and lines:
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    backend = choose_backend()
    anamnesis_text = get_multiline_input("Enter anamnesis text:")
    print("\nProcessing...\n")
    output = backend.process(anamnesis_text)
    print("\n=== Output ===\n")
    print(output)

if __name__ == "__main__":
    main()
