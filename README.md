These are our project's files purpose:

- generate_tests.py:
    generate input for tests;
    able to specify how many tests you want by calling function
        create_test(num_test) ## num_test default = 1

    For not creating chaos when we change num_test, we redirect input & output
        into directory 'experiment' when we run file compare.py

    Run-command example: 'python generate_tests.py'
        -> if not modify anything, there will be file 'input1.txt' in 'experiment/'

- solution_origin.py: code of our origin algorithm
    Run-command example: 'python solution_origin.py < experiment/input1.txt >> experiment/out_origin1.txt'

- solution_new.py: code of our updated algorithm
    Run-command example: 'python solution_new.py < experiment/input1.txt >> experiment/out_new1.txt'

- compare.py: this program first generate tests by running generate_tests.py
    Afterthat, it run them by solution_origin.py & solution_new.py to record 3 criterias:
        1. time running; 2. Total travel mileage; 3. Unbalance workload
        Then draw graph for visualization & save pictures at
            pic_runtime.png, pic_mileage.png, pic_unbalance.png respectively

- draft.py: just for testing in python, does not affect above programs
