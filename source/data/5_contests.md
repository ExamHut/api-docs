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