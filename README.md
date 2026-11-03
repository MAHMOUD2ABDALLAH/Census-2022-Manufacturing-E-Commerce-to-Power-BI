# Census 2022 E-Commerce to Power BI

This repository extracts data from the US Census Bureau API (2022 E-Commerce Statistics) and converts it to CSV files for use in Power BI.

## Branches
- `main`: Full project code, outputs, and documentation.
- `01-geography` to `08-data`: Isolated datasets with their own code and CSV outputs.
- `09-powerbi`: The Power BI `.pbix` dashboard file.

## Setup
1. Run `pip install -r requirements.txt`
2. Create a `.env` file with `CENSUS_KEY=your_key_here`
3. Run `python main.py` to fetch all data.

👉 **[View the Power BI Dashboard Branch](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/09-powerbi)**
