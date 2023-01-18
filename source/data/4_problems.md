
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
