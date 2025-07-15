# System File Migration

![ETL Pipeline](https://img.shields.io/badge/process-ETL%20%2F%20ELT-blue)
![Python](https://img.shields.io/badge/python-3.11%2B-green)
![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-orange)

Python project to migrate files stored in MongoDB. This application enables the extraction, optional transformation, and storage of files to a new destination (such as a local directory or another storage system). Useful for backup, data organization, or system integration.

---

### Installation

```bash
# Clone the repository
git clone https://github.com/gabrielmango/system-file-migration.git
cd system-file-migration

# Install dependencies
poetry install

# Activate environment
poetry shell

# Create your .env
cp .env.example .env
```

Then, edit `.env` to set your DB credentials, API keys, and configurations.

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push the branch: `git push origin feature/my-feature`
5. Open a pull request

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---
