# Census 2022 E-Commerce to Power BI

This repository extracts data from the US Census Bureau API (2022 E-Commerce Statistics) and converts it to CSV files for use in Power BI.

## Branches
1. **[main](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/main)**: Full project code, outputs, and documentation.
2. **[01-geography](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/01-geography)**: Isolated geography metadata.
3. **[02-variables](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/02-variables)**: Isolated variables and code lists.
4. **[03-tags](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/03-tags)**: Isolated tags metadata.
5. **[04-examples](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/04-examples)**: Isolated examples metadata.
6. **[05-groups](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/05-groups)**: Isolated groups metadata.
7. **[06-sorts](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/06-sorts)**: Isolated sorts metadata.
8. **[07-group-EC2231ECOMM](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/07-group-EC2231ECOMM)**: Isolated specific group metadata.
9. **[08-data](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/08-data)**: The actual 2022 E-Commerce data table.
10. **[09-powerbi](https://github.com/MAHMOUD2ABDALLAH/Census-2022-Manufacturing-E-Commerce-to-Power-BI/tree/09-powerbi)**: The Power BI `.pbix` dashboard file.

## Setup
1. Run `pip install -r requirements.txt`
2. Create a `.env` file with `CENSUS_KEY=your_key_here`
3. Run `python main.py` to fetch all data.
