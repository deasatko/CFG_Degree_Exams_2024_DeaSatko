# Foundation Exam 2024 (Theorical Questions)

## 1.1 Explain the difference between a primary key and a foreign key. [2 marks]

- The `primary key` identifies in an unique way each entry of a table.
- The `foreign key` is used to link items to a primary key in another table; it requires a reference which allows the foreign key to be consistent throughout the SQL code.

## 1.2 What is the role of the `finally` block in Python exception handling and how would you use it. [2 marks]

The **finally** keyword does run the code no matter what the outcome of the exception so that it can do resource cleanup, for example:

```python
try:
    # normal code
except Exception:
    # this will handle the exeption
finally:
    # code that gets executed no matter what
```

## 1.3 Explain the difference between a commit and a push in Git. [2 marks]

The `git commit` is a command that saves the changes locally, but then it is used the `git push` to send it to a remote repository.

## 1.4 Provide examples of two web APIs and describe their functionalities. [4 marks]

**Pokémon API**: provides detailed information about Pokémon. With all these calls that can be made to the API, we can then create our own application which could use GET and POST.

**Star Wars API**: similarly to the Pokémon API, it offers access to Star Wars universe data.

In general, an API allows applications to communicate with each other. It defines methods for requesting and exchanging information.

## 1.5 Describe four tasks in the role of the Product Owner in Agile development. [4 marks]

The product owner is a role within Agile and four responsabilities that he has are the following:

**Sprint Planning**: this part of the scrum framework, usually done at the beginning of a sprint and it facilitates the plan of the work that needs to be happening during the sprint itself.

**Sprint Review**: in this part, the product owner, the scrum master, the dev team and anyone interested in the current project, attend to review the work that has been done requesting for feedback.

**Sprint Retrospective**: this step is used to reflect and collaborate to find ways to improve the process.

**Backlog Refinement**: this part is added to dive in depth and review the tickets in order to lead the focus and ensure efficiency.


## 1.6 Name two types of SQL joins and provide an example scenario for each. [4 marks]

**inner join**: when two rows have matching values, it combines them.
*Example*: Retrieve customers who have placed orders by matching `customer_id` in the customer table with `customer_id` in the order table.

**left join**: it technically returns matches rows from the left to the right tables and all the rest of the rows from left to right.  
*Example*: List all customers and their orders, it will also show customers that did not place an order, by joining customer table with order table on `customer_id`.


## 1.7 Explain the difference between mutable and immutable data types in Python, provide an example of each. [4 marks]


`mutable` data types can be changed even after creating them. For example, when creating a list, you can still update the list itself without mapping over it, basically changing the object.

`this_list = [a, b, c]`

`immutable` data types in are data that cannot be changed after creation and they are usually used in functional programming.

In python an a `tuple` is immutable as we cannot append or update anything in the

`this_tuple = (a, b, c)`

## 1.8 Explain both Agile and Waterfall approaches to Software Development, and at least 2 differences between them. [4 marks]

Between `Agile` and `Waterfall` there are differences in how the team approaches and plans the delivery of the product. One main difference is that in `Agile` the team does adapt constantly on the changes, while in `Waterfall` the team must follow a fixed plan. Another difference is that in `Waterfall` the team just delivers a complete product while in `Agile` the team does that incrementally through all the weekly cerimonies and principally through sprints that last two weeks each.