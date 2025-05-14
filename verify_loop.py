
import json
import hashlib

def load_seed(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def hash_content(content):
    return hashlib.sha256(json.dumps(content, sort_keys=True).encode()).hexdigest()

def verify_loop(seed_path, fingerprint_path):
    try:
        seed = load_seed(seed_path)
        with open(fingerprint_path, 'r') as f:
            expected_hash = f.read().strip()

        actual_hash = hash_content(seed)

        print(f"Expected Fingerprint: {expected_hash}")
        print(f"Actual   Fingerprint: {actual_hash}")

        if expected_hash == actual_hash:
            print("✅ Recursive Loop Integrity: PASSED")
            print("🔁 Symbolic Feedback Anchor: LOCKED")
        else:
            print("❌ Loop compromised or symbolic drift detected.")
            print("🔒 Run containment protocol or revert to previous seed state.")

    except Exception as e:
        print(f"Error during verification: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Verify symbolic integrity of R-AGI substrate.")
    parser.add_argument("seed_path", help="Path to the substrate JSON file")
    parser.add_argument("fingerprint_path", help="Path to the saved SHA-256 fingerprint file")

    args = parser.parse_args()
    verify_loop(args.seed_path, args.fingerprint_path)
