--here should be a solution
-- START_EXCLUDE_FROM_PUSH
SELECT * FROM sensitive_table;
-- END_EXCLUDE_FROM_PUSH

-- heres code that should be pushed
SELECT * FROM public_table;
