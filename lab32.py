d=[{"v":"s001","v":"s002","vi":"s005","viii":"s005","v":"s009","viii":"s007"}]
print("original list:",d)
unique_value=set(value for dic in d for value in dic.values())
print(unique_value)
