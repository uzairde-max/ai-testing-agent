import json
from modules import api_tester, data_analyzer, ui_tester, security_analyzer

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    config = load_config()

    if config.get("api_testing"):
        api_tester.run_tests(config["api_testing"])

    if config.get("data_analysis"):
        data_analyzer.analyze_data(config["data_analysis"])

    if config.get("ui_testing"):
        ui_tester.run_ui_tests(config["ui_testing"])

    if config.get("security_analysis"):
        security_analyzer.run_security_scan(config["security_analysis"])

if __name__ == "__main__":
    main()
