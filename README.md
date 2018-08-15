# Lobster
1.edit /home3/ocn/jmanning/sql/write_emolt_set.sql by just changing:
   change site code

2.sqldump -u 'jmanning/emolt000$$$$' -o /data5/jmanning/fish/lobster/mala/sqldump_2018_07_BD -f /home3/ocn/jmanning/sql/write_emolt_set.sql -D','
   2-digit site code
   mela or mala directory

3.perl ~/sql/gettsll_justtemp.plx  BM01 to produce this2.dat by extracting from both emolt_sensor & site
   Modified in 2016 to make sure it outputs a 4-digit year
