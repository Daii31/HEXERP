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

## Deploying to Vercel

Vercel looks for serverless functions in the `api` directory. This repository
provides `api/index.py` which simply exports the FastAPI app so it can run as a
serverless function. A minimal `vercel.json` is included to set the function's
runtime options. After pushing the code to a Vercel-connected repository, the
application will be served from `/api` and you should no longer see a 404 page.
