# INSERT INTO student (`id`, `name`, `address`, `phone`) VALUES (NULL, 'Alex', 'Pokhara', '333');
# UPDATE `student` SET `address` = 'Baneshwor' WHERE `student`.`id` = 1;

import mysql.connector
db =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    port = "3306",
    database = "python_may26"
)
terminal = db.cursor()
# insert = "INSERT INTO student (name, address, phone) VALUES ( 'lex', 'Pokhara', '333');" 
# terminal.execute(insert)
# db.commit()
print(terminal.rowcount)

# update and delete

command = "Select name FROM student"
terminal.execute(command)
result = terminal.fetchall()
for i in result:
    print(i)