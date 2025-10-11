def format_removed_data(removed_data):
    result = []
    for k, val in removed_data.items():
        k = str(k).lower()
        result.append(f"Property '{k}' was removed")
    return result


def format_added_data(added_data):
    result = []
    for k, val in added_data.items():
        k = str(k).lower()
        val = str(val).lower()
        result.append(f"Property '{k}' was added with value: {val}")
    return result


def format_changed_data(before_change, after_change):
    result = []
    for k in before_change.keys():
        k = str(k).lower()
        val1 = str(before_change[k]).lower()
        val2 = str(after_change[k]).lower()
        result.append(
            f"""Property '{k}' was updated. From {val1} to {val2}"""
            )
    return result


def plain(same_data, removed_data, added_data, before_change, after_change):

    removed_data_formatted = format_removed_data(removed_data)
    added_data_formatted = format_added_data(added_data)
    changed_data_formatted = format_changed_data(before_change, after_change)

    big_list = (removed_data_formatted +
                added_data_formatted +
                changed_data_formatted)
    
    def sort_key(x):
        key_name = x.split("'")[1]  
        return key_name
    
    sorted_list = sorted(big_list, key=sort_key)
    joined = '\n'.join(sorted_list)
    return joined


