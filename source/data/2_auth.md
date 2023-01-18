# Authentication

ExamHut API use [JWT](https://jwt.io/) for authentication. To get a token, you need to send a `POST` request to the login endpoint with your credentials, which will be described in the next section.

## Login

> To login, use this code:

```shell
curl "https://example.com/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "$USERNAME",
    "password": "$PASSWORD"
  }'
```

> The above command return JSON contains the access token and the refresh token:

```json
{
  "access_token": "ACCESS_TOKEN_HERE",
  "refresh_token": "REFRESH_TOKEN_HERE"
}
```

Login requires a username and a password. By sending a `POST` request to the login endpoint with your credentials, you will receive a access token AND a refresh token (you can read about them [here](https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/)).

### HTTP Request

`POST http://example.com/login`

### Request Body

Name | Type | Description
---- | ---- | -----------
username | string | Your username
password | string | Your password

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the access token and the refresh token
400 | The request is invalid
401 | The provided credentials are invalid


## Access Token

> To authorize, use this code:

```shell
curl "api_endpoint_here" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

You can use your access token to authorize your requests. The lifespan is really short, so you should make sure to refresh it regularly with the refresh token, which will be described in the next section.

## Refresh Token

> To refresh your access token, use this code:

```shell
```

> This will return JSON contains the new access token:

```json
{
  "access_token": "NEW_ACCESS_TOKEN_HERE"
}
```

As the access token is short-lived, it should be refreshed regularly (or at least right after you receive a forbidden response). The refresh token is long-lived, so make sure to store it in a safe place.

### HTTP Request

`GET http://example.com/token/refresh`

## Logout

> To logout, use this code:

```shell
curl -X "DELETE" "http://example.com/logout" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return a 204 No Content response.

By sending a `DELETE` request to the logout endpoint, you will logout your account. This means that your refresh token is invalidated and removed from the database, and you will no longer be able to refresh your access token.

### HTTP Request

`DELETE http://example.com/logout`
