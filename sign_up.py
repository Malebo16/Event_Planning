OPTIONS NONOTES NOSTIMER NOSOURCE NOSYNTAXCHECK;
/* Define Parent Sign Up Function */
%macro SignUp(UserID=, Username=, Password=, Email=, FirstName=, LastName=);
    /* Perform necessary validations */
    %if %length(&UserID) = 0 or %length(&Username) = 0 or %length(&password) = 0 or %length(&Email) = 0 or %length(&FirstName) = 0 or %length(&LastName) = 0 %then %do;
        %put ERROR: Please provide all the required information.;
        %return;
    %end;


    /* Store parent information */
    data EVENTAPP.NewUser;
        length UserID $8 Username $50 Password $100 Email $100 FirstName $100 LastName $100;
        UserID = "&UserID";
        Username = "&Username";
        Password = "&password";
        Email = "&Email";
        FirstName = "&FirstName";
        LastName = "&LastName";
    run;

    %put USER Sign Up Successful!;
    %put UserID: &UserID;
    %put Username: &Username;
    %put Password: &password;
    %put Email: &Email;
    %put FirstName: &FirstName;
    %put LastName: &LastName;
%mend;

/* Example Usage */
%SignUp(UserID =3,Username = EddieBrave,Password = password3,Email = eddie@example.com,FirstName = Eddie,LastName = Brave);

OPTIONS NONOTES NOSTIMER NOSOURCE NOSYNTAXCHECK;





