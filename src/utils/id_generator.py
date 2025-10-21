def generate_unique_id(department_id: str, existing_ids: list[str]) -> str:
    """
    Generates a new unique employee ID based on the department ID and a list of existing IDs.
    For example, if the department is 'SAL' and the highest existing ID is 'SAL0009',
    this function will return 'SAL0010'.
    """
    if not department_id:
        raise ValueError("Department ID cannot be empty.")

    prefix = department_id.upper()
    
    # Filter IDs for the given prefix and extract the numeric part
    relevant_ids = [eid for eid in existing_ids if eid.startswith(prefix)]
    
    max_num = 0
    if relevant_ids:
        numeric_parts = []
        for eid in relevant_ids:
            try:
                # Extract the number part of the ID
                num_str = eid[len(prefix):]
                if num_str:
                    numeric_parts.append(int(num_str))
            except (ValueError, IndexError):
                # Ignore IDs that do not have a valid numeric part
                continue
        
        if numeric_parts:
            max_num = max(numeric_parts)

    new_num = max_num + 1
    
    # Format the new ID with leading zeros to a total length of 4 for the numeric part
    return f"{prefix}{new_num:04d}"
