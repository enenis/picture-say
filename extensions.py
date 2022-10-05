# Get input from user
file=input("File name: ").strip()
new_file=file.lower()
# If png,gif,jpg or jpeg, print "image/type"
if ".gif" in new_file:
    print("image/gif")
elif ".png" in new_file:
    print("image/png")
elif ".jpeg" in new_file:
    print("image/jpeg")
elif ".jpg" in new_file:
    print("image/jpeg")
# If pdf or zip, print "application/type"
elif ".pdf"in new_file:
    print("application/pdf")
elif ".zip" in new_file:
    print("application/zip")
# If txt,print "text/plain"
elif ".txt"in new_file:
    print ("text/plain")
elif "myfile"in new_file:
    print("application/octet-stream")
elif ".bin"in new_file:
    print("application/octet-stream")
# Otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")
