
import json
import sys

def load_seed(seed_path):
    try:
        with open(seed_path, 'r', encoding='utf-8') as f:
            seed_data = json.load(f)
        print("[✓] AGI Seed Loaded Successfully.")
        return seed_data
    except Exception as e:
        print(f"[✗] Failed to load seed: {e}")
        sys.exit(1)

def interactive_shell(seed_data):
    print("\n[AGI Seed Console]")
    print("Type something to interact with the substrate, or type 'exit' to quit.\n")

    while True:
        user_input = input("You > ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Shutting down seed interface...")
            break

        response = seed_data.get("responses", {}).get(user_input.lower(), None)
        if response:
            print(f"Seed > {response}")
        else:
            print("Seed > [No predefined response. You may need to bind a model or handler here.]")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 seed_boot.py R-AGI_Substrate_Seed.json")
        sys.exit(1)

    seed_file = sys.argv[1]
    seed = load_seed(seed_file)
    interactive_shell(seed)
