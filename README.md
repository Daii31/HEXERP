# HEXERP

HEXERP is a modular Enterprise Resource Planning (ERP) platform designed for UK retailers. It provides a SaaS-ready core with plug-and-play modules for features like sales and inventory. Administrators can manage customers and enable modules via a central configuration system.

## Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the development server:
   ```bash
   uvicorn erp.main:app --reload
   ```
