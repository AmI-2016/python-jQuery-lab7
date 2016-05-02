REST Server for Tasks
======================

A simple REST server for introducing REST and Flask in Python. It can be run from the command line by typing:

``` python task_server.py ```
or
```./task_server.py ```

It provides basic support for showing and creating tasks.

### API
-------

**Resource:** tasks

**Url:** /api/v1.0/tasks

**Description:** The tasks currently available on the server, without paging

**Method:** GET - Retrieve the list of available tasks

**Example Response:**

```
{
  "tasks": [
    {
      "description": "call Giovanni for AmI project organization",
      "id": 22,
      "urgent": 1
    },
    {
      "description": "buy a new mouse",
      "id": 23,
      "urgent": 1
    },
    {
      "description": "find a present for Angelina's birthday",
      "id": 24,
      "urgent": 0
    },
    {
      "description": "organize mega party (last week of April)",
      "id": 25,
      "urgent": 0
    },
...
}
```

**Method:** POST - Create a new task

**Parameters**: description, urgent

**Example**:

```
{
	"description" : "This is a new task",
	"urgent" : 0
}
```


**Url:** /api/v1.0/tasks/:task_id

**Method:** GET - Retrieve the task identified by the given *task_id* (an integer number)

**Example Response:**

```
{
  "task": {
    "description": "call Giovanni for AmI project organization",
    "id": 22,
    "urgent": 1
  }
}
```


**Url:** /api/v1.0/tasks/:task_id

**Method:** PUT - Update a task

**Parameters**: description, urgent

**Example**:

```
{
	"description" : "This is an updated task",
	"urgent" : 0
}
```

**Url:** /api/v1.0/tasks/:task_id

**Method:** DELETE - Delete a task
