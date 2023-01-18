
# User

## Get user information

> To get user information, use this code:

```shell
curl "https://example.com/user" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return JSON contains the user information like the example below:

```json
{
  "id": "1",
  "username": "john_doe",
  "name": "John Doe",
  "email": "johndoe@example.com",
  "classes": [1, 2, 3] // (TODO)
}
```

By sending a `GET` request to the user endpoint, you will get the user information.

### HTTP Request

`GET http://example.com/user`

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the user information
401 | The request is unauthorized
403 | The request is forbidden
404 | The user is not found

## Get class information (TODO)

> To get class information, use this code:

```shell
curl "https://example.com/class/{class_id}" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return JSON contains the user information like the example below:

```json
{
  "id": "1",
  "code": "sample_class",
  "name": "Sample Class",
  "users": [1, 2, 3] // (TODO)
}
```

By sending a `GET` request to the class endpoint, you will get the class information.

### HTTP Request

`GET http://example.com/class/{class_id}`

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the class information
401 | The request is unauthorized
403 | The request is forbidden
404 | The class is not found
