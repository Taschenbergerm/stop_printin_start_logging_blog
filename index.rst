
Stop Printing - Start Logging
##############################

:date: 2020-09-05 16:39
:modified: 2020-09-05 16:39
:tags: python, logging, loguru,
:category: production-code
:slug: stop-printing-start-logging
:lang: en
:status: published
:author: Marvin Taschenberger
:summary:



One Lesson that everyone will learn (maybe the hard way) is - that programs, once it leaves the development stage and your IDE - anything can happen to it. No matter how much effort you put into it, how many bugs you fixed, errors you anticipated - something will cause your program to behave differently from what you intended, maybe even breaking it completely.
In this cases you will need to figure out:

#. Is my program still alive 
#. What is it currently doing / what was it doing
#. In some cases - what where it's last words ?  


Since theory and everything is nice - lets make a little more practical by using an example that we will transform: 

.. include:: ./examples/production_code/start.py
    :code: python


Note that most of the output is due to print and the longer the code runs the more likely it becomes that the ``do_unstable_magic`` function will create an error - as in real life.

If now this programs crashes at some point and someone tells you to investigate and fix what went wrong. As you cannot recreate what has happened without any informations with this program you would be screwed and domed to make some try and error locally. As this is neither efficient, productive nor fun - we need to think about this scenarios already in the development stage. Seemingly the ``print`` function was not a good approach. It did work quite nicely while we were still in our local environment and executing the code manually but there are several disadvantages these statements do have:

#. They write only to std.out - are only visible in an interactive session 
#. There is no way to differentiate base on severity or importance of information 
#. You cannot silence them easily if you create a library or similar


The proper way to handle this would be to use a so called ``Logger``. These kind of object offer a more versatile way of handling information output by allowing for differentiation of information based on their priority ( e.g. debug, info, warning, error ...). Further we can also allow for multiple output-formats - also known as ``sinks``. The most basic sink that we already used is the ``std.out`` - that is what  print is using. 

Let us look at a simple example:


.. include:: examples/baselogging.py
    :code: python


Simply importing ``logging`` and configuring it with the ``baseConfig`` function enables us to directly replace any print with logging. The next best feature.

Let us take this to our example code an directly take the first step of improvement. 

.. include:: examples/production_code/step_1.py
    :code: python


Though that was easy and we now get more information like time and level - but it still would have prevented our lack of information. 

So next we want save our output and therefor need to use a ``File-Sink``. That way messages wont be lost but preserved in a log-file. To achieve this we only add the  ``filename`` argument and set the respective level - done. 

.. include:: examples/file_sink.py
    :code: python


Now things start to get interesting from here. As we are able to differentiating between levels ( debug, etc) and sinks (``std.out``, files, etc.) we could combine both and filter which message should go where and even duplicate ``sinks`` for different levels. As an example we can save our information that we need for debugging to a log file that we can read later while only those on an error gets printed directly. This combination allows for many different combinations e.g.  having multiple file-sinks one for errors and one for debug statements which you can then treat separately.

.. include:: examples/handler_logging.py
    :code: python


Now we can take the next big step with our project and enable the mechanism that can save us time and motivation in case of an issues: 

..  include:: examples/production_code/step_2.py
    :code: python


Now all we need to do is to deploy the project and we will automatically keep a long history of errors to analyze the reliability or debugging. But writing every single debug information might cause the file to explode?! If we let this project run for weeks or month we will run into two issues if the file will grow tremendously large: 

#. reading, copying or filtering  it will become slow if not impossible 
#. the file might grow too large for the file system and cause the system to crash  

Therefore we need to start thinking about a cleanup. We can either do that on the system level or within our code. But as most of the obvious task in python this is already wrapped together in an (awesome) library called ``loguru``. Personally, i haven been working with it since a long time and it is part of nearly all my productional services as it is easy to use and reduces the boilerplate code to a minimum. Moreover it ensures that my logging-practice stays homogeneous through out my projects. This library was original developed by delgan and i highly recommend you to check the `repo <https://github.com/Delgan/loguru>`_ out.

All we need to do now is to  install ``loguru`` using ``pip install loguru``   and specify two arguments - one for rotation and  one for retention - done.

.. include:: examples/retention_and_rotation.py
    :code: python


Now our log file will automatically rotate every day and as such create a daily debug log. This ensures that the file itself does not grow to big to handle it properly while the retention keeps deleting files older than a week s.t. the do not take too much space on disk.

Finally we can now finish our project by refactoring our code using loguru as following: 


.. include:: examples/production_code/step_3.py
    :code: python
