/* Macro to handle user sign-in */
%macro SignIn(Username, Password);
  /* Check if user exists in the Users table */
  DATA _NULL_;
    SET EVENTAPP.Users (WHERE=(Username="&Username" and Password="&Password")) END=found;
    IF found THEN
      PUT "User Sign-In Successful!";
    ELSE
      PUT "Invalid Username or Password!";
  RUN;
%mend;

/* Call the sign-in macro */
%SignIn(Username=JohnDoe, Password=password1);