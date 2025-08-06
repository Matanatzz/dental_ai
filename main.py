from dental_ai import backend_api

def main():
    api_key = input("Enter your OpenAI API key (or press Enter to use default): ").strip()
    backend = backend_api.APIBackend(api_key if api_key else None)

    anamnesis_lines = []
    print("Enter anamnesis text (end input with a blank line):")
    while True:
        line = input()
        if not line.strip():
            break
        anamnesis_lines.append(line)
    anamnesis_text = "\n".join(anamnesis_lines)

    print("\nProcessing...\n")
    output = backend.process(anamnesis_text)
    print("\n=== Output ===\n")
    print(output)

if __name__ == "__main__":
    main()
