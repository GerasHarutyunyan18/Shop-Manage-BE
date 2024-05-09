def signUpValidation(data):
    fields = ['name', 'surname', 'birthDate', 'email', 'password']
    errors = []
    result = {}

    for field in fields:
        value = data.get(field)

        if not value:
            errors.append(f'`{field}` is required.')
            continue

        result[field] = value

    return {"errors": errors, "result": result, "status": 403 if len(errors) > 0 else 200}


def marketCreationValidation(data):
    fields = ['name', 'address', 'workingTimeStart', 'workingTimeEnd', 'ownerToken']
    errors = []
    result = {}

    for field in fields:
        value = data.get(field)

        if not value:
            errors.append(f'`{field}` is required.')
            continue

        result[field] = value

    return {"errors": errors, "result": result, "status": 403 if len(errors) > 0 else 200}


def userCreationValidation(data):
    fields = ['name', 'surname', 'email', 'birthDate', 'creatorToken']
    errors = []
    result = {}

    for field in fields:
        value = data.get(field)

        if not value:
            errors.append(f'`{field}` is required.')
            continue

        result[field] = value

    return {"errors": errors, "result": result, "status": 403 if len(errors) > 0 else 200}

    