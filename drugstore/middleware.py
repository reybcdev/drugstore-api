class CorsMiddleware:
    """
    Middleware for handling Cross-Origin Resource Sharing (CORS) headers.
    Adds appropriate CORS headers to responses to enable cross-origin requests.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called
        response = self.get_response(request)
        
        # Add CORS headers to the response
        response["Access-Control-Allow-Origin"] = "http://localhost:5173"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Allow-Credentials"] = "true"
        
        # Handle preflight requests
        if request.method == "OPTIONS":
            response["Access-Control-Max-Age"] = "86400"  # 24 hours in seconds
            
        return response
