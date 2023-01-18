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
  "code": "john_doe",
  "name": "Problem John Doe",
  "statement_file": "https://example.com/problem/1/statement",
  "time_limit": "1.0",
  "memory_limit": "256"
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
  "problem_id": "1",
  "user_id": "1",
  "language": "CPP",
  "status": "Completed",
  "result": "Accepted",
  "date": "SUBMISSION_DATE_HERE",
  "time": "1.0",
  "memory": "1.0",
  "points": "100.0",
  "current_testcase": "1",
  "error": "ERROR_HERE",
  "case_points": "1",
  "case_total": "1",
  "judged_on": "JUDGE_HERE",
  "judged_date": "JUDGED_DATE_HERE",
  "rejudged_date": "REJUDGED_DATE_HERE",
  "is_pretested": "true"
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
    "problem_id": "1",
    "user_id": "1",
    "language": "CPP",
    "status": "Completed",
    "result": "Accepted",
    "date": "SUBMISSION_DATE_HERE",
    "time": "1.0",
    "memory": "1.0",
    "points": "100.0",
    "current_testcase": "1",
    "error": "ERROR_HERE",
    "case_points": "1",
    "case_total": "1",
    "judged_on": "JUDGE_HERE",
    "judged_date": "JUDGED_DATE_HERE",
    "rejudged_date": "REJUDGED_DATE_HERE",
    "is_pretested": "true"
  },
  {
    "id": "2",
    "problem_id": "2",
    "user_id": "2",
    "language": "PY",
    "status": "Completed",
    "result": "Accepted",
    "date": "SUBMISSION_DATE_HERE",
    "time": "1.0",
    "memory": "1.0",
    "points": "100.0",
    "current_testcase": "1",
    "error": "ERROR_HERE",
    "case_points": "1",
    "case_total": "1",
    "judged_on": "JUDGE_HERE",
    "judged_date": "JUDGED_DATE_HERE",
    "rejudged_date": "REJUDGED_DATE_HERE",
    "is_pretested": "true"
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
    "problem_id": "1",
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

# Contests

## Get contest information (TODO)

> To get contest info, use this code:

```shell
curl "https://example.com/contest/{contestId}" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return JSON contains the contest information like the example below:

```json
{
  "id": "1",
  "code": "example_contest",
  "name": "Example Contest",
  "description": "Example contest description.",
  "startDate": "START_DATE_HERE",
  "endDate": "END_DATE_HERE",
  "duration": "100", // minutes
  "author": "1", // id of author
  "class": "1", // id of class
}
```

By sending a `GET` request to the contest/{contestId} endpoint, you will get the contest information.

### HTTP Request

`GET http://example.com/contest/{contestId}`

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the submission source
401 | The request is unauthorized
403 | The request is forbidden
404 | The submission is not found

## Get contest problems (TODO)

> To get problems of a contest, use this code:

```shell
curl "https://example.com/contest/{contestId}/problems" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return JSON contains the contest problems like the example below:

```json
[
  {
    "id": "1",
    "code": "john_doe",
    "name": "Problem John Doe",
    "statement_file": "https://example.com/problem/1/statement",
    "time_limit": "1.0",
    "memory_limit": "256"
  },
  {
    "id": "2",
    "code": "not_john_doe",
    "name": "Not problem John Doe",
    "statement_file": "https://example.com/problem/2/statement",
    "time_limit": "3.0",
    "memory_limit": "512"
  }
]
```

By sending a `GET` request to the contest/{contestId}/problems endpoint, you will get the contest problems.

### HTTP Request

`GET http://example.com/contest/{contestId}/problems`

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the submission source
401 | The request is unauthorized
403 | The request is forbidden
404 | The submission is not found

## Get contest participants (TODO)

> To get participants of a contest, use this code:

```shell
curl "https://example.com/contest/{contestId}/participants" \
  -H "Authorization: Bearer $YOUR_TOKEN"
```

> The above command will return JSON contains the contest participants like the example below:

```json
[
  {
    "id": "1",
    "username": "john_doe",
    "name": "John Doe"
  },
  {
    "id": "2",
    "username": "not_john_doe",
    "name": "Not John Doe"
  }
]
```

By sending a `GET` request to the contest/{contestId}/participants endpoint, you will get the contest participants.

### HTTP Request

`GET http://example.com/contest/{contestId}/participants`

### Expected Response

Code | Description
---- | -----------
200 | OK. Return the submission source
401 | The request is unauthorized
403 | The request is forbidden
404 | The submission is not found
