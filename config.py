import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN" : "fsnd79.auth0.com",
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "casting"
}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExc0I4dXRPc1Rod2FOZV8xN25LZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ3OS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY5ZTEyMTM5ZmU1MDUwMDdiNWVmYmEyIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYwNDI1NzgwMSwiZXhwIjoxNjA0MzQ0MjAxLCJhenAiOiJ0UXRaSzQ5bFU0MkZENnNSVEZGbnhPdm43QnB2SU5BaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3Jmb3JtIiwiZ2V0OmFjdG9ycyIsImdldDpjYXN0Zm9ybSIsImdldDptb3ZpZWZvcm0iLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0OmNhc3QiLCJwb3N0Om1vdmllcyJdfQ.Gan6e4JKvVkI8UH3WWlyiiZrI3-o_FLXcK67hO18nlY5Z0ms1HAPvtrwYrFm9Qni5e85IoyQzvzstargslw8wOczLT_zT3rQQ0C5DloCA-VxSLOuMzoj8qNfrEG77qO5Ojv85uTqHJ2IDYhYv5aZt5sV-Utf79KC83VGnioGD8JTnj8cbH4701RjMGHCatY-svOxe8GH0G8StIGMLq1bD7lszg8_hZzx9mpxnvgqnCws-QGFuCMmhRrYqq03p3O1_Bb8wfICwZfZpOcHqWP61C1NK5CanIRPRPwQxFjYPUPQGbb2g7mif0Exp26S3aPCLR3W0ShwCl9ost9fAZLpew",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExc0I4dXRPc1Rod2FOZV8xN25LZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQ3OS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY5ZTEyMTM5ZmU1MDUwMDdiNWVmYmEyIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYwNDI3MTcyMywiZXhwIjoxNjA0MzU4MTIzLCJhenAiOiJ0UXRaSzQ5bFU0MkZENnNSVEZGbnhPdm43QnB2SU5BaSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3Jmb3JtIiwiZ2V0OmFjdG9ycyIsImdldDpjYXN0Zm9ybSIsImdldDptb3ZpZWZvcm0iLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0OmNhc3QiLCJwb3N0Om1vdmllcyJdfQ.aRQn2mJ1RhHJDZimbzOl01jdpjbw_ZdJ9GXe35uMobe-uaKKqs5sksx5hLZBeFDZNBOzXv4B9Q6GXPmLq91Pg3ms4fg_ZVsQaaipsUExuMZSlDFfCDDajNHFSjE1HkkyTMskc44dJb1OPnU5K9q3HzuyvjuPGAUYWPygO7QC8IytubmufyFbt1DCMlnnLXXa-HBU-VU88cFDLaEeZq1R6dqF8VZ51bPl5z3vyPamuzFy3PCDTCuVs7HcNB1x0wAlVmYikoYu8WYH_GHKgyGYqiAFHS-bgjrfRGy4hB-tDPJa-HC-UXmROw_VZHZQZSQe0YUQk6rZs169EZ4hjJ-OSQ"
}