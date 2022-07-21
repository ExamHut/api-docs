---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell
  - javascript

toc_footers:

includes:
  - errors

search: true

code_clipboard: true

meta:
  - name: description
    content: Documentation for the ExamHut API
---

# Introduction

Welcome to the ExamHut API Documentation!

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
  "email": "johndoe@example.com",
  "created_at": "CREATED_AT_HERE",
  "updated_at": "UPDATED_AT_HERE"
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

# Problems

## Get problem information

> To get problem information, use this code:

```shell
curl "https://example.com/problem/{problemId}" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return JSON contains the problem information like the example below:

```json
{
  "id": "1",
  "title": "Problem John Doe",
  "description": "This is the description of problem 1",
  "statementFile": "https://example.com/problem/1/statement",
  "created_at": "CREATED_AT_HERE",
  "updated_at": "UPDATED_AT_HERE"
}
```

### HTTP Request

`GET http://example.com/problem/{problemId}`

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the problem information
401 | The request is unauthorized
403 | The request is forbidden
404 | The problem is not found

## Get submission information

> To get submission information, use this code:

```shell
curl "https://example.com/submission/{submissionId}" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return JSON contains the submission information like the example below:

```json
{
  "id": "1",
  "problemId": "1",
  "userId": "1",
  "language": "CPP",
  "source": "SOURCE_HERE",
  "status": "ACCEPTED",
  "created_at": "CREATED_AT_HERE",
  "updated_at": "UPDATED_AT_HERE"
}
```

By sending a `GET` request to the submission endpoint, you will get the submission information.

For submissions with file-type source, the source will be a link to the file.

### HTTP Request

`GET http://example.com/submission/{submissionId}`

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the submission information
401 | The request is unauthorized
403 | The request is forbidden
404 | The submission is not found

## Get all submission of a problem

> To get all submission of a problem, use this code:

```shell
curl "https://example.com/problem/{problemId}/submissions" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return JSON contains the submission information like the example below:

```json
[
  {
    "id": "1",
    "problemId": "1",
    "userId": "1",
    "language": "CPP",
    "source": "SOURCE_HERE",
    "status": "ACCEPTED",
    "created_at": "CREATED_AT_HERE",
    "updated_at": "UPDATED_AT_HERE"
  },
  {
    "id": "2",
    "problemId": "1",
    "userId": "1",
    "language": "CPP",
    "source": "SOURCE_HERE",
    "status": "ACCEPTED",
    "created_at": "CREATED_AT_HERE",
    "updated_at": "UPDATED_AT_HERE"
  }
]
```

By sending a `GET` request to the problem/{problemId}/submissions endpoint, you will get a submission list of the problem. This is the same as running [#getSubmissionInformation](#getSubmissionInformation) for each submission.

### HTTP Request

`GET http://example.com/problem/{problemId}/submissions`

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the submission list
401 | The request is unauthorized
403 | The request is forbidden
404 | The problem is not found

## Submit a solution

> To submit a solution, use this code:

```shell
curl -X "POST" "https://example.com/submission" \
  -H "Authorization: Bearer $YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "problemId": "1",
    "language": "CPP",
    "source": "SOURCE_HERE"
  }'
```

> The above command will return a no content response.

### HTTP Request

`POST http://example.com/problem/{problemId}/submit`

### Expected Response

Code | Description
---- | -----------
201 | OK. Return the submission information
401 | The request is unauthorized
403 | The request is forbidden
404 | The problem is not found

## Download submission source

> To download submission source, use this code:

```shell
curl "https://example.com/submission/{submissionId}/source" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return JSON contains the submission source like the example below:

```json
{
  "source": "SOURCE_HERE"
}
```

By sending a `GET` request to the submission/{submissionId}/source endpoint, you will get the submission source.

### HTTP Request

`GET http://example.com/submission/{submissionId}/source`

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the submission source
401 | The request is unauthorized
403 | The request is forbidden
404 | The submission is not found
