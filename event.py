Title "CLIENT DETAILS";

data EVENT.CLIENT;
  length client_ID $ 100 client_Name $ 100 client_phone $20 address $ 100 client_email $ 100 Password 8;
  /* Define variables and their attributes */
  input client_ID client_Name client_phone address client_email Password ;
  datalines;
  

1001 John_Doe 012345678 123MainSt,City John@gmail.com 111
1002 Jane_Smith 0798765432 456ElmSt,City Jane@yahoo.com 222
1003 Mark_Johnson 0835432167 789OakSt,City Mark@gmail.com 333

;
run;
proc print;
run;

TITLE "SERVICE PROVIDER";

Data EVENT.SERVICE_PROVIDER;
	length Provider_ID $100 Provider_Name $100 Provider_Type $100 Provider_contact $100 Location $100;
	input Provider_ID Provider_Name Provider_Type Provider_contact Location;
	datalines;

 001 Eddie's_catering Catering 0152345678 123_JHB_2005
 002 Beatsaudio Disc_Jockey 012345678 111_PTA_2000
 003 Pretoria_Hall Venue 0129876543 123_PTA_2000
;
run;
proc print;
run;

/*SIGN UP*/
TITLE "SIGN UP";
OPTIONS NONOTES NOSTIMER NOSOURCE NOSYNTAXCHECK;
/* Define Parent Sign Up Function */
%macro SignUp(client_ID=, client_Name=, client_phone=, address=, client_email=, Password=);
    /* Perform necessary validations */
    %if %length(&client_ID) = 0 or %length(&client_Name) = 0 or %length(&client_phone) = 0 or %length(&address) = 0 or %length(&client_email) = 0 or %length(&Password) = 0 %then %do;
        %put ERROR: Please provide all the required information.;
        %return;
    %end;


    /* Store parent information */
    data NEW_CLIENT;
        length client_ID $8 client_Name $50 client_phone $100 address $100 client_email $100 Password 8;
        client_ID = "&client_ID";
        client_Name = "&client_Name";
        client_phone = "&client_phone";
        address = "&address";
        client_email = "&client_email";
        Password = "&Password";
    run;

    %put client Sign Up Successful!;
    %put client_ID: &client_ID;
    %put client_Name: &client_Name;
    %put client_phone: &client_phone;
    %put address: &address;
    %put client_email: &client_email;
    %put Password: &Password;
    
    data EVENT.CLIENT;
    set EVENT.CLIENT NEW_CLIENT;
    
%mend;

/* Example Usage */
%SignUp(client_ID =1004,client_Name = EddieBrave,client_phone = 0812345678,address = JHB,client_email = Eddie@gmail.com,Password = 444);
%SignUp(client_ID =1005,client_Name = Malebo,client_phone = 089876549,address = PTA,client_email = Malebo@gmail.com,Password = 555);
proc print;
OPTIONS NONOTES NOSTIMER NOSOURCE NOSYNTAXCHECK;



/*SIGN IN*/

/* Macro to handle user sign-in */
%macro SignIn(client_Name, Password);
  /* Check if user exists in the Users table */
  DATA _NULL_;
    SET EVENT.CLIENT (WHERE=(client_Name="&client_Name" and Password="&Password")) END=found;
    IF found THEN
      PUT "User Sign-In Successful!";
    ELSE
      PUT "Invalid Username or Password!";
  RUN;
%mend;

/* Call the sign-in macro */
%SignIn(client_Name=John_Doe, Password=111);


/*WALK_THROUGH*/


%macro WalkThroughWizard;
  /* Prompt the user to specify the type of event they want to plan */
  data EventWizard;
    length EventType $20;
    put "Welcome! Please specify the type of event you want to plan:";
    put "1. Birthday Party";
    put "2. Wedding";
    input EventType $;
    datalines;
  Birthday Party
  ;
  run;

  proc print data = EventWizard;
  run;

  /* Process the user's choice and provide a recommendation */
  data Recommendation;
    set EventWizard;
    if EventType = "1" then do;
      put "Based on your selection of Birthday Party, we recommend the following providers:";
      /* Fetch and display recommendations for birthday party providers */
      data Birthday;
        set EVENTAPP.ServiceProviders;
        where ProviderType = "Venue" and Location = "New York City";
        /* You can add additional criteria to filter the providers */
        put ProviderName;
      run;
    end;
    else if EventType = "2" then do;
      put "Based on your selection of Wedding, we recommend the following providers:";
      /* Fetch and display recommendations for wedding providers */
      data Wedding;
        set EVENTAPP.ServiceProviders;
        where ProviderType = "Caterer" and Location = "Los Angeles";
        /* You can add additional criteria to filter the providers */
        put ProviderName;
      run;
    end;
  run;
%mend;

/* Run the WalkThroughWizard macro */
%WalkThroughWizard;


TITLE "BOOKING";
/* Create an empty SERVICE_PROVIDER dataset */

data EVENT.BOOKING;
  length Client_ID $100.
  		 Provider_ID $100.
         provider_Name $100.
         Provider_Type $100.
         Contact_info $100.
         Location $100.;
   input Client_ID Provider_ID provider_Name Provider_Type Contact_info Location;
   datalines;
   
