# Dakoda Core

A Python library for [DAKODA](https://dakoda.org/) corpus management.

DAKODA is an interdisciplinary project with the overarching goal of advancing the data competencies of early-career researchers in German as a Foreign/Second Language (DaF/DaZ) in the field of learner corpus research. The project develops language technology resources for acquisition-related research questions and tests them based on a broad data foundation.

## Prerequisites

- **Python 3.11+** (recommended via [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#a-getting-pyenv))
- **Poetry** for dependency management (see [installation](https://python-poetry.org/docs/#installing-with-the-official-installer) guide)

## Setup

1. Clone the repository

    ```bash
    git clone git@github.com:dakoda-project/dakoda-core.git
    cd dakoda-core
   ```
    
2. Install dependencies and create virtual environment

    ```bash
    poetry install
    ```
   
3. Verify installation
    
    ```bash
    poetry run python -c "from dakoda import *; print('Dakoda Core installed successfully!')"
    ```

## Development

### Project Structure

```
dakoda-core/
├── src/
│   └── dakoda/           
│       ├── corpus.py     
│       ├── countries.py  
│       ├── languages.py  
│       ├── dakoda_types.py          
│       ├── dakoda_metadata_scheme.py 
│       ├── util.py      
│       └── res/          
│           ├── dakoda-logo.png
│           └── dakoda_typesystem.xml
├── tests/                
└── data/                 
```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=dakoda
```



## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `poetry run pytest`
5. Submit a pull request
