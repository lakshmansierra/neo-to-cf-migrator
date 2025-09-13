# neo-to-cf-migrator

## project structure
```
neo-to-cf-migrator/
│── app/
│   ├── api/                # FastAPI routes
│   │   ├── __init__.py
│   │   ├── git_routes.py   # endpoint: provide Git URL, clone repo
│   │   ├── migrate_routes.py # endpoint: start migration
│   │
│   ├── services/
│   │   ├── git_service.py  # logic to clone/pull from Git
│   │   ├── migration_service.py # call LangChain agent here
│   │
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── migration_agent.py  # LangChain agent logic for code conversion
│   │   ├── prompts/            # store reusable system prompts/templates
│   │
│   ├── main.py            # FastAPI app entrypoint
│   ├── config.py          # env vars (Git creds, CF/Neo mappings etc.)
│
├── tests/                 # unit + integration tests
│
├── requirements.txt
├── README.md
```