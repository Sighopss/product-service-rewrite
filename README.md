# Product Service - Python Flask Application

The Product Service is a simple web service built using Python and the Flask web framework. It is responsible for serving the product catalog, which includes a list of products that can be fetched via a RESTful API.

This service has been rewritten from Rust to Python to ensure compatibility with Azure App Service while maintaining compliance with the 12-Factor App methodology.

## Features

- **12-Factor App Compliant**: Follows the first four factors of the 12-Factor App methodology
- **Azure App Service Ready**: Configured for deployment on Azure App Service
- **CORS Enabled**: Supports cross-origin requests
- **Environment Configuration**: Uses environment variables for configuration
- **Health Check Endpoint**: Includes a health check endpoint for monitoring

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Setup Instructions

### Local Development

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables (optional):**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit .env file with your preferred settings
   # Default values:
   # PORT=3030
   # FLASK_DEBUG=False
   # ENVIRONMENT=development
   ```

3. **Run the service:**
   ```bash
   python app.py
   ```

   The service will be running on `http://localhost:3030` (or the port specified in the PORT environment variable).

### Azure App Service Deployment

1. **Prepare for deployment:**
   - Ensure all files are in the root directory
   - The `web.config` file is configured for Azure App Service
   - The `startup.py` file is the entry point for Azure

2. **Deploy to Azure App Service:**
   - Use Azure CLI, Visual Studio Code Azure extension, or Azure Portal
   - The service will automatically use the PORT environment variable set by Azure

## API Endpoints

### GET /products
Returns a JSON array of product objects.

**Response:**
```json
[
  {"id": 1, "name": "Dog Food", "price": 19.99},
  {"id": 2, "name": "Cat Food", "price": 34.99},
  {"id": 3, "name": "Bird Seeds", "price": 10.99}
]
```

### GET /health
Health check endpoint for monitoring.

**Response:**
```json
{"status": "healthy", "service": "product-service"}
```

## Testing

1. **Using REST Client extension in VS Code:**
   - Use the provided `test-product-service-python.http` file to test the service

2. **Using curl:**
   ```bash
   # Test products endpoint
   curl http://localhost:3030/products
   
   # Test health endpoint
   curl http://localhost:3030/health
   ```

3. **Using PowerShell (Windows):**
   ```powershell
   # Test products endpoint
   Invoke-RestMethod -Uri "http://localhost:3030/products" -Method GET
   
   # Test health endpoint
   Invoke-RestMethod -Uri "http://localhost:3030/health" -Method GET
   ```

## 12-Factor App Compliance

This service complies with the first four factors of the 12-Factor App methodology:

1. **Codebase**: Single codebase tracked in revision control
2. **Dependencies**: Explicitly declared dependencies in `requirements.txt`
3. **Config**: Configuration stored in environment variables
4. **Backing Services**: Treats backing services as attached resources

## Environment Variables

- `PORT`: Port number for the service to run on (default: 3030)
- `FLASK_DEBUG`: Enable Flask debug mode (default: False)
- `ENVIRONMENT`: Environment name (development, staging, production)

## File Structure

```
product-service/
├── app.py                    # Main Flask application
├── startup.py               # Azure App Service entry point
├── requirements.txt         # Python dependencies
├── web.config              # Azure App Service configuration
├── env.example             # Environment variables example
├── test-product-service-python.http  # API tests
└── README.md               # This file
```

## Migration from Rust

This Python service maintains the same API endpoints and functionality as the original Rust service:

- Same `/products` endpoint with identical JSON response
- Same port configuration (3030 default)
- Same CORS configuration
- Added health check endpoint for better monitoring
- Azure App Service compatibility