1001 001 Eddie's_catering Catering 0152345678 123_JHB_2005
1002 002 Beatsaudio Disc_Jockey 012345678 111_PTA_2000
1003 003 Pretoria_Hall Venue 0129876543 123_PTA_2000
   ;
run;


/* Define the service_provider macro */
%macro BOOKING(Client_Id, Provider_ID, provider_Name, Provider_Type, Contact_info, Location);
  
  /* Insert code to create a new booking record in the database */
  %put Booking confirmed!;
  %put Client_ID: &Client_ID.;
  %put Provider_ID: &Provider_ID.;
  %put provider_Name: &provider_Name.;
  %put Provider_Type: &Provider_Type.;
  %put Contact_info: &Contact_info.;
  %put Location: &Location.;
  
  

  /* Save data to the SERVICE_PROVIDER dataset using a DATA step */
  data temp;

    Client_ID= &Client_ID.;
    Provider_ID = &Provider_ID.;
    provider_Name = &provider_Name.;
    Provider_Type = &Provider_Type.;
    Contact_info = &Contact_info.;
    Location = &Location.;
  run;
  
  data event.booking;
  	set event.booking temp;
%mend;



/* Call the service_provider macro to add new service providers */
%BOOKING(Client_ID="1001",Provider_ID ="001", provider_Name ="music", Provider_Type ="Venue, 300 guests",Contact_info = "0812345678",Location = "PTA");
%BOOKING(Client_ID="1008",Provider_ID ="003", provider_Name ="venue", Provider_Type ="Venue, 300 guests",Contact_info = "0812345678", Location ="PTA");
%BOOKING(Client_ID="1010",Provider_ID ="007",provider_Name = "Black coffee", Provider_Type ="Venue, 300 guests", Contact_info ="0812345678",Location = "JHB");
%BOOKING(Client_ID="1011",Provider_ID ="010",provider_Name = "DJ Ganyani", Provider_Type ="DJ, 100 people", Contact_info ="081298765",Location = "PLK");

run;

/* Display the SERVICE_PROVIDER table */

run;
proc print;
run;


/* VIEW BOOKING*/

TITLE "VIEW BOOKING";

/* Define the view_booking macro */
%macro view_booking(booking_ID);
  
  /* Filter the EVENT.BOOKING dataset for the specified booking ID */
  data booking_view;
    set EVENT.BOOKING;
    where Client_ID = "&booking_ID.";
  run;
  
  /* Check if the booking exists */
  %let booking_count = %sysfunc(attrn(booking_view, nobs));
  
  /* Display the booking details if it exists */
  %if &booking_count > 0 %then %do;
    proc print data=booking_view;
    run;
  %end;
  %else %do;
    %put Booking not found.;
  %end;
%mend;

/* Call the view_booking macro with a booking ID */
%view_booking(1008);
%view_booking(1001);
%view_booking(1010);
run;
proc print;


/*ADD CONTENT*/

TITLE "ADD CONTENT";
/* Create a dataset to store gallery content */
data EVENT.CONTENT;
  length Content_ID $20 Provider_ID $20 ImageURL $200 Description $200;
  input Content_ID Provider_ID ImageURL Description;
  datalines;
1 001 https://cf.bstatic.com/xdata/images/hotel/max1280x900/73431856.jpg?k=b569948c017cb8c1d2185dcf48a57ed330386a9d8d029956750ec9be427994df&o=&hp=1 Venue_Booking
2 002 https://images.squarespace-cdn.com/content/v1/5fd8b1e0dba154430f79ad94/cd95396f-e45a-4faf-92c0-a1fb0904ef04/RTC_8649.jpg?format=1000w Dj_Booking
3 003 https://www.moemas.co.za/wp-content/uploads/2017/06/20170511_121829.jpg Cater_Booking
4 004 https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRUHTfu2yqXuQQLmDsyPJS-zrOWzqJapRQXQ&usqp=CAU Dj Booking
;
run;

data ADD_CONTENT;
  length Content_ID $20 Provider_ID $20 ImageURL $200 Description $200;
  infile datalines delimiter=' ';
  input Content_ID $ Provider_ID $ ImageURL $ Description $;
  datalines;
5 003 https://example.com/image4.jpg DJ entertaining the crowd
6 001 https://example.com/image5.jpg Elegant wedding decorations
;
run;

/* View the updated gallery */
data EVENT.CONTENT;
 set EVENT.CONTENT ADD_CONTENT;
  put Content_ID= &Content_ID.;
  put Provider ID = &Provider_ID.;
  put Image URL= &ImageURL.;
  put Description= &Description.;
  
run;
proc print;


TITLE "RATING";

/* Define the RATE_BOOKING macro */
%macro RATE_BOOKING(Client_Id, Provider_ID, Rating);
  /* Update the rating for the specified booking */
  data EVENT.BOOKING;
    set EVENT.BOOKING;
    where Client_ID = "&Client_Id" and Provider_ID = "&Provider_ID";
    Rating = &Rating;
  run;

  %put Rating updated for Client ID: &Client_Id, Provider ID: &Provider_ID.;
%mend;

/* Call the RATE_BOOKING macro to update the rating */
%RATE_BOOKING(Client_ID =1001, Provider_ID =001,Rating= 4.5);

/* Display the updated BOOKING table */
proc print data=EVENT.BOOKING;
run;






