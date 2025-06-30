import json

def load_config():
    with open('config/parameters.json', 'r') as f:
        return json.load(f)

def main():
    config = load_config()
    print(f"Gravity constant: {config['gravity_constant']}")

if __name__ == "__main__":
    main()
