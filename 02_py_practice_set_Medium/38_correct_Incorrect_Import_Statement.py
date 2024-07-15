def correct_Incorrect_Import_Statement(statement):
    if isinstance(statement, str):
        words = statement.split()
        module = None
        object_ = None
        for idx, word in enumerate(words):
            if word.lower() == 'from':
                module = words[idx + 1]
            elif word.lower() == 'import':
                object_ = words[idx + 1]
        if module and object_:
            return f"from {module} import {object_}"
        else:
            return "Invalid import statement format. Please use 'import object from module_name'"
    else:
        return "Statement should be in string format. Please correct the format."

result = correct_Incorrect_Import_Statement("import randint from random")
print(result)
