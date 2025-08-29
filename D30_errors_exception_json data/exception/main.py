try:
    file=open("data.txt")
    a_dictionary={"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file=open("data.txt","w")
    file.write("something")
except KeyError as e:
    print(f"Key {e} doesn't exist")
else:
    # won't execute if exception exists
    content=file.read()
    print(content)
finally:
    file.close()
    # raise an erro
    # raise ValueError("key: ss is not existing in a_dictionary")