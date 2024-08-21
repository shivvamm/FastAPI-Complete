Alembic commands
To create a revision :
alembic revision -m "Create phone number for user column"

To upgrade the db with the revision:
alembic upgrade 7bcd40d197d0

To downgrade the db with the revision:
alembic downgrade -1
