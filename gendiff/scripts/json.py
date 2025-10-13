
def format_changed_data(before_change, after_change):
    result = {}
    for k in before_change:
        result[k] = [before_change[k], after_change[k]]
    return result


def json_formatter(same_data, 
                   removed_data, 
                   added_data, 
                   before_change, 
                   after_change):
    changed_data_formatted = format_changed_data(before_change, after_change)
    result = {
        "removed": removed_data,
        "added": added_data,
        "changed": changed_data_formatted,
        #"same": same_data
    }
    return result