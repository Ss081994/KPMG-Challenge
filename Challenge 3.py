def retrieve_value(obj, key):
    keys = key.split('/')
    for k in keys:
        if k in obj:
            obj = obj[k]
        else:
            return None
    return obj

# Example usage:
object = {"a":{"b":{"c":"d"}}}
key = "a/b/c"
print(retrieve_value(object, key)) # Output: "d"

object = {"x":{"y":{"z":"a"}}}
key = "x/y/z"
print(retrieve_value(object, key)) # Output: "a"



#This code defines a function retrieve_value that takes an object and a key as arguments. 
#The key is split into a list of keys using the split method, and then each key is used to access the nested object. 
#If a key is not found in the object,the function returns None. If all keys are found, the function returns the final value.
