queries = [
    '''
SELECT *
FROM crime_scene_report
WHERE city = "SQL City"
ORDER BY date;
''',
    '''
SELECT *
FROM person
WHERE name like '%Morty%'  AND address_street_name = "Northwestern Dr";
''',
    '''
SELECT *
FROM person
WHERE name like '%Annabel%' AND address_street_name = "Franklin Ave";
''',
    '''
SELECT *
FROM interview
WHERE person_id = 14887 OR person_id = 16371;
''',
    '''
SELECT *
FROM get_fit_now_check_in 
WHERE membership_id like "%48Z%" AND check_in_date = 20180109 
order by check_in_date;
''',
    '''
SELECT *
FROM drivers_license
WHERE plate_number like "%H42W%";
''',
    '''
SELECT *
FROM person
WHERE license_id = "423327" OR license_id = "664760";
''',
    '''
SELECT *
FROM get_fit_now_member
WHERE person_id = "51739" OR person_id = "67318";
''',

]

questions = [
    "There's been a Murder in SQL City!  A crime has taken place and I need your help. I have given you the crime scene report, but you somehow lost it. You vaguely remember that murder occurred sometime on Jan 15, 2018 and that it took place in SQL City. Start by retrieving the corresponding crime scene report from the police department’s database.",
    "Security footage shows that there were two witnesses. The first witness named Morty lives at the last house on \"Northwestern Dr \". Let's, look for the details of first witness",
    "The second witness, named Annabel, lives somewhere on \"Franklin Ave\" \n Let's, look for the details of second witness",
    "lets view the interview of both the witnesses taken after the murder.",
    "So, we got 2 clues-  \n Killer is a man and a member of the gym with a status of gold and having a membership no. starting with 48Z and left in a car with a no. plate of H42W and He was working out in the gym on 9th of Jan. Check the gym database with above details",
    "Two member's found and their membership id. Now, let's check the car details by the above details",
    "Two male with a plate no. containg H42W. Check personal details of both the males from the above query",
    "Lets check which of this two are a member of the gym?",
    "Congrats, you found the murderer - Jeremy Bowers. Both the membership id and status also matches as per the information we found earlier.",
]

hints = [
    "Hints : Find all crime scene reports in 'SQL City' and sort them by date.",
    "Hints : Find all persons on 'Northwestern Dr' where street name is 'Northwestern Dr'. Note down the ID, It might be useful in further deduction.",
    "Hints : Find all persons on 'Annabel' where street name is 'Franklin Ave'.",
    "Hints : Retrieve all interviews for persons with ID 14887 or 16371.",
    "Hints : Retrieve all check-ins on Jan 9, 2018 for members with ID containing '48Z', and sort them by date.",
    "Hints : Retrieve all driver's licenses with a plate number containing 'H42W'.",
    "Hints : Retrieve all persons with license IDs 423327 or 664760",
    "Hints : Retrieve all members with person IDs 51739 or 67318."
]
