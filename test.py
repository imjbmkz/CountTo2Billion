import main
from datetime import datetime as dt

if __name__=="__main__":

    py_start_time = dt.now()
    main.count_to_billion_py()
    py_end_time = dt.now()
    py_duration = py_end_time - py_start_time
    print(f"Counting to 2 billion took {py_duration} in Python.")

    cy_start_time = dt.now()
    main.count_to_billion_cy()
    cy_end_time = dt.now()
    cy_duration = cy_end_time - cy_start_time
    print(f"Counting to 2 billion took {cy_duration} in Cython.")