Example:

seconds ="1015557";

Result should be:

11days 18h:05m:57s
    
SELECT
  DATE_FORMAT(date('1970-12-31 23:59:59')
   + interval 1015557 second,'%j days %Hh:%im:%ss') as result;
sample

mysql>     SELECT
    ->       DATE_FORMAT(date('1970-12-31 23:59:59')
    ->        + interval 1015557 second,'%j days %Hh:%im:%ss') as result;
+----------------------+
| result               |
+----------------------+
| 011 days 18h:05m:57s |
+----------------------+
1 row in set (0,00 sec)

mysql>
