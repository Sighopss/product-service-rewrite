# Azure App Service Deployment Guide

This guide explains how to deploy the Python Product Service to Azure App Service.

## Prerequisites

- Azure subscription
- Azure CLI installed and configured
- Git repository with the code

## Deployment Steps

### 1. Create Azure App Service

```bash
# Create a resource group
az group create --name product-service-rg --location eastus

# Create an App Service plan
az appservice plan create --name product-service-plan --resource-group product-service-rg --sku B1 --is-linux

# Create the web app
az webapp create --resource-group product-service-rg --plan product-service-plan --name your-product-service --runtime "PYTHON|3.9"
```

### 2. Configure Application Settings

```bash
# Set environment variables
az webapp config appsettings set --resource-group product-service-rg --name your-product-service --settings PORT=8000
az webapp config appsettings set --resource-group product-service-rg --name your-product-service --settings FLASK_DEBUG=False
az webapp config appsettings set --resource-group product-service-rg --name your-product-service --settings ENVIRONMENT=production
```

### 3. Deploy the Application

#### Option A: Using Azure CLI
```bash
# Deploy from local directory
az webapp deployment source config-zip --resource-group product-service-rg --name your-product-service --src deployment.zip
```

#### Option B: Using Git
```bash
# Configure local git deployment
az webapp deployment source config --resource-group product-service-rg --name your-product-service --repo-url https://github.com/yourusername/product-service --branch main --manual-integration

# Deploy
git add .
git commit -m "Deploy to Azure"
git push azure main
```

#### Option C: Using Visual Studio Code
1. Install the Azure App Service extension
2. Right-click on the project folder
3. Select "Deploy to Web App"
4. Choose your Azure subscription and App Service

### 4. Verify Deployment

After deployment, test the endpoints:

```bash
# Test products endpoint
curl https://your-product-service.azurewebsites.net/products

# Test health endpoint
curl https://your-product-service.azurewebsites.net/health
```

## Configuration Files

The following files are included for Azure App Service deployment:

- `web.config`: IIS configuration for Windows-based App Service
- `startup.py`: Entry point for the application
- `requirements.txt`: Python dependencies

## Environment Variables

The application uses the following environment variables:

- `PORT`: Port number (Azure sets this automatically)
- `FLASK_DEBUG`: Debug mode (set to False in production)
- `ENVIRONMENT`: Environment name

## Monitoring and Logs

```bash
# View application logs
az webapp log tail --resource-group product-service-rg --name your-product-service

# Download logs
az webapp log download --resource-group product-service-rg --name your-product-service
```

## Troubleshooting

### Common Issues

1. **Module not found errors**: Ensure all dependencies are in `requirements.txt`
2. **Port binding issues**: Azure sets the PORT environment variable automatically
3. **CORS issues**: The application is configured to allow all origins

### Health Check

The application includes a health check endpoint at `/health` that returns:
```json
{"status": "healthy", "service": "product-service"}
```

## Scaling

```bash
# Scale up the App Service plan
az appservice plan update --name product-service-plan --resource-group product-service-rg --sku P1V2

# Scale out (add instances)
az webapp scale --resource-group product-service-rg --name your-product-service --instance-count 3
```
