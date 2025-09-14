from dental_ai import backend_api

def main():
    api_key = input("Enter your OpenAI API key (or press Enter to use default): ").strip()
    backend = backend_api.APIBackend(api_key if api_key else None)

    # Choose mode
    print("\nChoose output mode:")
    print("1 - Clinician Report")
    print("2 - Patient Explanation (Hebrew)")
    mode_choice = input("Enter choice [1/2]: ").strip()
    mode = "clinician" if mode_choice == "1" else "patient"

    # Input anamnesis
    anamnesis_lines = []
    print("\nEnter anamnesis text (end input with a blank line):")
    while True:
        line = input()
        if not line.strip():
            break
        anamnesis_lines.append(line)
    anamnesis_text = "\n".join(anamnesis_lines)

    # Process
    print("\nProcessing...\n")
    output = backend.process(anamnesis_text, mode=mode)

    # Output
    print("\n=== Output ===\n")
    print(output)

if __name__ == "__main__":
    main()
