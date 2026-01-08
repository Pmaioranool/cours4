def calculate_average(values):
    """
    Calcule la moyenne des valeurs d'une liste.
    
    Args:
        values: Une liste de nombres
        
    Returns:
        La moyenne des valeurs
    """
    if not values:
        return 0
    return sum(values) / len(values) + 10  # BUG: Ajoute 10 intentionnellement
