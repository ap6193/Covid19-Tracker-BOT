## happy info path
* more_info
  - utter_website

## Greet
* greet
  - utter_greet

## Happy Path 1
* greet
  - utter_greet
* details
  - utter_choose

## Happy Path
* what_is_corona
  - utter_corona
* symptoms
  - utter_symptoms
* concern
  - utter_concern
* prevention
  - utter_prevent
* Vaccination
  - utter_Vaccination
* incubation
  - utter_incubation
* Find
  - utter_choose_case
  
## What is Corona
* concern
  - utter_concern

## Concern
* what_is_corona
  - utter_corona

## Info path 1
* greet
  - utter_greet
* details
  - utter_choose
* affirm
  - utter_choose

## Info path 2
* greet
  - utter_greet
* details
  - utter_choose
* deny
  - utter_end
  
## Denial
* deny
  - utter_end

## symptoms
* symptoms
  - utter_symptoms

## preventions
* prevention
  - utter_prevent

## happy vaccine
* Vaccination
  - utter_Vaccination

## happy incubation
* incubation
  - utter_incubation

## happy thanks
* thanks
  - utter_thanks

## say goodbye
* goodbye
  - utter_goodbye
  
## cases flow
* ask_location
  - utter_location
* cases_world
  - action_world_cases
* ask_states
  - utter_state
* cases_states
  - action_state_cases
* ask_world
  - action_total_cases
* cases_India
  - action_cases_India
  
## cases in India
* cases_India
  - action_cases_India
  
## cases across world
* ask_location
  - utter_location
* cases_world
  - action_world_cases
  
## cases across states
* ask_states
  - utter_state
* cases_states
  - action_state_cases

## Total cases
* ask_world
  - action_total_cases
  
## Report cases
* Find
  - utter_choose_case
  
## Statistics story
* greet
  - utter_greet

## default fallback 
* bot_challenge
  - action_default_fallback
  
## Stats flow
* greet
  - utter_greet
* details
  - utter_choose
* Find
  - utter_choose_case
* ask_location
  - utter_location
* cases_world
  - action_world_cases
* affirm
  - utter_choose
* Find
  - utter_choose_case
* ask_states
  - utter_state
* cases_states
  - action_state_cases
* affirm
  - utter_choose
* Find
  - utter_choose_case
* ask_world
  - action_total_cases
  
## Complete Story flow affirm
* greet
  - utter_greet
* details
  - utter_choose
* what_is_corona
  - utter_corona
* affirm
  - utter_choose  
* symptoms
  - utter_symptoms
* affirm
  - utter_choose
* concern
  - utter_concern
* affirm
  - utter_choose
* prevention
  - utter_prevent
* affirm
  - utter_choose
* Vaccination
  - utter_Vaccination
* affirm
  - utter_choose
* incubation
  - utter_incubation
* affirm
  - utter_choose
* Find
  - utter_choose_case
* ask_location
  - utter_location
* cases_world
  - action_world_cases
* affirm
  - utter_choose
* Find
  - utter_choose_case
* ask_states
  - utter_state
* cases_states
  - action_state_cases
* affirm
  - utter_choose
* Find
  - utter_choose_case
* ask_world
  - action_total_cases
* affirm
  - utter_choose
* more_info
  - utter_website
* deny
  - utter_end
* thanks
  - utter_thanks
* goodbye
  - utter_goodbye
  




  
  