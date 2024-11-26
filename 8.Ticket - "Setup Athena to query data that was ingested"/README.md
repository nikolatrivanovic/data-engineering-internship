# Setup Athena to qu ery data that was ingested

1. [athena_sql.sql](athena_sql.sql) je za pravljenje baze
2. [generate_sqls_skeletons.py](generate_sqls_skeletons.py) je za generisanje sql skripti za kreiranje tabela
3. create_table_TABLE__NAME su izgenerisani iz skripte, pa onda nasminkani da bolje rade (ukoliko je bilo potrebe)
4. [test.sql](test.sql) nije exec skripta, nego pokazuje upite i njihove rezultate