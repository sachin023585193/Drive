def calc_total_used(data):
    total_used = 0
    for file in data:
        total_used += file.size
    return total_used