import os

structure = {
    "stockdb": {
        "__init__.py": "",
        "config": {"__init__.py": "", "settings.py": ""},
        "db": {"__init__.py": "", "schema.sql": "", "connection.py": "", "writers.py": ""},
        "loaders": {"__init__.py": "", "fundamentals.py": "", "technicals.py": "", "analyst.py": "", "market.py": ""},
        "transformers": {"__init__.py": "", "indicators.py": "", "validators.py": ""},
        "pipelines": {"__init__.py": "", "daily_update.py": "", "backfill.py": ""},
        "utils": {"__init__.py": "", "logging.py": "", "helpers.py": ""},
        "tests": {"__init__.py": "", "test_db.py": "", "test_loaders.py": "", "test_indicators.py": ""},
    },
    "scripts": {"init_db.py": "", "run_daily.py": "", "export_csv.py": ""},
    "requirements.txt": "",
    "setup.py": "",
    "README.md": "",
}

def create_structure(base, struct):
    for name, content in struct.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write(content)

create_structure(".", structure)
print("✅ Project scaffold created.")