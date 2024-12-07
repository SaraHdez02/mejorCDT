# Mejor CDT API

This project provides a FastAPI-based service for calculating financial metrics such as return on investment (ROI) and expired rates for bank investments.

## Project Overview
A Python-based financial investment rate calculation system using FastAPI, focusing on bank investment rates and returns.

## Key Modifications and Implementations

### Code Structure Refactoring
- Translated entire codebase from Spanish to English
- Removed redundant routers and consolidated functionality
- Updated naming conventions across files
- Simplified project structure

### Services Implemented
1. **Calculadora Service**:
   - `calculate_expired_rate()`: Calculates expired rates for banks
   - `calculate_roi()`: Computes return on investment
   - `find_rates()`: Retrieves effective annual rates

2. **Data Processing**
   - Enhanced CSV file handling
   - Implemented robust filtering for investment amounts and terms
   - Added type checking and error handling

### Testing
- Created comprehensive test suite using pytest
- Added tests for:
  - ROI calculation
  - Expired rate calculation
  - Rate finding functionality
- Implemented dynamic file path resolution for cross-machine compatibility

### API Endpoints
- `/rates`: Returns bank interest rates
- `/expired-rate`: Calculates expired period rates
- `/roi`: Computes return on investment

## Technical Decisions
- Used FastAPI for web framework
- Pandas for data manipulation
- Modular service-based architecture
- Relative path handling for file references

## Dependencies
- Python 3.x
- FastAPI
- Pandas
- Pytest

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd mejorCDT
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the FastAPI Server**

   Navigate to the project root and run:

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## Running Tests

To run the tests, use `pytest`:

```bash
pytest app/tests
```

## Project Structure
```
mejorCDT/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── gestion_datos.py
│   ├── services/
│   │   └── calculadora_service.py
│   ├── tests/
│   │   └── test_calculadora.py
│   └── utils/
│       └── file_utils.py
│
└── data/
    └── bank_rates.csv
```

## Unresolved Items / Potential Improvements
- Add more comprehensive error handling
- Implement logging
- Create more granular filtering options
- Add authentication for financial calculations

## Security Considerations
- Basic input validation implemented
- Recommend adding more robust authentication
- Validate and sanitize all input data

## Development Environment
- Location: `/home/sarahdez02/Documents/Test Mejor CDT/mejorCDT/`
- Primary development focus: Financial rate calculations and API services

## Special Notes
- Emphasis on English-language naming
- Type hinting used throughout
- Docstrings for all functions
- Modular design with separation of concerns

## Next Steps
1. Enhance error handling
2. Add more comprehensive testing
3. Implement logging mechanisms
4. Consider adding caching for rate calculations

## Notes
- Ensure the `data/bank_rates.csv` file is present in the `data` directory for the application to function correctly.
- Modify the paths in the test files if the directory structure changes.
