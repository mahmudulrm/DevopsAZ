# Kill Multiple Querys
show full processlist;
show processlist;
select concat('KILL ',id,';') from information_schema.processlist where user='user';

# Too Manny Connections
FLUSH HOSTS;
