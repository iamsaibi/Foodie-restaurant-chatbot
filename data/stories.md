## Story_1
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - action_check_location
  - slot{"location": "delhi"}
  - slot{"valid_location": "found"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
  - slot{"budget": "more than 700"}
  - action_search_restaurants
  - slot{"restaurant_found": "True"}
  - utter_email_pref
* affirm
  - utter_email_id
* email_input{"mail_id":"xyz@gmail.com"}
  - slot{"mail_id":"xyz@gmail.com"}
  - action_send_mail
  - action_restart

## Story_2
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "abcd"}
  - slot{"location": "abcd"}
  - action_check_location
  - slot{"location": "null"}
  - slot{"valid_location": "not_found"}
  - utter_notfound
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
  - slot{"budget": "more than 700"}
  - action_search_restaurants
  - slot{"restaurant_found": "True"}
  - utter_email_pref
* affirm
  - utter_email_id
* email_input{"mail_id":"xyz@gmail.com"}
  - slot{"mail_id":"xyz@gmail.com"}
  - action_send_mail
  - utter_goodbye
  - action_restart

## Story_3
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "majholi"}
  - slot{"location": "majholi"}
  - action_check_location
  - slot{"location": "null"}
  - slot{"valid_location": "not_operable"}
  - utter_not_operable
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
  - slot{"budget": "more than 700"}
  - action_search_restaurants
  - slot{"restaurant_found": "True"}
  - utter_email_pref
* affirm
  - utter_email_id
* email_input{"mail_id":"xyz@gmail.com"}
  - slot{"mail_id":"xyz@gmail.com"}
  - action_send_mail
  - utter_goodbye
  - action_restart

## Story_4
* greet
    - utter_greet
* restaurant_search{"location": "nashik"}
    - slot{"location": "nashik"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "nashik"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_email_pref
* affirm
    - utter_email_id
* email_input
    - utter_invalid_email
* email_input
    - utter_invalid_email
    - utter_max_invalid
    - utter_goodbye
    - action_restart



## Story_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_email_pref
* deny
    - utter_goodbye
    - action_restart

## Story_6
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "coimbatore"}
    - utter_ask_budget_pref
* affirm
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_email_pref
* deny
    - utter_goodbye
    - action_restart

## Story_7
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget_pref
* deny
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_email_pref
* affirm
    - utter_email_id
* email_input{"mail_id": "upgradtest123@gmail.com"}
    - slot{"mail_id": "upgradtest123@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "upgradtest123@gmail.com"}
    - utter_goodbye
    - action_restart

# Story_8
* greet
    - utter_greet
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"restaurant_found": false}
    - utter_goodbye
    - action_restart

## Story_9
* greet
    - utter_greet
* geosearch
    - utter_geofence
* greet
    - utter_greet
* restaurant_search{"rating": "4", "cuisine": "north indian", "location": "mumbai"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "mumbai"}
    - slot{"rating": "4"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "mumbai"}
    - utter_ask_budget_pref
* deny
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_email_pref
* deny
    - utter_goodbye
    - action_restart


## Story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price_lowerbound": "300"}
    - slot{"cuisine": "american"}
    - slot{"price_lowerbound": "300"}
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "kanpur"}
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_email_pref
* deny
    - utter_goodbye
    - action_restart


## Story_11
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "aligarh"}
    - slot{"location": "aligarh"}
    - action_check_location
    - slot{"valid_location": "not_operable"}
    - slot{"location": null}
    - utter_not_operable
* restaurant_search{"location": "bhavnagar"}
    - slot{"location": "bhavnagar"}
    - action_check_location
    - slot{"valid_location": "not_operable"}
    - slot{"location": null}
    - utter_not_operable
    - utter_max_invalid
    - utter_goodbye
    - action_restart


## Story_12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"valid_location": "not_operable"}
    - slot{"location": null}
    - utter_not_operable
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurant_found": false}
    - utter_goodbye
    - action_restart

## Story_13
    - utter_ask_location
* restaurant_search{"location": "kedarkantha"}
    - slot{"location": "kedarkantha"}
    - action_check_location
    - slot{"valid_location": "not_found"}
    - slot{"location": null}
    - utter_notfound
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"restaurant_found": false}
    - utter_goodbye
    - action_restart

## Story_14
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_email_pref
* email_input{"mail_id": "xyz@gmail.com"}
    - slot{"mail_id": "xyz@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "xyz@gmail.com"}
    - utter_goodbye
    - action_restart

## Story_15
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "budget": "low", "location": "ahmedabad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "ahmedabad"}
    - slot{"budget": "low"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
    - action_search_restaurants
    - slot{"restaurant_found": false}
    - utter_goodbye
    - action_restart

## Story_16
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi", "cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"valid_location": "found"}
    - slot{"location": "New Delhi"}
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_email_pref
    - utter_goodbye
    - action_restart
