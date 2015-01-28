# python-logparser
continuous parsing of log file and lookout for the exceptions 

python logparser.py

The output will look like following. 

    scanning batch  0 --------------------------------------------------------------------------------
    scanning batch  1 --------------------------------------------------------------------------------
    scanning batch  2 --------------------------------------------------------------------------------
    scanning batch  3 --------------------------------------------------------------------------------
    64.242.88.10 - - [07/Mar/2004:16:58:54 -0800] "GET /mailman/listinfo/administration HTTP/1.1" 400 Exception in thread "main" java.lang.NullPointerException
        at com.example.myproject.Book.getTitle(Book.java:16)
        at com.example.myproject.Author.getBookTitles(Author.java:25)
    scanning batch  4 --------------------------------------------------------------------------------

1>  The "scanning batch 0----" tells you that it is scanning first 10 lines of log file.

2>  It then sleeps for 1 second

3>  After wake up it scans next 10 lines if available. 

4>  If it prints same batch number after every 1 sec then that indicates it has reached the eof and there are no more lines to scan. It will scan the new lines if appended and available in next scan though.


The log file name, batchsize and seeptime can be feed to script through command line arguments as shown below

                   python logparser.py ./apache_log.log 100 1
                   
                                        logfilename batchsize sleeptime
