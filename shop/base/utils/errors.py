MethodNotAllowed = {"error": "Method not allowed.", "status": 405}
UserExist = {"error": "User with this email already exist.", "status": 409}
UserNotExist = {"error": "User doesn`t exist.", "status": 404}
MarketNotExist = {"error": "Market doesn`t exist.", "status": 404}
InvalidLoginCreds = {"error": "Password is invalid.", "status": 404}
AccessDenied = {"error": "Access denied.", "status": 403}
ArgumentError = lambda arguments: {"error": f"Not all arguments passed({", ".join(arguments)}).", "status": 403}
