# 12-Factor App Compliance

This document outlines how the Python Product Service complies with the first four factors of the 12-Factor App methodology.

## Factor I: Codebase
**One codebase tracked in revision control, many deploys**

✅ **Compliant**
- Single codebase managed in Git
- All application code is in the repository
- Multiple environments (development, staging, production) deploy from the same codebase
- No environment-specific code in the repository

## Factor II: Dependencies
**Explicitly declare and isolate dependencies**

✅ **Compliant**
- Dependencies are explicitly declared in `requirements.txt`
- All Python packages and their versions are specified
- No implicit dependencies on system packages
- Virtual environment isolation (recommended for local development)

**Dependencies:**
```
Flask==2.3.3
Flask-CORS==4.0.0
python-dotenv==1.0.0
gunicorn==21.2.0
```

## Factor III: Config
**Store config in the environment**

✅ **Compliant**
- Configuration is stored in environment variables
- No hardcoded configuration values
- Environment-specific settings are externalized
- Default values provided for local development

**Environment Variables:**
- `PORT`: Port number for the service (default: 3030)
- `FLASK_DEBUG`: Debug mode flag (default: False)
- `ENVIRONMENT`: Environment name (development, staging, production)

**Implementation:**
```python
# Get port from environment variable or default to 3030
port = int(os.environ.get('PORT', 3030))

# Debug mode from environment
debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
```

## Factor IV: Backing Services
**Treat backing services as attached resources**

✅ **Compliant**
- The service is stateless and doesn't rely on local storage
- No backing services currently required (simple product catalog)
- Ready to attach backing services (database, cache, etc.) via environment variables
- Service can be easily moved between environments

**Future Backing Services:**
- Database connection strings via environment variables
- Cache service URLs via environment variables
- External API endpoints via environment variables

## Additional Compliance Considerations

### Statelessness
- No session state stored in the application
- Each request is independent
- Horizontal scaling ready

### Port Binding
- Service binds to port specified by PORT environment variable
- Azure App Service automatically sets the PORT variable
- No hardcoded port numbers

### Concurrency
- Flask development server for local development
- Gunicorn WSGI server for production deployment
- Ready for horizontal scaling

### Disposability
- Fast startup and shutdown
- Graceful handling of shutdown signals
- No data loss on restart

## Environment-Specific Configuration

### Development
```bash
PORT=3030
FLASK_DEBUG=True
ENVIRONMENT=development
```

### Production (Azure App Service)
```bash
PORT=8000  # Set by Azure
FLASK_DEBUG=False
ENVIRONMENT=production
```

## Benefits of 12-Factor Compliance

1. **Deployability**: Easy deployment to any environment
2. **Scalability**: Horizontal scaling capability
3. **Maintainability**: Clear separation of concerns
4. **Portability**: Runs anywhere Python is supported
5. **Reliability**: Stateless and disposable design
