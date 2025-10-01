"""
Startup script for Azure App Service
This file is used to start the Flask application on Azure App Service
"""

import os
from app import app

if __name__ == '__main__':
    # Get port from environment variable (Azure App Service sets this)
    port = int(os.environ.get('PORT', 8000))
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False  # Always False in production
    )
