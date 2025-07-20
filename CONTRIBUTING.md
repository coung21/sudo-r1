# 📘 CONTRIBUTING GUIDE

To ensure consistency, reproducibility, and collaboration efficiency, please follow the guidelines below.

---

## ✅ Commit Guidelines

We use [Conventional Commits](https://www.conventionalcommits.org/) with some research-specific extensions.

### 📌 Commit Format

```
<type>(<scope>): <short description>
```

### ✅ Recommended Commit Types

| Type         | Purpose                                                               |
| ------------ | --------------------------------------------------------------------- |
| **feat**     | Introduce new functionality or experimental methods/models            |
| **fix**      | Fix bugs in training loops, evaluation scripts, data handling, etc.   |
| **data**     | Add or modify datasets, preprocessing scripts, or data configs        |
| **exp**      | Log new experiment configurations or results                          |
| **test**     | Add/update unit tests, integration tests, or experiment validations   |
| **refactor** | Improve code structure or readability without changing core behavior  |
| **docs**     | Update documentation, README, or usage guides                         |
| **chore**    | Routine tasks like updating requirements, CI/CD changes, or cleanups  |
| **style**    | Code formatting, linting, no logic changes                            |
| **log**      | Add or improve logging/debug outputs                                  |
| **viz**      | Add/update visualization utilities (e.g., plots, TensorBoard configs) |
| **config**   | Change to YAML/JSON/Hydra configs for experiments or models           |

### 🔍 Examples

```bash
feat(model): add attention mask support to decoder
fix(eval): correct BLEU score calculation logic
data: add cleaned WMT14-en-de dataset
exp(config): update batch size and optimizer for run 42
test(trainer): add regression test for KL divergence behavior
refactor(utils): split tokenizer helpers into separate file
log(trainer): improve reward debugging info
viz: add training loss heatmap visualization
```

Use `cz commit` (Commitizen) to enforce format.

---

## 🔃 Pull Request (PR) Workflow

### 📋 PR Checklist

* [ ] Clear and descriptive title (e.g., `[fix]`, `[feat]`, etc.)
* [ ] Linked to relevant issue (e.g., `Closes #42`)
* [ ] Contains only one logical change
* [ ] Code passes tests and linting
* [ ] Updated documentation if needed
* [ ] At least one reviewer approved

### 📄 PR Description Template

```
## 📌 Summary
Brief overview of what this PR does.

## ✅ Checklist
- [ ] Tests added or updated
- [ ] CI/CD passes
- [ ] Linked issues closed

## 📎 Related Issues
Closes #...
```

### ✅ Merging Rules

* Use **Squash and Merge** only
* CI must pass
* One approval required

---

## 🔍 Pre-commit Hooks

Pre-commit hooks ensure code consistency before committing.

### Setup

```bash
pip install pre-commit
pre-commit install
```

### Hooks Used

* `black` (code formatter)
* `isort` (import sorter)
* `flake8` (optional linting)
* `trailing-whitespace`, `end-of-file-fixer`

Run manually:

```bash
pre-commit run --all-files
```

---

## 🔖 Versioning and Changelog

We use [Commitizen](https://commitizen-tools.github.io/commitizen/) for version management and changelog generation.

### Bump version

```bash
cz bump
```

### Generate changelog

```bash
cz changelog
```

Changelog is stored in `CHANGELOG.md`

---

## 🧪 Testing Standards

* Use `pytest` for writing and running tests
* Organize tests under `tests/`
* Ensure key functionality is covered by automated tests

Run tests:

```bash
pytest tests/
```

---

## 📁 Recommended Project Structure

```bash
project-root/
├── src/                    # Core logic
├── tests/                  # Tests
├── configs/                # Hydra or YAML config files
├── commands                # bash scripts
├── scripts/                # Python scripts
├── notebooks/              # Debugging or exploratory notebooks
├── .github/workflows/      # CI/CD configuration
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── CONTRIBUTING.md
└── CHANGELOG.md
```

---

## 🧠 Best Practices

* Keep datasets and model weights out of Git (use DVC or external storage)
* Document all experiments and configurations
* Ensure experiments are reproducible (e.g., fixed seeds, saved configs)
* Use `wandb` for experiment tracking

---

## 🙏 Thank You

By following this guide, you help build a sustainable and collaborative research environment. If you have questions, open an issue or start a discussion.
