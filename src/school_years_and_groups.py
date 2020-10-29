def csSchoolYearsAndGroups(years: int, groups: int) -> str:
    # keep `letters` string so that we can grab the letters we need
    letters = "abcdefghijklmnopqrstuvwxyz"
    output = []
    
    # iterate over each year, starting at 1 since years are 1-indexed
    for year in range(1, years + 1):
        # for each group
        for i in range(groups):
            # construct the group string from the year and the letter
            output.append(f"{year}{letters[i]}")
            
    # at this point, we have a list of strings with each string
    # representing a group
    # join them into one comma-separated string
    return ", ".join(output)
    