# Errors

<aside class="notice">
These error codes below are expected to be returned by the API whenever the it receives a bad requests, unauthorized request, or anything else prevent it to return a valid response.
</aside>

The ExamHut API uses the following error codes:

Error Code | Meaning
---------- | -------
400 | Bad Request -- Your request is invalid.
401 | Unauthorized -- Your API key is wrong (For login, this means your username or password is wrong).
403 | Forbidden -- You are not allowed to access this resource.
404 | Not Found -- The resource you are trying to access does not exist.
405 | Method Not Allowed -- The method you are trying to use is not allowed for this resource.
