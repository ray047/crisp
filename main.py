# main.py

import argparse
import subprocess
import sys

def run_simulation(attack_type):
    attack_map = {
        'phishing': 'attacks/phishing.py',
        'ransomware': 'attacks/ransomware.py',
        'data_breach': 'attacks/data_breach.py',
        'ddos': 'attacks/ddos.py',
        'insider_threat': 'attacks/insider_threat.py',
        'zero_day': 'attacks/zero_day.py',
        'social_engineering': 'attacks/social_engineering.py',
        'sql_injection': 'attacks/sql_injection.py',
        'malware_outbreak': 'attacks/malware_outbreak.py',
        'mitm': 'attacks/mitm.py',
    }

    script = attack_map.get(attack_type)
    if script:
        try:
            subprocess.run(['python3', script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {attack_type} attack simulation: {e}", file=sys.stderr)
    else:
        print("Unknown attack type. Please choose from:", ", ".join(attack_map.keys()), file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="CRISP Attack Simulation Tool")
    parser.add_argument('attack', type=str, help='Specify the type of attack to simulate')
    args = parser.parse_args()

    run_simulation(args.attack)

if __name__ == "__main__":
    main()
